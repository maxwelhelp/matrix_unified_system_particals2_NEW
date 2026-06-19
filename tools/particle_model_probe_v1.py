#!/usr/bin/env python3
import argparse,json,torch
from pathlib import Path

def shape(x):
    if x is None: return None
    if hasattr(x,'weight'): return list(x.weight.shape)
    if isinstance(x, torch.nn.Parameter): return list(x.shape)
    return type(x).__name__

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--checkpoint', default=None)
    ap.add_argument('--out-dir', default='runs/particle_model_probe_v1')
    args=ap.parse_args()
    out=Path(args.out_dir); out.mkdir(parents=True,exist_ok=True)
    rec={'status':'skeleton','note':'Import actual ParT model, then wrap it with adapters.part_adapter.ParticleTransformerAdapter.'}
    rec['expected_modules']={
      'embed':'input particle feature embedding',
      'pair_embed':'pairwise particle interaction bias before softmax',
      'blocks':'particle self-attention transformer blocks',
      'cls_blocks':'class-token attention blocks',
      'cls_token':'learned class token',
      'norm':'final class token norm',
      'fc':'classifier head',
      'block.attn':'torch MultiheadAttention with packed qkv',
      'block.fc1/fc2':'MLP up/down',
      'block norms':'pre/post attention and MLP norms',
      'block scales':'c_attn and w_resid if enabled'
    }
    (out/'particle_model_probe.json').write_text(json.dumps(rec,indent=2,ensure_ascii=False),encoding='utf-8')
    (out/'particle_model_probe.md').write_text('# Particle model probe v1\n\n'+json.dumps(rec,indent=2,ensure_ascii=False),encoding='utf-8')
    print(json.dumps(rec,indent=2,ensure_ascii=False))
if __name__=='__main__': main()
