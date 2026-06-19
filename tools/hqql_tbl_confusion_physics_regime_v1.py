#!/usr/bin/env python3
import argparse,csv,json,sys,math,gc
from pathlib import Path
from collections import defaultdict,Counter
import torch
ROOT=Path(__file__).resolve().parents[1]; sys.path.insert(0,str(ROOT))
from tools.particlenet_real_patch_controls_v1 import load_balanced
from tools.particle0_topk_controls_v2 import make_model, pt_values, real_mask
from data.jetclass_tiny_loader_v3_official import LABELS

def wcsv(p,rows):
    p=Path(p); p.parent.mkdir(parents=True,exist_ok=True); keys=[]; seen=set()
    for r in rows:
        for k in r:
            if k not in seen: keys.append(k); seen.add(k)
    with p.open('w',encoding='utf-8',newline='') as f:
        wr=csv.DictWriter(f,fieldnames=keys); wr.writeheader(); [wr.writerow({k:r.get(k,'') for k in keys}) for r in rows]
def wjson(p,o): p=Path(p); p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(o,indent=2,ensure_ascii=False),encoding='utf-8')
def fmean(xs): return sum(xs)/len(xs) if xs else 0.0
def fmt(x):
    try: return f'{float(x):.4f}'
    except Exception: return 'n/a'
def mdtab(h,rs):
    if not rs: return '_No rows._\n'
    return '\n'.join(['| '+' | '.join(h)+' |','| '+' | '.join(['---']*len(h))+' |']+['| '+' | '.join(str(x).replace('\n',' ') for x in r)+' |' for r in rs])+'\n'
def slice_batch(batch,s,e):
    out={}
    for k,v in batch.items():
        if torch.is_tensor(v) and v.shape[0] >= e:
            out[k]=v[s:e]
        else:
            out[k]=v
    return out
def forward_microbatch(model,batch,mb,device):
    B=int(batch['y'].shape[0]); chunks=[]
    with torch.no_grad():
        for s in range(0,B,mb):
            e=min(B,s+mb); b=slice_batch(batch,s,e)
            chunks.append(model(b['points'],b['features'],b['mask']).detach().cpu())
            if str(device).startswith('cuda'):
                torch.cuda.empty_cache()
    return torch.cat(chunks,0)
def knn_microbatch(points,k,mb,device):
    from weaver.nn.model.ParticleNet import knn
    B=int(points.shape[0]); chunks=[]
    with torch.no_grad():
        for s in range(0,B,mb):
            e=min(B,s+mb)
            chunks.append(knn(points[s:e],k).detach().cpu())
            if str(device).startswith('cuda'):
                torch.cuda.empty_cache()
    return torch.cat(chunks,0)
def pid_name(feat,ei,idx):
    if feat.shape[1] < 11: return 'no_pid'
    vals={'charged_hadron':float(feat[ei,6,idx]),'neutral_hadron':float(feat[ei,7,idx]),'photon':float(feat[ei,8,idx]),'electron':float(feat[ei,9,idx]),'muon':float(feat[ei,10,idx])}
    return max(vals.items(),key=lambda kv:kv[1])[0]
def part_row(prefix,feat,pt,rank,ei,idx,knn_idx):
    C=feat.shape[1]; nb=knn_idx[ei,idx].long(); nb_pt=pt[ei,nb]
    near_sum=float(nb_pt.sum().clamp_min(1e-9)); p_pt=float(pt[ei,idx])
    out={prefix+'_idx':int(idx),prefix+'_pt':p_pt,prefix+'_pt_rank':int(rank[ei,idx]),prefix+'_pid':pid_name(feat,ei,idx),prefix+'_iso_pt_ratio':p_pt/(p_pt+near_sum),prefix+'_knn_pt_sum':near_sum}
    if C>=11:
        out.update({prefix+'_charge':float(feat[ei,5,idx]),prefix+'_is_charged_hadron':float(feat[ei,6,idx]),prefix+'_is_neutral_hadron':float(feat[ei,7,idx]),prefix+'_is_photon':float(feat[ei,8,idx]),prefix+'_is_electron':float(feat[ei,9,idx]),prefix+'_is_muon':float(feat[ei,10,idx]),prefix+'_is_lepton':float((feat[ei,9,idx]>0.5) or (feat[ei,10,idx]>0.5))})
        for j,nm in [(6,'charged_hadron'),(7,'neutral_hadron'),(8,'photon'),(9,'electron'),(10,'muon')]: out[prefix+'_knn_'+nm+'_frac']=float(feat[ei,j,nb].float().mean())
    return out
def group_name(y,pred):
    yt=LABELS[int(y)]; pr=LABELS[int(pred)]
    if yt=='label_Hqql' and pr=='label_Hqql': return 'Hqql_correct'
    if yt=='label_Hqql' and pr=='label_Tbl': return 'Hqql_to_Tbl'
    if yt=='label_Tbl' and pr=='label_Tbl': return 'Tbl_correct'
    if yt=='label_Tbl' and pr=='label_Hqql': return 'Tbl_to_Hqql'
    return ''
def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--checkpoint',default='local_checkpoints/part/ParticleNet_kinpid.pt')
    ap.add_argument('--data-dir',default=str(Path.home()/'Рабочий стол/jetclass_tiny_balanced'))
    ap.add_argument('--mode',default='kinpid')
    ap.add_argument('--samples-per-file',type=int,default=256)
    ap.add_argument('--max-files',type=int,default=20)
    ap.add_argument('--micro-batch',type=int,default=128)
    ap.add_argument('--knn-micro-batch',type=int,default=256)
    ap.add_argument('--device',default='cuda' if torch.cuda.is_available() else 'cpu')
    ap.add_argument('--out-events',default='reports/latest/tables/hqql_tbl_confusion_physics_events.csv')
    ap.add_argument('--out-summary',default='reports/latest/tables/hqql_tbl_confusion_physics_summary.csv')
    ap.add_argument('--out-json',default='manifests/latest/hqql_tbl_confusion_physics_regime_v1.json')
    ap.add_argument('--out-md',default='reports/latest/HQQL_TBL_CONFUSION_PHYSICS_REGIME_V1.md')
    a=ap.parse_args(); model,res=make_model(a.checkpoint,a.mode,a.device); batch=load_balanced(a.data_dir,mode=a.mode,samples_per_file=a.samples_per_file,max_files=a.max_files,device=a.device)
    logits=forward_microbatch(model,batch,max(1,a.micro_batch),a.device)
    pred=logits.argmax(1); prob=torch.softmax(logits.float(),1); y=batch['y'].detach().cpu(); feat=batch['features'].detach().cpu(); pt=pt_values(batch).detach().cpu(); mask=real_mask(batch).detach().cpu(); vectors=batch['vectors'].detach().cpu()
    k=int(getattr(model.edge_convs[0],'k',16)); knn_idx=knn_microbatch(batch['points'],k,max(1,a.knn_micro_batch),a.device)
    order=torch.argsort(pt.masked_fill(~mask,-1e30),dim=1,descending=True); rank=torch.empty_like(order)
    for i in range(order.shape[0]): rank[i,order[i]]=torch.arange(order.shape[1])
    rows=[]
    for ei in range(len(y)):
        g=group_name(y[ei],pred[ei])
        if not g: continue
        lead=int(order[ei,0]); p0=0
        px,py=vectors[ei,0],vectors[ei,1]
        sum_px=float((px*mask[ei]).sum()); sum_py=float((py*mask[ei]).sum()); miss_pt=math.sqrt(sum_px*sum_px+sum_py*sum_py)
        row={'event_index':ei,'group':g,'true_label':LABELS[int(y[ei])],'pred_label':LABELS[int(pred[ei])],'confidence':float(prob[ei,int(pred[ei])]),'missing_pt_proxy':miss_pt,'lead_idx':lead}
        row.update(part_row('particle0',feat,pt,rank,ei,p0,knn_idx)); row.update(part_row('leading',feat,pt,rank,ei,lead,knn_idx))
        lep_mask=((feat[ei,9]>0.5) | (feat[ei,10]>0.5)) & mask[ei] if feat.shape[1]>=11 else torch.zeros_like(mask[ei])
        if bool(lep_mask.any()):
            lep_idx=int(torch.where(lep_mask)[0][pt[ei,lep_mask].argmax()])
            row.update(part_row('best_lepton',feat,pt,rank,ei,lep_idx,knn_idx))
            row['has_lepton']=1
            row['deltaR_p0_lepton']=float(torch.sqrt((feat[ei,-2,p0]-feat[ei,-2,lep_idx])**2+(feat[ei,-1,p0]-feat[ei,-1,lep_idx])**2+1e-9))
            row['deltaR_lead_lepton']=float(torch.sqrt((feat[ei,-2,lead]-feat[ei,-2,lep_idx])**2+(feat[ei,-1,lead]-feat[ei,-1,lep_idx])**2+1e-9))
        else:
            row['has_lepton']=0
        rows.append(row)
    groups=defaultdict(list)
    for r in rows: groups[r['group']].append(r)
    summ=[]
    metrics=['confidence','missing_pt_proxy','particle0_pt','particle0_pt_rank','particle0_is_lepton','particle0_is_electron','particle0_is_muon','particle0_iso_pt_ratio','particle0_knn_charged_hadron_frac','particle0_knn_electron_frac','particle0_knn_muon_frac','leading_is_lepton','leading_iso_pt_ratio','has_lepton','best_lepton_iso_pt_ratio','deltaR_p0_lepton','deltaR_lead_lepton']
    for g,xs in groups.items():
        row={'group':g,'n':len(xs)}
        pids=Counter(r.get('particle0_pid','') for r in xs); lpids=Counter(r.get('leading_pid','') for r in xs)
        row['particle0_pid_modes']=', '.join(f'{k}:{v}' for k,v in pids.most_common(5)); row['leading_pid_modes']=', '.join(f'{k}:{v}' for k,v in lpids.most_common(5))
        for m in metrics: row[m+'_mean']=fmean([float(r[m]) for r in xs if m in r and str(r[m])!=''])
        summ.append(row)
    wcsv(a.out_events,rows); wcsv(a.out_summary,summ); wjson(a.out_json,{'ok':True,'events':len(rows),'groups':{k:len(v) for k,v in groups.items()},'k':k,'micro_batch':a.micro_batch,'knn_micro_batch':a.knn_micro_batch,'missing':list(res.missing_keys),'unexpected':list(res.unexpected_keys)})
    md=['# Hqql/Tbl Confusion Physics Regime v1\n\nThis report asks what particle0/leading/core physically is in Hqql/Tbl confusion regimes. Forward and KNN are microbatched for large Phase 1 runs.\n\n','## Group summary\n',mdtab(['group','n','particle0_pid_modes','p0_lepton','p0_iso','has_lepton','lead_pid_modes','lead_lepton','missing_pt'],[[r['group'],r['n'],r.get('particle0_pid_modes',''),fmt(r.get('particle0_is_lepton_mean')),fmt(r.get('particle0_iso_pt_ratio_mean')),fmt(r.get('has_lepton_mean')),r.get('leading_pid_modes',''),fmt(r.get('leading_is_lepton_mean')),fmt(r.get('missing_pt_proxy_mean'))] for r in summ]),'\n## Event examples\n',mdtab(['event','group','true','pred','conf','p0_pid','p0_pt','p0_rank','p0_lep','lead_pid','lead_lep','has_lep','best_lep_iso'],[[r['event_index'],r['group'],r['true_label'],r['pred_label'],fmt(r['confidence']),r.get('particle0_pid',''),fmt(r.get('particle0_pt')),r.get('particle0_pt_rank',''),fmt(r.get('particle0_is_lepton')),r.get('leading_pid',''),fmt(r.get('leading_is_lepton')),r.get('has_lepton'),fmt(r.get('best_lepton_iso_pt_ratio'))] for r in rows[:80]]),'\n## Interpretation\n\nCompare Hqql_correct vs Hqql_to_Tbl vs Tbl_correct. If Hqql_to_Tbl particle0/leading/lepton/KNN profile matches Tbl_correct more than Hqql_correct, the confusion route has physical meaning.\n']
    Path(a.out_md).parent.mkdir(parents=True,exist_ok=True); Path(a.out_md).write_text(''.join(md),encoding='utf-8')
    print(json.dumps({'ok':True,'events':len(rows),'groups':{k:len(v) for k,v in groups.items()},'micro_batch':a.micro_batch,'knn_micro_batch':a.knn_micro_batch,'out_md':a.out_md},indent=2,ensure_ascii=False))
if __name__=='__main__': main()
