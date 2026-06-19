#!/usr/bin/env python3
import argparse, csv, json, sys
from pathlib import Path
import torch
import torch.nn.functional as F

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools.particle0_topk_controls_v2 import make_model, load_balanced, model_logits, real_mask, topk_keep_mask, particle0_keep_mask, remove_from_keep, apply_remove_mask, random_remove_mask
from data.jetclass_tiny_loader_v3_official import LABELS


def mkdir(p): Path(p).mkdir(parents=True, exist_ok=True)
def fmt(x):
    try: x=float(x)
    except Exception: return 'n/a'
    return f'{x:.3e}' if abs(x)>0 and (abs(x)<1e-3 or abs(x)>1e4) else f'{x:.4f}'
def wjson(path,obj):
    p=Path(path); mkdir(p.parent); p.write_text(json.dumps(obj,indent=2,ensure_ascii=False),encoding='utf-8')
def wcsv(path,rows):
    p=Path(path); mkdir(p.parent)
    keys=[]; seen=set()
    for r in rows:
        for k in r:
            if k not in seen: keys.append(k); seen.add(k)
    with p.open('w',encoding='utf-8',newline='') as f:
        wr=csv.DictWriter(f,fieldnames=keys); wr.writeheader()
        for r in rows: wr.writerow({k:r.get(k,'') for k in keys})
def table(headers, rows):
    if not rows: return '_No rows._\n'
    out=['| '+' | '.join(headers)+' |','| '+' | '.join(['---']*len(headers))+' |']
    for r in rows: out.append('| '+' | '.join(str(x) for x in r)+' |')
    return '\n'.join(out)+'\n'


def control_masks(batch, topks, seed=123):
    out={'baseline': torch.zeros_like(real_mask(batch)), 'remove_particle0': particle0_keep_mask(batch), 'keep_only_particle0': remove_from_keep(batch, particle0_keep_mask(batch))}
    for k in topks:
        keep=topk_keep_mask(batch,k)
        out[f'remove_top{k}']=keep
        out[f'keep_top{k}']=remove_from_keep(batch,keep)
        out[f'random_remove{k}']=random_remove_mask(batch,k,seed+1000*k)
    return out

def logits_for_control(model,batch,name,rm,micro_batch,base_logits):
    if name=='baseline': return base_logits
    return model_logits(model,apply_remove_mask(batch,rm),micro_batch)

def transition_rows(control, y, base_pred, ctrl_pred, base_logits, ctrl_logits, topn=50):
    rows=[]; C=len(LABELS); idx=base_pred[:,None]
    for src in range(C):
        sm=(base_pred==src); denom=int(sm.sum())
        if denom==0: continue
        for dst in range(C):
            cm=sm & (ctrl_pred==dst); n=int(cm.sum())
            if n==0: continue
            rows.append({'control':control,'transition_type':'baseline_pred_to_control_pred','from_id':src,'from_label':LABELS[src],'to_id':dst,'to_label':LABELS[dst],'n':n,'from_total':denom,'rate':n/denom})
    for true in range(C):
        tm=(y==true); denom=int(tm.sum())
        if denom==0: continue
        for dst in range(C):
            cm=tm & (ctrl_pred==dst); n=int(cm.sum())
            if n==0: continue
            rows.append({'control':control,'transition_type':'true_class_to_control_pred','from_id':true,'from_label':LABELS[true],'to_id':dst,'to_label':LABELS[dst],'n':n,'from_total':denom,'rate':n/denom})
    return sorted(rows,key=lambda r:(r['control'],r['transition_type'],-r['rate'],-r['n']))

def class_summary_rows(control,y,base_pred,ctrl_pred,base_logits,ctrl_logits):
    rows=[]; C=len(LABELS)
    for c in range(C):
        cm=(y==c); n=int(cm.sum())
        if n==0: continue
        base_acc=float((base_pred[cm]==y[cm]).float().mean())
        ctrl_acc=float((ctrl_pred[cm]==y[cm]).float().mean())
        flip=float((ctrl_pred[cm]!=base_pred[cm]).float().mean())
        idx=base_pred[cm,None]
        rows.append({'control':control,'class_id':c,'class_label':LABELS[c],'n':n,'base_acc':base_acc,'ctrl_acc':ctrl_acc,'acc_drop':base_acc-ctrl_acc,'flip_rate':flip,'delta_base_pred_logit_mean':float(ctrl_logits[cm].gather(1,idx).mean()-base_logits[cm].gather(1,idx).mean())})
    return rows

def top_transition_markdown(rows, control, typ, n=12):
    xs=[r for r in rows if r['control']==control and r['transition_type']==typ and r['from_label']!=r['to_label']]
    xs=sorted(xs,key=lambda r:(-float(r['rate']),-int(r['n'])))[:n]
    return table(['from','to','n','rate'],[[r['from_label'],r['to_label'],r['n'],fmt(r['rate'])] for r in xs])


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--checkpoint',default='local_checkpoints/part/ParticleNet_kinpid.pt')
    ap.add_argument('--data-dir',default=str(Path.home()/'Рабочий стол/jetclass_tiny_balanced'))
    ap.add_argument('--mode',default='kinpid',choices=['kin','kinpid','full'])
    ap.add_argument('--samples-per-file',type=int,default=256)
    ap.add_argument('--max-files',type=int,default=20)
    ap.add_argument('--micro-batch',type=int,default=128)
    ap.add_argument('--top-k',default='1,2,4,8,16')
    ap.add_argument('--seed',type=int,default=123)
    ap.add_argument('--device',default='cuda' if torch.cuda.is_available() else 'cpu')
    ap.add_argument('--out-dir',default='runs/control_confusion_atlas_v1')
    args=ap.parse_args(); out=Path(args.out_dir); mkdir(out/'tables')
    topks=[int(x) for x in str(args.top_k).split(',') if x.strip()]
    model,res=make_model(args.checkpoint,args.mode,args.device)
    batch=load_balanced(args.data_dir,mode=args.mode,samples_per_file=args.samples_per_file,max_files=args.max_files,device=args.device)
    y=batch['y'].detach().cpu()
    base_logits=model_logits(model,batch,args.micro_batch); base_pred=base_logits.argmax(-1)
    masks=control_masks(batch,topks,args.seed)
    all_trans=[]; all_cls=[]; all_summary=[]
    for name,rm in masks.items():
        logits=logits_for_control(model,batch,name,rm,args.micro_batch,base_logits)
        pred=logits.argmax(-1)
        all_trans.extend(transition_rows(name,y,base_pred,pred,base_logits,logits))
        all_cls.extend(class_summary_rows(name,y,base_pred,pred,base_logits,logits))
        all_summary.append({'control':name,'acc':float((pred==y).float().mean()),'flip_rate':float((pred!=base_pred).float().mean()),'mean_abs_logit_diff':float((logits-base_logits).abs().mean()),'delta_base_pred_logit_mean':float(logits.gather(1,base_pred[:,None]).mean()-base_logits.gather(1,base_pred[:,None]).mean())})
    wcsv(out/'tables/control_confusion_transitions.csv',all_trans)
    wcsv(out/'tables/control_confusion_by_class.csv',all_cls)
    wcsv(out/'tables/control_confusion_summary.csv',all_summary)
    focus=['remove_particle0','keep_only_particle0','remove_top1','keep_top1','remove_top4','keep_top4','remove_top16','keep_top16']
    summary={'ok':True,'checkpoint':args.checkpoint,'mode':args.mode,'n_events':int(y.numel()),'top_k':topks,'summary_rows':all_summary,'missing':list(res.missing_keys),'unexpected':list(res.unexpected_keys)}
    wjson(out/'control_confusion_atlas_v1.json',summary)
    md=['# Control Confusion Atlas v1\n\n',
        'Shows where predictions move under particle0/top-k controls. This answers: when a class collapses, what class wins instead?\n\n',
        f"n_events={summary['n_events']} mode={args.mode}\n\n",
        '## Control summary\n',
        table(['control','acc','flip','mean_abs_logit_diff','delta_base_pred_logit'],[[r['control'],fmt(r['acc']),fmt(r['flip_rate']),fmt(r['mean_abs_logit_diff']),fmt(r['delta_base_pred_logit_mean'])] for r in all_summary]),
        '\n## Top baseline-pred -> control-pred transitions\n']
    for c in focus:
        md += [f'\n### {c}\n', top_transition_markdown(all_trans,c,'baseline_pred_to_control_pred',12)]
    md += ['\n## Top true-class -> control-pred transitions\n']
    for c in focus:
        md += [f'\n### {c}\n', top_transition_markdown(all_trans,c,'true_class_to_control_pred',12)]
    md += ['\n## Interpretation\n\n',
           '- Use `baseline_pred_to_control_pred` to see model-decision competition after a control.\n',
           '- Use `true_class_to_control_pred` to see which real classes become confused.\n',
           '- Tbl/Hqql transitions after `remove_particle0` are the first place to inspect for class-local shortcuts/proxies.\n']
    (out/'CONTROL_CONFUSION_ATLAS_V1.md').write_text(''.join(md),encoding='utf-8')
    print(json.dumps(summary,indent=2,ensure_ascii=False)[:20000])

if __name__=='__main__': main()
