#!/usr/bin/env python3
import argparse, csv, gc, json, re, sys
from pathlib import Path
from collections import defaultdict
import torch

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from tools.part_attention_supertrace_real_contract_v1 import LABELS, load_model, build_batch, wcsv, wjson
from tools.part_exact_route_patch_real_contract_v1 import role_positions

HQQL=LABELS.index('label_Hqql'); TBL=LABELS.index('label_Tbl')
GROUPS=['A_Hqql_correct','B_Hqql_to_Tbl','C_Tbl_correct','D_Tbl_to_Hqql']
ROLES=['CLS','electron','muon','charged_hadron','neutral_hadron','photon']

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

def to_btc(x,B):
    if not torch.is_tensor(x) or x.ndim!=3: return None
    if x.shape[0]==B: return x
    if x.shape[1]==B: return x.permute(1,0,2)
    return None

class ResidualTracerV2:
    def __init__(self,metas):
        self.metas=metas; self.records=[]; self.handles=[]; self.missed=[]
    def want(self,name,m):
        return re.match(r'^mod\.blocks\.\d+$',name) or re.match(r'^mod\.cls_blocks\.\d+$',name)
    def hook(self,name):
        def fn(module,args,kwargs,out):
            B=len(self.metas)
            y=out[0] if isinstance(out,tuple) else out
            # Particle blocks: residual=input x. CLS blocks: residual=input x_cls.
            if re.match(r'^mod\.cls_blocks\.\d+$',name):
                x=kwargs.get('x_cls', None)
                kind='cls'
            else:
                x=args[0] if args else kwargs.get('x', None)
                kind='particle'
            xb=to_btc(x,B); yb=to_btc(y,B)
            if xb is None or yb is None or xb.shape!=yb.shape:
                self.missed.append({'name':name,'kind':kind,'x_shape':str(tuple(x.shape)) if torch.is_tensor(x) else str(type(x)),'y_shape':str(tuple(y.shape)) if torch.is_tensor(y) else str(type(y))})
                return
            y.retain_grad()
            self.records.append({'name':name,'kind':kind,'x':xb.detach(),'y_tensor':y,'y':yb,'shape':tuple(yb.shape)})
        return fn
    def attach(self,model):
        for name,m in model.named_modules():
            if self.want(name,m): self.handles.append(m.register_forward_hook(self.hook(name),with_kwargs=True))
        if not self.handles: raise RuntimeError('no residual block modules hooked')
    def close(self):
        for h in self.handles: h.remove()
        self.handles=[]

def aggregate(records,metas,objective,weight):
    rows=[]; role_rows=[]; B=len(metas)
    for rec in records:
        grad=rec['y_tensor'].grad
        if grad is None: continue
        gb=to_btc(grad,B)
        if gb is None: continue
        delta=(rec['y']-rec['x']).detach().float().cpu(); gb=gb.detach().float().cpu(); token_score=(delta*gb).sum(-1)
        for bi,m in enumerate(metas):
            g=m['analysis_group']; T=token_score.shape[1]
            rows.append({'objective':objective,'module':rec['name'],'kind':rec['kind'],'analysis_group':g,'event_score':float(token_score[bi].sum()),'abs_event_score':float(token_score[bi].abs().sum()),'mean_delta_norm':float(torch.sqrt((delta[bi]**2).sum(-1)+1e-12).mean()),'mean_grad_norm':float(torch.sqrt((gb[bi]**2).sum(-1)+1e-12).mean())})
            for role in ROLES:
                pos=role_positions(m,role,T,True)
                if not pos: continue
                vals=token_score[bi,pos]
                role_rows.append({'objective':objective,'module':rec['name'],'kind':rec['kind'],'analysis_group':g,'role':role,'role_score':float(vals.mean()),'role_abs_score':float(vals.abs().mean()),'n_pos':len(pos)})
    return rows,role_rows

def summarize(rows,keys,score_key='event_score'):
    acc=defaultdict(lambda:{'n':0,'sum':0.0,'abs':0.0,'dn':0.0,'gn':0.0})
    for r in rows:
        k=tuple(r[x] for x in keys); a=acc[k]; a['n']+=1; a['sum']+=f(r.get(score_key)); a['abs']+=f(r.get('abs_'+score_key,''),abs(f(r.get(score_key))))
        if 'mean_delta_norm' in r: a['dn']+=f(r.get('mean_delta_norm'))
        if 'mean_grad_norm' in r: a['gn']+=f(r.get('mean_grad_norm'))
    out=[]
    for k,a in acc.items():
        n=max(1,a['n']); row={keys[i]:k[i] for i in range(len(keys))}; row.update({'n':a['n'],'mean_score':a['sum']/n,'mean_abs_score':a['abs']/n,'mean_delta_norm':a['dn']/n,'mean_grad_norm':a['gn']/n}); out.append(row)
    return sorted(out,key=lambda r:abs(f(r['mean_score']))+0.25*f(r['mean_abs_score']),reverse=True)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--groups-csv',default='reports/latest/tables/part_hqql_tbl_groups_direct_replay_v1.csv')
    ap.add_argument('--network-file',default='external/particle_transformer/networks/example_ParticleTransformer_legacy.py')
    ap.add_argument('--checkpoint',default='external/particle_transformer/models/ParT_kinpid.pt')
    ap.add_argument('--data-config',default='external/particle_transformer/data/JetClass/JetClass_kinpid.yaml')
    ap.add_argument('--events-per-group',type=int,default=32); ap.add_argument('--micro-batch',type=int,default=8)
    ap.add_argument('--objectives',default='signed_hqql_tbl,B_tbl_minus_hqql')
    ap.add_argument('--device',default='cuda' if torch.cuda.is_available() else 'cpu')
    ap.add_argument('--out-md',default='reports/latest/PART_RESIDUAL_PATH_TRACE_REAL_CONTRACT_V2.md')
    ap.add_argument('--out-summary',default='reports/latest/tables/part_residual_path_trace_summary_v2.csv')
    ap.add_argument('--out-role',default='reports/latest/tables/part_residual_path_trace_role_summary_v2.csv')
    ap.add_argument('--out-missed',default='reports/latest/tables/part_residual_path_trace_missed_v2.csv')
    ap.add_argument('--out-json',default='manifests/latest/part_residual_path_trace_real_contract_v2.json')
    a=ap.parse_args(); ev=select_events(a.groups_csv,a.events_per_group); objectives=[x.strip() for x in a.objectives.split(',') if x.strip()]
    device=torch.device(a.device); model,dc=load_model(a.network_file,a.checkpoint,a.data_config,device); mb=max(1,a.micro_batch)
    all_rows=[]; all_role=[]; missed=[]
    for obj in objectives:
        for s in range(0,len(ev),mb):
            sub=ev[s:s+mb]; pts,fts,vec,msk,metas=build_batch(sub,device,dc); model.zero_grad(set_to_none=True)
            tr=ResidualTracerV2(metas); tr.attach(model); logits=model(pts,fts,vec,msk); J=obj_value(logits,metas,obj)
            if J is not None:
                J.backward(); rows,roles=aggregate(tr.records,metas,obj,len(sub)/max(1,len(ev))); all_rows+=rows; all_role+=roles
            missed += tr.missed; tr.close(); del pts,fts,vec,msk,logits,J,tr; gc.collect();
            if device.type=='cuda': torch.cuda.empty_cache()
    summ=summarize(all_rows,['objective','module','kind','analysis_group']); role_summ=summarize(all_role,['objective','module','kind','analysis_group','role'],'role_score')
    wcsv(a.out_summary,summ); wcsv(a.out_role,role_summ); wcsv(a.out_missed,missed)
    kinds=defaultdict(int)
    for r in all_rows: kinds[r['kind']]+=1
    wjson(a.out_json,{'ok':True,'events':len(ev),'rows':len(all_rows),'summary_rows':len(summ),'role_rows':len(role_summ),'kind_rows':dict(kinds),'missed_rows':len(missed),'top':summ[:40]})
    lines=['# PART_RESIDUAL_PATH_TRACE_REAL_CONTRACT_V2\n\nResidual path composition trace with correct CLS-block residual capture. Particle blocks use residual `x`; CLS blocks use residual `x_cls`. Contribution is `dot(block_out - residual_in, dJ/dblock_out)`.\n\n',f'- events: **{len(ev)}**\n',f'- rows: **{len(all_rows)}**\n',f'- summary_rows: **{len(summ)}**\n',f'- kind_rows: `{dict(kinds)}`\n',f'- missed_rows: **{len(missed)}**\n\n','## Top residual block contributions\n']
    lines.append(mdtab(['rank','objective','module','kind','group','mean_score','mean_abs','delta_norm','grad_norm'],[[i+1,r['objective'],r['module'],r['kind'],r['analysis_group'],fmt(r['mean_score']),fmt(r['mean_abs_score']),fmt(r['mean_delta_norm']),fmt(r['mean_grad_norm'])] for i,r in enumerate(summ[:80])]))
    cls=[r for r in summ if r['kind']=='cls']
    lines.append('\n## CLS residual contributions\n')
    lines.append(mdtab(['rank','objective','module','group','mean_score','mean_abs','delta_norm','grad_norm'],[[i+1,r['objective'],r['module'],r['analysis_group'],fmt(r['mean_score']),fmt(r['mean_abs_score']),fmt(r['mean_delta_norm']),fmt(r['mean_grad_norm'])] for i,r in enumerate(cls[:40])]))
    lines.append('\n## Top role-level residual contributions\n')
    lines.append(mdtab(['rank','objective','module','kind','group','role','mean_score','mean_abs'],[[i+1,r['objective'],r['module'],r['kind'],r['analysis_group'],r['role'],fmt(r['mean_score']),fmt(r['mean_abs_score'])] for i,r in enumerate(role_summ[:100])]))
    lines.append('\n## Formula\n\n```text\nparticle block: R_l = block_l(x) - x\nCLS block:      R_l = block_l(x, x_cls) - x_cls\nPATH(l, role) = mean dot(R_l[token], dJ/d block_l_out[token])\npositive = residual update supports objective J\nnegative = residual update resists objective J\n```\n')
    Path(a.out_md).parent.mkdir(parents=True,exist_ok=True); Path(a.out_md).write_text(''.join(lines),encoding='utf-8')
    print(json.dumps({'ok':True,'events':len(ev),'rows':len(all_rows),'summary_rows':len(summ),'kind_rows':dict(kinds),'out_md':a.out_md},indent=2))
if __name__=='__main__': main()
