#!/usr/bin/env python3
import argparse, csv, json, sys
from pathlib import Path
import torch
import torch.nn.functional as F

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools.particlenet_real_patch_controls_v1 import (
    load_balanced, clean, unwrap, logits, metric, fmt, table
)
from data.jetclass_tiny_loader_v3_official import LABELS


def mkdir(p): Path(p).mkdir(parents=True, exist_ok=True)
def wjson(p,o): p=Path(p); mkdir(p.parent); p.write_text(json.dumps(o,indent=2,ensure_ascii=False),encoding='utf-8')
def wcsv(p,rows):
    p=Path(p); mkdir(p.parent); keys=[]; seen=set()
    for r in rows:
        for k in r:
            if k not in seen: keys.append(k); seen.add(k)
    with p.open('w',encoding='utf-8',newline='') as f:
        wr=csv.DictWriter(f,fieldnames=keys); wr.writeheader(); [wr.writerow({k:r.get(k,'') for k in keys}) for r in rows]

def patch_batch(batch, patch, layer=None, group=None, input_dims=13):
    b=dict(batch)
    if patch == 'points_zero':
        b['points'] = torch.zeros_like(batch['points'])
    elif patch == 'features_zero':
        b['features'] = torch.zeros_like(batch['features'])
    elif patch == 'mask_all_true':
        b['mask'] = torch.ones_like(batch['mask']).bool()
    elif patch == 'feature_group_zero':
        groups={
            'kin_logs_0_4': list(range(0,5)),
            'pid_charge_5_10': list(range(5,11)) if input_dims>=13 else [],
            'coords_last2': [input_dims-2,input_dims-1],
            'impact_11_14': [11,12,13,14] if input_dims>=17 else [],
        }
        idxs=groups[group]
        z=batch['features'].clone(); z[:,idxs,:]=0; b['features']=z
    return b

def make_model(checkpoint, mode, device):
    from weaver.nn.model.ParticleNet import ParticleNet
    input_dims={'kin':7,'kinpid':13,'full':17}[mode]
    model=ParticleNet(
        input_dims=input_dims, num_classes=10,
        conv_params=[(16,(64,64,64)),(16,(128,128,128)),(16,(256,256,256))],
        fc_params=[(256,0.1)], use_fusion=False, use_fts_bn=True, use_counts=True,
        trim=True, for_inference=False
    ).to(device).eval()
    sd=clean(unwrap(torch.load(checkpoint,map_location='cpu')))
    res=model.load_state_dict(sd, strict=False)
    return model,res,input_dims

def top_examples(base,y,k=3):
    probs=F.softmax(base.float(),dim=-1); pred=base.argmax(-1)
    conf=probs.max(dim=-1).values
    rows=[]
    for cls in range(10):
        idx=torch.where(pred==cls)[0]
        if len(idx)==0: continue
        vals=conf[idx]
        top=idx[torch.topk(vals,min(k,len(vals))).indices]
        for t in top.detach().cpu().tolist():
            rows.append({'idx':int(t),'pred':int(pred[t]),'pred_label':LABELS[int(pred[t])],'true':int(y[t]),'true_label':LABELS[int(y[t])],'conf':float(conf[t].detach().cpu()),'pred_logit':float(base[t,pred[t]].detach().cpu()),'true_logit':float(base[t,y[t]].detach().cpu())})
    return rows

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--checkpoint', default='local_checkpoints/part/ParticleNet_kinpid.pt')
    ap.add_argument('--data-dir', default=str(Path.home()/'Рабочий стол/jetclass_tiny_balanced'))
    ap.add_argument('--mode', default='kinpid', choices=['kin','kinpid','full'])
    ap.add_argument('--samples-per-file', type=int, default=128)
    ap.add_argument('--max-files', type=int, default=20)
    ap.add_argument('--device', default='cuda' if torch.cuda.is_available() else 'cpu')
    ap.add_argument('--examples-per-class', type=int, default=3)
    ap.add_argument('--out-dir', default='runs/particlenet_why_class_report_v2')
    args=ap.parse_args(); out=Path(args.out_dir); mkdir(out/'tables')
    model,res,input_dims=make_model(args.checkpoint,args.mode,args.device)
    batch=load_balanced(args.data_dir, mode=args.mode, samples_per_file=args.samples_per_file, max_files=args.max_files, device=args.device)
    base=logits(model,batch); y=batch['y']; pred=base.argmax(-1)
    baseline={'n':int(y.numel()),'acc':float((pred==y).float().mean().cpu()),'pred_counts':torch.bincount(pred.cpu(),minlength=10).tolist(),'true_counts':torch.bincount(y.cpu(),minlength=10).tolist()}

    patches=[]
    # input groups
    patch_specs=[('points_zero',None,None),('features_zero',None,None),('mask_all_true',None,None),('feature_group_zero',None,'kin_logs_0_4'),('feature_group_zero',None,'coords_last2')]
    if input_dims>=13: patch_specs.append(('feature_group_zero',None,'pid_charge_5_10'))
    if input_dims>=17: patch_specs.append(('feature_group_zero',None,'impact_11_14'))
    for patch,layer,group in patch_specs:
        pb=patch_batch(batch,patch,layer,group,input_dims); p=logits(model,pb); m=metric(base,p,y)
        patches.append({'patch':patch,'layer':'input','group':group or patch,**m})
    # module groups
    edge_convs=list(model.edge_convs)
    for i,conv in enumerate(edge_convs):
        h=conv.register_forward_hook(lambda m,inp,out: torch.zeros_like(out))
        p=logits(model,batch); h.remove(); patches.append({'patch':'edge_conv_zero','layer':i,'group':'edge_conv',**metric(base,p,y)})
    for i,fc in enumerate(list(model.fc)):
        h=fc.register_forward_hook(lambda m,inp,out: torch.zeros_like(out))
        p=logits(model,batch); h.remove(); patches.append({'patch':'fc_zero','layer':i,'group':'fc',**metric(base,p,y)})
    patches=sorted(patches,key=lambda r:abs(float(r['delta_pred_logit'])),reverse=True)

    examples=top_examples(base,y,args.examples_per_class)
    # For top examples, measure per-example predicted-logit drop for top 5 global patches.
    ex_rows=[]
    top_patch_specs=[]
    for r in patches[:6]:
        top_patch_specs.append((r['patch'], r.get('layer'), r.get('group')))
    for ex in examples:
        idx=ex['idx']; pred_id=ex['pred']
        row=dict(ex)
        for patch,layer,group in top_patch_specs:
            if patch in ['edge_conv_zero','fc_zero']:
                module = model.edge_convs[int(layer)] if patch=='edge_conv_zero' else list(model.fc)[int(layer)]
                h=module.register_forward_hook(lambda m,inp,out: torch.zeros_like(out))
                p=logits(model,batch); h.remove()
            else:
                p=logits(model, patch_batch(batch,patch,layer,group,input_dims))
            key=f"drop_{patch}_{layer}_{group}".replace(' ','_')
            row[key]=float((base[idx,pred_id]-p[idx,pred_id]).detach().cpu())
        ex_rows.append(row)

    wcsv(out/'tables/why_class_examples.csv',ex_rows)
    wcsv(out/'tables/why_class_global_patches.csv',patches)
    summary={'ok':True,'checkpoint':args.checkpoint,'mode':args.mode,'missing':list(res.missing_keys),'unexpected':list(res.unexpected_keys),'baseline':baseline,'top_patches':patches[:20],'examples':ex_rows[:50]}
    wjson(out/'particlenet_why_class_summary.json',summary)
    md=['# ParticleNet WHY_CLASS_REPORT v2\n\n',
        f"checkpoint={args.checkpoint}\nmode={args.mode}\nn={baseline['n']}\nmissing={summary['missing']} unexpected={summary['unexpected']}\n\n",
        '## Baseline\n\n```json\n',json.dumps(baseline,indent=2,ensure_ascii=False),'\n```\n\n',
        '## Global causal ranking\n',
        table(['rank','patch','layer','group','delta_logit','KL','top1','acc->patch_acc'],[[i+1,r['patch'],r.get('layer',''),r.get('group',''),fmt(r.get('delta_pred_logit')),fmt(r.get('kl')),fmt(r.get('top1_match')),f"{fmt(r.get('base_acc'))}->{fmt(r.get('patch_acc'))}"] for i,r in enumerate(patches[:20])]),
        '\n## Example-level signed logit drops\n\n',
        'Rows are high-confidence examples per predicted class. Positive drop means the patched component supported the original predicted class logit.\n\n',
        table(list(ex_rows[0].keys())[:9] if ex_rows else [], [[r.get(k,'') for k in list(ex_rows[0].keys())[:9]] for r in ex_rows[:30]] if ex_rows else []),
        '\nFull tables: `reports/latest/tables/why_class_examples.csv` and `reports/latest/tables/why_class_global_patches.csv`.\n']
    (out/'PARTICLENET_WHY_CLASS_REPORT.md').write_text(''.join(md),encoding='utf-8')
    print(json.dumps(summary,indent=2,ensure_ascii=False)[:20000])

if __name__=='__main__': main()
