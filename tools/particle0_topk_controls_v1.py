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
def fnum(x):
    try: return float(x)
    except Exception: return 0.0
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
            if k not in seen:
                keys.append(k); seen.add(k)
    with p.open('w',encoding='utf-8',newline='') as f:
        wr=csv.DictWriter(f,fieldnames=keys); wr.writeheader()
        for r in rows: wr.writerow({k:r.get(k,'') for k in keys})
def table(headers, rows):
    if not rows: return '_No rows._\n'
    out=['| '+' | '.join(headers)+' |','| '+' | '.join(['---']*len(headers))+' |']
    for r in rows:
        out.append('| '+' | '.join(str(x) for x in r)+' |')
    return '\n'.join(out)+'\n'


def make_model(checkpoint, mode, device):
    from weaver.nn.model.ParticleNet import ParticleNet
    input_dims={'kin':7,'kinpid':13,'full':17}[mode]
    model=ParticleNet(input_dims=input_dims,num_classes=10,conv_params=[(16,(64,64,64)),(16,(128,128,128)),(16,(256,256,256))],fc_params=[(256,0.1)],use_fusion=False,use_fts_bn=True,use_counts=True,trim=True,for_inference=False).to(device).eval()
    sd=clean(unwrap(torch.load(checkpoint,map_location='cpu')))
    res=model.load_state_dict(sd, strict=False)
    return model, res


def slice_batch(batch,s,e):
    out={}; B=batch['y'].shape[0]
    for k,v in batch.items():
        if torch.is_tensor(v) and v.shape and v.shape[0]==B:
            out[k]=v[s:e]
        else:
            out[k]=v
    return out


def model_logits(model,batch,micro_batch=128):
    B=int(batch['y'].shape[0]); chunks=[]
    with torch.no_grad():
        for s in range(0,B,micro_batch):
            e=min(B,s+micro_batch)
            b=slice_batch(batch,s,e)
            chunks.append(model(b['points'],b['features'],b['mask']).detach().cpu())
    return torch.cat(chunks,dim=0)


def clone_batch(batch):
    out={}
    for k,v in batch.items():
        out[k]=v.clone() if torch.is_tensor(v) else v
    return out


def zero_particles(batch, remove_mask):
    # remove_mask [B,N] True means particle is removed/masked out.
    b=clone_batch(batch)
    rm=remove_mask.to(b['features'].device).bool()
    b['features']=b['features'].masked_fill(rm[:,None,:],0)
    b['points']=b['points'].masked_fill(rm[:,None,:],0)
    if 'vectors' in b:
        b['vectors']=b['vectors'].masked_fill(rm[:,None,:],0)
    # In this loader, mask is True for valid/real particles. Removing => False.
    b['mask']=b['mask'].masked_fill(rm[:,None,:],False)
    return b


def real_mask(batch):
    return batch['mask'][:,0,:].detach().bool()


def pt_values(batch):
    vec=batch.get('vectors')
    if vec is not None and torch.is_tensor(vec) and vec.shape[1]>=2:
        return torch.sqrt(vec[:,0,:].float()**2 + vec[:,1,:].float()**2)
    # fallback: first feature is usually log-pt-like; not exact pt but enough for ranking.
    return batch['features'][:,0,:].float()


def topk_remove_mask(batch,k):
    m=real_mask(batch)
    pt=pt_values(batch).masked_fill(~m, -1e30)
    B,N=pt.shape
    out=torch.zeros(B,N,device=pt.device,dtype=torch.bool)
    kk=min(k,N)
    if kk<=0: return out
    idx=torch.topk(pt,kk,dim=1).indices
    out.scatter_(1,idx,True)
    out &= m
    return out


def particle0_remove_mask(batch):
    m=real_mask(batch); out=torch.zeros_like(m)
    if out.shape[1]>0: out[:,0]=m[:,0]
    return out


def keep_only_mask(batch, keep_mask):
    # Returns remove_mask for all real particles except keep_mask.
    m=real_mask(batch)
    return m & (~keep_mask.bool())


def random_remove_mask(batch,k,seed=123):
    m=real_mask(batch); B,N=m.shape
    out=torch.zeros_like(m)
    rng=random.Random(seed)
    for i in range(B):
        inds=torch.where(m[i])[0].detach().cpu().tolist()
        if not inds: continue
        kk=min(k,len(inds))
        for j in rng.sample(inds,kk):
            out[i,j]=True
    return out


def metrics_for_logits(logits, y, base_pred=None, base_logits=None):
    pred=logits.argmax(dim=-1)
    prob=F.softmax(logits.float(),dim=-1)
    out={
        'acc':float((pred==y).float().mean()),
        'mean_conf':float(prob.gather(1,pred[:,None]).mean()),
    }
    if base_pred is not None and base_logits is not None:
        out['pred_flip_rate']=float((pred!=base_pred).float().mean())
        idx=base_pred[:,None]
        out['base_pred_logit_mean']=float(base_logits.gather(1,idx).mean())
        out['ctrl_base_pred_logit_mean']=float(logits.gather(1,idx).mean())
        out['delta_base_pred_logit_mean']=out['ctrl_base_pred_logit_mean']-out['base_pred_logit_mean']
    return out


def class_rows(control_name, logits, y, base_pred, base_logits, base_acc_by_class=None):
    pred=logits.argmax(dim=-1)
    rows=[]
    for c,lbl in enumerate(LABELS):
        mask=(y==c)
        n=int(mask.sum())
        if n==0: continue
        acc=float((pred[mask]==y[mask]).float().mean())
        flip=float((pred[mask]!=base_pred[mask]).float().mean())
        idx=base_pred[mask,None]
        base_logit=float(base_logits[mask].gather(1,idx).mean())
        ctrl_logit=float(logits[mask].gather(1,idx).mean())
        rows.append({
            'control':control_name,
            'class_id':c,
            'class_label':lbl,
            'n':n,
            'acc':acc,
            'acc_drop_from_baseline':(base_acc_by_class.get(c,acc)-acc) if base_acc_by_class else '',
            'pred_flip_rate':flip,
            'delta_base_pred_logit_mean':ctrl_logit-base_logit,
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
    ap.add_argument('--out-dir',default='runs/particle0_topk_controls_v1')
    args=ap.parse_args()
    out=Path(args.out_dir); mkdir(out/'tables')
    model,res=make_model(args.checkpoint,args.mode,args.device)
    batch=load_balanced(args.data_dir,mode=args.mode,samples_per_file=args.samples_per_file,max_files=args.max_files,device=args.device)
    y=batch['y'].detach().cpu()
    base_logits=model_logits(model,batch,args.micro_batch)
    base_pred=base_logits.argmax(dim=-1)
    base_m=metrics_for_logits(base_logits,y)
    base_acc_by_class={}
    for c in range(len(LABELS)):
        cm=(y==c)
        if int(cm.sum())>0:
            base_acc_by_class[c]=float((base_pred[cm]==y[cm]).float().mean())

    controls=[]
    controls.append(('baseline', None))
    controls.append(('remove_particle0', particle0_remove_mask(batch)))
    p0_keep=torch.zeros_like(real_mask(batch));
    if p0_keep.shape[1]>0: p0_keep[:,0]=real_mask(batch)[:,0]
    controls.append(('keep_only_particle0', keep_only_mask(batch,p0_keep)))
    topks=[int(x) for x in str(args.top_k).split(',') if str(x).strip()]
    for k in topks:
        rm=topk_remove_mask(batch,k)
        controls.append((f'remove_top{k}',rm))
        controls.append((f'keep_top{k}',keep_only_mask(batch,~rm)))
        for rr in range(args.random_repeats):
            controls.append((f'random_remove{k}_r{rr}',random_remove_mask(batch,k,seed=args.seed+1000*k+rr)))

    summary_rows=[]; cls_rows=[]
    logits_cache={'baseline':base_logits}
    for name,rm in controls:
        if name=='baseline':
            logits=base_logits
        else:
            ctrl_batch=zero_particles(batch,rm)
            logits=model_logits(model,ctrl_batch,args.micro_batch)
            logits_cache[name]=logits
        m=metrics_for_logits(logits,y,base_pred=base_pred,base_logits=base_logits)
        row={'control':name,'n_events':int(y.numel())}
        row.update(m)
        row['acc_drop_from_baseline']=base_m['acc']-m['acc']
        summary_rows.append(row)
        cls_rows.extend(class_rows(name,logits,y,base_pred,base_logits,base_acc_by_class))

    # Aggregate random controls by k.
    random_rows=[]
    for k in topks:
        rs=[r for r in summary_rows if r['control'].startswith(f'random_remove{k}_')]
        if not rs: continue
        random_rows.append({
            'control_family':f'random_remove{k}',
            'repeats':len(rs),
            'acc_mean':sum(r['acc'] for r in rs)/len(rs),
            'acc_drop_mean':sum(r['acc_drop_from_baseline'] for r in rs)/len(rs),
            'flip_rate_mean':sum(r.get('pred_flip_rate',0) for r in rs)/len(rs),
            'delta_base_pred_logit_mean':sum(r.get('delta_base_pred_logit_mean',0) for r in rs)/len(rs),
        })

    wcsv(out/'tables/particle0_topk_control_summary.csv',summary_rows)
    wcsv(out/'tables/particle0_topk_control_by_class.csv',cls_rows)
    wcsv(out/'tables/particle0_topk_random_baselines.csv',random_rows)

    # Interpret key controls.
    by={r['control']:r for r in summary_rows}
    interpretation=[]
    rem0=by.get('remove_particle0',{})
    keep0=by.get('keep_only_particle0',{})
    if rem0:
        interpretation.append({'finding':'remove_particle0_acc_drop','value':rem0.get('acc_drop_from_baseline'),'meaning':'Large value => leading/core particle is causally important.'})
    if keep0:
        interpretation.append({'finding':'keep_only_particle0_acc','value':keep0.get('acc'),'meaning':'High value => possible shortcut / leading-particle proxy.'})
    for k in topks:
        rt=by.get(f'remove_top{k}',{})
        kt=by.get(f'keep_top{k}',{})
        if rt: interpretation.append({'finding':f'remove_top{k}_acc_drop','value':rt.get('acc_drop_from_baseline'),'meaning':'Core/top-k causal dependence curve.'})
        if kt: interpretation.append({'finding':f'keep_top{k}_acc','value':kt.get('acc'),'meaning':'How much class information top-k alone retains.'})

    summary={
        'ok':True,
        'checkpoint':args.checkpoint,
        'mode':args.mode,
        'samples_per_file':args.samples_per_file,
        'max_files':args.max_files,
        'n_events':int(y.numel()),
        'baseline_acc':base_m['acc'],
        'top_k':topks,
        'random_repeats':args.random_repeats,
        'missing':list(res.missing_keys),
        'unexpected':list(res.unexpected_keys),
        'summary_rows':summary_rows,
        'random_rows':random_rows,
        'interpretation':interpretation,
    }
    wjson(out/'particle0_topk_controls_v1.json',summary)
    md=['# Particle0 / Top-k Controls v1\n\n',
        'This report tests whether the strong stream signal `particle0/core_high_pt -> Hqql/Tbl` is causal or just attribution/ordering.\n\n',
        f"n_events={summary['n_events']} baseline_acc={fmt(summary['baseline_acc'])} mode={args.mode}\n\n",
        '## Control summary\n',
        table(['control','acc','acc_drop','flip_rate','delta_base_pred_logit'],[[r['control'],fmt(r.get('acc')),fmt(r.get('acc_drop_from_baseline')),fmt(r.get('pred_flip_rate')),fmt(r.get('delta_base_pred_logit_mean'))] for r in summary_rows]),
        '\n## Random baselines\n',
        table(['family','repeats','acc_mean','acc_drop_mean','flip_mean','delta_logit_mean'],[[r['control_family'],r['repeats'],fmt(r['acc_mean']),fmt(r['acc_drop_mean']),fmt(r['flip_rate_mean']),fmt(r['delta_base_pred_logit_mean'])] for r in random_rows]),
        '\n## Interpretation hooks\n',
        table(['finding','value','meaning'],[[r['finding'],fmt(r['value']),r['meaning']] for r in interpretation]),
        '\n## Next decision\n\n',
        '- If `remove_particle0` causes a large drop but random_remove1 does not, leading/core evidence is causally important.\n',
        '- If `keep_only_particle0` keeps high accuracy, shortcut/proxy risk is high.\n',
        '- If remove_top-k curve is much stronger than random baselines, core/top-k dependence is real.\n',
        '- If effects are class-specific, run class-specific gradients next.\n']
    (out/'PARTICLE0_TOPK_CONTROLS_V1.md').write_text(''.join(md),encoding='utf-8')
    print(json.dumps(summary,indent=2,ensure_ascii=False)[:20000])

if __name__=='__main__': main()
