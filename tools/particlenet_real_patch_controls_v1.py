#!/usr/bin/env python3
import argparse, csv, glob, json, sys
from pathlib import Path
import numpy as np
import torch
import torch.nn.functional as F

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from adapters.particlenet_adapter import ParticleNetAdapter
from data.jetclass_tiny_loader_v3_official import (
    LABELS, PART_BASE, JET, _pad_wrap_array, _pad_const_array, make_features_official
)


def mkdir(p): Path(p).mkdir(parents=True, exist_ok=True)
def wjson(p,o): p=Path(p); mkdir(p.parent); p.write_text(json.dumps(o,indent=2,ensure_ascii=False),encoding='utf-8')
def wcsv(p,rows):
    p=Path(p); mkdir(p.parent); keys=[]; seen=set()
    for r in rows:
        for k in r:
            if k not in seen: keys.append(k); seen.add(k)
    with p.open('w',encoding='utf-8',newline='') as f:
        wr=csv.DictWriter(f,fieldnames=keys); wr.writeheader(); [wr.writerow({k:r.get(k,'') for k in keys}) for r in rows]
def fmt(x):
    try: x=float(x)
    except Exception: return 'n/a'
    return f'{x:.3e}' if abs(x)>0 and (abs(x)<1e-3 or abs(x)>1e4) else f'{x:.4f}'
def table(h,rs):
    if not rs: return '_No rows._\n'
    return '\n'.join(['| '+' | '.join(h)+' |','| '+' | '.join(['---']*len(h))+' |']+['| '+' | '.join(map(str,r))+' |' for r in rs])+'\n'


def unwrap(o):
    if isinstance(o, dict):
        for k in ['state_dict','model_state_dict','model','net','module']:
            if k in o and isinstance(o[k], dict): return o[k]
    return o

def clean(sd):
    out={}
    for k,v in sd.items():
        if not torch.is_tensor(v): continue
        nk=k
        for pref in ['module.','model.','mod.','particlenet.','pn.']:
            if nk.startswith(pref): nk=nk[len(pref):]
        out[nk]=v
    return out


def load_balanced(data_dir, mode='kinpid', samples_per_file=64, max_files=20, particles=128, device='cpu'):
    import uproot
    files=sorted(glob.glob(str(Path(data_dir)/'**/*.root'), recursive=True))[:max_files]
    if not files: raise FileNotFoundError(data_dir)
    need=list(dict.fromkeys(PART_BASE+JET+LABELS))
    xs=[]; vs=[]; ms=[]; ys=[]; labs=[]; pts=[]; used=[]
    for fp in files:
        tr=uproot.open(fp)['tree']; n=min(samples_per_file,int(tr.num_entries))
        arr=tr.arrays(need, entry_stop=n, library='ak')
        x,v,m,y,la=make_features_official(arr, mode, particles)
        p=np.stack([_pad_wrap_array(arr['part_deta'],particles), _pad_wrap_array(arr['part_dphi'],particles)], axis=1).astype('float32')
        xs.append(x); vs.append(v); ms.append(m); ys.append(y); labs.append(la); pts.append(p); used.append(fp)
    return {
        'points': torch.tensor(np.concatenate(pts,0),device=device),
        'features': torch.tensor(np.concatenate(xs,0),device=device),
        'vectors': torch.tensor(np.concatenate(vs,0),device=device),
        'mask': torch.tensor(np.concatenate(ms,0),device=device).bool(),
        'y': torch.tensor(np.concatenate(ys,0),device=device),
        'labels': torch.tensor(np.concatenate(labs,0),device=device),
        'files': used,
        'label_names': LABELS,
    }

def logits(model,b):
    with torch.no_grad():
        return model(b['points'], b['features'], b['mask']).detach()

def metric(base,patch,y):
    pred=base.argmax(-1)
    base_log=base.gather(1,pred[:,None]).mean(); pat_log=patch.gather(1,pred[:,None]).mean()
    la=F.log_softmax(base.float(),-1); lb=F.log_softmax(patch.float(),-1)
    return {
        'delta_pred_logit': float((base_log-pat_log).cpu()),
        'kl': float((la.exp()*(la-lb)).sum(-1).mean().cpu()),
        'logit_rel': float(((base.float()-patch.float()).norm()/(base.float().norm()+1e-9)).cpu()),
        'top1_match': float((patch.argmax(-1)==pred).float().mean().cpu()),
        'base_acc': float((pred==y).float().mean().cpu()),
        'patch_acc': float((patch.argmax(-1)==y).float().mean().cpu()),
    }

def pred_counts(x): return torch.bincount(x.detach().cpu(), minlength=10).tolist()

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--checkpoint', default='local_checkpoints/part/ParticleNet_kinpid.pt')
    ap.add_argument('--data-dir', default=str(Path.home()/'Рабочий стол/jetclass_tiny_balanced'))
    ap.add_argument('--mode', default='kinpid', choices=['kin','kinpid','full'])
    ap.add_argument('--samples-per-file', type=int, default=64)
    ap.add_argument('--max-files', type=int, default=20)
    ap.add_argument('--device', default='cuda' if torch.cuda.is_available() else 'cpu')
    ap.add_argument('--out-dir', default='runs/particlenet_real_patch_controls_v1')
    a=ap.parse_args(); out=Path(a.out_dir); mkdir(out/'tables')

    from weaver.nn.model.ParticleNet import ParticleNet
    input_dims={'kin':7,'kinpid':13,'full':17}[a.mode]
    model=ParticleNet(
        input_dims=input_dims, num_classes=10,
        conv_params=[(16,(64,64,64)),(16,(128,128,128)),(16,(256,256,256))],
        fc_params=[(256,0.1)], use_fusion=False, use_fts_bn=True, use_counts=True,
        trim=True, for_inference=False
    ).to(a.device).eval()
    sd=clean(unwrap(torch.load(a.checkpoint,map_location='cpu')))
    res=model.load_state_dict(sd, strict=False)
    batch=load_balanced(a.data_dir, mode=a.mode, samples_per_file=a.samples_per_file, max_files=a.max_files, device=a.device)
    ad=ParticleNetAdapter(model)
    base=logits(model,batch); y=batch['y']; pred=base.argmax(-1)
    rows=[{'patch':'baseline','layer':'','group':'','n':int(y.numel()),'acc':float((pred==y).float().mean().cpu()),'pred_counts':json.dumps(pred_counts(pred)),'true_counts':json.dumps(pred_counts(y))}]

    # input-level controls
    for name, fn in [
        ('points_zero', lambda b: {**b, 'points': torch.zeros_like(b['points'])}),
        ('features_zero', lambda b: {**b, 'features': torch.zeros_like(b['features'])}),
        ('mask_all_true', lambda b: {**b, 'mask': torch.ones_like(b['mask']).bool()}),
    ]:
        bb=fn(batch); p=logits(model,bb); rows.append({'patch':name,'layer':'input','group':name,**metric(base,p,y)})

    feature_groups={
        'kin_logs_0_4': list(range(0,5)),
        'pid_charge_5_10': list(range(5,11)) if input_dims>=13 else [],
        'coords_last2': [input_dims-2,input_dims-1],
    }
    if a.mode=='full': feature_groups['impact_11_14']=[11,12,13,14]
    for g,idxs in feature_groups.items():
        if not idxs: continue
        bb=dict(batch); z=batch['features'].clone(); z[:,idxs,:]=0; bb['features']=z
        p=logits(model,bb); rows.append({'patch':'feature_group_zero','layer':'input','group':g,'channels':json.dumps(idxs),**metric(base,p,y)})

    # module-level controls
    for i,conv in enumerate(ad.edge_convs()):
        def hook(m,inp,out): return torch.zeros_like(out)
        h=conv.register_forward_hook(hook); p=logits(model,batch); h.remove()
        rows.append({'patch':'edge_conv_zero','layer':i,'group':'edge_conv',**metric(base,p,y)})
    for i,fc in enumerate(ad.fc_layers()):
        def hook(m,inp,out): return torch.zeros_like(out)
        h=fc.register_forward_hook(hook); p=logits(model,batch); h.remove()
        rows.append({'patch':'fc_zero','layer':i,'group':'fc',**metric(base,p,y)})

    rows_sorted=sorted(rows[1:], key=lambda r: abs(float(r.get('delta_pred_logit',0))), reverse=True)
    wcsv(out/'tables/particlenet_patch_controls.csv', rows)
    summary={
        'ok': True,
        'checkpoint': a.checkpoint,
        'mode': a.mode,
        'missing': list(res.missing_keys),
        'unexpected': list(res.unexpected_keys),
        'adapter': ad.describe(),
        'n': int(y.numel()),
        'files': batch['files'],
        'baseline': rows[0],
        'top_patches': rows_sorted[:30],
    }
    wjson(out/'particlenet_patch_summary.json', summary)
    md=['# ParticleNet Real Patch Controls v1\n\n',
        f"checkpoint={a.checkpoint}\nmode={a.mode}\nn={summary['n']}\nmissing={summary['missing']} unexpected={summary['unexpected']}\n\n",
        '## Baseline\n', json.dumps(rows[0],indent=2,ensure_ascii=False), '\n\n',
        '## Adapter\n', json.dumps(summary['adapter'],indent=2,ensure_ascii=False), '\n\n',
        '## Top causal patches\n',
        table(['rank','patch','layer','group','delta_logit','KL','top1','acc->patch_acc'],[[i+1,r['patch'],r.get('layer',''),r.get('group',''),fmt(r.get('delta_pred_logit')),fmt(r.get('kl')),fmt(r.get('top1_match')),f"{fmt(r.get('base_acc'))}->{fmt(r.get('patch_acc'))}"] for i,r in enumerate(rows_sorted[:40])])]
    (out/'PARTICLENET_REAL_PATCH_REPORT.md').write_text(''.join(md),encoding='utf-8')
    print(json.dumps(summary,indent=2,ensure_ascii=False))

if __name__=='__main__': main()
