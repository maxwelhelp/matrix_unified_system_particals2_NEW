#!/usr/bin/env python3
import argparse,csv,json,sys
from pathlib import Path
import torch
import torch.nn.functional as F

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from adapters.part_adapter import ParticleTransformerAdapter


def mkdir(p): Path(p).mkdir(parents=True,exist_ok=True)
def wjson(p,o): p=Path(p); mkdir(p.parent); p.write_text(json.dumps(o,indent=2,ensure_ascii=False),encoding='utf-8')
def wcsv(p,rows):
    p=Path(p); mkdir(p.parent); keys=[]; seen=set()
    for r in rows:
        for k in r:
            if k not in seen: keys.append(k); seen.add(k)
    with p.open('w',encoding='utf-8',newline='') as f:
        wr=csv.DictWriter(f,fieldnames=keys); wr.writeheader()
        for r in rows: wr.writerow({k:r.get(k,'') for k in keys})
def fmt(x):
    try: x=float(x)
    except Exception: return 'n/a'
    return f'{x:.3e}' if abs(x)>0 and (abs(x)<1e-3 or abs(x)>1e4) else f'{x:.4f}'
def table(h,rs):
    if not rs: return '_No rows._\n'
    s=['| '+' | '.join(h)+' |','| '+' | '.join(['---']*len(h))+' |']
    s += ['| '+' | '.join(map(str,r))+' |' for r in rs]
    return '\n'.join(s)+'\n'
def make_lv(batch,particles,device):
    p=torch.randn(batch,3,particles,device=device)*0.5
    e=p.square().sum(dim=1,keepdim=True).sqrt()+1.0
    return torch.cat([p,e],dim=1)
def logits(model,x,v,mask):
    with torch.no_grad(): return model(x,v,mask).detach()
def kl(a,b):
    la=F.log_softmax(a.float(),-1); lb=F.log_softmax(b.float(),-1); p=la.exp()
    return float((p*(la-lb)).sum(dim=-1).mean().detach().cpu())
def rel(a,b): return float(((a.float()-b.float()).norm()/(a.float().norm()+1e-9)).detach().cpu())
def patch_metric(base,patched):
    top=base.argmax(dim=-1); base_log=base.gather(1,top[:,None]).mean(); pat_log=patched.gather(1,top[:,None]).mean()
    return {'delta_top_logit':float((base_log-pat_log).cpu()),'logit_rel':rel(base,patched),'kl':kl(base,patched),'top1_match':float((patched.argmax(dim=-1)==top).float().mean().cpu())}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--device',default='cuda' if torch.cuda.is_available() else 'cpu'); ap.add_argument('--input-dim',type=int,default=16); ap.add_argument('--classes',type=int,default=10); ap.add_argument('--particles',type=int,default=32); ap.add_argument('--batch',type=int,default=8); ap.add_argument('--embed-dim',type=int,default=64); ap.add_argument('--heads',type=int,default=4); ap.add_argument('--layers',type=int,default=2); ap.add_argument('--cls-layers',type=int,default=1); ap.add_argument('--mlp-top-k',type=int,default=16); ap.add_argument('--out-dir',default='runs/particle_dummy_patch_controls_v2')
    a=ap.parse_args(); out=Path(a.out_dir); mkdir(out/'tables')
    from weaver.nn.model.ParticleTransformer import ParticleTransformer
    model=ParticleTransformer(input_dim=a.input_dim,num_classes=a.classes,pair_input_dim=4,pair_extra_dim=0,embed_dims=[a.embed_dim,a.embed_dim],pair_embed_dims=[32,32],num_heads=a.heads,num_layers=a.layers,num_cls_layers=a.cls_layers,fc_params=[],trim=False,for_inference=False,use_amp=False).to(a.device).eval()
    adapter=ParticleTransformerAdapter(model)
    x=torch.randn(a.batch,a.input_dim,a.particles,device=a.device); v=make_lv(a.batch,a.particles,a.device); mask=torch.ones(a.batch,1,a.particles,device=a.device,dtype=torch.bool)
    base=logits(model,x,v,mask); rows=[]; caps={}
    # Pair bias zero patch.
    def pair_zero(m,inp,outp): return torch.zeros_like(outp)
    h=adapter.get_pair_embed().register_forward_hook(pair_zero)
    patched=logits(model,x,v,mask); h.remove(); rows.append({'patch':'pair_embed_zero','layer':'','group':'pair_bias',**patch_metric(base,patched)})
    # Particle block skip patch: return input as output.
    for i,b in enumerate(adapter.get_layers()):
        def mk():
            def hook(m,inp,outp): return inp[0]
            return hook
        h=b.register_forward_hook(mk()); patched=logits(model,x,v,mask); h.remove(); rows.append({'patch':'particle_block_skip','layer':i,'group':'block',**patch_metric(base,patched)})
    # cls block zero output patch.
    for i,b in enumerate(adapter.get_cls_layers()):
        def hook(m,inp,outp): return torch.zeros_like(outp)
        h=b.register_forward_hook(hook); patched=logits(model,x,v,mask); h.remove(); rows.append({'patch':'cls_block_zero','layer':i,'group':'cls_block',**patch_metric(base,patched)})
    # Capture fc2 inputs.
    handles=[]
    for i,b in enumerate(adapter.get_layers()):
        def mk(layer):
            def pre(m,inp): caps[layer]=inp[0].detach().float().cpu()
            return pre
        handles.append(b.fc2.register_forward_pre_hook(mk(i)))
    _=logits(model,x,v,mask)
    for hh in handles: hh.remove()
    # MLP group patch per block.
    for i,b in enumerate(adapter.get_layers()):
        if i not in caps: continue
        hid=caps[i]; W=b.fc2.weight.detach().float().cpu(); score=hid.abs().mean(dim=tuple(range(hid.ndim-1)))*W.norm(dim=0); vals,idx=torch.topk(score,min(a.mlp_top_k,score.numel())); neurons=[int(z) for z in idx.tolist()]
        idx_t=torch.tensor(neurons,dtype=torch.long,device=a.device)
        def pre(m,inp):
            y=inp[0].clone(); y.index_fill_(-1,idx_t,0); return (y,)+tuple(inp[1:])
        h=b.fc2.register_forward_pre_hook(pre); patched=logits(model,x,v,mask); h.remove(); rows.append({'patch':'mlp_top_group_zero','layer':i,'group':f'top{len(neurons)}','neurons':json.dumps(neurons),'score_sum':float(vals.sum()),**patch_metric(base,patched)})
    rows=sorted(rows,key=lambda r:abs(float(r['delta_top_logit'])),reverse=True)
    wcsv(out/'tables/dummy_patch_controls.csv',rows)
    rec={'ok':True,'base_logits_shape':list(base.shape),'top1':base.argmax(dim=-1).cpu().tolist(),'adapter':adapter.describe(),'patch_rows':rows}
    wjson(out/'dummy_patch_controls_summary.json',rec)
    md=['# Dummy Particle Patch Controls v2\n\n','Checks causal patch handles on dummy ParT: pair-bias zero, particle-block skip, cls-block zero, MLP top-neuron group zero.\n\n',table(['rank','patch','layer','group','delta_top_logit','KL','top1'],[[i+1,r['patch'],r.get('layer',''),r.get('group',''),fmt(r['delta_top_logit']),fmt(r['kl']),fmt(r['top1_match'])] for i,r in enumerate(rows)])]
    (out/'DUMMY_PARTICLE_PATCH_REPORT.md').write_text(''.join(md),encoding='utf-8')
    print(json.dumps(rec,indent=2,ensure_ascii=False))
if __name__=='__main__': main()
