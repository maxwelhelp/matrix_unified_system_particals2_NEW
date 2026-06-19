#!/usr/bin/env python3
import argparse, csv, glob, json, sys
from pathlib import Path
import numpy as np
import torch
import torch.nn.functional as F

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from tools.particlenet_real_patch_controls_v1 import load_balanced, clean, unwrap, logits, fmt, table
from data.jetclass_tiny_loader_v3_official import LABELS

FEATURE_NAMES={
 'kin':['part_pt_log','part_e_log','part_logptrel','part_logerel','part_deltaR','part_deta','part_dphi'],
 'kinpid':['part_pt_log','part_e_log','part_logptrel','part_logerel','part_deltaR','part_charge','part_isChargedHadron','part_isNeutralHadron','part_isPhoton','part_isElectron','part_isMuon','part_deta','part_dphi'],
 'full':['part_pt_log','part_e_log','part_logptrel','part_logerel','part_deltaR','part_charge','part_isChargedHadron','part_isNeutralHadron','part_isPhoton','part_isElectron','part_isMuon','part_d0','part_d0err','part_dz','part_dzerr','part_deta','part_dphi'],
}
OBS=['jet_pt','jet_energy','jet_nparticles','jet_sdmass','jet_tau1','jet_tau2','jet_tau3','jet_tau4']
CONTRASTS=[('label_Wqq','label_Zqq'),('label_Tbqq','label_Tbl'),('label_Hbb','label_Hcc'),('label_Hbb','label_Hgg'),('label_H4q','label_Hqql'),('label_QCD','label_Wqq'),('label_QCD','label_Tbqq')]

def mkdir(p): Path(p).mkdir(parents=True,exist_ok=True)
def wjson(p,o): p=Path(p); mkdir(p.parent); p.write_text(json.dumps(o,indent=2,ensure_ascii=False),encoding='utf-8')
def wcsv(p,rows):
    p=Path(p); mkdir(p.parent); keys=[]; seen=set()
    for r in rows:
        for k in r:
            if k not in seen: keys.append(k); seen.add(k)
    with p.open('w',encoding='utf-8',newline='') as f:
        wr=csv.DictWriter(f,fieldnames=keys); wr.writeheader(); [wr.writerow({k:r.get(k,'') for k in keys}) for r in rows]
def readcsv(p):
    p=Path(p)
    if not p.exists(): return []
    with p.open('r',encoding='utf-8') as f: return list(csv.DictReader(f))
def fnum(x):
    try: return float(x)
    except Exception: return 0.0

def make_model(checkpoint,mode,device):
    from weaver.nn.model.ParticleNet import ParticleNet
    input_dims={'kin':7,'kinpid':13,'full':17}[mode]
    model=ParticleNet(input_dims=input_dims,num_classes=10,conv_params=[(16,(64,64,64)),(16,(128,128,128)),(16,(256,256,256))],fc_params=[(256,0.1)],use_fusion=False,use_fts_bn=True,use_counts=True,trim=True,for_inference=False).to(device).eval()
    sd=clean(unwrap(torch.load(checkpoint,map_location='cpu')))
    res=model.load_state_dict(sd,strict=False)
    return model,res,input_dims

def metric(base,patch,y):
    pred=base.argmax(-1); pp=patch.argmax(-1)
    la=F.log_softmax(base.float(),-1); lb=F.log_softmax(patch.float(),-1)
    return {'delta_pred_logit':float((base.gather(1,pred[:,None]).mean()-patch.gather(1,pred[:,None]).mean()).cpu()),'kl':float((la.exp()*(la-lb)).sum(-1).mean().cpu()),'top1_match':float((pp==pred).float().mean().cpu()),'base_acc':float((pred==y).float().mean().cpu()),'patch_acc':float((pp==y).float().mean().cpu())}

def per_class_rows(base,patch,y,patch_name,layer,group):
    pred=base.argmax(-1); pp=patch.argmax(-1); rows=[]
    for c,lbl in enumerate(LABELS):
        m=(y==c)
        if int(m.sum())==0: continue
        ba=float((pred[m]==y[m]).float().mean().cpu()); pa=float((pp[m]==y[m]).float().mean().cpu())
        drop=float((base[m].gather(1,pred[m,None])-patch[m].gather(1,pred[m,None])).mean().cpu())
        rows.append({'patch':patch_name,'layer':layer,'group':group,'class_id':c,'class_label':lbl,'n':int(m.sum().cpu()),'base_acc':ba,'patch_acc':pa,'acc_drop':ba-pa,'pred_logit_drop':drop})
    return rows

def edge_channel_head_ablation(model,batch,base,y,groups=8):
    rows=[]; pc=[]
    for layer,conv in enumerate(model.edge_convs):
        # Capture output channels once.
        cap={}
        def caphook(m,inp,out): cap['shape']=tuple(out.shape)
        h=conv.register_forward_hook(caphook); _=logits(model,batch); h.remove()
        shape=cap.get('shape')
        if not shape or len(shape)<2: continue
        C=shape[1]
        cuts=[]
        for g in range(groups):
            a=(C*g)//groups; b=(C*(g+1))//groups
            if a<b: cuts.append((g,a,b))
        for g,a,b in cuts:
            def hook(m,inp,out,a=a,b=b):
                z=out.clone(); z[:,a:b,...]=0; return z
            h=conv.register_forward_hook(hook); p=logits(model,batch); h.remove()
            r={'patch':'edge_channel_head_zero','layer':layer,'group':f'ch{a}:{b}','channel_head':g,'channels':f'{a}:{b}',**metric(base,p,y)}
            rows.append(r); pc.extend(per_class_rows(base,p,y,'edge_channel_head_zero',layer,f'ch{a}:{b}'))
    rows=sorted(rows,key=lambda r:abs(r['delta_pred_logit']),reverse=True)
    pc=sorted(pc,key=lambda r:(r['class_label'],-abs(r['pred_logit_drop'])))
    return rows,pc

def feature_channel_per_class(model,batch,base,y,mode):
    rows=[]; names=FEATURE_NAMES[mode]
    for i,name in enumerate(names):
        b={k:(v.clone() if torch.is_tensor(v) else v) for k,v in batch.items()}
        b['features'][:,i,:]=0
        p=logits(model,b)
        for r in per_class_rows(base,p,y,'feature_channel_zero','input',name):
            r['feature_id']=i; rows.append(r)
    return sorted(rows,key=lambda r:(r['class_label'],-abs(r['pred_logit_drop'])))

def load_observables(data_dir,samples_per_file=128,max_files=20):
    try:
        import uproot
    except Exception:
        return []
    files=sorted(glob.glob(str(Path(data_dir)/'**/*.root'),recursive=True))[:max_files]
    rows=[]
    for fp in files:
        try:
            tr=uproot.open(fp)['tree']; branches=set(tr.keys()); need=[b for b in OBS if b in branches]
            labels=[b for b in LABELS if b in branches]
            if not need or not labels: continue
            arr=tr.arrays(need+labels,entry_stop=min(samples_per_file,int(tr.num_entries)),library='np')
            y=np.stack([arr[l] for l in LABELS],axis=1).argmax(axis=1)
            for c,lbl in enumerate(LABELS):
                m=(y==c)
                if not np.any(m): continue
                row={'class_id':c,'class_label':lbl,'n':int(m.sum())}
                for ob in need:
                    vals=np.asarray(arr[ob])[m]
                    row[ob+'_mean']=float(np.nanmean(vals)); row[ob+'_p50']=float(np.nanmedian(vals)); row[ob+'_p90']=float(np.nanquantile(vals,0.9))
                rows.append(row)
        except Exception as e:
            rows.append({'file':fp,'error':str(e)})
    # merge class means across files by simple averaging weighted by n
    merged={}
    for r in rows:
        if 'error' in r: continue
        key=r['class_label']; merged.setdefault(key,[]).append(r)
    out=[]
    for key,rs in merged.items():
        tot=sum(int(r.get('n',0)) for r in rs); row={'class_label':key,'n':tot}
        for ob in OBS:
            for suf in ['mean','p50','p90']:
                k=ob+'_'+suf; vals=[(float(r[k]),int(r['n'])) for r in rs if k in r]
                if vals and tot>0: row[k]=sum(v*n for v,n in vals)/sum(n for _,n in vals)
        out.append(row)
    return out

def class_contrasts(route_rows,obs_rows,feat_pc,edge_pc):
    by_route={(r.get('layer'),r.get('class_label')):r for r in route_rows}
    by_obs={r.get('class_label'):r for r in obs_rows}
    rows=[]
    for a,b in CONTRASTS:
        row={'contrast':f'{a}_vs_{b}','A':a,'B':b}
        for layer in ['0','1','2',0,1,2]:
            ra=by_route.get((layer,a)); rb=by_route.get((layer,b))
            if ra and rb:
                row[f'layer{layer}_neighbor_dr_mean_A']=ra.get('neighbor_dr_mean'); row[f'layer{layer}_neighbor_dr_mean_B']=rb.get('neighbor_dr_mean')
                row[f'layer{layer}_neighbor_dr_mean_delta_A_minus_B']=fnum(ra.get('neighbor_dr_mean'))-fnum(rb.get('neighbor_dr_mean'))
        oa=by_obs.get(a); ob=by_obs.get(b)
        if oa and ob:
            for key in ['jet_sdmass_mean','jet_nparticles_mean','jet_tau1_mean','jet_tau2_mean','jet_tau3_mean','jet_tau4_mean']:
                if key in oa and key in ob:
                    row[key+'_A']=oa[key]; row[key+'_B']=ob[key]; row[key+'_delta_A_minus_B']=fnum(oa[key])-fnum(ob[key])
        rows.append(row)
    return rows

def synthesize(edge_rows,feat_rows,route_rows,particle_rows,contrast_rows,obs_rows):
    hyps=[]
    top_heads=edge_rows[:5]
    if top_heads:
        hyps.append('EdgeConv pseudo-head hypothesis: strongest channel-head groups are '+', '.join([f"L{r['layer']}:{r['group']}" for r in top_heads])+'. These groups should be traced as internal model heads.')
    # Per-class route width
    for layer in ['0','1','2',0,1,2]:
        rs=[r for r in route_rows if str(r.get('layer'))==str(layer)]
        if rs:
            lo=min(rs,key=lambda r:fnum(r.get('neighbor_dr_mean'))); hi=max(rs,key=lambda r:fnum(r.get('neighbor_dr_mean')))
            hyps.append(f"Route-width hypothesis L{layer}: {lo.get('class_label')} has compact neighbor routing ({fnum(lo.get('neighbor_dr_mean')):.4f}), {hi.get('class_label')} has wide routing ({fnum(hi.get('neighbor_dr_mean')):.4f}).")
    # Feature per class strongest
    by_cls={}
    for r in feat_rows: by_cls.setdefault(r['class_label'],[]).append(r)
    for cls,rs in by_cls.items():
        best=max(rs,key=lambda r:abs(fnum(r.get('pred_logit_drop'))))
        if abs(fnum(best.get('pred_logit_drop')))>5:
            hyps.append(f"{cls}: strongest explicit feature-channel candidate is {best.get('group')} with logit_drop={fnum(best.get('pred_logit_drop')):.2f}.")
    # Particle vs random
    pr={r.get('group'):r for r in particle_rows}
    if 'top_pt' in pr and 'random_control' in pr:
        hyps.append(f"Leading-particle control: top_pt ablation accuracy={fnum(pr['top_pt'].get('patch_acc')):.3f} vs random={fnum(pr['random_control'].get('patch_acc')):.3f}; leading particles are not interchangeable with random particles.")
    return hyps[:30]

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--checkpoint',default='local_checkpoints/part/ParticleNet_kinpid.pt')
    ap.add_argument('--data-dir',default=str(Path.home()/'Рабочий стол/jetclass_tiny_balanced'))
    ap.add_argument('--mode',default='kinpid',choices=['kin','kinpid','full'])
    ap.add_argument('--samples-per-file',type=int,default=128)
    ap.add_argument('--max-files',type=int,default=20)
    ap.add_argument('--edge-head-groups',type=int,default=8)
    ap.add_argument('--device',default='cuda' if torch.cuda.is_available() else 'cpu')
    ap.add_argument('--out-dir',default='runs/particlenet_research_compass_v5')
    args=ap.parse_args(); out=Path(args.out_dir); mkdir(out/'tables')
    model,res,input_dims=make_model(args.checkpoint,args.mode,args.device)
    batch=load_balanced(args.data_dir,mode=args.mode,samples_per_file=args.samples_per_file,max_files=args.max_files,device=args.device)
    base=logits(model,batch); y=batch['y']; pred=base.argmax(-1)
    baseline={'n':int(y.numel()),'acc':float((pred==y).float().mean().cpu()),'pred_counts':torch.bincount(pred.cpu(),minlength=10).tolist(),'true_counts':torch.bincount(y.cpu(),minlength=10).tolist()}
    edge_rows,edge_pc=edge_channel_head_ablation(model,batch,base,y,args.edge_head_groups)
    feat_pc=feature_channel_per_class(model,batch,base,y,args.mode)
    route_rows=readcsv('reports/latest/tables/discovery_route_knn_stats.csv')
    particle_rows=readcsv('reports/latest/tables/discovery_particle_controls.csv')
    obs_rows=load_observables(args.data_dir,args.samples_per_file,args.max_files)
    contrast_rows=class_contrasts(route_rows,obs_rows,feat_pc,edge_pc)
    hyps=synthesize(edge_rows,feat_pc,route_rows,particle_rows,contrast_rows,obs_rows)
    wcsv(out/'tables/research_edge_channel_heads.csv',edge_rows)
    wcsv(out/'tables/research_edge_channel_heads_per_class.csv',edge_pc)
    wcsv(out/'tables/research_feature_channels_per_class.csv',feat_pc)
    wcsv(out/'tables/research_known_observables_by_class.csv',obs_rows)
    wcsv(out/'tables/research_class_contrasts.csv',contrast_rows)
    summary={'ok':True,'checkpoint':args.checkpoint,'mode':args.mode,'baseline':baseline,'missing':list(res.missing_keys),'unexpected':list(res.unexpected_keys),'hypotheses':hyps,'n_edge_heads':len(edge_rows),'n_feature_class_rows':len(feat_pc),'n_observable_rows':len(obs_rows)}
    wjson(out/'particlenet_research_compass_v5_summary.json',summary)
    # compact report
    top_feat=[]
    by_cls={}
    for r in feat_pc: by_cls.setdefault(r['class_label'],[]).append(r)
    for cls,rs in by_cls.items():
        best=max(rs,key=lambda r:abs(fnum(r.get('pred_logit_drop')))); top_feat.append(best)
    md=['# ParticleNet Research Compass v5\n\n',
        'Purpose: richer research layer for particle-interaction hypotheses. It adds EdgeConv channel-head groups, per-class feature channels, known observables, and class contrasts.\n\n',
        f"checkpoint={args.checkpoint}\nmode={args.mode}\nn={baseline['n']}\nmissing={summary['missing']} unexpected={summary['unexpected']}\n\n",
        '## Baseline\n\n```json\n',json.dumps(baseline,indent=2,ensure_ascii=False),'\n```\n\n',
        '## Priority hypotheses / research notes\n\n']
    md += [f"- {h}\n" for h in hyps]
    md += ['\n## EdgeConv pseudo-head groups: strongest causal channel groups\n',
           table(['rank','layer','channel_head','channels','delta_logit','KL','top1','acc->patch_acc'],[[i+1,r['layer'],r['channel_head'],r['channels'],fmt(r['delta_pred_logit']),fmt(r['kl']),fmt(r['top1_match']),f"{fmt(r['base_acc'])}->{fmt(r['patch_acc'])}"] for i,r in enumerate(edge_rows[:25])]),
           '\n## Per-class strongest explicit feature channel\n',
           table(['class','feature','logit_drop','acc_drop','base->patch_acc'],[[r['class_label'],r['group'],fmt(r['pred_logit_drop']),fmt(r['acc_drop']),f"{fmt(r['base_acc'])}->{fmt(r['patch_acc'])}"] for r in top_feat]),
           '\n## Known observables by class\n',
           table(['class','n','jet_nparticles_mean','jet_sdmass_mean','jet_tau1_mean','jet_tau2_mean','jet_tau3_mean','jet_tau4_mean'],[[r.get('class_label'),r.get('n'),fmt(r.get('jet_nparticles_mean')),fmt(r.get('jet_sdmass_mean')),fmt(r.get('jet_tau1_mean')),fmt(r.get('jet_tau2_mean')),fmt(r.get('jet_tau3_mean')),fmt(r.get('jet_tau4_mean'))] for r in obs_rows]),
           '\n## Class contrast table\n',
           table(['contrast','L0_dr_delta','L1_dr_delta','L2_dr_delta','sdmass_delta','nparticles_delta'],[[r.get('contrast'),fmt(r.get('layer0_neighbor_dr_mean_delta_A_minus_B')),fmt(r.get('layer1_neighbor_dr_mean_delta_A_minus_B')),fmt(r.get('layer2_neighbor_dr_mean_delta_A_minus_B')),fmt(r.get('jet_sdmass_mean_delta_A_minus_B')),fmt(r.get('jet_nparticles_mean_delta_A_minus_B'))] for r in contrast_rows]),
           '\n## Tables written\n\n- `reports/latest/tables/research_edge_channel_heads.csv`\n- `reports/latest/tables/research_edge_channel_heads_per_class.csv`\n- `reports/latest/tables/research_feature_channels_per_class.csv`\n- `reports/latest/tables/research_known_observables_by_class.csv`\n- `reports/latest/tables/research_class_contrasts.csv`\n']
    (out/'PARTICLENET_RESEARCH_COMPASS_V5.md').write_text(''.join(md),encoding='utf-8')
    print(json.dumps(summary,indent=2,ensure_ascii=False)[:20000])

if __name__=='__main__': main()
