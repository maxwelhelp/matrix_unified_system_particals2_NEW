#!/usr/bin/env python3
import argparse, csv, json, sys
from pathlib import Path
import torch
import torch.nn.functional as F

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools.particlenet_real_patch_controls_v1 import load_balanced, clean, unwrap, logits, fmt, table
from data.jetclass_tiny_loader_v3_official import LABELS

FEATURE_NAMES = {
    'kin': ['part_pt_log','part_e_log','part_logptrel','part_logerel','part_deltaR','part_deta','part_dphi'],
    'kinpid': ['part_pt_log','part_e_log','part_logptrel','part_logerel','part_deltaR','part_charge','part_isChargedHadron','part_isNeutralHadron','part_isPhoton','part_isElectron','part_isMuon','part_deta','part_dphi'],
    'full': ['part_pt_log','part_e_log','part_logptrel','part_logerel','part_deltaR','part_charge','part_isChargedHadron','part_isNeutralHadron','part_isPhoton','part_isElectron','part_isMuon','part_d0','part_d0err','part_dz','part_dzerr','part_deta','part_dphi'],
}


def mkdir(p): Path(p).mkdir(parents=True, exist_ok=True)
def wjson(p,o): p=Path(p); mkdir(p.parent); p.write_text(json.dumps(o,indent=2,ensure_ascii=False),encoding='utf-8')
def wcsv(p,rows):
    p=Path(p); mkdir(p.parent); keys=[]; seen=set()
    for r in rows:
        for k in r:
            if k not in seen: keys.append(k); seen.add(k)
    with p.open('w',encoding='utf-8',newline='') as f:
        wr=csv.DictWriter(f,fieldnames=keys); wr.writeheader(); [wr.writerow({k:r.get(k,'') for k in keys}) for r in rows]

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

def pred_counts(x): return torch.bincount(x.detach().cpu(),minlength=10).tolist()

def metric(base,patch,y):
    pred=base.argmax(-1)
    la=F.log_softmax(base.float(),-1); lb=F.log_softmax(patch.float(),-1)
    return {
        'delta_pred_logit': float((base.gather(1,pred[:,None]).mean()-patch.gather(1,pred[:,None]).mean()).cpu()),
        'kl': float((la.exp()*(la-lb)).sum(-1).mean().cpu()),
        'top1_match': float((patch.argmax(-1)==pred).float().mean().cpu()),
        'base_acc': float((pred==y).float().mean().cpu()),
        'patch_acc': float((patch.argmax(-1)==y).float().mean().cpu()),
    }

def per_class_metric(base,patch,y,name,layer='',group=''):
    pred=base.argmax(-1); pp=patch.argmax(-1)
    rows=[]
    for c,lbl in enumerate(LABELS):
        m=(y==c)
        if int(m.sum())==0: continue
        base_acc=float((pred[m]==y[m]).float().mean().cpu())
        patch_acc=float((pp[m]==y[m]).float().mean().cpu())
        # drop for original predicted logit on examples from this true class
        drop=float((base[m].gather(1,pred[m,None]) - patch[m].gather(1,pred[m,None])).mean().cpu())
        rows.append({'patch':name,'layer':layer,'group':group,'class_id':c,'class_label':lbl,'n':int(m.sum().cpu()),'base_acc':base_acc,'patch_acc':patch_acc,'acc_drop':base_acc-patch_acc,'pred_logit_drop':drop})
    return rows

def clone_batch(batch): return {k:(v.clone() if torch.is_tensor(v) else v) for k,v in batch.items()}

def apply_input_patch(batch, patch, group=None, channel=None, topk=8):
    b=clone_batch(batch)
    if patch=='points_zero': b['points'].zero_()
    elif patch=='features_zero': b['features'].zero_()
    elif patch=='mask_all_true': b['mask']=torch.ones_like(batch['mask']).bool()
    elif patch=='feature_group_zero':
        idxs=group
        b['features'][:,idxs,:]=0
    elif patch=='feature_channel_zero':
        b['features'][:,channel,:]=0
    elif patch=='particle_topk_mask_zero':
        v=batch['vectors']; px,py,en=v[:,0,:],v[:,1,:],v[:,3,:]
        pt=torch.sqrt(px*px+py*py)
        deta=batch['points'][:,0,:]; dphi=batch['points'][:,1,:]
        dr=torch.sqrt(deta*deta+dphi*dphi)
        if group=='top_pt': score=pt
        elif group=='top_energy': score=en
        elif group=='high_deltaR': score=dr
        else: score=pt
        mask=batch['mask'].clone()
        idx=torch.topk(score, min(topk,score.shape[-1]), dim=-1).indices
        mask.scatter_(2, idx[:,None,:], False)
        b['mask']=mask.bool()
    return b

def run_patch(model,batch,base,y,spec,input_dims):
    name=spec['patch']; layer=spec.get('layer',''); group=spec.get('group','')
    handle=None
    if name=='edge_conv_zero':
        module=model.edge_convs[int(layer)]
        handle=module.register_forward_hook(lambda m,inp,out: torch.zeros_like(out))
        p=logits(model,batch); handle.remove()
    elif name=='fc_zero':
        module=list(model.fc)[int(layer)]
        handle=module.register_forward_hook(lambda m,inp,out: torch.zeros_like(out))
        p=logits(model,batch); handle.remove()
    else:
        pb=apply_input_patch(batch,name,group=spec.get('channels'),channel=spec.get('channel'),topk=spec.get('topk',8))
        p=logits(model,pb)
    g=metric(base,p,y); g.update({'patch':name,'layer':layer,'group':group})
    pc=per_class_metric(base,p,y,name,layer,group)
    return p,g,pc

def build_specs(mode,input_dims):
    specs=[]
    specs += [{'patch':'points_zero','layer':'input','group':'all_points'}, {'patch':'features_zero','layer':'input','group':'all_features'}, {'patch':'mask_all_true','layer':'input','group':'mask'}]
    specs += [{'patch':'feature_group_zero','layer':'input','group':'kin_logs_0_4','channels':list(range(0,5))}]
    if input_dims>=13: specs += [{'patch':'feature_group_zero','layer':'input','group':'pid_charge_5_10','channels':list(range(5,11))}]
    if input_dims>=17: specs += [{'patch':'feature_group_zero','layer':'input','group':'impact_11_14','channels':[11,12,13,14]}]
    specs += [{'patch':'feature_group_zero','layer':'input','group':'coords_last2','channels':[input_dims-2,input_dims-1]}]
    for i,n in enumerate(FEATURE_NAMES[mode]): specs.append({'patch':'feature_channel_zero','layer':'input','group':n,'channel':i})
    for g in ['top_pt','top_energy','high_deltaR']: specs.append({'patch':'particle_topk_mask_zero','layer':'particles','group':g,'topk':8})
    for i in range(3): specs.append({'patch':'edge_conv_zero','layer':i,'group':'edge_conv'})
    for i in range(2): specs.append({'patch':'fc_zero','layer':i,'group':'fc'})
    return specs

def high_conf_examples(base,y,k=2):
    prob=F.softmax(base.float(),-1); pred=base.argmax(-1); conf=prob.max(-1).values
    rows=[]
    for c in range(10):
        idx=torch.where(pred==c)[0]
        if len(idx)==0: continue
        good=idx[torch.topk(conf[idx], min(k,len(idx))).indices]
        for j in good.detach().cpu().tolist():
            rows.append({'idx':j,'pred':int(pred[j]),'pred_label':LABELS[int(pred[j])],'true':int(y[j]),'true_label':LABELS[int(y[j])],'conf':float(conf[j].cpu()),'pred_logit':float(base[j,pred[j]].cpu()),'true_logit':float(base[j,y[j]].cpu())})
    return rows

def candidate_hypotheses(per_class, global_rows):
    hyps=[]
    # Per-class strongest patch by accuracy drop.
    by_cls={}
    for r in per_class:
        by_cls.setdefault(r['class_label'],[]).append(r)
    for cls,rs in by_cls.items():
        best=max(rs,key=lambda x:(x['acc_drop'], abs(x['pred_logit_drop'])))
        if best['acc_drop']>0.25:
            hyps.append(f"{cls}: class decision is strongly dependent on `{best['patch']}:{best['layer']}:{best['group']}`; patch acc drop={best['acc_drop']:.3f}.")
    # Global strongest modules.
    top=global_rows[:3]
    if top:
        hyps.append('Global mechanism: strongest causal components are ' + ', '.join([f"{r['patch']}[{r['layer']}:{r['group']}]" for r in top]) + '.')
    return hyps[:20]

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--checkpoint',default='local_checkpoints/part/ParticleNet_kinpid.pt')
    ap.add_argument('--data-dir',default=str(Path.home()/'Рабочий стол/jetclass_tiny_balanced'))
    ap.add_argument('--mode',default='kinpid',choices=['kin','kinpid','full'])
    ap.add_argument('--samples-per-file',type=int,default=128)
    ap.add_argument('--max-files',type=int,default=20)
    ap.add_argument('--examples-per-class',type=int,default=2)
    ap.add_argument('--device',default='cuda' if torch.cuda.is_available() else 'cpu')
    ap.add_argument('--out-dir',default='runs/particlenet_hypothesis_atlas_v3')
    args=ap.parse_args(); out=Path(args.out_dir); mkdir(out/'tables')
    model,res,input_dims=make_model(args.checkpoint,args.mode,args.device)
    batch=load_balanced(args.data_dir,mode=args.mode,samples_per_file=args.samples_per_file,max_files=args.max_files,device=args.device)
    base=logits(model,batch); y=batch['y']; pred=base.argmax(-1)
    baseline={'n':int(y.numel()),'acc':float((pred==y).float().mean().cpu()),'pred_counts':pred_counts(pred),'true_counts':pred_counts(y)}
    global_rows=[]; per_class=[]; patched_cache={}
    for spec in build_specs(args.mode,input_dims):
        p,g,pc=run_patch(model,batch,base,y,spec,input_dims)
        global_rows.append(g); per_class.extend(pc)
        if len(patched_cache)<12: patched_cache[(g['patch'],str(g['layer']),str(g['group']))]=p
    global_rows=sorted(global_rows,key=lambda r:abs(float(r['delta_pred_logit'])),reverse=True)
    per_class=sorted(per_class,key=lambda r:(r['class_label'],-r['acc_drop'], -abs(r['pred_logit_drop'])))
    ex=high_conf_examples(base,y,args.examples_per_class)
    top_specs=[(r['patch'],str(r['layer']),str(r['group'])) for r in global_rows[:8]]
    ex_rows=[]
    for e in ex:
        row=dict(e); idx=e['idx']; pid=e['pred']
        for key in top_specs:
            p=patched_cache.get(key)
            if p is None: continue
            col='drop_'+('_'.join(key)).replace(' ','_')
            row[col]=float((base[idx,pid]-p[idx,pid]).detach().cpu())
        ex_rows.append(row)
    hyps=candidate_hypotheses(per_class,global_rows)
    wcsv(out/'tables/hypothesis_global_patches.csv',global_rows)
    wcsv(out/'tables/hypothesis_per_class.csv',per_class)
    wcsv(out/'tables/hypothesis_examples.csv',ex_rows)
    summary={'ok':True,'checkpoint':args.checkpoint,'mode':args.mode,'missing':list(res.missing_keys),'unexpected':list(res.unexpected_keys),'baseline':baseline,'top_global':global_rows[:30],'candidate_hypotheses':hyps,'n_examples':len(ex_rows)}
    wjson(out/'particlenet_hypothesis_atlas_summary.json',summary)
    # compact markdown tables
    pc_top=[]
    for c in LABELS:
        rows=[r for r in per_class if r['class_label']==c]
        if rows: pc_top.append(rows[0])
    ex_cols=list(ex_rows[0].keys()) if ex_rows else []
    ex_cols=ex_cols[:8] + [c for c in ex_cols if c.startswith('drop_')][:8]
    md=['# ParticleNet Hypothesis Atlas v3\n\n',
        f"checkpoint={args.checkpoint}\nmode={args.mode}\nn={baseline['n']}\nmissing={summary['missing']} unexpected={summary['unexpected']}\n\n",
        '## Baseline\n\n```json\n',json.dumps(baseline,indent=2,ensure_ascii=False),'\n```\n\n',
        '## Global causal map: all inputs, particles, EdgeConv and FC layers\n',
        table(['rank','patch','layer','group','delta_logit','KL','top1','acc->patch_acc'],[[i+1,r['patch'],r.get('layer',''),r.get('group',''),fmt(r['delta_pred_logit']),fmt(r['kl']),fmt(r['top1_match']),f"{fmt(r['base_acc'])}->{fmt(r['patch_acc'])}"] for i,r in enumerate(global_rows[:30])]),
        '\n## Per-class strongest causal patch\n',
        table(['class','patch','layer','group','acc_drop','logit_drop','base->patch_acc'],[[r['class_label'],r['patch'],r['layer'],r['group'],fmt(r['acc_drop']),fmt(r['pred_logit_drop']),f"{fmt(r['base_acc'])}->{fmt(r['patch_acc'])}"] for r in pc_top]),
        '\n## Candidate hypotheses\n\n']
    md += [f"- {h}\n" for h in hyps]
    md += ['\n## Example-level signed drops\n', table(ex_cols, [[r.get(c,'') for c in ex_cols] for r in ex_rows[:40]]),
           '\nFull CSV tables:\n- `reports/latest/tables/hypothesis_global_patches.csv`\n- `reports/latest/tables/hypothesis_per_class.csv`\n- `reports/latest/tables/hypothesis_examples.csv`\n']
    (out/'PARTICLENET_HYPOTHESIS_ATLAS_V3.md').write_text(''.join(md),encoding='utf-8')
    print(json.dumps(summary,indent=2,ensure_ascii=False)[:20000])

if __name__=='__main__': main()
