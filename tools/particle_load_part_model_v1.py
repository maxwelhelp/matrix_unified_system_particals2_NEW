#!/usr/bin/env python3
import argparse,json,sys
from pathlib import Path
import torch

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from adapters.part_adapter import ParticleTransformerAdapter

def mkdir(p): Path(p).mkdir(parents=True,exist_ok=True)
def wjson(p,o): p=Path(p); mkdir(p.parent); p.write_text(json.dumps(o,indent=2,ensure_ascii=False),encoding='utf-8')
def make_lv(batch,particles,device):
    p=torch.randn(batch,3,particles,device=device)*0.5
    e=p.square().sum(dim=1,keepdim=True).sqrt()+1.0
    return torch.cat([p,e],dim=1)
def unwrap_state(obj):
    if isinstance(obj,dict):
        for k in ['state_dict','model_state_dict','model','net','module']:
            if k in obj and isinstance(obj[k],dict): return obj[k]
    return obj
def clean_keys(sd):
    out={}
    for k,v in sd.items():
        nk=k
        for pref in ['module.','model.','mod.','part.']:
            if nk.startswith(pref): nk=nk[len(pref):]
        out[nk]=v
    return out
def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--checkpoint',default='')
    ap.add_argument('--device',default='cuda' if torch.cuda.is_available() else 'cpu')
    ap.add_argument('--input-dim',type=int,default=16)
    ap.add_argument('--classes',type=int,default=10)
    ap.add_argument('--particles',type=int,default=32)
    ap.add_argument('--batch',type=int,default=4)
    ap.add_argument('--embed-dim',type=int,default=64)
    ap.add_argument('--heads',type=int,default=4)
    ap.add_argument('--layers',type=int,default=2)
    ap.add_argument('--cls-layers',type=int,default=1)
    ap.add_argument('--out-dir',default='runs/particle_load_part_model_v1')
    a=ap.parse_args(); out=Path(a.out_dir); mkdir(out)
    from weaver.nn.model.ParticleTransformer import ParticleTransformer
    model=ParticleTransformer(input_dim=a.input_dim,num_classes=a.classes,pair_input_dim=4,pair_extra_dim=0,embed_dims=[a.embed_dim,a.embed_dim],pair_embed_dims=[32,32],num_heads=a.heads,num_layers=a.layers,num_cls_layers=a.cls_layers,fc_params=[],trim=False,for_inference=False,use_amp=False).to(a.device).eval()
    load={'checkpoint':a.checkpoint,'loaded':False,'missing':None,'unexpected':None,'error':None}
    if a.checkpoint:
        try:
            raw=torch.load(a.checkpoint,map_location='cpu')
            sd=clean_keys(unwrap_state(raw))
            res=model.load_state_dict(sd,strict=False)
            load.update({'loaded':True,'missing':list(res.missing_keys),'unexpected':list(res.unexpected_keys)})
        except Exception as e:
            load.update({'error':repr(e)})
    adapter=ParticleTransformerAdapter(model)
    x=torch.randn(a.batch,a.input_dim,a.particles,device=a.device)
    v=make_lv(a.batch,a.particles,a.device)
    mask=torch.ones(a.batch,1,a.particles,device=a.device,dtype=torch.bool)
    with torch.no_grad(): logits=model(x,v,mask)
    rec={'ok':True,'load':load,'logits_shape':list(logits.shape),'top1':logits.argmax(dim=-1).detach().cpu().tolist(),'adapter':adapter.describe(),'config':vars(a)}
    wjson(out/'part_model_load_report.json',rec)
    md=['# Particle real/checkpoint loader v1\n\n',f"ok={rec['ok']} logits_shape={rec['logits_shape']}\n\n",'## Load\n',json.dumps(load,indent=2,ensure_ascii=False),'\n\n## Adapter\n',json.dumps(rec['adapter'],indent=2,ensure_ascii=False)]
    (out/'PART_MODEL_LOAD_REPORT.md').write_text(''.join(md),encoding='utf-8')
    print(json.dumps(rec,indent=2,ensure_ascii=False))
if __name__=='__main__': main()
