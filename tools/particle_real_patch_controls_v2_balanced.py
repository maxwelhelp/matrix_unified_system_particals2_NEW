#!/usr/bin/env python3
import argparse, json, sys, csv
from pathlib import Path
import torch
ROOT=Path(__file__).resolve().parents[1]; sys.path.insert(0,str(ROOT))
from tools.particle_real_patch_controls_v1 import cfg_for, clean, unwrap, logits, metric, fmt, table, wcsv, wjson
from adapters.part_adapter import ParticleTransformerAdapter
from data.jetclass_tiny_loader import load_jetclass_batch, LABELS

def mode_from_ckpt(p):
    n=Path(p).name.lower()
    if 'kinpid' in n: return 'kinpid'
    if 'kin' in n: return 'kin'
    return 'full'

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--checkpoint',default='local_checkpoints/part/ParT_full.pt')
    ap.add_argument('--data-dir',default=str(Path.home()/'Рабочий стол/jetclass_tiny_balanced'))
    ap.add_argument('--samples-per-file',type=int,default=32)
    ap.add_argument('--max-files',type=int,default=20)
    ap.add_argument('--device',default='cuda' if torch.cuda.is_available() else 'cpu')
    ap.add_argument('--mlp-top-k',type=int,default=32)
    ap.add_argument('--out-dir',default='runs/particle_real_patch_controls_v2_balanced')
    a=ap.parse_args(); out=Path(a.out_dir); (out/'tables').mkdir(parents=True,exist_ok=True)
    from weaver.nn.model.ParticleTransformer import ParticleTransformer
    mode=mode_from_ckpt(a.checkpoint); model=ParticleTransformer(**cfg_for(mode)).to(a.device).eval()
    res=model.load_state_dict(clean(unwrap(torch.load(a.checkpoint,map_location='cpu'))),strict=False)
    # Key fix: load samples_per_file from each ROOT, not all from first ROOT.
    import glob, os, shutil, tempfile
    files=sorted(glob.glob(str(Path(a.data_dir)/'**/*.root'),recursive=True))[:a.max_files]
    if not files: raise FileNotFoundError(a.data_dir)
    import uproot, awkward as ak, numpy as np
    from data.jetclass_tiny_loader import _make_features, PART_BASE, JET
    need=list(dict.fromkeys(PART_BASE+JET+LABELS))
    xs=[];vs=[];ms=[];ys=[];labs=[];used=[]
    for fp in files:
        tr=uproot.open(fp)['tree']; n=min(a.samples_per_file,int(tr.num_entries))
        arr=tr.arrays(need,entry_stop=n,library='ak')
        x,v,m,y,la=_make_features(arr,mode,128)
        xs.append(x); vs.append(v); ms.append(m); ys.append(y); labs.append(la); used.append(fp)
    import numpy as np
    batch={'x':torch.tensor(np.concatenate(xs,0),device=a.device),'v':torch.tensor(np.concatenate(vs,0),device=a.device),'mask':torch.tensor(np.concatenate(ms,0),device=a.device),'y':torch.tensor(np.concatenate(ys,0),device=a.device),'labels':torch.tensor(np.concatenate(labs,0),device=a.device),'files':used,'label_names':LABELS}
    ad=ParticleTransformerAdapter(model); base=logits(model,batch); rows=[]
    pred=base.argmax(-1); y=batch['y']
    rows.append({'patch':'baseline','layer':'','group':'','n':int(y.numel()),'pred_counts':json.dumps(torch.bincount(pred.cpu(),minlength=10).tolist()),'true_counts':json.dumps(torch.bincount(y.cpu(),minlength=10).tolist()),'acc':float((pred==y).float().mean().cpu())})
    h=ad.get_pair_embed().register_forward_hook(lambda m,inp,outp: torch.zeros_like(outp)); p=logits(model,batch); h.remove(); rows.append({'patch':'pair_embed_zero','layer':'','group':'pair_bias',**metric(base,p,y)})
    for i,b in enumerate(ad.get_layers()):
        h=b.register_forward_hook(lambda m,inp,outp: inp[0]); p=logits(model,batch); h.remove(); rows.append({'patch':'particle_block_skip','layer':i,'group':'block',**metric(base,p,y)})
    for i,b in enumerate(ad.get_cls_layers()):
        h=b.register_forward_hook(lambda m,inp,outp: torch.zeros_like(outp)); p=logits(model,batch); h.remove(); rows.append({'patch':'cls_block_zero','layer':i,'group':'cls_block',**metric(base,p,y)})
    caps={}; hs=[]
    for i,b in enumerate(ad.get_layers()): hs.append(b.fc2.register_forward_pre_hook(lambda m,inp,i=i: caps.__setitem__(i,inp[0].detach().float().cpu())))
    _=logits(model,batch)
    for h in hs: h.remove()
    for i,b in enumerate(ad.get_layers()):
        if i not in caps: continue
        hid=caps[i]; W=b.fc2.weight.detach().float().cpu(); score=hid.abs().mean(tuple(range(hid.ndim-1)))*W.norm(dim=0)
        vals,idx=torch.topk(score,min(a.mlp_top_k,score.numel())); ns=[int(z) for z in idx.tolist()]; idx_t=torch.tensor(ns,device=a.device)
        def pre(m,inp,idx_t=idx_t):
            z=inp[0].clone(); z.index_fill_(-1,idx_t,0); return (z,)+tuple(inp[1:])
        h=b.fc2.register_forward_pre_hook(pre); p=logits(model,batch); h.remove(); rows.append({'patch':'mlp_top_group_zero','layer':i,'group':f'top{len(ns)}','neurons':json.dumps(ns),'score_sum':float(vals.sum()),**metric(base,p,y)})
    rows_sorted=sorted(rows[1:],key=lambda r:abs(float(r['delta_pred_logit'])),reverse=True)
    wcsv(out/'tables/real_particle_patch_controls_balanced.csv',rows)
    summary={'ok':True,'checkpoint':a.checkpoint,'mode':mode,'missing':list(res.missing_keys),'unexpected':list(res.unexpected_keys),'n':int(y.numel()),'files':used,'labels':LABELS,'baseline':rows[0],'top_patches':rows_sorted[:30]}
    wjson(out/'real_particle_patch_balanced_summary.json',summary)
    md=['# Real Particle Patch Controls v2 balanced\n\n',f"checkpoint={a.checkpoint}\nmode={mode}\nn={summary['n']} samples_per_file={a.samples_per_file}\nmissing={summary['missing']} unexpected={summary['unexpected']}\n\n",'## Baseline\n',json.dumps(rows[0],indent=2,ensure_ascii=False),'\n\n## Top patches\n',table(['rank','patch','layer','group','delta_logit','KL','top1','acc->patch_acc'],[[i+1,r['patch'],r.get('layer',''),r.get('group',''),fmt(r['delta_pred_logit']),fmt(r['kl']),fmt(r['top1_match']),f"{fmt(r['base_acc'])}->{fmt(r['patch_acc'])}"] for i,r in enumerate(rows_sorted[:40])])]
    (out/'REAL_PARTICLE_PATCH_BALANCED_REPORT.md').write_text(''.join(md),encoding='utf-8')
    print(json.dumps(summary,indent=2,ensure_ascii=False))
if __name__=='__main__': main()
