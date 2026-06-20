#!/usr/bin/env python3
import argparse, csv, json, sys, gc
from pathlib import Path
from collections import defaultdict
import torch

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from tools.part_attention_supertrace_real_contract_v1 import LABELS, load_model, build_batch, wcsv, wjson
from tools.part_exact_route_patch_real_contract_v1 import role_positions

HQQL=LABELS.index('label_Hqql'); TBL=LABELS.index('label_Tbl')
GROUPS=['A_Hqql_correct','B_Hqql_to_Tbl','C_Tbl_correct','D_Tbl_to_Hqql']

def f(x,d=0.0):
    try:
        if x is None or x=='': return d
        return float(x)
    except Exception:
        return d

def fmt(x):
    try: x=float(x)
    except Exception: return 'n/a'
    return f'{x:.3e}' if abs(x)>0 and (abs(x)<1e-3 or abs(x)>1e4) else f'{x:.4f}'

def rcsv(p):
    p=Path(p)
    if not p.exists(): return []
    with p.open(newline='',encoding='utf-8') as h: return list(csv.DictReader(h))

def events(path,n):
    by=defaultdict(list)
    for r in rcsv(path): by[r['analysis_group']].append(r)
    out=[]
    for g in GROUPS: out+=by[g][:n]
    return out

def split_head(hid):
    if '.h' not in hid: return hid,-1
    m,h=hid.rsplit('.h',1); return m,int(h)

def choose(rows,total=24):
    order=['causal_candidate','B_Tbl_push_read_write','B_Tbl_resist_or_protective_read_write','high_gradient_write_node']
    out=[]; seen=set()
    for diag in order:
        xs=[r for r in rows if r.get('diagnosis')==diag]
        xs.sort(key=lambda r:f(r.get('evidence_score')),reverse=True)
        for r in xs:
            k=(r.get('head_id',''),r.get('pair_role',''))
            if k in seen or not k[0] or '<-' not in k[1]: continue
            out.append(r); seen.add(k)
            if len(out)>=total: return out
    xs=sorted(rows,key=lambda r:f(r.get('evidence_score')),reverse=True)
    for r in xs:
        k=(r.get('head_id',''),r.get('pair_role',''))
        if k in seen or not k[0] or '<-' not in k[1]: continue
        out.append(r); seen.add(k)
        if len(out)>=total: break
    return out

class PairBias:
    def __init__(self,module,head,pair,metas,bias):
        self.module=module; self.head=int(head); self.qr,self.kr=pair.split('<-',1); self.metas=metas; self.bias=float(bias); self.h=None; self.hits=0
    def hook(self,m,args,kw):
        q,k,v=args[0],args[1],args[2]; H=int(m.num_heads)
        legacy=hasattr(m,'in_proj_weight') and not hasattr(m,'in_proj')
        if legacy:
            T,B,_=q.shape; S=k.shape[0]; patch=torch.zeros((B*H,T,S),device=q.device,dtype=q.dtype)
        else:
            B,T,_=q.shape; S=k.shape[1]; patch=torch.zeros((B,H,T,S),device=q.device,dtype=q.dtype)
        hits=0
        for bi,meta in enumerate(self.metas):
            for qi in role_positions(meta,self.qr,T,True):
                for ki in role_positions(meta,self.kr,S,False):
                    if legacy: patch[bi*H+self.head,qi,ki]+=self.bias
                    else: patch[bi,self.head,qi,ki]+=self.bias
                    hits+=1
        self.hits+=hits
        if hits==0: return args,kw
        base=kw.get('attn_mask')
        if base is None:
            kw['attn_mask']=patch; return args,kw
        if base.dtype==torch.bool:
            basef=torch.zeros_like(base,dtype=q.dtype).masked_fill(base,-abs(self.bias))
        else:
            basef=base.to(dtype=q.dtype)
        if legacy:
            if basef.ndim==2: basef=basef.view(1,basef.shape[-2],basef.shape[-1]).expand(B*H,T,S)
            elif basef.ndim==4: basef=basef.reshape(B*H,basef.shape[-2],basef.shape[-1])
        else:
            if basef.ndim==2: basef=basef.view(1,1,basef.shape[-2],basef.shape[-1]).expand(B,H,T,S)
            elif basef.ndim==3 and basef.shape[0]==B*H: basef=basef.view(B,H,basef.shape[-2],basef.shape[-1])
            elif basef.ndim==3 and basef.shape[0]==B: basef=basef.view(B,1,basef.shape[-2],basef.shape[-1]).expand(B,H,T,S)
        kw['attn_mask']=basef+patch if basef.shape==patch.shape else base
        return args,kw
    def attach(self,model):
        for name,m in model.named_modules():
            if name==self.module:
                self.h=m.register_forward_pre_hook(self.hook,with_kwargs=True); return
        raise RuntimeError('module not found '+self.module)
    def close(self):
        if self.h: self.h.remove(); self.h=None

def forward(model,batch,patch=None):
    if patch: patch.attach(model)
    pts,fts,vec,msk=batch
    with torch.no_grad(): out=model(pts,fts,vec,msk).detach().cpu()
    hits=patch.hits if patch else 0
    if patch: patch.close()
    return out,hits

def mets(logits,metas):
    pred=logits.argmax(1).tolist(); h=logits[:,HQQL].float(); t=logits[:,TBL].float()
    d=defaultdict(lambda:{'n':0,'m':0.0,'tbl':0})
    for i,m in enumerate(metas):
        g=m['analysis_group']; d[g]['n']+=1; d[g]['m']+=float(t[i]-h[i]); d[g]['tbl']+=int(pred[i]==TBL)
    return {g:{'n':x['n'],'margin':x['m']/max(1,x['n']),'tbl_rate':x['tbl']/max(1,x['n'])} for g,x in d.items()}

def mdtab(headers,rows):
    if not rows: return '_No rows._\n'
    return '\n'.join(['| '+' | '.join(headers)+' |','| '+' | '.join(['---']*len(headers))+' |']+['| '+' | '.join(str(x) for x in r)+' |' for r in rows])+'\n'

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--groups-csv',default='reports/latest/tables/part_hqql_tbl_groups_direct_replay_v1.csv')
    ap.add_argument('--candidates-csv',default='reports/latest/tables/part_discovery_candidates_real_contract_v1.csv')
    ap.add_argument('--network-file',default='external/particle_transformer/networks/example_ParticleTransformer_legacy.py')
    ap.add_argument('--checkpoint',default='external/particle_transformer/models/ParT_kinpid.pt')
    ap.add_argument('--data-config',default='external/particle_transformer/data/JetClass/JetClass_kinpid.yaml')
    ap.add_argument('--events-per-group',type=int,default=64); ap.add_argument('--micro-batch',type=int,default=8)
    ap.add_argument('--max-candidates',type=int,default=24); ap.add_argument('--strengths',default='20,40,80')
    ap.add_argument('--device',default='cuda' if torch.cuda.is_available() else 'cpu')
    ap.add_argument('--out-md',default='reports/latest/PART_CANDIDATE_PAIR_VALIDATION_V1.md')
    ap.add_argument('--out-rows',default='reports/latest/tables/part_candidate_pair_validation_v1_rows.csv')
    ap.add_argument('--out-summary',default='reports/latest/tables/part_candidate_pair_validation_v1_summary.csv')
    ap.add_argument('--out-json',default='manifests/latest/part_candidate_pair_validation_v1.json')
    a=ap.parse_args(); strengths=[float(x) for x in a.strengths.split(',') if x.strip()]
    ev=events(a.groups_csv,a.events_per_group); cand=choose(rcsv(a.candidates_csv),a.max_candidates)
    device=torch.device(a.device); model,dc=load_model(a.network_file,a.checkpoint,a.data_config,device); mb=max(1,a.micro_batch)
    base=[]; metas_all=[]
    for s in range(0,len(ev),mb):
        pts,fts,vec,msk,metas=build_batch(ev[s:s+mb],device,dc); logits,_=forward(model,(pts,fts,vec,msk)); base.append(logits); metas_all+=metas
        del pts,fts,vec,msk; gc.collect();
        if device.type=='cuda': torch.cuda.empty_cache()
    base=torch.cat(base,0); bm=mets(base,metas_all); rows=[]
    for ci,c in enumerate(cand,1):
        mod,head=split_head(c.get('head_id','')); pair=c.get('pair_role','')
        for st in strengths:
            for action,sgn in [('down',-1.0),('up',1.0)]:
                chunks=[]; hits=0
                for s in range(0,len(ev),mb):
                    sub=ev[s:s+mb]; pts,fts,vec,msk,metas=build_batch(sub,device,dc)
                    patch=PairBias(mod,head,pair,metas,sgn*st); logits,h=forward(model,(pts,fts,vec,msk),patch); chunks.append(logits); hits+=h
                    del pts,fts,vec,msk,patch; gc.collect();
                    if device.type=='cuda': torch.cuda.empty_cache()
                pm=mets(torch.cat(chunks,0),metas_all)
                r={'candidate_rank':ci,'diagnosis':c.get('diagnosis',''),'head_id':c.get('head_id',''),'pair_role':pair,'action':action,'strength':st,'patch_hits':hits,'B_write':c.get('B_write_dot_grad',''),'B_AxGrad':c.get('B_AxGrad',''),'rules':c.get('compiled_rule_count',''),'evidence_score':c.get('evidence_score','')}
                for g in GROUPS:
                    r[g+'_delta_margin']=pm.get(g,{}).get('margin',0)-bm.get(g,{}).get('margin',0)
                    r[g+'_delta_tbl_pred']=pm.get(g,{}).get('tbl_rate',0)-bm.get(g,{}).get('tbl_rate',0)
                sign=f(c.get('B_write_dot_grad')) if abs(f(c.get('B_write_dot_grad')))>=abs(f(c.get('B_AxGrad'))) else f(c.get('B_AxGrad'))
                if sign>0: ok=(action=='down' and r['B_Hqql_to_Tbl_delta_margin']<0) or (action=='up' and r['B_Hqql_to_Tbl_delta_margin']>0)
                elif sign<0: ok=(action=='down' and r['B_Hqql_to_Tbl_delta_margin']>0) or (action=='up' and r['B_Hqql_to_Tbl_delta_margin']<0)
                else: ok=False
                r['direction_ok']=int(ok); r['B_effect_abs']=abs(r['B_Hqql_to_Tbl_delta_margin']); r['B_flip_abs']=abs(r['B_Hqql_to_Tbl_delta_tbl_pred']); rows.append(r)
    by=defaultdict(list)
    for r in rows: by[(r['head_id'],r['pair_role'],r['diagnosis'],r['action'])].append(r)
    summ=[]
    for (hid,pair,diag,action),xs in by.items():
        best=max(xs,key=lambda r:r['B_effect_abs']+2*r['B_flip_abs']); ok=sum(int(x['direction_ok']) for x in xs)
        summ.append({'head_id':hid,'pair_role':pair,'diagnosis':diag,'action':action,'runs':len(xs),'direction_ok_runs':ok,'best_strength':best['strength'],'best_B_delta_margin':best['B_Hqql_to_Tbl_delta_margin'],'best_B_delta_tbl_pred':best['B_Hqql_to_Tbl_delta_tbl_pred'],'A_damage_abs':abs(best['A_Hqql_correct_delta_margin']),'C_damage_abs':abs(best['C_Tbl_correct_delta_margin']),'B_write':best['B_write'],'B_AxGrad':best['B_AxGrad'],'rules':best['rules'],'score':(1 if ok else 0)*(best['B_effect_abs']+2*best['B_flip_abs'])-0.25*(abs(best['A_Hqql_correct_delta_margin'])+abs(best['C_Tbl_correct_delta_margin']))})
    summ.sort(key=lambda r:f(r['score']),reverse=True)
    wcsv(a.out_rows,rows); wcsv(a.out_summary,summ); wjson(a.out_json,{'ok':True,'events':len(ev),'candidates_tested':len(cand),'rows':len(rows),'summary_rows':len(summ),'top':summ[:40]})
    lines=['# PART_CANDIDATE_PAIR_VALIDATION_V1\n\nExact head+role-pair validation over discovery candidates. It applies down/up attention-logit interventions to the exact candidate pair and checks whether B_Hqql_to_Tbl margin moves in the expected direction.\n\n',f'- events: **{len(ev)}**\n',f'- candidates_tested: **{len(cand)}**\n',f'- rows: **{len(rows)}**\n\n','## Top validated pair candidates\n']
    lines.append(mdtab(['rank','head','pair','diag','action','ok','best_s','B_delta','B_flip','A_dmg','C_dmg','B_write','Agrad','rules','score'],[[i+1,r['head_id'],r['pair_role'],r['diagnosis'],r['action'],r['direction_ok_runs'],fmt(r['best_strength']),fmt(r['best_B_delta_margin']),fmt(r['best_B_delta_tbl_pred']),fmt(r['A_damage_abs']),fmt(r['C_damage_abs']),fmt(r['B_write']),fmt(r['B_AxGrad']),r['rules'],fmt(r['score'])] for i,r in enumerate(summ[:60])]))
    Path(a.out_md).write_text(''.join(lines),encoding='utf-8'); print(json.dumps({'ok':True,'rows':len(rows),'summary_rows':len(summ),'out_md':a.out_md},indent=2))
if __name__=='__main__': main()
