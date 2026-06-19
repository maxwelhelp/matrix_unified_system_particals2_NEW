#!/usr/bin/env python3
import argparse,json,sys
from pathlib import Path
import torch
ROOT=Path(__file__).resolve().parents[1]; sys.path.insert(0,str(ROOT))
from adapters.part_adapter import ParticleTransformerAdapter

def mkdir(p): Path(p).mkdir(parents=True,exist_ok=True)
def wjson(p,o): p=Path(p); mkdir(p.parent); p.write_text(json.dumps(o,indent=2,ensure_ascii=False),encoding='utf-8')
def feature_dim(name):
    n=Path(name).name.lower()
    if 'full' in n: return 17
    if 'kinpid' in n: return 13
    if 'kin' in n: return 7
    return 17
def make_lv(b,p,dev):
    q=torch.randn(b,3,p,device=dev)*0.5; e=q.square().sum(1,keepdim=True).sqrt()+1.0
    return torch.cat([q,e],1)
def unwrap(o):
    if isinstance(o,dict):
        for k in ['state_dict','model_state_dict','model','net','module']:
            if k in o and isinstance(o[k],dict): return o[k]
    return o
def clean(sd):
    out={}
    for k,v in sd.items():
        nk=k
        for pref in ['module.','model.','mod.','part.']:
            if nk.startswith(pref): nk=nk[len(pref):]
        out[nk]=v
    return out
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--checkpoint',required=True); ap.add_argument('--device',default='cuda' if torch.cuda.is_available() else 'cpu'); ap.add_argument('--batch',type=int,default=4); ap.add_argument('--particles',type=int,default=128); ap.add_argument('--input-dim',type=int,default=0); ap.add_argument('--out-dir',default='runs/particle_load_part_model_v2')
    a=ap.parse_args(); out=Path(a.out_dir); mkdir(out)
    from weaver.nn.model.ParticleTransformer import ParticleTransformer
    in_dim=a.input_dim or feature_dim(a.checkpoint)
    cfg=dict(input_dim=in_dim,num_classes=10,pair_input_dim=4,use_pre_activation_pair=False,embed_dims=[128,512,128],pair_embed_dims=[64,64,64],num_heads=8,num_layers=8,num_cls_layers=2,block_params=None,cls_block_params={'dropout':0,'attn_dropout':0,'activation_dropout':0},fc_params=[],activation='gelu',trim=False,for_inference=False,use_amp=False)
    model=ParticleTransformer(**cfg).to(a.device).eval()
    load={'checkpoint':a.checkpoint,'loaded':False,'missing':None,'unexpected':None,'error':None}
    try:
        sd=clean(unwrap(torch.load(a.checkpoint,map_location='cpu')))
        res=model.load_state_dict(sd,strict=False)
        load.update({'loaded':True,'missing':list(res.missing_keys),'unexpected':list(res.unexpected_keys)})
    except Exception as e: load['error']=repr(e)
    ad=ParticleTransformerAdapter(model)
    x=torch.randn(a.batch,in_dim,a.particles,device=a.device); v=make_lv(a.batch,a.particles,a.device); mask=torch.ones(a.batch,1,a.particles,device=a.device,dtype=torch.bool)
    with torch.no_grad(): logits=model(x,v,mask)
    rec={'ok':True,'config':cfg,'load':load,'logits_shape':list(logits.shape),'top1':logits.argmax(-1).detach().cpu().tolist(),'adapter':ad.describe(),'loaded_good':bool(load['loaded'] and not load['missing'] and not load['unexpected'] and load['error'] is None)}
    wjson(out/'part_model_load_report_v2.json',rec)
    md=['# Particle official ParT loader v2\n\n',f"checkpoint={a.checkpoint}\ninput_dim={in_dim}\nok={rec['ok']} loaded_good={rec['loaded_good']} logits_shape={rec['logits_shape']}\n\n",'## Load\n',json.dumps(load,indent=2,ensure_ascii=False),'\n\n## Adapter\n',json.dumps(rec['adapter'],indent=2,ensure_ascii=False)]
    (out/'PART_MODEL_LOAD_REPORT_V2.md').write_text(''.join(md),encoding='utf-8')
    print(json.dumps(rec,indent=2,ensure_ascii=False))
if __name__=='__main__': main()
