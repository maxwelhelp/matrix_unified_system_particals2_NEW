#!/usr/bin/env python3
import argparse,json,sys
from pathlib import Path
import torch
ROOT=Path(__file__).resolve().parents[1]; sys.path.insert(0,str(ROOT))
from tools.particle_real_patch_controls_v1 import cfg_for, clean, unwrap
from data.jetclass_tiny_loader_v3_official import load_jetclass_balanced_official, LABELS

def mode_from_ckpt(p):
    n=Path(p).name.lower()
    if 'kinpid' in n: return 'kinpid'
    if 'kin' in n: return 'kin'
    return 'full'

def binc(x,n=10): return torch.bincount(x.detach().cpu(),minlength=n).tolist()
def confusion(y,p,n=10):
    m=torch.zeros(n,n,dtype=torch.long)
    for a,b in zip(y.detach().cpu().tolist(),p.detach().cpu().tolist()): m[int(a),int(b)]+=1
    return m

def run_one(ckpt,data_dir,samples_per_file,max_files,device,trim):
    from weaver.nn.model.ParticleTransformer import ParticleTransformer
    mode=mode_from_ckpt(ckpt); cfg=cfg_for(mode); cfg['trim']=trim
    model=ParticleTransformer(**cfg).to(device).eval()
    res=model.load_state_dict(clean(unwrap(torch.load(ckpt,map_location='cpu'))),strict=False)
    batch=load_jetclass_balanced_official(data_dir,mode=mode,samples_per_file=samples_per_file,max_files=max_files,device=device)
    with torch.no_grad(): logits=model(batch['x'],batch['v'],batch['mask']).detach()
    pred=logits.argmax(-1); y=batch['y']; cm=confusion(y,pred,10)
    acc=float((pred==y).float().mean().cpu())
    rowmax=int(cm.max(dim=1).values.sum().item())
    upper=rowmax/max(1,int(y.numel()))
    per_true=[]
    for i,row in enumerate(cm.tolist()):
        top=sorted([(j,c) for j,c in enumerate(row)],key=lambda x:x[1],reverse=True)[:3]
        per_true.append({'true_id':i,'true_label':LABELS[i],'top_pred':[(LABELS[j],int(c)) for j,c in top]})
    return {'checkpoint':ckpt,'mode':mode,'trim':trim,'missing':list(res.missing_keys),'unexpected':list(res.unexpected_keys),'n':int(y.numel()),'acc':acc,'label_permutation_upper_bound':upper,'true_counts':binc(y),'pred_counts':binc(pred),'confusion':cm.tolist(),'per_true_top_preds':per_true,'files':batch['files']}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--checkpoint',default='local_checkpoints/part/ParT_kinpid.pt'); ap.add_argument('--data-dir',default=str(Path.home()/'Рабочий стол/jetclass_tiny_balanced')); ap.add_argument('--samples-per-file',type=int,default=256); ap.add_argument('--max-files',type=int,default=20); ap.add_argument('--device',default='cuda' if torch.cuda.is_available() else 'cpu'); ap.add_argument('--out-dir',default='runs/particle_accuracy_diagnostic_v4')
    a=ap.parse_args(); out=Path(a.out_dir); out.mkdir(parents=True,exist_ok=True)
    rows=[]
    for trim in [False,True]: rows.append(run_one(a.checkpoint,a.data_dir,a.samples_per_file,a.max_files,a.device,trim))
    best=max(rows,key=lambda r:r['acc'])
    rec={'ok':True,'diagnostic':'accuracy/confusion/label-order/trim check','results':rows,'best':best}
    (out/'particle_accuracy_diagnostic_v4.json').write_text(json.dumps(rec,indent=2,ensure_ascii=False),encoding='utf-8')
    md=['# Particle accuracy diagnostic v4\n\n','Checks whether low accuracy is caused by trim mode or label-order permutation. If `label_permutation_upper_bound` is also low, label order is not the main problem; input preprocessing/model-data format is still wrong.\n\n','| trim | acc | label_perm_upper | pred_counts |\n| --- | ---: | ---: | --- |\n']
    for r in rows: md.append(f"| {r['trim']} | {r['acc']:.4f} | {r['label_permutation_upper_bound']:.4f} | `{r['pred_counts']}` |\n")
    md.append('\n## Best per true class\n\n')
    for item in best['per_true_top_preds']: md.append(f"- {item['true_label']}: {item['top_pred']}\n")
    md.append('\n## Confusion matrix best run\n\n```json\n'+json.dumps(best['confusion'],indent=2)+'\n```\n')
    (out/'PARTICLE_ACCURACY_DIAGNOSTIC_V4.md').write_text(''.join(md),encoding='utf-8')
    print(json.dumps(rec,indent=2,ensure_ascii=False))
if __name__=='__main__': main()
