#!/usr/bin/env python3
import argparse, csv, json, math, gc, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from collections import defaultdict, Counter
import torch
import torch.nn.functional as F

from tools.part_attention_supertrace_real_contract_v1 import (
    LABELS, SRC, TGT, load_groups, load_model, build_batch, wcsv, wjson, mdtab
)

HQL=LABELS.index(SRC); TBL=LABELS.index(TGT)

def split_ranges(C,H):
    return [(h,(C*h)//H,(C*(h+1))//H) for h in range(H) if (C*h)//H < (C*(h+1))//H]

def slice_rows(rows,n):
    by=defaultdict(list)
    for r in rows: by[r['analysis_group']].append(r)
    out=[]
    for g in ['A_Hqql_correct','B_Hqql_to_Tbl','C_Tbl_correct','D_Tbl_to_Hqql']:
        out += by[g][:n]
    return out

class OutputGateTrace:
    def __init__(self):
        self.gates={}; self.meta={}; self.hooks=[]
    def hook(self,name):
        def fn(m,inp,out):
            x=out[0] if isinstance(out,tuple) else out
            if not torch.is_tensor(x) or x.ndim!=3: return out
            H=int(getattr(m,'num_heads',8)); C=x.shape[-1]
            ranges=split_ranges(C,H)
            g=torch.ones(len(ranges),device=x.device,requires_grad=True)
            self.gates[name]=g; self.meta[name]=[(i,a,b) for i,a,b in ranges]
            parts=[]; last=0
            for idx,a,b in ranges:
                if a>last: parts.append(x[...,last:a])
                parts.append(x[...,a:b]*g[idx])
                last=b
            if last<C: parts.append(x[...,last:C])
            y=torch.cat(parts,dim=-1)
            if isinstance(out,tuple): return (y,)+out[1:]
            return y
        return fn
    def attach(self,model):
        for name,m in model.named_modules():
            if hasattr(m,'num_heads') and hasattr(m,'in_proj') and hasattr(m,'head_dim'):
                self.hooks.append(m.register_forward_hook(self.hook(name)))
    def close(self):
        for h in self.hooks: h.remove()
        self.hooks=[]
    def rows(self,weight,objective):
        out=[]
        for name,g in self.gates.items():
            grad=g.grad.detach().cpu() if g.grad is not None else torch.zeros_like(g.detach().cpu())
            for j,(hi,a,b) in enumerate(self.meta[name]):
                val=float(grad[j])*weight
                out.append({'module':name,'head':hi,'channels':f'{a}:{b}','objective':objective,'grad':val,'abs_grad':abs(val),'positive_grad':max(0.0,val),'negative_grad':min(0.0,val)})
        return out

def add_acc(acc,rows):
    for r in rows:
        k=(r['module'],r['head'],r['channels'],r['objective'])
        acc[k]+=r['grad']

def acc_rows(acc):
    out=[]
    for (m,h,ch,obj),g in acc.items():
        out.append({'module':m,'head':h,'channels':ch,'objective':obj,'grad':g,'abs_grad':abs(g),'positive_grad':max(0.0,g),'negative_grad':min(0.0,g)})
    return sorted(out,key=lambda r:r['abs_grad'],reverse=True)

def obj_vec(logits, metas):
    vals=[]
    for i,m in enumerate(metas):
        g=m['analysis_group']
        if g in ('B_Hqql_to_Tbl','C_Tbl_correct'):
            vals.append(logits[i,TBL]-logits[i,HQL])
        else:
            vals.append(logits[i,HQL]-logits[i,TBL])
    return torch.stack(vals)

def load_rules(path):
    p=Path(path)
    if not p.exists(): return []
    obj=json.loads(p.read_text(encoding='utf-8'))
    return obj.get('rules',[])

def join_rules(gate_rows,rules):
    best={}
    for r in gate_rows:
        best[(r['module'],str(r['head']))]=r
    out=[]
    for rule in rules:
        g=best.get((rule.get('module'),str(rule.get('head'))))
        if not g: continue
        rr=dict(rule)
        rr.update({'gate_grad':g['grad'],'gate_abs_grad':g['abs_grad'],'gate_positive_grad':g['positive_grad'],'gate_negative_grad':g['negative_grad'],'gate_channels':g['channels']})
        out.append(rr)
    return sorted(out,key=lambda r:abs(float(r.get('gate_grad',0))),reverse=True)

def table(h,rs):
    if not rs: return '_No rows._\n'
    return '\n'.join(['| '+' | '.join(h)+' |','| '+' | '.join(['---']*len(h))+' |']+['| '+' | '.join(str(x) for x in r)+' |' for r in rs])+'\n'

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--events-per-group',type=int,default=64)
    ap.add_argument('--micro-batch',type=int,default=8)
    ap.add_argument('--device',default='cuda' if torch.cuda.is_available() else 'cpu')
    ap.add_argument('--groups-csv',default='reports/latest/tables/part_hqql_tbl_groups_real_contract_v1.csv')
    ap.add_argument('--rules-json',default='manifests/latest/part_real_contract_pseudocode_compiler_v1.json')
    ap.add_argument('--data-config',default='external/particle_transformer/data/JetClass/JetClass_kinpid.yaml')
    ap.add_argument('--checkpoint',default='external/particle_transformer/models/ParT_kinpid.pt')
    ap.add_argument('--network-file',default='external/particle_transformer/networks/example_ParticleTransformer_legacy.py')
    ap.add_argument('--out-md',default='reports/latest/PART_ALL_HEAD_GATE_TRACE_REAL_CONTRACT_V1.md')
    ap.add_argument('--out-gates',default='reports/latest/tables/part_all_head_gate_gradients_real_contract_v1.csv')
    ap.add_argument('--out-join',default='reports/latest/tables/part_rule_gate_join_real_contract_v1.csv')
    ap.add_argument('--out-json',default='manifests/latest/part_all_head_gate_trace_real_contract_v1.json')
    a=ap.parse_args()
    rows,_=load_groups(a.groups_csv,'reports/latest/part_weaver_predict_smoke_v3_*.root','manifests/latest/part_weaver_predict_smoke_v3_args.txt',a.events_per_group,a.events_per_group,a.events_per_group,a.events_per_group)
    rows=slice_rows(rows,a.events_per_group)
    model,dc=load_model(a.network_file,a.checkpoint,a.data_config,torch.device(a.device))
    mb=max(1,a.micro_batch); acc=defaultdict(float); base_logits=[]; ys=[]
    for s in range(0,len(rows),mb):
        sub=rows[s:s+mb]
        pts,fts,vec,msk,meta=build_batch(sub,torch.device(a.device),dc)
        with torch.no_grad():
            bl=model(pts,fts,vec,msk).detach().cpu(); base_logits.append(bl)
        model.zero_grad(set_to_none=True)
        tr=OutputGateTrace(); tr.attach(model)
        logits=model(pts,fts,vec,msk)
        obj=obj_vec(logits,meta).mean()
        obj.backward()
        tr.close()
        add_acc(acc,tr.rows(len(sub)/max(1,len(rows)),'signed_Hqql_Tbl_margin'))
        for m in meta: ys.append(m['analysis_group'])
        del pts,fts,vec,msk,logits,obj
        if a.device.startswith('cuda'): torch.cuda.empty_cache()
        gc.collect()
    gates=acc_rows(acc)
    rules=load_rules(a.rules_json)
    joined=join_rules(gates,rules)
    wcsv(a.out_gates,gates); wcsv(a.out_join,joined)
    top_pos=sorted(gates,key=lambda r:r['positive_grad'],reverse=True)[:20]
    top_neg=sorted(gates,key=lambda r:r['negative_grad'])[:20]
    cnt=Counter(ys)
    out={'ok':True,'events':len(rows),'group_counts':dict(cnt),'gate_rows':len(gates),'joined_rules':len(joined),'checkpoint':a.checkpoint,'data_config':a.data_config,'note':'ParT all-head differentiable output-gate trace. Gates are applied to attention module output head/channel slices; next version should patch exact pre-out-proj head routes.'}
    wjson(a.out_json,out)
    md=['# PART_ALL_HEAD_GATE_TRACE_REAL_CONTRACT_V1\n\n','ParT real-contract all-head differentiable gate trace. This ports the ParticleNet all-head gate idea onto the current `ParT_kinpid` run.\n\n',f'- events: **{len(rows)}**\n- groups: `{dict(cnt)}`\n- checkpoint: `{a.checkpoint}`\n- data_config: `{a.data_config}`\n- gate rows: **{len(gates)}**\n- joined pseudocode rules: **{len(joined)}**\n\n','## Important status\n\nThis is a real differentiable all-head trace, but v1 gates attention module output head/channel slices. It is stronger than static route scoring, but the next version should patch exact pre-output-projection attention head routes.\n\n','## Top positive gates\n',table(['module','head','channels','grad','abs'],[[r['module'],r['head'],r['channels'],f"{r['grad']:.5e}",f"{r['abs_grad']:.5e}"] for r in top_pos]),'\n## Top negative gates\n',table(['module','head','channels','grad','abs'],[[r['module'],r['head'],r['channels'],f"{r['grad']:.5e}",f"{r['abs_grad']:.5e}"] for r in top_neg]),'\n## Top pseudocode rules with differentiable gate support\n',table(['rule','module','head','route','type','rule_strength','gate_grad'],[[r.get('id'),r.get('module'),r.get('head'),r.get('pair'),r.get('type'),round(float(r.get('strength',0)),5),f"{float(r.get('gate_grad',0)):.5e}"] for r in joined[:30]]),'\n## Next\n\nRun exact route patch for the top joined rules: R001_B_to_Tbl, R002_B_to_Tbl, R003_B_to_Tbl, and the top A_protect rules.\n']
    Path(a.out_md).write_text(''.join(md),encoding='utf-8')
    print(json.dumps(out,indent=2,ensure_ascii=False))
if __name__=='__main__': main()
