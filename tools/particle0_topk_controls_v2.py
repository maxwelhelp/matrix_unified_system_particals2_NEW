#!/usr/bin/env python3
import argparse, csv, json, sys, random
from pathlib import Path
import torch
import torch.nn.functional as F

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools.particlenet_real_patch_controls_v1 import load_balanced, clean, unwrap
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


def make_model(checkpoint, mode, device):
    from weaver.nn.model.ParticleNet import ParticleNet
    input_dims={'kin':7,'kinpid':13,'full':17}[mode]
    # trim=False is intentional for aggressive controls like keep_only_particle0.
    # With trim=True, SequenceTrimmer can reduce N to 1 and EdgeConv knn(k=16)
    # crashes. Keeping padded N lets KNN run while removed particles have zeroed
    # features/points and mask=False.
    model=ParticleNet(input_dims=input_dims,num_classes=10,conv_params=[(16,(64,64,64)),(16,(128,128,128)),(16,(256,256,256))],fc_params=[(256,0.1)],use_fusion=False,use_fts_bn=True,use_counts=True,trim=False,for_inference=False).to(device).eval()
    sd=clean(unwrap(torch.load(checkpoint,map_location='cpu')))
    res=model.load_state_dict(sd, strict=False)
    return model, res


def slice_batch(batch,s,e):
    B=batch['y'].shape[0]; out={}
    for k,v in batch.items():
        if torch.is_tensor(v) and v.shape and v.shape[0]==B: out[k]=v[s:e]
        else: out[k]=v
    return out

def model_logits(model,batch,micro_batch=128):
    B=int(batch['y'].shape[0]); chunks=[]
    with torch.no_grad():
        for s in range(0,B,micro_batch):
            e=min(B,s+micro_batch); b=slice_batch(batch,s,e)
            chunks.append(model(b['points'],b['features'],b['mask']).detach().cpu())
    return torch.cat(chunks,dim=0)

def clone_batch(batch):
    return {k:(v.clone() if torch.is_tensor(v) else v) for k,v in batch.items()}

def real_mask(batch):
    return batch['mask'][:,0,:].detach().bool()

def pt_values(batch):
    vec=batch.get('vectors')
    if vec is not None and torch.is_tensor(vec) and vec.shape[1]>=2:
        return torch.sqrt(vec[:,0,:].float()**2 + vec[:,1,:].float()**2)
    return batch['features'][:,0,:].float()

def apply_remove_mask(batch, remove_mask):
    b=clone_batch(batch)
    rm=remove_mask.to(b['features'].device).bool()
    b['features']=b['features'].masked_fill(rm[:,None,:],0)
    b['points']=b['points'].masked_fill(rm[:,None,:],0)
    if 'vectors' in b:
        b['vectors']=b['vectors'].masked_fill(rm[:,None,:],0)
    b['mask']=b['mask'].masked_fill(rm[:,None,:],False)
    return b

def topk_keep_mask(batch,k):
    m=real_mask(batch); pt=pt_values(batch).masked_fill(~m,-1e30)
    B,N=pt.shape; keep=torch.zeros(B,N,device=pt.device,dtype=torch.bool)
    kk=min(max(0,int(k)),N)
    if kk<=0: return keep
    idx=torch.topk(pt,kk,dim=1).indices
    keep.scatter_(1,idx,True)
    return keep & m

def particle0_keep_mask(batch):
    m=real_mask(batch); keep=torch.zeros_like(m)
    if keep.shape[1]>0: keep[:,0]=m[:,0]
    return keep

def remove_from_keep(batch, keep):
    m=real_mask(batch)
    return m & (~keep.bool())

def remove_particle0_mask(batch):
    return particle0_keep_mask(batch)

def remove_topk_mask(batch,k):
    return topk_keep_mask(batch,k)

def random_remove_mask(batch,k,seed):
    m=real_mask(batch); B,N=m.shape; out=torch.zeros_like(m); rng=random.Random(seed)
    for i in range(B):
        inds=torch.where(m[i])[0].detach().cpu().tolist()
        if not inds: continue
        kk=min(int(k),len(inds))
        for j in rng.sample(inds,kk): out[i,j]=True
    return out

def valid_mean_after(batch, remove_mask):
    m=real_mask(batch); keep=m & (~remove_mask.bool())
    return float(keep.sum(dim=1).float().mean().detach().cpu())

def metrics_for_logits(logits, y, base_pred=None, base_logits=None):
    pred=logits.argmax(-1); prob=F.softmax(logits.float(),-1)
    out={'acc':float((pred==y).float().mean()), 'mean_conf':float(prob.gather(1,pred[:,None]).mean())}
    if base_pred is not None and base_logits is not None:
        idx=base_pred[:,None]
        out['pred_flip_rate']=float((pred!=base_pred).float().mean())
        out['base_pred_logit_mean']=float(base_logits.gather(1,idx).mean())
        out['ctrl_base_pred_logit_mean']=float(logits.gather(1,idx).mean())
        out['delta_base_pred_logit_mean']=out['ctrl_base_pred_logit_mean']-out['base_pred_logit_mean']
    return out

def class_rows(control, logits, y, base_pred, base_logits, base_acc_by_class):
    pred=logits.argmax(-1); rows=[]
    for c,lbl in enumerate(LABELS):
        cm=(y==c); n=int(cm.sum())
        if n==0: continue
        idx=base_pred[cm,None]
        acc=float((pred[cm]==y[cm]).float().mean())
        rows.append({
            'control':control,'class_id':c,'class_label':lbl,'n':n,
            'acc':acc,'acc_drop_from_baseline':base_acc_by_class.get(c,acc)-acc,
            'pred_flip_rate':float((pred[cm]!=base_pred[cm]).float().mean()),
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
    ap.add_argument('--top-k',default='1,2,4,8,16')
    ap.add_argument('--random-repeats',type=int,default=3)
    ap.add_argument('--seed',type=int,default=123)
    ap.add_argument('--device',default='cuda' if torch.cuda.is_available() else 'cpu')
    ap.add_argument('--out-dir',default='runs/particle0_topk_controls_v2')
    args=ap.parse_args(); out=Path(args.out_dir); mkdir(out/'tables')
    model,res=make_model(args.checkpoint,args.mode,args.device)
    batch=load_balanced(args.data_dir,mode=args.mode,samples_per_file=args.samples_per_file,max_files=args.max_files,device=args.device)
    y=batch['y'].detach().cpu()
    base_logits=model_logits(model,batch,args.micro_batch); base_pred=base_logits.argmax(-1)
    base_m=metrics_for_logits(base_logits,y)
    base_acc_by_class={c:float((base_pred[y==c]==y[y==c]).float().mean()) for c in range(len(LABELS)) if int((y==c).sum())>0}

    topks=[int(x) for x in str(args.top_k).split(',') if str(x).strip()]
    controls=[('baseline', torch.zeros_like(real_mask(batch)))]
    controls.append(('remove_particle0', remove_particle0_mask(batch)))
    controls.append(('keep_only_particle0', remove_from_keep(batch, particle0_keep_mask(batch))))
    for k in topks:
        topk=topk_keep_mask(batch,k)
        controls.append((f'remove_top{k}', remove_topk_mask(batch,k)))
        controls.append((f'keep_top{k}', remove_from_keep(batch, topk)))
        for rr in range(args.random_repeats):
            controls.append((f'random_remove{k}_r{rr}', random_remove_mask(batch,k,args.seed+1000*k+rr)))

    summary_rows=[]; cls_rows=[]
    for name,rm in controls:
        if name=='baseline': logits=base_logits
        else: logits=model_logits(model,apply_remove_mask(batch,rm),args.micro_batch)
        m=metrics_for_logits(logits,y,base_pred,base_logits)
        row={'control':name,'n_events':int(y.numel()),'valid_particles_mean_after':valid_mean_after(batch,rm)}
        row.update(m); row['acc_drop_from_baseline']=base_m['acc']-m['acc']
        summary_rows.append(row)
        cls_rows.extend(class_rows(name,logits,y,base_pred,base_logits,base_acc_by_class))

    random_rows=[]
    for k in topks:
        rs=[r for r in summary_rows if r['control'].startswith(f'random_remove{k}_')]
        if rs:
            random_rows.append({'control_family':f'random_remove{k}','repeats':len(rs),'acc_mean':sum(r['acc'] for r in rs)/len(rs),'acc_drop_mean':sum(r['acc_drop_from_baseline'] for r in rs)/len(rs),'flip_rate_mean':sum(r['pred_flip_rate'] for r in rs)/len(rs),'delta_base_pred_logit_mean':sum(r['delta_base_pred_logit_mean'] for r in rs)/len(rs)})

    wcsv(out/'tables/particle0_topk_control_summary_v2.csv',summary_rows)
    wcsv(out/'tables/particle0_topk_control_by_class_v2.csv',cls_rows)
    wcsv(out/'tables/particle0_topk_random_baselines_v2.csv',random_rows)
    by={r['control']:r for r in summary_rows}
    interpretation=[]
    for key,meaning in [('remove_particle0','Large drop => particle0/leading-core is causally important.'),('keep_only_particle0','High acc => shortcut/proxy risk.'),('remove_top1','Targeted top1 removal vs random_remove1 tests if leading particle matters beyond random deletion.'),('keep_top16','High acc means top-16 particles carry much of class evidence.')]:
        if key in by: interpretation.append({'finding':key,'acc':by[key]['acc'],'acc_drop':by[key]['acc_drop_from_baseline'],'flip_rate':by[key]['pred_flip_rate'],'meaning':meaning})
    summary={'ok':True,'version':'v2_knn_safe_trim_false','checkpoint':args.checkpoint,'mode':args.mode,'samples_per_file':args.samples_per_file,'max_files':args.max_files,'n_events':int(y.numel()),'baseline_acc':base_m['acc'],'top_k':topks,'random_repeats':args.random_repeats,'missing':list(res.missing_keys),'unexpected':list(res.unexpected_keys),'summary_rows':summary_rows,'random_rows':random_rows,'interpretation':interpretation}
    wjson(out/'particle0_topk_controls_v2.json',summary)
    md=['# Particle0 / Top-k Controls v2\n\n',
        'KNN-safe version: ParticleNet is loaded with `trim=False`, so aggressive controls like `keep_only_particle0` do not crash EdgeConv KNN. Removed particles have zero features/points and mask=False.\n\n',
        f"n_events={summary['n_events']} baseline_acc={fmt(summary['baseline_acc'])} mode={args.mode}\n\n",
        '## Control summary\n',
        table(['control','valid_mean','acc','acc_drop','flip_rate','delta_base_pred_logit'],[[r['control'],fmt(r['valid_particles_mean_after']),fmt(r['acc']),fmt(r['acc_drop_from_baseline']),fmt(r['pred_flip_rate']),fmt(r['delta_base_pred_logit_mean'])] for r in summary_rows]),
        '\n## Random baselines\n',
        table(['family','repeats','acc_mean','acc_drop_mean','flip_mean','delta_logit_mean'],[[r['control_family'],r['repeats'],fmt(r['acc_mean']),fmt(r['acc_drop_mean']),fmt(r['flip_rate_mean']),fmt(r['delta_base_pred_logit_mean'])] for r in random_rows]),
        '\n## Interpretation hooks\n',
        table(['finding','acc','acc_drop','flip_rate','meaning'],[[r['finding'],fmt(r['acc']),fmt(r['acc_drop']),fmt(r['flip_rate']),r['meaning']] for r in interpretation]),
        '\n## Decision logic\n\n',
        '- `remove_particle0` >> `random_remove1` drop: leading particle is specifically causal.\n',
        '- `keep_only_particle0` high accuracy: shortcut/proxy risk is high.\n',
        '- `remove_topK` curve stronger than random baselines: core/top-k dependence is real.\n',
        '- Class-wise table tells which classes depend on core/top-k most.\n']
    (out/'PARTICLE0_TOPK_CONTROLS_V2.md').write_text(''.join(md),encoding='utf-8')
    print(json.dumps(summary,indent=2,ensure_ascii=False)[:20000])

if __name__=='__main__': main()
