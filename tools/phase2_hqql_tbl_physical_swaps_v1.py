#!/usr/bin/env python3
import argparse,csv,json,sys,random,math,gc
from pathlib import Path
from collections import defaultdict
import torch
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from tools.particlenet_real_patch_controls_v1 import load_balanced
from tools.particle0_topk_controls_v2 import make_model, pt_values, real_mask
from data.jetclass_tiny_loader_v3_official import LABELS

HQQL=LABELS.index('label_Hqql')
TBL=LABELS.index('label_Tbl')

def fnum(x,d=0.0):
    try: return float(x) if x not in ('',None) else d
    except Exception: return d
def fmt(x):
    try: return f'{float(x):.4f}'
    except Exception: return 'n/a'
def wcsv(p,rows):
    p=Path(p); p.parent.mkdir(parents=True,exist_ok=True); keys=[]; seen=set()
    for r in rows:
        for k in r:
            if k not in seen: keys.append(k); seen.add(k)
    with p.open('w',encoding='utf-8',newline='') as f:
        wr=csv.DictWriter(f,fieldnames=keys); wr.writeheader(); [wr.writerow({k:r.get(k,'') for k in keys}) for r in rows]
def wjson(p,o): p=Path(p); p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(o,indent=2,ensure_ascii=False),encoding='utf-8')
def mdtab(h,rs):
    if not rs: return '_No rows._\n'
    return '\n'.join(['| '+' | '.join(h)+' |','| '+' | '.join(['---']*len(h))+' |']+['| '+' | '.join(str(x).replace('\n',' ') for x in r)+' |' for r in rs])+'\n'
def slice_batch(batch,s,e):
    return {k:(v[s:e] if torch.is_tensor(v) and v.shape[0]>=e else v) for k,v in batch.items()}
def forward_micro(model,batch,mb,device):
    B=int(batch['y'].shape[0]); out=[]
    with torch.no_grad():
        for s in range(0,B,mb):
            e=min(B,s+mb); b=slice_batch(batch,s,e)
            out.append(model(b['points'],b['features'],b['mask']).detach().cpu())
            if str(device).startswith('cuda'): torch.cuda.empty_cache()
    return torch.cat(out,0)
def single_forward(model,b):
    with torch.no_grad(): return model(b['points'],b['features'],b['mask']).detach().cpu()[0]
def one_event_batch(batch,ei):
    out={}
    for k,v in batch.items():
        out[k]=v[ei:ei+1].clone() if torch.is_tensor(v) and v.shape[0]>ei else v
    return out
def copy_particle(dst, dst_idx, src, src_idx):
    # dst/src are one-event batches [1,C,N]
    for k in ['points','features','vectors']:
        if k in dst and k in src and torch.is_tensor(dst[k]) and dst[k].dim()==3:
            dst[k][0,:,dst_idx]=src[k][0,:,src_idx]
    if 'mask' in dst and torch.is_tensor(dst['mask']):
        dst['mask'][0,:,dst_idx]=1
def mask_particles(dst, idxs):
    for idx in idxs:
        for k in ['points','features','vectors']:
            if k in dst and torch.is_tensor(dst[k]) and dst[k].dim()==3:
                dst[k][0,:,idx]=0
        if 'mask' in dst and torch.is_tensor(dst['mask']): dst['mask'][0,:,idx]=0
def pid(feat,ei,idx):
    if feat.shape[1]<11: return 'no_pid'
    vals={'charged_hadron':float(feat[ei,6,idx]),'neutral_hadron':float(feat[ei,7,idx]),'photon':float(feat[ei,8,idx]),'electron':float(feat[ei,9,idx]),'muon':float(feat[ei,10,idx])}
    return max(vals.items(),key=lambda kv:kv[1])[0]
def is_lepton(feat,ei,idx): return feat.shape[1]>=11 and bool((feat[ei,9,idx]>0.5) or (feat[ei,10,idx]>0.5))
def is_hadron(feat,ei,idx): return feat.shape[1]>=8 and bool((feat[ei,6,idx]>0.5) or (feat[ei,7,idx]>0.5))
def event_group(y,p):
    if int(y)==HQQL and int(p)==HQQL: return 'Hqql_correct'
    if int(y)==HQQL and int(p)==TBL: return 'Hqql_to_Tbl'
    if int(y)==TBL and int(p)==TBL: return 'Tbl_correct'
    if int(y)==TBL and int(p)==HQQL: return 'Tbl_to_Hqql'
    return ''
def best_match(candidates,target_pt,pt,feat,prefer_hadron=False):
    best=None; bd=1e30
    for ei in candidates:
        idx=0
        if prefer_hadron:
            valid=[j for j in range(pt.shape[1]) if is_hadron(feat,ei,j)]
            if not valid: continue
            idx=max(valid,key=lambda j: float(pt[ei,j]))
        d=abs(math.log((float(pt[ei,idx])+1e-6)/(target_pt+1e-6)))
        if d<bd: best=(ei,idx); bd=d
    return best
def hadron_candidates(feat,pt,ei,limit=64):
    xs=[j for j in range(pt.shape[1]) if is_hadron(feat,ei,j)]
    xs=sorted(xs,key=lambda j: float(pt[ei,j]),reverse=True)
    return xs[:limit]
def logit_info(base,patched):
    bpred=int(base.argmax()); ppred=int(patched.argmax())
    bm=float(base[HQQL]-base[TBL]); pm=float(patched[HQQL]-patched[TBL])
    return bpred,ppred,bm,pm,pm-bm,float(patched[bpred]-base[bpred]),float(patched[HQQL]-base[HQQL]),float(patched[TBL]-base[TBL])
def run_patch(model,batch,target_ei,donor_ei,mode,knn_idx,pt,feat,rng,patch_k):
    tb=one_event_batch(batch,target_ei); db=one_event_batch(batch,donor_ei)
    top=0
    target_nb=[int(x) for x in knn_idx[target_ei,top].tolist() if int(x)!=top][:patch_k]
    donor_nb=[int(x) for x in knn_idx[donor_ei,0].tolist() if int(x)!=0]
    used=[]; donor_used=[]
    if mode=='2A_isolation_hadronic_injection':
        # keep target lepton/core; replace KNN neighbors with highest-pt donor hadrons
        had=hadron_candidates(feat,pt,donor_ei,limit=patch_k*2)
        for di,si in zip(target_nb,had[:len(target_nb)]):
            copy_particle(tb,di,db,si); used.append(di); donor_used.append(si)
    elif mode=='2B_lepton_core_swap':
        copy_particle(tb,0,db,0); used=[0]; donor_used=[0]
    elif mode=='2C_neighbor_swap':
        for di,si in zip(target_nb,donor_nb[:len(target_nb)]):
            copy_particle(tb,di,db,si); used.append(di); donor_used.append(si)
    elif mode=='random_same_count':
        count=max(1,patch_k if patch_k else len(target_nb))
        valid=[i for i in range(pt.shape[1]) if i!=0]
        dst=rng.sample(valid,min(count,len(valid)))
        src=rng.sample(valid,min(count,len(valid)))
        for di,si in zip(dst,src):
            copy_particle(tb,di,db,si); used.append(di); donor_used.append(si)
    else:
        raise ValueError(mode)
    return single_forward(model,tb),used,donor_used,target_nb,donor_nb

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--checkpoint',default='local_checkpoints/part/ParticleNet_kinpid.pt')
    ap.add_argument('--data-dir',default=str(Path.home()/'Рабочий стол/jetclass_tiny_balanced'))
    ap.add_argument('--mode',default='kinpid')
    ap.add_argument('--samples-per-file',type=int,default=1024)
    ap.add_argument('--max-files',type=int,default=100)
    ap.add_argument('--micro-batch',type=int,default=64)
    ap.add_argument('--max-targets',type=int,default=80)
    ap.add_argument('--patch-k',type=int,default=8)
    ap.add_argument('--seed',type=int,default=123)
    ap.add_argument('--device',default='cuda' if torch.cuda.is_available() else 'cpu')
    ap.add_argument('--out-csv',default='reports/latest/tables/phase2_hqql_tbl_physical_swaps.csv')
    ap.add_argument('--out-summary',default='reports/latest/tables/phase2_hqql_tbl_physical_swaps_summary.csv')
    ap.add_argument('--out-json',default='manifests/latest/phase2_hqql_tbl_physical_swaps_v1.json')
    ap.add_argument('--out-md',default='reports/latest/PHASE2_HQQL_TBL_PHYSICAL_SWAPS_V1.md')
    a=ap.parse_args(); rng=random.Random(a.seed)
    model,res=make_model(a.checkpoint,a.mode,a.device); batch=load_balanced(a.data_dir,mode=a.mode,samples_per_file=a.samples_per_file,max_files=a.max_files,device=a.device)
    logits=forward_micro(model,batch,max(1,a.micro_batch),a.device)
    pred=logits.argmax(1); y=batch['y'].detach().cpu(); pt=pt_values(batch).detach().cpu(); feat=batch['features'].detach().cpu(); mask=real_mask(batch).detach().cpu()
    from weaver.nn.model.ParticleNet import knn
    with torch.no_grad(): knn_idx=knn(batch['points'],int(getattr(model.edge_convs[0],'k',16))).detach().cpu()
    groups=defaultdict(list)
    for ei in range(len(y)):
        g=event_group(y[ei],pred[ei])
        if g: groups[g].append(ei)
    rows=[]
    # 2A/2C: Hqql_to_Tbl target, Hqql_correct donor matched by p0 pt.
    targets=groups['Hqql_to_Tbl'][:a.max_targets]
    for ei in targets:
        donor=best_match(groups['Hqql_correct'],float(pt[ei,0]),pt,feat)
        if donor is None: continue
        de,_=donor; base=logits[ei]
        for mode in ['2A_isolation_hadronic_injection','2C_neighbor_swap','random_same_count']:
            patched,used,donor_used,target_nb,donor_nb=run_patch(model,batch,ei,de,mode,knn_idx,pt,feat,rng,a.patch_k)
            bpred,ppred,bm,pm,dm,dbase,dhq,dtbl=logit_info(base,patched)
            rows.append({'test':mode,'target_event':ei,'donor_event':de,'target_group':'Hqql_to_Tbl','donor_group':'Hqql_correct','true_label':LABELS[int(y[ei])],'baseline_pred':LABELS[bpred],'patched_pred':LABELS[ppred],'success_to_Hqql':int(ppred==HQQL),'flip':int(ppred!=bpred),'baseline_margin_Hqql_minus_Tbl':bm,'patched_margin_Hqql_minus_Tbl':pm,'delta_margin':dm,'delta_baseline_pred_logit':dbase,'delta_Hqql_logit':dhq,'delta_Tbl_logit':dtbl,'target_p0_pid':pid(feat,ei,0),'donor_p0_pid':pid(feat,de,0),'target_p0_pt':float(pt[ei,0]),'donor_p0_pt':float(pt[de,0]),'patched_indices':json.dumps(used),'donor_indices':json.dumps(donor_used),'target_knn':json.dumps(target_nb),'donor_knn':json.dumps(donor_nb)})
    # 2B: Tbl_correct target, Hqql_correct donor matched by p0 pt.
    targets=groups['Tbl_correct'][:a.max_targets]
    for ei in targets:
        donor=best_match(groups['Hqql_correct'],float(pt[ei,0]),pt,feat)
        if donor is None: continue
        de,_=donor; base=logits[ei]
        for mode in ['2B_lepton_core_swap','random_same_count']:
            patched,used,donor_used,target_nb,donor_nb=run_patch(model,batch,ei,de,mode,knn_idx,pt,feat,rng,a.patch_k)
            bpred,ppred,bm,pm,dm,dbase,dhq,dtbl=logit_info(base,patched)
            rows.append({'test':mode,'target_event':ei,'donor_event':de,'target_group':'Tbl_correct','donor_group':'Hqql_correct','true_label':LABELS[int(y[ei])],'baseline_pred':LABELS[bpred],'patched_pred':LABELS[ppred],'success_to_Hqql':int(ppred==HQQL),'flip':int(ppred!=bpred),'baseline_margin_Hqql_minus_Tbl':bm,'patched_margin_Hqql_minus_Tbl':pm,'delta_margin':dm,'delta_baseline_pred_logit':dbase,'delta_Hqql_logit':dhq,'delta_Tbl_logit':dtbl,'target_p0_pid':pid(feat,ei,0),'donor_p0_pid':pid(feat,de,0),'target_p0_pt':float(pt[ei,0]),'donor_p0_pt':float(pt[de,0]),'patched_indices':json.dumps(used),'donor_indices':json.dumps(donor_used),'target_knn':json.dumps(target_nb),'donor_knn':json.dumps(donor_nb)})
    wcsv(a.out_csv,rows)
    by=defaultdict(list)
    for r in rows: by[(r['test'],r['target_group'])].append(r)
    summ=[]
    for (test,tg),xs in by.items():
        n=len(xs)
        summ.append({'test':test,'target_group':tg,'n':n,'flip_rate':sum(fnum(x['flip']) for x in xs)/n,'success_to_Hqql_rate':sum(fnum(x['success_to_Hqql']) for x in xs)/n,'mean_delta_margin_Hqql_minus_Tbl':sum(fnum(x['delta_margin']) for x in xs)/n,'mean_delta_baseline_pred_logit':sum(fnum(x['delta_baseline_pred_logit']) for x in xs)/n,'mean_delta_Hqql_logit':sum(fnum(x['delta_Hqql_logit']) for x in xs)/n,'mean_delta_Tbl_logit':sum(fnum(x['delta_Tbl_logit']) for x in xs)/n})
    wcsv(a.out_summary,summ)
    wjson(a.out_json,{'ok':True,'rows':len(rows),'groups':{k:len(v) for k,v in groups.items()},'max_targets':a.max_targets,'patch_k':a.patch_k,'missing':list(res.missing_keys),'unexpected':list(res.unexpected_keys)})
    md=['# Phase 2 Hqql/Tbl Physical Swaps v1\n\nPhysical causal tests for Hqql/Tbl ambiguity.\n\n','## Summary\n',mdtab(['test','target_group','n','flip','success_to_Hqql','delta_margin','delta_base_logit'],[[r['test'],r['target_group'],r['n'],fmt(r['flip_rate']),fmt(r['success_to_Hqql_rate']),fmt(r['mean_delta_margin_Hqql_minus_Tbl']),fmt(r['mean_delta_baseline_pred_logit'])] for r in summ]),'\n## Example rows\n',mdtab(['test','target','donor','group','base','patched','success_Hqql','d_margin','p0','donor_p0','idx'],[[r['test'],r['target_event'],r['donor_event'],r['target_group'],r['baseline_pred'],r['patched_pred'],r['success_to_Hqql'],fmt(r['delta_margin']),r['target_p0_pid'],r['donor_p0_pid'],r['patched_indices']] for r in rows[:120]]),'\n## Interpretation\n\n2A asks whether adding hadronic Hqql-like neighbors around the same lepton restores Hqql. 2B asks whether the lepton itself is enough. 2C asks whether neighbor context alone restores Hqql. Compare targeted tests against random_same_count for each target group.\n']
    Path(a.out_md).parent.mkdir(parents=True,exist_ok=True); Path(a.out_md).write_text(''.join(md),encoding='utf-8')
    print(json.dumps({'ok':True,'rows':len(rows),'summary_rows':len(summ),'out_md':a.out_md},indent=2,ensure_ascii=False))
if __name__=='__main__': main()
