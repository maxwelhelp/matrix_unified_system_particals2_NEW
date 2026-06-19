#!/usr/bin/env python3
import argparse, csv, json, sys, gc
from pathlib import Path
import torch

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from data.jetclass_tiny_loader_v3_official import LABELS
from tools.particlenet_all_head_supertrace_v1 import make_model, load_balanced, slice_batch, gated_forward, collect_gate_grads, add_grad_accum, grad_rows_from_accum


def mkdir(p): Path(p).mkdir(parents=True,exist_ok=True)
def fmt(x):
    try: x=float(x)
    except Exception: return 'n/a'
    return f'{x:.3e}' if abs(x)>0 and (abs(x)<1e-3 or abs(x)>1e4) else f'{x:.4f}'
def wjson(p,o): p=Path(p); mkdir(p.parent); p.write_text(json.dumps(o,indent=2,ensure_ascii=False),encoding='utf-8')
def wcsv(p,rows):
    p=Path(p); mkdir(p.parent); keys=[]; seen=set()
    for r in rows:
        for k in r:
            if k not in seen: keys.append(k); seen.add(k)
    with p.open('w',encoding='utf-8',newline='') as f:
        wr=csv.DictWriter(f,fieldnames=keys); wr.writeheader()
        for r in rows: wr.writerow({k:r.get(k,'') for k in keys})
def table(h,rs):
    if not rs: return '_No rows._\n'
    return '\n'.join(['| '+' | '.join(h)+' |','| '+' | '.join(['---']*len(h))+' |']+['| '+' | '.join(str(x) for x in r)+' |' for r in rs])+'\n'

def parse_classes(s):
    out=[]
    for t in str(s).split(','):
        t=t.strip()
        if not t: continue
        if t.isdigit(): out.append(int(t)); continue
        if not t.startswith('label_'): t='label_'+t
        out.append(LABELS.index(t))
    return list(dict.fromkeys(out))

def baseline(model,batch,mb,device):
    chunks=[]; B=int(batch['y'].shape[0])
    with torch.no_grad():
        for s in range(0,B,mb):
            e=min(B,s+mb); b=slice_batch(batch,s,e)
            chunks.append(model(b['points'],b['features'],b['mask']).detach().cpu())
            if device.startswith('cuda'): torch.cuda.empty_cache()
    return torch.cat(chunks,0)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--checkpoint',default='local_checkpoints/part/ParticleNet_kinpid.pt')
    ap.add_argument('--data-dir',default=str(Path.home()/'Рабочий стол/jetclass_tiny_balanced'))
    ap.add_argument('--mode',default='kinpid',choices=['kin','kinpid','full'])
    ap.add_argument('--samples-per-file',type=int,default=256)
    ap.add_argument('--max-files',type=int,default=20)
    ap.add_argument('--head-groups',type=int,default=8)
    ap.add_argument('--micro-batch',type=int,default=32)
    ap.add_argument('--classes',default='Hqql,Tbl,H4q,QCD,Wqq,Zqq,Hcc')
    ap.add_argument('--device',default='cuda' if torch.cuda.is_available() else 'cpu')
    ap.add_argument('--out-dir',default='runs/class_specific_all_head_gradients_v1')
    a=ap.parse_args(); out=Path(a.out_dir); mkdir(out/'tables')
    model,res,_=make_model(a.checkpoint,a.mode,a.device)
    batch=load_balanced(a.data_dir,mode=a.mode,samples_per_file=a.samples_per_file,max_files=a.max_files,device=a.device)
    B=int(batch['y'].shape[0]); mb=max(1,int(a.micro_batch))
    base=baseline(model,batch,mb,a.device); pred=base.argmax(-1); y=batch['y'].detach().cpu()
    classes=parse_classes(a.classes)
    rows=[]; summ=[]
    for cid in classes:
        mask_all=(y==cid); n=int(mask_all.sum())
        if n<=0:
            summ.append({'class_id':cid,'class_label':LABELS[cid],'n':0,'status':'empty'}); continue
        acc={}; obj_mean=0.0
        for s in range(0,B,mb):
            e=min(B,s+mb); local=mask_all[s:e]
            if int(local.sum())<=0: continue
            b=slice_batch(batch,s,e); model.zero_grad(set_to_none=True)
            logits,gates,meta,_=gated_forward(model,b,a.head_groups)
            lm=local.to(a.device); obj=logits[lm,cid].mean(); obj.backward()
            add_grad_accum(acc,collect_gate_grads(gates,meta),int(local.sum())/n)
            obj_mean += float(obj.detach().cpu())*int(local.sum())/n
            del logits,gates,meta,obj; gc.collect()
            if a.device.startswith('cuda'): torch.cuda.empty_cache()
        grads=grad_rows_from_accum(acc)
        for rank,r in enumerate(grads,1):
            rr=dict(r); rr.update({'rank':rank,'class_id':cid,'class_label':LABELS[cid],'n':n,'objective_logit_mean':obj_mean}); rows.append(rr)
        summ.append({'class_id':cid,'class_label':LABELS[cid],'n':n,'top_head':grads[0]['head_id'] if grads else '', 'top_abs_grad':grads[0]['abs_grad'] if grads else 0.0,'objective_logit_mean':obj_mean,'status':'ok'})
    wcsv(out/'tables/class_specific_head_gradients.csv',rows)
    wcsv(out/'tables/class_specific_head_gradient_summary.csv',summ)
    summary={'ok':True,'n_events':B,'baseline_acc':float((pred==y).float().mean()),'classes':[LABELS[c] for c in classes],'head_groups':a.head_groups,'micro_batch':mb,'summary_rows':summ,'missing':list(res.missing_keys),'unexpected':list(res.unexpected_keys)}
    wjson(out/'class_specific_all_head_gradients_v1.json',summary)
    md=['# Class Specific All-Head Gradients v1\n\n',f"n_events={B} baseline_acc={fmt(summary['baseline_acc'])}\n\n",'## Summary\n',table(['class','n','top_head','top_abs_grad','obj_logit'],[[r['class_label'],r['n'],r.get('top_head',''),fmt(r.get('top_abs_grad')),fmt(r.get('objective_logit_mean'))] for r in summ])]
    for cid in classes:
        xs=[r for r in rows if int(r['class_id'])==cid][:8]
        md += [f"\n## {LABELS[cid]} top heads\n", table(['rank','head','grad','abs_grad'],[[r['rank'],r['head_id'],fmt(r['grad']),fmt(r['abs_grad'])] for r in xs])]
    (out/'CLASS_SPECIFIC_ALL_HEAD_GRADIENTS_V1.md').write_text(''.join(md),encoding='utf-8')
    print(json.dumps(summary,indent=2,ensure_ascii=False)[:20000])

if __name__=='__main__': main()
