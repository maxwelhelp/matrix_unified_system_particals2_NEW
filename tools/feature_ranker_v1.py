#!/usr/bin/env python3
import argparse,csv,json,math,sys,datetime
from pathlib import Path
from collections import defaultdict
import torch
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from tools.particlenet_real_patch_controls_v1 import load_balanced
from tools.particle0_topk_controls_v2 import make_model, pt_values, real_mask
from data.jetclass_tiny_loader_v3_official import LABELS

def readcsv(p):
    p=Path(p)
    if not p.exists(): return []
    with p.open('r',encoding='utf-8') as f: return list(csv.DictReader(f))
def wcsv(p,rows):
    p=Path(p); p.parent.mkdir(parents=True,exist_ok=True); keys=[]; seen=set()
    for r in rows:
        for k in r:
            if k not in seen: keys.append(k); seen.add(k)
    with p.open('w',encoding='utf-8',newline='') as f:
        wr=csv.DictWriter(f,fieldnames=keys); wr.writeheader(); [wr.writerow({k:r.get(k,'') for k in keys}) for r in rows]
def wjson(p,o): p=Path(p); p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(o,indent=2,ensure_ascii=False),encoding='utf-8')
def fnum(x,d=0.0):
    try:
        v=float(x); return v if math.isfinite(v) else d
    except Exception: return d
def fmt(x):
    try: return f'{float(x):.4f}'
    except Exception: return 'n/a'
def mdtab(h,rs):
    if not rs: return '_No rows._\n'
    return '\n'.join(['| '+' | '.join(h)+' |','| '+' | '.join(['---']*len(h))+' |']+['| '+' | '.join(str(x).replace('\n',' ') for x in r)+' |' for r in rs])+'\n'
def slice_batch(batch,s,e): return {k:(v[s:e] if torch.is_tensor(v) and v.shape[0]>=e else v) for k,v in batch.items()}
def forward_micro(model,batch,mb,device):
    B=int(batch['y'].shape[0]); outs=[]
    with torch.no_grad():
        for s in range(0,B,mb):
            e=min(B,s+mb); b=slice_batch(batch,s,e)
            outs.append(model(b['points'],b['features'],b['mask']).detach().cpu())
            if str(device).startswith('cuda'): torch.cuda.empty_cache()
    return torch.cat(outs,0)
def knn_micro(points,k,mb,device):
    from weaver.nn.model.ParticleNet import knn
    B=int(points.shape[0]); outs=[]
    with torch.no_grad():
        for s in range(0,B,mb):
            e=min(B,s+mb)
            outs.append(knn(points[s:e],k).detach().cpu())
            if str(device).startswith('cuda'): torch.cuda.empty_cache()
    return torch.cat(outs,0)
def pid_feats(prefix,feat,ei,idx,out):
    if feat.shape[1] >= 11:
        out[prefix+'_charge']=float(feat[ei,5,idx])
        out[prefix+'_is_charged_hadron']=float(feat[ei,6,idx])
        out[prefix+'_is_neutral_hadron']=float(feat[ei,7,idx])
        out[prefix+'_is_photon']=float(feat[ei,8,idx])
        out[prefix+'_is_electron']=float(feat[ei,9,idx])
        out[prefix+'_is_muon']=float(feat[ei,10,idx])
        out[prefix+'_is_lepton']=float((feat[ei,9,idx]>0.5) or (feat[ei,10,idx]>0.5))
def event_features(batch,logits,pred,knn_idx,kmax=16):
    y=batch['y'].detach().cpu().long(); feat=batch['features'].detach().cpu(); pt=pt_values(batch).detach().cpu(); mask=real_mask(batch).detach().cpu(); vectors=batch['vectors'].detach().cpu(); points=batch['points'].detach().cpu()
    probs=torch.softmax(logits.float(),1); order=torch.argsort(pt.masked_fill(~mask,-1e30),dim=1,descending=True)
    rows=[]
    for ei in range(len(y)):
        p0=0; lead=int(order[ei,0]); nb=[int(x) for x in knn_idx[ei,p0].tolist() if int(x)!=p0][:kmax]
        nb_pt=pt[ei,nb] if nb else torch.tensor([])
        px,py=vectors[ei,0],vectors[ei,1]; sum_px=float((px*mask[ei]).sum()); sum_py=float((py*mask[ei]).sum())
        out={'event_index':ei,'true_label':LABELS[int(y[ei])],'pred_label':LABELS[int(pred[ei])],'pred_conf':float(probs[ei,int(pred[ei])]),'n_particles':int(mask[ei].sum()),'missing_pt_proxy':math.sqrt(sum_px*sum_px+sum_py*sum_py),'p0_pt':float(pt[ei,p0]),'leading_pt':float(pt[ei,lead]),'leading_pt_fraction':float(pt[ei,lead]/pt[ei].masked_select(mask[ei]).sum().clamp_min(1e-9)),'p0_is_leading':float(p0==lead),'knn_pt_sum':float(nb_pt.sum()) if len(nb) else 0.0,'knn_pt_mean':float(nb_pt.mean()) if len(nb) else 0.0,'knn_pt_max':float(nb_pt.max()) if len(nb) else 0.0,'p0_iso_pt_ratio':float(pt[ei,p0]/(pt[ei,p0]+nb_pt.sum()).clamp_min(1e-9)) if len(nb) else 1.0}
        pid_feats('p0',feat,ei,p0,out); pid_feats('leading',feat,ei,lead,out)
        if feat.shape[1]>=11 and nb:
            for j,nm in [(6,'charged_hadron'),(7,'neutral_hadron'),(8,'photon'),(9,'electron'),(10,'muon')]: out['knn_'+nm+'_frac']=float(feat[ei,j,nb].float().mean())
        lep_mask=((feat[ei,9]>0.5)|(feat[ei,10]>0.5)) & mask[ei] if feat.shape[1]>=11 else torch.zeros_like(mask[ei])
        if bool(lep_mask.any()):
            lep_idx=int(torch.where(lep_mask)[0][pt[ei,lep_mask].argmax()])
            out['has_lepton']=1.0; out['best_lepton_pt']=float(pt[ei,lep_idx]); out['p0_best_lepton_deltaR']=float(torch.sqrt(((points[ei,:,p0]-points[ei,:,lep_idx])**2).sum()+1e-9)); out['p0_lepton_aligned']=float(out['p0_best_lepton_deltaR']<0.05)
            nb_lep=[int(x) for x in knn_idx[ei,lep_idx].tolist() if int(x)!=lep_idx][:kmax]
            nb_lp_pt=pt[ei,nb_lep] if nb_lep else torch.tensor([])
            out['best_lepton_iso_pt_ratio']=float(pt[ei,lep_idx]/(pt[ei,lep_idx]+nb_lp_pt.sum()).clamp_min(1e-9)) if len(nb_lep) else 1.0
        else:
            out['has_lepton']=0.0; out['best_lepton_pt']=0.0; out['p0_best_lepton_deltaR']=999.0; out['p0_lepton_aligned']=0.0; out['best_lepton_iso_pt_ratio']=0.0
        rows.append(out)
    return rows
def mean_std(xs,feat):
    vals=[fnum(x.get(feat)) for x in xs if x.get(feat,'')!='']
    if not vals: return 0.0,0.0,0
    m=sum(vals)/len(vals); s=math.sqrt(sum((v-m)**2 for v in vals)/max(1,len(vals)-1)); return m,s,len(vals)
def bin_scan(rows,feat,true_label,pred_label,bins=5):
    sub=[r for r in rows if r['true_label']==true_label]
    vals=[fnum(r.get(feat)) for r in sub if r.get(feat,'')!='']
    if len(vals)<20: return [],1.0
    vals_sorted=sorted(vals); cuts=[vals_sorted[int(i*len(vals_sorted)/bins)] for i in range(bins)]+[vals_sorted[-1]+1e-9]
    out=[]; rates=[]
    for i in range(bins):
        lo,hi=cuts[i],cuts[i+1]
        xs=[r for r in sub if lo<=fnum(r.get(feat))<hi]
        n=len(xs); hit=sum(1 for r in xs if r['pred_label']==pred_label); rate=hit/n if n else 0.0; rates.append(rate)
        out.append({'feature':feat,'bin_index':i,'lo':lo,'hi':hi,'n':n,'target_confusions':hit,'confusion_rate':rate})
    mn=max(min(r for r in rates if r>0),1e-9) if any(rates) else 1e-9
    ratio=max(rates)/mn if any(rates) else 1.0
    return out,ratio
def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--signals',default='reports/latest/tables/signal_board_v1.csv')
    ap.add_argument('--checkpoint',default='local_checkpoints/part/ParticleNet_kinpid.pt')
    ap.add_argument('--data-dir',default=str(Path.home()/'Рабочий стол/jetclass_tiny_balanced'))
    ap.add_argument('--mode',default='kinpid')
    ap.add_argument('--samples-per-file',type=int,default=1024)
    ap.add_argument('--max-files',type=int,default=100)
    ap.add_argument('--micro-batch',type=int,default=64)
    ap.add_argument('--knn-micro-batch',type=int,default=128)
    ap.add_argument('--max-pairs',type=int,default=12)
    ap.add_argument('--top-features-per-pair',type=int,default=8)
    ap.add_argument('--device',default='cuda' if torch.cuda.is_available() else 'cpu')
    ap.add_argument('--out-md',default='reports/latest/FEATURE_RANKER_V1.md')
    ap.add_argument('--out-candidates',default='reports/latest/tables/feature_ranker_v1_candidates.csv')
    ap.add_argument('--out-bins',default='reports/latest/tables/feature_ranker_v1_bins.csv')
    ap.add_argument('--out-signal-board',default='reports/latest/tables/signal_board_v1_feature_candidates.csv')
    ap.add_argument('--out-json',default='manifests/latest/feature_ranker_v1.json')
    args=ap.parse_args()
    signals=[r for r in readcsv(args.signals) if r.get('status') in ('ALERT','WATCH')][:args.max_pairs]
    model,res=make_model(args.checkpoint,args.mode,args.device); batch=load_balanced(args.data_dir,mode=args.mode,samples_per_file=args.samples_per_file,max_files=args.max_files,device=args.device)
    logits=forward_micro(model,batch,max(1,args.micro_batch),args.device); pred=logits.argmax(1).long(); knn_idx=knn_micro(batch['points'],int(getattr(model.edge_convs[0],'k',16)),max(1,args.knn_micro_batch),args.device)
    rows=event_features(batch,logits,pred,knn_idx)
    numeric=[k for k in rows[0].keys() if k not in ('event_index','true_label','pred_label')]
    cand=[]; bins_all=[]; board=[]
    for sig in signals:
        pair=sig['class_pair']; A,B=pair.split('->')
        A_correct=[r for r in rows if r['true_label']==A and r['pred_label']==A]
        A_to_B=[r for r in rows if r['true_label']==A and r['pred_label']==B]
        if len(A_to_B)<10 or len(A_correct)<10: continue
        for feat in numeric:
            ma,sa,na=mean_std(A_correct,feat); mb,sb,nb=mean_std(A_to_B,feat); pooled=math.sqrt((sa*sa+sb*sb)/2)+1e-9; effect=(mb-ma)/pooled
            brows,mratio=bin_scan(rows,feat,A,B,bins=5)
            score=abs(effect)*mratio*math.log1p(len(A_to_B))
            direction='confused_higher' if effect>0 else 'correct_higher'
            cand.append({'class_pair':pair,'feature':feat,'A_correct_n':len(A_correct),'A_to_B_n':len(A_to_B),'correct_mean':ma,'confused_mean':mb,'std_effect_confused_minus_correct':effect,'direction':direction,'monotonic_ratio':mratio,'rank_score':score,'next_action':'if top candidate, run monotonic/patch/deep probe'})
            for br in brows: br.update({'class_pair':pair}); bins_all.append(br)
    cand=sorted(cand,key=lambda r:r['rank_score'],reverse=True)
    grouped=defaultdict(list)
    for r in cand: grouped[r['class_pair']].append(r)
    for pair,xs in grouped.items():
        for r in xs[:args.top_features_per_pair]:
            board.append({'signal_id':f'feature::{pair}::{r["feature"]}','source':'FEATURE_RANKER_V1','class_pair':pair,'status':'CANDIDATE','score':r['rank_score'],'reason':f'feature={r["feature"]}, effect={r["std_effect_confused_minus_correct"]:.3f}, monotonic_ratio={r["monotonic_ratio"]:.3f}','recommended_next_action':'run deep probe / patch if physics meaning is plausible','claim_level':1})
    wcsv(args.out_candidates,cand); wcsv(args.out_bins,bins_all); wcsv(args.out_signal_board,board)
    manifest={'schema':'feature_ranker.v1','generated_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'signals_in':len(signals),'candidates':len(cand),'board':board,'settings':vars(args),'model_missing':list(res.missing_keys),'model_unexpected':list(res.unexpected_keys)}; wjson(args.out_json,manifest)
    md=['# Feature Ranker v1\n\nAutomatic contrastive feature ranking for WATCH/ALERT class pairs. No LLM is used.\n\n',f'- input signals: **{len(signals)}**\n',f'- candidates: **{len(cand)}**\n\n','## Top feature candidates\n',mdtab(['pair','feature','score','effect','mono_ratio','direction','n_confused'],[[r['class_pair'],r['feature'],fmt(r['rank_score']),fmt(r['std_effect_confused_minus_correct']),fmt(r['monotonic_ratio']),r['direction'],r['A_to_B_n']] for r in cand[:40]]),'\n## Signal board candidates\n',mdtab(['pair','feature','score','reason','next'],[[r['class_pair'],r['signal_id'].split('::')[-1],fmt(r['score']),r['reason'],r['recommended_next_action']] for r in board[:40]]),'\n## Interpretation\n\nTop rows are observable candidates. They are not physics claims yet. The next stage should run only for candidates that have plausible semantics and enough counts.\n']
    Path(args.out_md).parent.mkdir(parents=True,exist_ok=True); Path(args.out_md).write_text(''.join(md),encoding='utf-8')
    print(json.dumps({'ok':True,'signals':len(signals),'candidates':len(cand),'out_md':args.out_md},indent=2,ensure_ascii=False))
if __name__=='__main__': main()
