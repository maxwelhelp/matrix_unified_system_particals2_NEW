#!/usr/bin/env python3
import argparse, csv, gc, json, os, sys
from pathlib import Path
from collections import defaultdict
import torch
import torch.nn as nn

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from tools.part_attention_supertrace_real_contract_v1 import LABELS, load_model, build_batch, wcsv, wjson

HQQL=LABELS.index('label_Hqql'); TBL=LABELS.index('label_Tbl')
GROUPS=['A_Hqql_correct','B_Hqql_to_Tbl','C_Tbl_correct','D_Tbl_to_Hqql']

def f(x,d=0.0):
    try:
        if x is None or x=='': return d
        return float(x)
    except Exception: return d

def fmt(x):
    try: x=float(x)
    except Exception: return 'n/a'
    return f'{x:.3e}' if abs(x)>0 and (abs(x)<1e-3 or abs(x)>1e4) else f'{x:.4f}'

def rcsv(p):
    with open(p,newline='',encoding='utf-8') as h: return list(csv.DictReader(h))

def select_events(path,n):
    by=defaultdict(list)
    for r in rcsv(path): by[r['analysis_group']].append(r)
    out=[]
    for g in GROUPS: out+=by[g][:n]
    return out

def mdtab(headers,rows):
    if not rows: return '_No rows._\n'
    return '\n'.join(['| '+' | '.join(headers)+' |','| '+' | '.join(['---']*len(headers))+' |']+['| '+' | '.join(str(x) for x in r)+' |' for r in rows])+'\n'

def obj_value(logits,metas,mode):
    vals=[]
    for i,m in enumerate(metas):
        g=m['analysis_group']
        if mode=='signed_hqql_tbl':
            vals.append((logits[i,TBL]-logits[i,HQQL]) if g in ('B_Hqql_to_Tbl','C_Tbl_correct') else (logits[i,HQQL]-logits[i,TBL]))
        elif mode=='B_tbl_minus_hqql':
            if g=='B_Hqql_to_Tbl': vals.append(logits[i,TBL]-logits[i,HQQL])
    if not vals: return None
    return torch.stack(vals).mean()

class ClassifierTracer:
    def __init__(self):
        self.records=[]; self.handles=[]
    def hook_named(self,name):
        def fn(module,args,out):
            x=args[0] if args else None
            if torch.is_tensor(x): x.retain_grad()
            if torch.is_tensor(out): out.retain_grad()
            self.records.append({'name':name,'type':module.__class__.__name__,'x':x,'out':out})
        return fn
    def attach(self,model):
        # final norm before classifier, whole fc, and linear layers inside fc.
        for name,m in model.named_modules():
            if name in ('mod.norm','mod.fc') or (name.startswith('mod.fc') and isinstance(m,nn.Linear)):
                self.handles.append(m.register_forward_hook(self.hook_named(name)))
        if not self.handles:
            raise RuntimeError('no classifier/norm modules hooked')
    def close(self):
        for h in self.handles: h.remove()
        self.handles=[]

def aggregate(records,metas,objective,weight):
    rows=[]; dim_rows=[]
    B=len(metas)
    for rec in records:
        x=rec['x']; out=rec['out']
        for tensor_name,tensor in [('input',x),('output',out)]:
            if not torch.is_tensor(tensor) or tensor.grad is None or tensor.ndim!=2 or tensor.shape[0]!=B: continue
            val=tensor.detach().float().cpu(); grad=tensor.grad.detach().float().cpu(); contrib=val*grad
            for bi,m in enumerate(metas):
                g=m['analysis_group']
                rows.append({'objective':objective,'module':rec['name'],'module_type':rec['type'],'tensor':tensor_name,'analysis_group':g,'score':float(contrib[bi].sum()),'abs_score':float(contrib[bi].abs().sum()),'act_norm':float(torch.sqrt((val[bi]**2).sum()+1e-12)),'grad_norm':float(torch.sqrt((grad[bi]**2).sum()+1e-12))})
                # keep top dims by abs contribution per event; enough for compact report.
                k=min(12,contrib.shape[1])
                idx=torch.topk(contrib[bi].abs(),k=k).indices.tolist()
                for j in idx:
                    dim_rows.append({'objective':objective,'module':rec['name'],'module_type':rec['type'],'tensor':tensor_name,'analysis_group':g,'dim':j,'contrib':float(contrib[bi,j]),'abs_contrib':float(abs(contrib[bi,j])),'activation':float(val[bi,j]),'grad':float(grad[bi,j])})
    return rows,dim_rows

def summarize(rows,keys,score_key='score'):
    acc=defaultdict(lambda:{'n':0,'sum':0.0,'abs':0.0,'an':0.0,'gn':0.0})
    for r in rows:
        k=tuple(r[x] for x in keys); a=acc[k]; a['n']+=1; a['sum']+=f(r.get(score_key)); a['abs']+=f(r.get('abs_'+score_key,''),abs(f(r.get(score_key))))
        if 'act_norm' in r: a['an']+=f(r.get('act_norm'))
        if 'grad_norm' in r: a['gn']+=f(r.get('grad_norm'))
    out=[]
    for k,a in acc.items():
        n=max(1,a['n']); row={keys[i]:k[i] for i in range(len(keys))}; row.update({'n':a['n'],'mean_score':a['sum']/n,'mean_abs_score':a['abs']/n,'mean_act_norm':a['an']/n,'mean_grad_norm':a['gn']/n}); out.append(row)
    return sorted(out,key=lambda r:abs(f(r['mean_score']))+0.2*f(r['mean_abs_score']),reverse=True)

def summarize_dims(rows):
    acc=defaultdict(lambda:{'n':0,'sum':0.0,'abs':0.0,'act':0.0,'grad':0.0})
    for r in rows:
        k=(r['objective'],r['module'],r['tensor'],r['analysis_group'],r['dim']); a=acc[k]; a['n']+=1; a['sum']+=f(r['contrib']); a['abs']+=f(r['abs_contrib']); a['act']+=f(r['activation']); a['grad']+=f(r['grad'])
    out=[]
    for k,a in acc.items():
        n=max(1,a['n']); out.append({'objective':k[0],'module':k[1],'tensor':k[2],'analysis_group':k[3],'dim':k[4],'n':a['n'],'mean_contrib':a['sum']/n,'mean_abs_contrib':a['abs']/n,'mean_activation':a['act']/n,'mean_grad':a['grad']/n})
    return sorted(out,key=lambda r:abs(f(r['mean_contrib']))+0.2*f(r['mean_abs_contrib']),reverse=True)

def final_linear_exact(model, src_label=None, tgt_label=None):
    fc=getattr(getattr(model,'mod',None),'fc',None)
    if fc is None: return []
    linears=[(n,m) for n,m in fc.named_modules() if isinstance(m,nn.Linear)]
    if not linears: return []
    src_label = src_label or os.environ.get('PART_PAIR_SRC_LABEL', 'label_Hqql')
    tgt_label = tgt_label or os.environ.get('PART_PAIR_TGT_LABEL', 'label_Tbl')
    if src_label not in LABELS: src_label='label_Hqql'
    if tgt_label not in LABELS: tgt_label='label_Tbl'
    src_i = LABELS.index(src_label)
    tgt_i = LABELS.index(tgt_label)
    name,m=linears[-1]
    W=m.weight.detach().float().cpu(); b=m.bias.detach().float().cpu() if m.bias is not None else torch.zeros(W.shape[0])
    if W.shape[0] <= max(src_i,tgt_i): return []
    diff=W[tgt_i]-W[src_i]
    idx=torch.topk(diff.abs(),k=min(40,diff.numel())).indices.tolist()
    return [{'module':'mod.fc.'+name if name else 'mod.fc','dim':j,'weight_tgt_minus_src':float(diff[j]),'bias_tgt_minus_src':float(b[tgt_i]-b[src_i]),'src_label':src_label,'tgt_label':tgt_label,'legacy_weight_tbl_minus_hqql':float(diff[j]),'legacy_bias_tbl_minus_hqql':float(b[tgt_i]-b[src_i])} for j in idx]

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--groups-csv',default='reports/latest/tables/part_hqql_tbl_groups_direct_replay_v1.csv')
    ap.add_argument('--network-file',default='external/particle_transformer/networks/example_ParticleTransformer_legacy.py')
    ap.add_argument('--checkpoint',default='external/particle_transformer/models/ParT_kinpid.pt')
    ap.add_argument('--data-config',default='external/particle_transformer/data/JetClass/JetClass_kinpid.yaml')
    ap.add_argument('--events-per-group',type=int,default=32); ap.add_argument('--micro-batch',type=int,default=8)
    ap.add_argument('--objectives',default='signed_hqql_tbl,B_tbl_minus_hqql')
    ap.add_argument('--src-label', default=os.environ.get('PART_PAIR_SRC_LABEL','label_Hqql'))
    ap.add_argument('--tgt-label', default=os.environ.get('PART_PAIR_TGT_LABEL','label_Tbl'))
    ap.add_argument('--device',default='cuda' if torch.cuda.is_available() else 'cpu')
    ap.add_argument('--out-md',default='reports/latest/PART_CLASSIFIER_LOGIT_DECODER_REAL_CONTRACT_V1.md')
    ap.add_argument('--out-summary',default='reports/latest/tables/part_classifier_logit_decoder_summary_v1.csv')
    ap.add_argument('--out-dims',default='reports/latest/tables/part_classifier_logit_decoder_dims_v1.csv')
    ap.add_argument('--out-linear',default='reports/latest/tables/part_classifier_logit_decoder_final_linear_v1.csv')
    ap.add_argument('--out-json',default='manifests/latest/part_classifier_logit_decoder_real_contract_v1.json')
    a=ap.parse_args(); ev=select_events(a.groups_csv,a.events_per_group); objectives=[x.strip() for x in a.objectives.split(',') if x.strip()]
    device=torch.device(a.device); model,dc=load_model(a.network_file,a.checkpoint,a.data_config,device); mb=max(1,a.micro_batch)
    all_rows=[]; all_dims=[]
    for obj in objectives:
        for s in range(0,len(ev),mb):
            sub=ev[s:s+mb]; pts,fts,vec,msk,metas=build_batch(sub,device,dc); model.zero_grad(set_to_none=True)
            tr=ClassifierTracer(); tr.attach(model); logits=model(pts,fts,vec,msk); J=obj_value(logits,metas,obj)
            if J is not None:
                J.backward(); rows,dims=aggregate(tr.records,metas,obj,len(sub)/max(1,len(ev))); all_rows+=rows; all_dims+=dims
            tr.close(); del pts,fts,vec,msk,logits,J,tr; gc.collect();
            if device.type=='cuda': torch.cuda.empty_cache()
    summ=summarize(all_rows,['objective','module','module_type','tensor','analysis_group']); dims=summarize_dims(all_dims); lin=final_linear_exact(model,a.src_label,a.tgt_label)
    wcsv(a.out_summary,summ); wcsv(a.out_dims,dims); wcsv(a.out_linear,lin); wjson(a.out_json,{'ok':True,'events':len(ev),'rows':len(all_rows),'summary_rows':len(summ),'dim_rows':len(dims),'linear_rows':len(lin),'src_label':a.src_label,'tgt_label':a.tgt_label,'top':summ[:40]})
    lines=['# PART_CLASSIFIER_LOGIT_DECODER_REAL_CONTRACT_V1\n\nClassifier / CLS-logit decoder. Captures `mod.norm`, `mod.fc`, and final linear layers. Contribution is activation × gradient for `J`, plus exact final-linear target-source directions where available. This closes `CLS vector → class logits`.\n\n',f'- events: **{len(ev)}**\n',f'- rows: **{len(all_rows)}**\n',f'- summary_rows: **{len(summ)}**\n',f'- dim_rows: **{len(dims)}**\n',f'- src_label: `{a.src_label}`\n',f'- tgt_label: `{a.tgt_label}`\n\n','## Top classifier/norm module contributions\n']
    lines.append(mdtab(['rank','objective','module','type','tensor','group','mean_score','mean_abs','act_norm','grad_norm'],[[i+1,r['objective'],r['module'],r['module_type'],r['tensor'],r['analysis_group'],fmt(r['mean_score']),fmt(r['mean_abs_score']),fmt(r['mean_act_norm']),fmt(r['mean_grad_norm'])] for i,r in enumerate(summ[:80])]))
    lines.append('\n## Top classifier dimensions\n')
    lines.append(mdtab(['rank','objective','module','tensor','group','dim','mean_contrib','mean_abs','act','grad'],[[i+1,r['objective'],r['module'],r['tensor'],r['analysis_group'],r['dim'],fmt(r['mean_contrib']),fmt(r['mean_abs_contrib']),fmt(r['mean_activation']),fmt(r['mean_grad'])] for i,r in enumerate(dims[:100])]))
    lines.append('\n## Exact final linear target-source direction\n')
    lines.append(mdtab(['rank','module','dim','src','tgt','W_tgt_minus_src','bias_tgt_minus_src'],[[i+1,r['module'],r['dim'],r.get('src_label',''),r.get('tgt_label',''),fmt(r.get('weight_tgt_minus_src',r.get('legacy_weight_tbl_minus_hqql'))),fmt(r.get('bias_tgt_minus_src',r.get('legacy_bias_tbl_minus_hqql')))] for i,r in enumerate(lin[:40])]))
    lines.append('\n## Formula\n\n```text\nz = norm(cls_token)\nlogits = fc(z)\nCLASSIFIER_PATH(dim) = z_dim * dJ/dz_dim\nFINAL_LINEAR_DIR(dim) = W[tgt,dim] - W[src,dim]\npositive supports J = target-source; negative resists it.\n```\n')
    Path(a.out_md).parent.mkdir(parents=True,exist_ok=True); Path(a.out_md).write_text(''.join(lines),encoding='utf-8')
    print(json.dumps({'ok':True,'events':len(ev),'rows':len(all_rows),'summary_rows':len(summ),'src_label':a.src_label,'tgt_label':a.tgt_label,'out_md':a.out_md},indent=2))
if __name__=='__main__': main()
