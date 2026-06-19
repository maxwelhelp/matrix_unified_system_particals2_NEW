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
def readcsv(p):
    p=Path(p)
    if not p.exists(): return []
    with p.open('r',encoding='utf-8') as f: return list(csv.DictReader(f))

def make_model(checkpoint, mode, device):
    from weaver.nn.model.ParticleNet import ParticleNet
    input_dims={'kin':7,'kinpid':13,'full':17}[mode]
    model=ParticleNet(input_dims=input_dims,num_classes=10,conv_params=[(16,(64,64,64)),(16,(128,128,128)),(16,(256,256,256))],fc_params=[(256,0.1)],use_fusion=False,use_fts_bn=True,use_counts=True,trim=True,for_inference=False).to(device).eval()
    sd=clean(unwrap(torch.load(checkpoint,map_location='cpu')))
    res=model.load_state_dict(sd, strict=False)
    return model,res,input_dims

def pairwise_dist(x):
    inner=-2*torch.matmul(x.transpose(2,1),x)
    xx=torch.sum(x*x,dim=1,keepdim=True)
    return (xx.transpose(2,1)+inner+xx).clamp(min=0)

def knn_idx(x,k):
    return pairwise_dist(x).topk(k=k+1,dim=-1,largest=False,sorted=True)[1][:,:,1:]

def gather_vals(vals, idx):
    b,n,k=idx.shape
    return vals.gather(1, idx.reshape(b,-1)).reshape(b,n,k)

def route_probe(model,batch,y,base,out_dir):
    captures=[]; hooks=[]
    def make_hook(layer_id):
        def hook(m,inp):
            points=inp[0].detach()
            feats=inp[1].detach()
            captures.append({'layer':layer_id,'k':int(getattr(m,'k',16)),'points':points,'features':feats})
        return hook
    for i,conv in enumerate(model.edge_convs):
        hooks.append(conv.register_forward_pre_hook(make_hook(i)))
    _=logits(model,batch)
    for h in hooks: h.remove()
    rows=[]
    # original physical coordinates for physical-route summaries
    deta=batch['points'][:,0,:].detach(); dphi=batch['points'][:,1,:].detach()
    dr=torch.sqrt(deta*deta+dphi*dphi)
    pt=torch.sqrt(batch['vectors'][:,0,:]**2 + batch['vectors'][:,1,:]**2).detach()
    energy=batch['vectors'][:,3,:].detach()
    mask=batch['mask'][:,0,:].detach().bool()
    for cap in captures:
        layer=cap['layer']; pts=cap['points']; k=cap['k']
        idx=knn_idx(pts,k)
        dist=gather_vals(pairwise_dist(pts).mean(dim=1), idx).float() if False else None
        neigh_dr=gather_vals(dr, idx).masked_fill(~gather_vals(mask.float(),idx).bool(), float('nan'))
        neigh_pt=gather_vals(pt, idx).masked_fill(~gather_vals(mask.float(),idx).bool(), float('nan'))
        neigh_energy=gather_vals(energy, idx).masked_fill(~gather_vals(mask.float(),idx).bool(), float('nan'))
        for c,lbl in enumerate(LABELS):
            m=(y==c)
            if int(m.sum())==0: continue
            vals_dr=neigh_dr[m].reshape(-1)
            vals_pt=neigh_pt[m].reshape(-1)
            vals_en=neigh_energy[m].reshape(-1)
            vals_dr=vals_dr[~torch.isnan(vals_dr)]; vals_pt=vals_pt[~torch.isnan(vals_pt)]; vals_en=vals_en[~torch.isnan(vals_en)]
            row={'layer':layer,'class_id':c,'class_label':lbl,'n_events':int(m.sum().cpu()),'k':k}
            for name,vals in [('neighbor_dr',vals_dr),('neighbor_pt',vals_pt),('neighbor_energy',vals_en)]:
                if vals.numel()==0:
                    row[name+'_mean']=''; row[name+'_p90']=''; row[name+'_max']=''
                else:
                    row[name+'_mean']=float(vals.mean().cpu())
                    row[name+'_p90']=float(torch.quantile(vals.float(),0.9).cpu())
                    row[name+'_max']=float(vals.max().cpu())
            rows.append(row)
    return rows

def metric(base,patch,y):
    pred=base.argmax(-1); pp=patch.argmax(-1)
    la=F.log_softmax(base.float(),-1); lb=F.log_softmax(patch.float(),-1)
    return {'delta_pred_logit':float((base.gather(1,pred[:,None]).mean()-patch.gather(1,pred[:,None]).mean()).cpu()),'kl':float((la.exp()*(la-lb)).sum(-1).mean().cpu()),'top1_match':float((pp==pred).float().mean().cpu()),'base_acc':float((pred==y).float().mean().cpu()),'patch_acc':float((pp==y).float().mean().cpu())}

def particle_ablation_rows(model,batch,base,y):
    rows=[]
    px,py=batch['vectors'][:,0,:],batch['vectors'][:,1,:]
    pt=torch.sqrt(px*px+py*py); en=batch['vectors'][:,3,:]
    dr=torch.sqrt(batch['points'][:,0,:]**2+batch['points'][:,1,:]**2)
    scores={'top_pt':pt,'top_energy':en,'wide_angle_high_dr':dr,'core_low_dr':-dr}
    g=torch.Generator(device=pt.device); g.manual_seed(123)
    scores['random_control']=torch.rand(pt.shape,device=pt.device,generator=g)
    for name,score in scores.items():
        b={k:(v.clone() if torch.is_tensor(v) else v) for k,v in batch.items()}
        idx=torch.topk(score,min(8,score.shape[-1]),dim=-1).indices
        b['mask']=batch['mask'].clone(); b['mask'].scatter_(2,idx[:,None,:],False)
        p=logits(model,b)
        r={'patch':'particle_top8_mask_zero','layer':'particles','group':name,**metric(base,p,y)}
        # overlap with top_pt for debugging
        top_pt=torch.topk(pt,min(8,pt.shape[-1]),dim=-1).indices
        inter=[]
        for a,bidx in zip(idx.detach().cpu(), top_pt.detach().cpu()):
            inter.append(len(set(a.tolist()) & set(bidx.tolist()))/max(1,len(set(a.tolist()) | set(bidx.tolist()))))
        r['mean_jaccard_with_top_pt']=sum(inter)/len(inter)
        rows.append(r)
    return rows

def synthesize(global_rows, per_class_rows, route_rows, particle_rows):
    hyps=[]
    def fnum(x):
        try: return float(x)
        except Exception: return 0.0
    top=sorted(global_rows,key=lambda r:abs(fnum(r.get('delta_pred_logit',0))),reverse=True)[:5]
    if top:
        hyps.append('Global: strongest causal components are '+', '.join([f"{r.get('patch')}[{r.get('layer')}:{r.get('group')}]" for r in top])+'.')
    # non-edge feature hypotheses
    feats=[r for r in global_rows if 'feature_channel_zero' in r.get('patch','') or 'feature_group_zero' in r.get('patch','')]
    feats=sorted(feats,key=lambda r:abs(fnum(r.get('delta_pred_logit',0))),reverse=True)[:5]
    if feats:
        hyps.append('Feature hypothesis: most influential explicit channels/groups are '+', '.join([str(r.get('group')) for r in feats])+'.')
    # particle control
    pr=sorted(particle_rows,key=lambda r:abs(fnum(r.get('delta_pred_logit',0))),reverse=True)
    if pr:
        hyps.append('Particle-subset hypothesis: removing '+str(pr[0].get('group'))+f" particles produces strongest top-8 particle control effect; compare against random_control before claiming physics.")
    # route class difference
    if route_rows:
        by_layer={}
        for r in route_rows:
            by_layer.setdefault(r['layer'],[]).append(r)
        for layer,rs in by_layer.items():
            vals=[(r['class_label'],fnum(r.get('neighbor_dr_mean',0))) for r in rs]
            if vals:
                lo=min(vals,key=lambda x:x[1]); hi=max(vals,key=lambda x:x[1])
                hyps.append(f"Route layer {layer}: neighbor ΔR differs by class; lowest mean {lo[0]}={lo[1]:.4f}, highest mean {hi[0]}={hi[1]:.4f}.")
    return hyps[:20]

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--checkpoint',default='local_checkpoints/part/ParticleNet_kinpid.pt')
    ap.add_argument('--data-dir',default=str(Path.home()/'Рабочий стол/jetclass_tiny_balanced'))
    ap.add_argument('--mode',default='kinpid',choices=['kin','kinpid','full'])
    ap.add_argument('--samples-per-file',type=int,default=128)
    ap.add_argument('--max-files',type=int,default=20)
    ap.add_argument('--device',default='cuda' if torch.cuda.is_available() else 'cpu')
    ap.add_argument('--out-dir',default='runs/particlenet_discovery_atlas_v4')
    args=ap.parse_args(); out=Path(args.out_dir); mkdir(out/'tables')
    model,res,input_dims=make_model(args.checkpoint,args.mode,args.device)
    batch=load_balanced(args.data_dir,mode=args.mode,samples_per_file=args.samples_per_file,max_files=args.max_files,device=args.device)
    base=logits(model,batch); y=batch['y']; pred=base.argmax(-1)
    baseline={'n':int(y.numel()),'acc':float((pred==y).float().mean().cpu()),'pred_counts':torch.bincount(pred.cpu(),minlength=10).tolist(),'true_counts':torch.bincount(y.cpu(),minlength=10).tolist()}
    # Read v3 tables if present; v4 adds route and corrected particle controls.
    global_rows=readcsv('reports/latest/tables/hypothesis_global_patches.csv')
    per_class_rows=readcsv('reports/latest/tables/hypothesis_per_class.csv')
    route_rows=route_probe(model,batch,y,base,out)
    particle_rows=particle_ablation_rows(model,batch,base,y)
    hyps=synthesize(global_rows,per_class_rows,route_rows,particle_rows)
    wcsv(out/'tables/discovery_route_knn_stats.csv',route_rows)
    wcsv(out/'tables/discovery_particle_controls.csv',particle_rows)
    summary={'ok':True,'checkpoint':args.checkpoint,'mode':args.mode,'missing':list(res.missing_keys),'unexpected':list(res.unexpected_keys),'baseline':baseline,'candidate_discovery_hypotheses':hyps,'n_route_rows':len(route_rows),'n_particle_rows':len(particle_rows)}
    wjson(out/'particlenet_discovery_atlas_v4_summary.json',summary)
    md=['# ParticleNet Discovery Atlas v4\n\n',
        'Purpose: convert causal patches and dynamic graph routes into candidate physics/mechanistic hypotheses. These are not discovery claims yet; they are candidates requiring heldout validation and physics review.\n\n',
        f"checkpoint={args.checkpoint}\nmode={args.mode}\nn={baseline['n']}\nmissing={summary['missing']} unexpected={summary['unexpected']}\n\n",
        '## Baseline\n\n```json\n',json.dumps(baseline,indent=2,ensure_ascii=False),'\n```\n\n',
        '## Candidate discovery hypotheses\n\n']
    md += [f"- {h}\n" for h in hyps]
    md += ['\n## Corrected particle-subset controls\n', table(['group','delta_logit','KL','top1','acc->patch_acc','jaccard_top_pt'],[[r['group'],fmt(r['delta_pred_logit']),fmt(r['kl']),fmt(r['top1_match']),f"{fmt(r['base_acc'])}->{fmt(r['patch_acc'])}",fmt(r.get('mean_jaccard_with_top_pt'))] for r in particle_rows]),
           '\n## Dynamic KNN / EdgeConv route stats by class\n', table(['layer','class','k','neighbor_dr_mean','neighbor_dr_p90','neighbor_pt_mean','neighbor_energy_mean'],[[r['layer'],r['class_label'],r['k'],fmt(r.get('neighbor_dr_mean')),fmt(r.get('neighbor_dr_p90')),fmt(r.get('neighbor_pt_mean')),fmt(r.get('neighbor_energy_mean'))] for r in route_rows[:60]]),
           '\n## Existing v3 causal tables used as context\n\n- `reports/latest/tables/hypothesis_global_patches.csv`\n- `reports/latest/tables/hypothesis_per_class.csv`\n- `reports/latest/tables/hypothesis_examples.csv`\n\n## New v4 tables\n\n- `reports/latest/tables/discovery_route_knn_stats.csv`\n- `reports/latest/tables/discovery_particle_controls.csv`\n']
    (out/'PARTICLENET_DISCOVERY_ATLAS_V4.md').write_text(''.join(md),encoding='utf-8')
    print(json.dumps(summary,indent=2,ensure_ascii=False)[:20000])

if __name__=='__main__': main()
