#!/usr/bin/env python3
import argparse,json,sys
from pathlib import Path
import torch

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from adapters.part_adapter import ParticleTransformerAdapter


def make_lv(batch, particles, device):
    p=torch.randn(batch,3,particles,device=device)*0.5
    e=p.square().sum(dim=1,keepdim=True).sqrt()+1.0
    return torch.cat([p,e],dim=1)

def shape(x):
    if x is None: return None
    if isinstance(x,(tuple,list)): return [shape(y) for y in x]
    if torch.is_tensor(x): return list(x.shape)
    if hasattr(x,'weight'): return list(x.weight.shape)
    return type(x).__name__

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--device',default='cuda' if torch.cuda.is_available() else 'cpu')
    ap.add_argument('--input-dim',type=int,default=16)
    ap.add_argument('--classes',type=int,default=10)
    ap.add_argument('--particles',type=int,default=32)
    ap.add_argument('--batch',type=int,default=4)
    ap.add_argument('--embed-dim',type=int,default=64)
    ap.add_argument('--heads',type=int,default=4)
    ap.add_argument('--layers',type=int,default=2)
    ap.add_argument('--cls-layers',type=int,default=1)
    ap.add_argument('--out-dir',default='runs/particle_part_dummy_probe_v1')
    args=ap.parse_args()
    out=Path(args.out_dir); out.mkdir(parents=True,exist_ok=True)
    from weaver.nn.model.ParticleTransformer import ParticleTransformer
    model=ParticleTransformer(
        input_dim=args.input_dim,
        num_classes=args.classes,
        pair_input_dim=4,
        pair_extra_dim=0,
        embed_dims=[args.embed_dim,args.embed_dim],
        pair_embed_dims=[32,32],
        num_heads=args.heads,
        num_layers=args.layers,
        num_cls_layers=args.cls_layers,
        fc_params=[],
        trim=False,
        for_inference=False,
        use_amp=False,
    ).to(args.device).eval()
    adapter=ParticleTransformerAdapter(model)
    captures={}
    handles=[]
    def hook(name):
        def f(m,inp,outp): captures[name]={'input':shape(inp),'output':shape(outp)}
        return f
    for name,mod in [('embed',adapter.get_input_embed()),('pair_embed',adapter.get_pair_embed()),('classifier',adapter.get_classifier_head())]:
        if mod is not None: handles.append(mod.register_forward_hook(hook(name)))
    for i,b in enumerate(adapter.get_layers()): handles.append(b.register_forward_hook(hook(f'block_{i}')))
    for i,b in enumerate(adapter.get_cls_layers()): handles.append(b.register_forward_hook(hook(f'cls_block_{i}')))
    x=torch.randn(args.batch,args.input_dim,args.particles,device=args.device)
    v=make_lv(args.batch,args.particles,args.device)
    mask=torch.ones(args.batch,1,args.particles,device=args.device,dtype=torch.bool)
    with torch.no_grad(): logits=model(x,v,mask)
    for h in handles: h.remove()
    rec={'ok':True,'logits_shape':list(logits.shape),'adapter':adapter.describe(),'captures':captures,'class_top1':torch.argmax(logits,dim=1).detach().cpu().tolist()}
    (out/'dummy_probe.json').write_text(json.dumps(rec,indent=2,ensure_ascii=False),encoding='utf-8')
    md=['# Particle dummy ParT probe v1\n\n',f"ok={rec['ok']} logits_shape={rec['logits_shape']}\n\n",'## Adapter\n',json.dumps(rec['adapter'],indent=2,ensure_ascii=False),'\n\n## Captures\n',json.dumps(captures,indent=2,ensure_ascii=False)]
    (out/'DUMMY_PARTICLE_PROBE_REPORT.md').write_text(''.join(md),encoding='utf-8')
    print(json.dumps(rec,indent=2,ensure_ascii=False))
if __name__=='__main__': main()
