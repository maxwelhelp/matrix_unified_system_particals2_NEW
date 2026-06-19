#!/usr/bin/env python3
import argparse,csv,json,sys
from pathlib import Path
import torch
import torch.nn.functional as F
ROOT=Path(__file__).resolve().parents[1]; sys.path.insert(0,str(ROOT))
from adapters.part_adapter import ParticleTransformerAdapter
from data.jetclass_tiny_loader import load_jetclass_batch, LABELS

def mkdir(p): Path(p).mkdir(parents=True,exist_ok=True)
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
def mode_from_ckpt(p):
    n=Path(p).name.lower()
    if 'kinpid' in n: return 'kinpid'
    if 'kin' in n: return 'kin'
    return 'full'
def cfg_for(mode):
    return dict(input_dim={'kin':7,'kinpid':13,'full':17}[mode],num_classes=10,pair_input_dim=4,use_pre_activation_pair=False,embed_dims=[128,512,128],pair_embed_dims=[64,64,64],num_heads=8,num_layers=8,num_cls_layers=2,block_params=None,cls_block_params={'dropout':0,'attn_dropout':0,'activation_dropout':0},fc_params=[],activation='gelu',trim=True,for_inference=False,use_amp=False)
def clean(sd):
    out={}
    for k,v in sd.items():
        nk=k
        for pref in ['module.','model.','mod.','part.']:
            if nk.startswith(pref): nk=nk[len(pref):]
        out[nk]=v
    return out
def unwrap(o):
    if isinstance(o,dict):
        for k in ['state_dict','model_state_dict','model','net','module']:
            if k in o and isinstance(o[k],dict): return o[k]
    return o
def logits(model,b):
    with torch.no_grad(): return model(b['x'],b['v'],b['mask']).detach()
def metric(base,patch,y):
    pred=base.argmax(-1); base_log=base.gather(1,pred[:,None]).mean(); pat_log=patch.gather(1,pred[:,None]).mean()
    acc=float((pred==y).float().mean().cpu()); pacc=float((patch.argmax(-1)==y).float().mean().cpu())
    la=F.log_softmax(base.float(),-1); lb=F.log_softmax(patch.float(),-1); kl=float((la.exp()*(la-lb)).sum(-1).mean().cpu())
    return {'delta_pred_logit':float((base_log-pat_log).cpu()),'kl':kl,'logit_rel':float(((base.float()-patch.float()).norm()/(base.float().norm()+1e-9)).cpu()),'top1_match':float((patch.argmax(-1)==pred).float().mean().cpu()),'base_acc':acc,'patch_acc':pacc}
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--checkpoint',default='local_checkpoints/part/ParT_full.pt'); ap.add_argument('--data-dir',default=str(Path.home()/'Рабочий стол/jetclass_tiny_balanced')); ap.add_argument('--limit',type=int,default=128); ap.add_argument('--max-files',type=int,default=20); ap.add_argument('--device',default='cuda' if torch.cuda.is_available() else 'cpu'); ap.add_argument('--mlp-top-k',type=int,default=32); ap.add_argument('--out-dir',default='runs/particle_real_patch_controls_v1')
    a=ap.parse_args(); out=Path(a.out_dir); mkdir(out/'tables')
    from weaver.nn.model.ParticleTransformer import ParticleTransformer
    mode=mode_from_ckpt(a.checkpoint); cfg=cfg_for(mode); model=ParticleTransformer(**cfg).to(a.device).eval(); res=model.load_state_dict(clean(unwrap(torch.load(a.checkpoint,map_location='cpu'))),strict=False)
    batch=load_jetclass_batch(a.data_dir,mode=mode,limit=a.limit,max_files=a.max_files,device=a.device)
    ad=ParticleTransformerAdapter(model); base=logits(model,batch); rows=[]
    rows.append({'patch':'baseline','layer':'','group':'','pred_counts':json.dumps(torch.bincount(base.argmax(-1).cpu(),minlength=10).tolist()),'acc':float((base.argmax(-1)==batch['y']).float().mean().cpu())})
    h=ad.get_pair_embed().register_forward_hook(lambda m,inp,outp: torch.zeros_like(outp)); p=logits(model,batch); h.remove(); rows.append({'patch':'pair_embed_zero','layer':'','group':'pair_bias',**metric(base,p,batch['y'])})
    for i,b in enumerate(ad.get_layers()):
        h=b.register_forward_hook(lambda m,inp,outp: inp[0]); p=logits(model,batch); h.remove(); rows.append({'patch':'particle_block_skip','layer':i,'group':'block',**metric(base,p,batch['y'])})
    for i,b in enumerate(ad.get_cls_layers()):
        h=b.register_forward_hook(lambda m,inp,outp: torch.zeros_like(outp)); p=logits(model,batch); h.remove(); rows.append({'patch':'cls_block_zero','layer':i,'group':'cls_block',**metric(base,p,batch['y'])})
    caps={}; hs=[]
    for i,b in enumerate(ad.get_layers()):
        hs.append(b.fc2.register_forward_pre_hook(lambda m,inp,i=i: caps.__setitem__(i,inp[0].detach().float().cpu())))
    _=logits(model,batch)
    for h in hs: h.remove()
    for i,b in enumerate(ad.get_layers()):
        if i not in caps: continue
        hid=caps[i]; W=b.fc2.weight.detach().float().cpu(); score=hid.abs().mean(tuple(range(hid.ndim-1)))*W.norm(dim=0); vals,idx=torch.topk(score,min(a.mlp_top_k,score.numel())); ns=[int(z) for z in idx.tolist()]; idx_t=torch.tensor(ns,device=a.device)
        def pre(m,inp,idx_t=idx_t):
            y=inp[0].clone(); y.index_fill_(-1,idx_t,0); return (y,)+tuple(inp[1:])
        h=b.fc2.register_forward_pre_hook(pre); p=logits(model,batch); h.remove(); rows.append({'patch':'mlp_top_group_zero','layer':i,'group':f'top{len(ns)}','neurons':json.dumps(ns),'score_sum':float(vals.sum()),**metric(base,p,batch['y'])})
    rows_sorted=sorted(rows[1:],key=lambda r:abs(float(r['delta_pred_logit'])),reverse=True)
    wcsv(out/'tables/real_particle_patch_controls.csv',rows)
    summary={'ok':True,'checkpoint':a.checkpoint,'mode':mode,'missing':list(res.missing_keys),'unexpected':list(res.unexpected_keys),'n':int(batch['y'].numel()),'files':batch['files'],'labels':LABELS,'baseline':rows[0],'top_patches':rows_sorted[:30]}
    wjson(out/'real_particle_patch_summary.json',summary)
    md=['# Real Particle Patch Controls v1\n\n',f"checkpoint={a.checkpoint}\nmode={mode}\nn={summary['n']}\nmissing={summary['missing']} unexpected={summary['unexpected']}\n\n",'## Baseline\n',json.dumps(rows[0],indent=2,ensure_ascii=False),'\n\n## Top patches\n',table(['rank','patch','layer','group','delta_logit','KL','top1','acc->patch_acc'],[[i+1,r['patch'],r.get('layer',''),r.get('group',''),fmt(r['delta_pred_logit']),fmt(r['kl']),fmt(r['top1_match']),f"{fmt(r['base_acc'])}->{fmt(r['patch_acc'])}"] for i,r in enumerate(rows_sorted[:40])])]
    (out/'REAL_PARTICLE_PATCH_REPORT.md').write_text(''.join(md),encoding='utf-8')
    print(json.dumps(summary,indent=2,ensure_ascii=False))
if __name__=='__main__': main()
