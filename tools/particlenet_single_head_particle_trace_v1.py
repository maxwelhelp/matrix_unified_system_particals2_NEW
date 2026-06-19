#!/usr/bin/env python3
import argparse, csv, json, sys
from pathlib import Path
import torch
import torch.nn.functional as F

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools.particlenet_real_patch_controls_v1 import load_balanced, clean, unwrap, logits
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
def fmt(x):
    try: x=float(x)
    except Exception: return 'n/a'
    return f'{x:.3e}' if abs(x)>0 and (abs(x)<1e-3 or abs(x)>1e4) else f'{x:.4f}'
def table(h,rs):
    if not rs: return '_No rows._\n'
    return '\n'.join(['| '+' | '.join(h)+' |','| '+' | '.join(['---']*len(h))+' |']+['| '+' | '.join(str(x) for x in r)+' |' for r in rs])+'\n'

def parse_group(s):
    s=str(s).replace('ch','')
    a,b=s.split(':')
    return int(a),int(b)

def make_model(checkpoint, mode, device):
    from weaver.nn.model.ParticleNet import ParticleNet
    input_dims={'kin':7,'kinpid':13,'full':17}[mode]
    model=ParticleNet(input_dims=input_dims,num_classes=10,conv_params=[(16,(64,64,64)),(16,(128,128,128)),(16,(256,256,256))],fc_params=[(256,0.1)],use_fusion=False,use_fts_bn=True,use_counts=True,trim=True,for_inference=False).to(device).eval()
    sd=clean(unwrap(torch.load(checkpoint,map_location='cpu')))
    res=model.load_state_dict(sd, strict=False)
    return model,res,input_dims

def capture_head(model,batch,layer,group):
    a,b=parse_group(group)
    cap={}
    def hook(m,inp,out):
        cap['out']=out.detach()
    h=model.edge_convs[layer].register_forward_hook(hook)
    base=logits(model,batch)
    h.remove()
    out=cap['out']
    # out usually [B,C,N]
    head=out[:,a:b,:].float()
    energy=torch.sqrt((head*head).sum(dim=1)+1e-12)
    return base,energy,out.shape

def particle_features(batch, mode, event_idx, particle_idx):
    features=batch['features'][event_idx,:,particle_idx].detach().cpu().float().tolist()
    names=FEATURE_NAMES[mode]
    row={}
    for n,v in zip(names,features): row[n]=float(v)
    vec=batch['vectors'][event_idx,:,particle_idx].detach().cpu().float()
    px,py,pz,e=float(vec[0]),float(vec[1]),float(vec[2]),float(vec[3])
    pt=(px*px+py*py)**0.5
    deta=float(batch['points'][event_idx,0,particle_idx].detach().cpu())
    dphi=float(batch['points'][event_idx,1,particle_idx].detach().cpu())
    dr=(deta*deta+dphi*dphi)**0.5
    row.update({'px':px,'py':py,'pz':pz,'energy':e,'pt':pt,'deta':deta,'dphi':dphi,'deltaR_from_axis':dr})
    return row

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--checkpoint',default='local_checkpoints/part/ParticleNet_kinpid.pt')
    ap.add_argument('--data-dir',default=str(Path.home()/'Рабочий стол/jetclass_tiny_balanced'))
    ap.add_argument('--mode',default='kinpid',choices=['kin','kinpid','full'])
    ap.add_argument('--layer',type=int,default=1)
    ap.add_argument('--group',default='ch16:32')
    ap.add_argument('--samples-per-file',type=int,default=64)
    ap.add_argument('--max-files',type=int,default=20)
    ap.add_argument('--top-events',type=int,default=20)
    ap.add_argument('--top-particles',type=int,default=8)
    ap.add_argument('--device',default='cuda' if torch.cuda.is_available() else 'cpu')
    ap.add_argument('--out-dir',default='runs/particlenet_single_head_particle_trace_v1')
    args=ap.parse_args(); out=Path(args.out_dir); mkdir(out/'tables')
    model,res,input_dims=make_model(args.checkpoint,args.mode,args.device)
    batch=load_balanced(args.data_dir,mode=args.mode,samples_per_file=args.samples_per_file,max_files=args.max_files,device=args.device)
    base,energy,out_shape=capture_head(model,batch,args.layer,args.group)
    prob=F.softmax(base.float(),dim=-1); pred=base.argmax(-1); y=batch['y']
    event_score=energy.max(dim=1).values
    top_e=torch.topk(event_score,min(args.top_events,event_score.numel())).indices.detach().cpu().tolist()
    event_rows=[]; particle_rows=[]
    for ei in top_e:
        real_mask=batch['mask'][ei,0,:].detach().bool()
        real_n=int(real_mask.sum().cpu())
        pe=energy[ei].masked_fill(~real_mask, -1)
        idx=torch.topk(pe,min(args.top_particles,real_n)).indices.detach().cpu().tolist()
        event_rows.append({'event_idx':ei,'true':int(y[ei]),'true_label':LABELS[int(y[ei])],'pred':int(pred[ei]),'pred_label':LABELS[int(pred[ei])],'conf':float(prob[ei,pred[ei]].detach().cpu()),'pred_logit':float(base[ei,pred[ei]].detach().cpu()),'head_max_particle_energy':float(pe.max().detach().cpu()),'real_particles':real_n,'top_particle_indices':json.dumps(idx)})
        for rank,pi in enumerate(idx,1):
            fr=particle_features(batch,args.mode,ei,pi)
            row={'event_idx':ei,'rank':rank,'particle_idx':pi,'head_energy':float(energy[ei,pi].detach().cpu()),'true_label':LABELS[int(y[ei])],'pred_label':LABELS[int(pred[ei])],'conf':float(prob[ei,pred[ei]].detach().cpu())}
            row.update(fr); particle_rows.append(row)
    # Aggregate by predicted class.
    agg=[]
    for c,lbl in enumerate(LABELS):
        m=(pred==c)
        if int(m.sum())==0: continue
        vals=event_score[m]
        agg.append({'pred_label':lbl,'n_pred':int(m.sum().cpu()),'head_event_score_mean':float(vals.mean().detach().cpu()),'head_event_score_p90':float(torch.quantile(vals.float(),0.9).detach().cpu()),'acc_within_pred':float((y[m]==pred[m]).float().mean().detach().cpu())})
    wcsv(out/'tables/single_head_event_trace.csv',event_rows)
    wcsv(out/'tables/single_head_particle_trace.csv',particle_rows)
    wcsv(out/'tables/single_head_class_summary.csv',agg)
    summary={'ok':True,'checkpoint':args.checkpoint,'mode':args.mode,'layer':args.layer,'group':args.group,'captured_output_shape':list(out_shape),'n_events':int(y.numel()),'baseline_acc':float((pred==y).float().mean().detach().cpu()),'missing':list(res.missing_keys),'unexpected':list(res.unexpected_keys),'top_events':event_rows[:10],'class_summary':agg}
    wjson(out/'single_head_particle_trace_summary.json',summary)
    md=['# ParticleNet Single Head Particle Trace v1\n\n',
        f"Head: EdgeConv L{args.layer} {args.group}\n\n",
        f"n_events={summary['n_events']} baseline_acc={fmt(summary['baseline_acc'])} captured_shape={summary['captured_output_shape']}\n\n",
        'This is the particle analogue of text-token tracing: for one pseudo-head, rank concrete particles inside concrete jets by head activation energy.\n\n',
        '## Class summary by predicted class\n',
        table(['pred_label','n_pred','head_score_mean','head_score_p90','acc_within_pred'],[[r['pred_label'],r['n_pred'],fmt(r['head_event_score_mean']),fmt(r['head_event_score_p90']),fmt(r['acc_within_pred'])] for r in agg]),
        '\n## Top events for this head\n',
        table(['event','true','pred','conf','head_max','real_particles','top_particle_indices'],[[r['event_idx'],r['true_label'],r['pred_label'],fmt(r['conf']),fmt(r['head_max_particle_energy']),r['real_particles'],r['top_particle_indices']] for r in event_rows[:30]]),
        '\n## Top particles inside top events\n',
        table(['event','rank','particle','head_energy','pt','energy','deta','dphi','deltaR','charge','pred'],[[r['event_idx'],r['rank'],r['particle_idx'],fmt(r['head_energy']),fmt(r.get('pt')),fmt(r.get('energy')),fmt(r.get('deta')),fmt(r.get('dphi')),fmt(r.get('deltaR_from_axis')),fmt(r.get('part_charge','')),r['pred_label']] for r in particle_rows[:80]]),
        '\nFull CSV tables:\n- `reports/latest/tables/single_head_event_trace.csv`\n- `reports/latest/tables/single_head_particle_trace.csv`\n- `reports/latest/tables/single_head_class_summary.csv`\n']
    (out/'PARTICLENET_SINGLE_HEAD_PARTICLE_TRACE_V1.md').write_text(''.join(md),encoding='utf-8')
    print(json.dumps(summary,indent=2,ensure_ascii=False)[:20000])

if __name__=='__main__': main()
