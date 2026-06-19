#!/usr/bin/env python3
import argparse, csv, json, sys, random
from pathlib import Path
import torch
import torch.nn.functional as F

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools.particle0_topk_controls_v2 import make_model, load_balanced, model_logits, real_mask, pt_values
from data.jetclass_tiny_loader_v3_official import LABELS


def mkdir(p): Path(p).mkdir(parents=True, exist_ok=True)
def fmt(x):
    try: x=float(x)
    except Exception: return 'n/a'
    return f'{x:.3e}' if abs(x)>0 and (abs(x)<1e-3 or abs(x)>1e4) else f'{x:.4f}'
def wjson(path,obj):
    p=Path(path); mkdir(p.parent); p.write_text(json.dumps(obj,indent=2,ensure_ascii=False),encoding='utf-8')
def wcsv(path,rows):
    p=Path(path); mkdir(p.parent)
    keys=[]; seen=set()
    for r in rows:
        for k in r:
            if k not in seen: keys.append(k); seen.add(k)
    with p.open('w',encoding='utf-8',newline='') as f:
        wr=csv.DictWriter(f,fieldnames=keys); wr.writeheader()
        for r in rows: wr.writerow({k:r.get(k,'') for k in keys})
def table(headers, rows):
    if not rows: return '_No rows._\n'
    out=['| '+' | '.join(headers)+' |','| '+' | '.join(['---']*len(headers))+' |']
    for r in rows: out.append('| '+' | '.join(str(x) for x in r)+' |')
    return '\n'.join(out)+'\n'


def clone_batch(batch):
    return {k:(v.clone() if torch.is_tensor(v) else v) for k,v in batch.items()}

def apply_perm(batch, idx):
    # idx shape [B,N], permutes last particle dimension for tensors with [B,C,N].
    b=clone_batch(batch)
    B,N=idx.shape
    for k in ['points','features','mask','vectors']:
        if k not in b or not torch.is_tensor(b[k]):
            continue
        v=b[k]
        if v.dim()==3 and v.shape[0]==B and v.shape[-1]==N:
            gather_idx=idx[:,None,:].expand(v.shape[0],v.shape[1],v.shape[2])
            b[k]=torch.gather(v,2,gather_idx)
    return b

def permutation_index(batch, mode, seed=123):
    m=real_mask(batch); B,N=m.shape; device=m.device
    base=torch.arange(N,device=device).unsqueeze(0).repeat(B,1)
    if mode=='identity':
        return base
    if mode=='reverse':
        return torch.flip(base,dims=[1])
    if mode=='particle0_to_end':
        return torch.cat([base[:,1:],base[:,:1]],dim=1)
    if mode=='particle0_to_middle':
        mid=N//2
        rest=base[:,1:]
        return torch.cat([rest[:,:mid],base[:,:1],rest[:,mid:]],dim=1)
    pt=pt_values(batch).masked_fill(~m,-1e30)
    if mode=='sort_pt_desc':
        return torch.argsort(pt,dim=1,descending=True)
    if mode=='sort_pt_asc':
        # Put padded invalid particles at the end after valid low-pt particles.
        pt2=pt.masked_fill(~m,1e30)
        return torch.argsort(pt2,dim=1,descending=False)
    if mode.startswith('random_shuffle'):
        rng=random.Random(seed)
        out=[]
        for i in range(B):
            inds=list(range(N)); rng.shuffle(inds); out.append(torch.tensor(inds,device=device,dtype=torch.long))
        return torch.stack(out,0)
    raise ValueError(f'unknown permutation mode {mode}')

def metrics(logits,y,base_logits,base_pred):
    pred=logits.argmax(-1)
    prob=F.softmax(logits.float(),-1)
    idx=base_pred[:,None]
    return {
        'acc':float((pred==y).float().mean()),
        'mean_conf':float(prob.gather(1,pred[:,None]).mean()),
        'pred_flip_rate':float((pred!=base_pred).float().mean()),
        'mean_abs_logit_diff':float((logits-base_logits).abs().mean()),
        'max_abs_logit_diff':float((logits-base_logits).abs().max()),
        'delta_base_pred_logit_mean':float(logits.gather(1,idx).mean()-base_logits.gather(1,idx).mean()),
    }

def class_rows(control, logits, y, base_logits, base_pred, base_acc_by_class):
    pred=logits.argmax(-1); rows=[]
    for c,lbl in enumerate(LABELS):
        cm=(y==c); n=int(cm.sum())
        if n==0: continue
        idx=base_pred[cm,None]
        acc=float((pred[cm]==y[cm]).float().mean())
        rows.append({
            'control':control,'class_id':c,'class_label':lbl,'n':n,
            'acc':acc,'acc_delta_from_baseline':acc-base_acc_by_class.get(c,acc),
            'pred_flip_rate':float((pred[cm]!=base_pred[cm]).float().mean()),
            'mean_abs_logit_diff':float((logits[cm]-base_logits[cm]).abs().mean()),
            'delta_base_pred_logit_mean':float(logits[cm].gather(1,idx).mean()-base_logits[cm].gather(1,idx).mean()),
        })
    return rows


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--checkpoint',default='local_checkpoints/part/ParticleNet_kinpid.pt')
    ap.add_argument('--data-dir',default=str(Path.home()/'Рабочий стол/jetclass_tiny_balanced'))
    ap.add_argument('--mode',default='kinpid',choices=['kin','kinpid','full'])
    ap.add_argument('--samples-per-file',type=int,default=256)
    ap.add_argument('--max-files',type=int,default=20)
    ap.add_argument('--micro-batch',type=int,default=128)
    ap.add_argument('--random-repeats',type=int,default=3)
    ap.add_argument('--seed',type=int,default=123)
    ap.add_argument('--device',default='cuda' if torch.cuda.is_available() else 'cpu')
    ap.add_argument('--out-dir',default='runs/particle_order_control_v1')
    args=ap.parse_args(); out=Path(args.out_dir); mkdir(out/'tables')
    model,res=make_model(args.checkpoint,args.mode,args.device)
    batch=load_balanced(args.data_dir,mode=args.mode,samples_per_file=args.samples_per_file,max_files=args.max_files,device=args.device)
    y=batch['y'].detach().cpu()
    base_logits=model_logits(model,batch,args.micro_batch); base_pred=base_logits.argmax(-1)
    base_acc=float((base_pred==y).float().mean())
    base_acc_by_class={c:float((base_pred[y==c]==y[y==c]).float().mean()) for c in range(len(LABELS)) if int((y==c).sum())>0}

    controls=['identity','reverse','particle0_to_end','particle0_to_middle','sort_pt_desc','sort_pt_asc']
    for r in range(args.random_repeats): controls.append(f'random_shuffle_r{r}')

    summary_rows=[]; cls_rows=[]
    for name in controls:
        if name=='identity':
            logits=base_logits
        else:
            idx=permutation_index(batch,name,seed=args.seed+1000*len(summary_rows))
            logits=model_logits(model,apply_perm(batch,idx),args.micro_batch)
        m=metrics(logits,y,base_logits,base_pred)
        row={'control':name,'n_events':int(y.numel()),'baseline_acc':base_acc,'acc_delta_from_baseline':m['acc']-base_acc}
        row.update(m); summary_rows.append(row)
        cls_rows.extend(class_rows(name,logits,y,base_logits,base_pred,base_acc_by_class))

    wcsv(out/'tables/particle_order_control_summary.csv',summary_rows)
    wcsv(out/'tables/particle_order_control_by_class.csv',cls_rows)
    randoms=[r for r in summary_rows if r['control'].startswith('random_shuffle')]
    random_summary={}
    if randoms:
        for key in ['acc','pred_flip_rate','mean_abs_logit_diff','max_abs_logit_diff','delta_base_pred_logit_mean']:
            random_summary[key+'_mean']=sum(float(r[key]) for r in randoms)/len(randoms)
    verdict='ORDER_INVARIANT_OR_NEAR_INVARIANT' if random_summary.get('pred_flip_rate_mean',0) < 0.02 and random_summary.get('mean_abs_logit_diff_mean',0) < 1e-3 else 'ORDER_SENSITIVE_NEEDS_DEBUG'
    summary={'ok':True,'checkpoint':args.checkpoint,'mode':args.mode,'samples_per_file':args.samples_per_file,'max_files':args.max_files,'n_events':int(y.numel()),'baseline_acc':base_acc,'random_summary':random_summary,'verdict':verdict,'summary_rows':summary_rows,'missing':list(res.missing_keys),'unexpected':list(res.unexpected_keys)}
    wjson(out/'particle_order_control_v1.json',summary)
    md=['# Particle Order Control v1\n\n',
        'Tests whether the model depends on particle array index/order, or whether particle0 effect is tied to physical leading/core content.\n\n',
        f"n_events={summary['n_events']} baseline_acc={fmt(base_acc)} verdict={verdict}\n\n",
        '## Summary\n',
        table(['control','acc','flip','mean_abs_logit_diff','max_abs_logit_diff','delta_base_pred_logit'],[[r['control'],fmt(r['acc']),fmt(r['pred_flip_rate']),fmt(r['mean_abs_logit_diff']),fmt(r['max_abs_logit_diff']),fmt(r['delta_base_pred_logit_mean'])] for r in summary_rows]),
        '\n## Interpretation\n\n',
        '- If random/reverse/particle0_to_end barely change logits/predictions, ParticleNet is effectively permutation invariant here. Then particle0/top-k causality is about the physical leading/core particle, not literal index position.\n',
        '- If order shuffles change predictions, order/sorting is a serious artifact and must be fixed before physics claims.\n',
        '- `sort_pt_asc` is intentionally extreme: if it changes outputs, inspect whether padding/trim/implementation creates order sensitivity.\n']
    (out/'PARTICLE_ORDER_CONTROL_V1.md').write_text(''.join(md),encoding='utf-8')
    print(json.dumps(summary,indent=2,ensure_ascii=False)[:20000])

if __name__=='__main__': main()
