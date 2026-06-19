#!/usr/bin/env python3
import argparse,csv,json,math,random
from pathlib import Path
from collections import defaultdict
import numpy as np

HQQL='label_Hqql'; TBL='label_Tbl'

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
def fmt(x):
    try: return f'{float(x):.4f}'
    except Exception: return 'n/a'
def mdtab(h,rs):
    if not rs: return '_No rows._\n'
    return '\n'.join(['| '+' | '.join(h)+' |','| '+' | '.join(['---']*len(h))+' |']+['| '+' | '.join(str(x).replace('\n',' ') for x in r)+' |' for r in rs])+'\n'
def fnum(x,d=0.0):
    try:
        if x in ('',None): return d
        v=float(x)
        if math.isnan(v) or math.isinf(v): return d
        return v
    except Exception: return d

def feature_names():
    base=['confidence','missing_pt_proxy','particle0_pt','particle0_pt_rank','particle0_iso_pt_ratio','particle0_is_lepton','particle0_is_electron','particle0_is_muon','particle0_charge','particle0_knn_pt_sum','particle0_knn_charged_hadron_frac','particle0_knn_neutral_hadron_frac','particle0_knn_photon_frac','particle0_knn_electron_frac','particle0_knn_muon_frac','leading_pt','leading_pt_rank','leading_iso_pt_ratio','leading_is_lepton','has_lepton','best_lepton_pt','best_lepton_iso_pt_ratio','deltaR_p0_lepton','deltaR_lead_lepton']
    return base

def build_xy(rows,names):
    X=[]; y=[]; meta=[]
    for r in rows:
        if r.get('true_label') not in (HQQL,TBL): continue
        X.append([fnum(r.get(n)) for n in names])
        y.append(1 if r.get('true_label')==TBL else 0) # 1=Tbl, 0=Hqql
        meta.append(r)
    return np.asarray(X,dtype='float64'),np.asarray(y,dtype='int64'),meta

def standardize(X,train):
    mu=X[train].mean(0,keepdims=True); sd=X[train].std(0,keepdims=True)+1e-6
    return (X-mu)/sd,mu,sd

def logistic_fit(X,y,idx,lr=0.05,steps=2000,l2=1e-3):
    Xb=np.concatenate([X,np.ones((X.shape[0],1))],1); w=np.zeros(Xb.shape[1])
    tr=idx
    for _ in range(steps):
        z=Xb[tr]@w; p=1/(1+np.exp(-np.clip(z,-50,50)))
        grad=Xb[tr].T@(p-y[tr])/len(tr)+l2*np.r_[w[:-1],0]
        w-=lr*grad
    return w

def pred_proba(X,w):
    Xb=np.concatenate([X,np.ones((X.shape[0],1))],1); z=Xb@w
    return 1/(1+np.exp(-np.clip(z,-50,50)))
def split_indices(meta,seed):
    rng=random.Random(seed)
    correct=[i for i,m in enumerate(meta) if m.get('group') in ('Hqql_correct','Tbl_correct')]
    confused=[i for i,m in enumerate(meta) if m.get('group') in ('Hqql_to_Tbl','Tbl_to_Hqql')]
    rng.shuffle(correct); ntr=int(0.7*len(correct)); return correct[:ntr], correct[ntr:], confused

def metrics_for(idxs,y,pred,meta):
    if not idxs: return {'n':0,'surrogate_true_acc':0,'particlenet_true_acc':0,'surrogate_agreement_with_particlenet':0}
    sur=pred[idxs]; yy=y[idxs]
    pn=np.asarray([1 if meta[i].get('pred_label')==TBL else 0 for i in idxs],dtype='int64')
    return {'n':len(idxs),'surrogate_true_acc':float((sur==yy).mean()),'particlenet_true_acc':float((pn==yy).mean()),'surrogate_agreement_with_particlenet':float((sur==pn).mean()),'surrogate_tbl_rate':float(sur.mean()),'particlenet_tbl_rate':float(pn.mean())}

def isolation_bin_rows(meta,y,pred):
    bins=[(0,0.10),(0.10,0.15),(0.15,0.20),(0.20,0.30),(0.30,999)]
    rows=[]
    pn=np.asarray([1 if m.get('pred_label')==TBL else 0 for m in meta],dtype='int64')
    for lo,hi in bins:
        idx=[i for i,m in enumerate(meta) if m.get('true_label')==HQQL and lo<=fnum(m.get('particle0_iso_pt_ratio'))<hi]
        if idx:
            rows.append({'bin':f'{lo:.2f}-{hi:.2f}' if hi<999 else f'{lo:.2f}+','n_hqql':len(idx),'particlenet_hqql_to_tbl_rate':float(pn[idx].mean()),'surrogate_hqql_to_tbl_rate':float(pred[idx].mean()),'gap_surrogate_minus_particlenet':float(pred[idx].mean()-pn[idx].mean())})
        else:
            rows.append({'bin':f'{lo:.2f}-{hi:.2f}' if hi<999 else f'{lo:.2f}+','n_hqql':0,'particlenet_hqql_to_tbl_rate':0,'surrogate_hqql_to_tbl_rate':0,'gap_surrogate_minus_particlenet':0})
    return rows

def feature_importance(names,w):
    vals=np.abs(w[:-1])
    return sorted([{'feature':n,'abs_weight':float(v)} for n,v in zip(names,vals)],key=lambda r:r['abs_weight'],reverse=True)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--phase1-events',default='reports/latest/tables/hqql_tbl_confusion_physics_events.csv')
    ap.add_argument('--seed',type=int,default=123)
    ap.add_argument('--lr',type=float,default=0.05)
    ap.add_argument('--steps',type=int,default=2000)
    ap.add_argument('--l2',type=float,default=1e-3)
    ap.add_argument('--out-md',default='reports/latest/KNOWN_OBSERVABLE_RESIDUAL_V2.md')
    ap.add_argument('--out-json',default='manifests/latest/known_observable_residual_v2.json')
    ap.add_argument('--out-summary',default='reports/latest/tables/known_observable_residual_v2_summary.csv')
    ap.add_argument('--out-bins',default='reports/latest/tables/known_observable_residual_v2_isolation_bins.csv')
    ap.add_argument('--out-importance',default='reports/latest/tables/known_observable_residual_v2_feature_importance.csv')
    args=ap.parse_args()
    rows=readcsv(args.phase1_events); names=feature_names(); X,y,meta=build_xy(rows,names)
    tr,te,conf=split_indices(meta,args.seed)
    Xs,mu,sd=standardize(X,tr); w=logistic_fit(Xs,y,tr,args.lr,args.steps,args.l2)
    p=pred_proba(Xs,w); pred=(p>=0.5).astype('int64')
    groups={'correct_test':te,'confused_eval':conf,'all_hqql_tbl':list(range(len(y))),'train_correct':tr}
    summary=[]
    for g,idx in groups.items():
        m=metrics_for(idx,y,pred,meta); m['split']=g; summary.append(m)
    for g in ['Hqql_correct','Hqql_to_Tbl','Tbl_correct','Tbl_to_Hqql']:
        idx=[i for i,m in enumerate(meta) if m.get('group')==g]
        m=metrics_for(idx,y,pred,meta); m['split']=g; summary.append(m)
    bins=isolation_bin_rows(meta,y,pred); imp=feature_importance(names,w)
    wcsv(args.out_summary,summary); wcsv(args.out_bins,bins); wcsv(args.out_importance,imp)
    conf_m=metrics_for(conf,y,pred,meta); te_m=metrics_for(te,y,pred,meta)
    result={'ok':True,'n_events':len(meta),'train_correct_n':len(tr),'correct_test_n':len(te),'confused_eval_n':len(conf),'surrogate_v2_acc_correct_test':te_m['surrogate_true_acc'],'particlenet_acc_correct_test':te_m['particlenet_true_acc'],'surrogate_v2_acc_confused_eval':conf_m['surrogate_true_acc'],'particlenet_acc_confused_eval':conf_m['particlenet_true_acc'],'surrogate_agreement_confused_eval':conf_m['surrogate_agreement_with_particlenet'],'top_features':imp[:20]}
    wjson(args.out_json,result)
    md=['# Known Observable Residual v2 — Hqql/Tbl lepton-isolation surrogate\n\n','This report tests whether explicit lepton/core isolation and hadronic-neighborhood features explain the Hqql/Tbl ambiguity found in Phases 1-3.\n\n','## Three numbers\n',mdtab(['metric','value'],[['surrogate_v2_acc_correct_test',fmt(te_m['surrogate_true_acc'])],['ParticleNet_acc_correct_test',fmt(te_m['particlenet_true_acc'])],['surrogate_v2_acc_confused_eval',fmt(conf_m['surrogate_true_acc'])],['ParticleNet_acc_confused_eval',fmt(conf_m['particlenet_true_acc'])],['surrogate_agreement_with_ParticleNet_on_confused',fmt(conf_m['surrogate_agreement_with_particlenet'])]]),'\n## Summary by split/group\n',mdtab(['split','n','surrogate_acc','ParticleNet_acc','agreement','surrogate_tbl_rate','ParticleNet_tbl_rate'],[[r['split'],r['n'],fmt(r['surrogate_true_acc']),fmt(r['particlenet_true_acc']),fmt(r['surrogate_agreement_with_particlenet']),fmt(r.get('surrogate_tbl_rate',0)),fmt(r.get('particlenet_tbl_rate',0))] for r in summary]),'\n## Hqql->Tbl rate by isolation bin\n',mdtab(['bin','n_hqql','ParticleNet_rate','surrogate_rate','gap'],[[r['bin'],r['n_hqql'],fmt(r['particlenet_hqql_to_tbl_rate']),fmt(r['surrogate_hqql_to_tbl_rate']),fmt(r['gap_surrogate_minus_particlenet'])] for r in bins]),'\n## Top explicit features\n',mdtab(['feature','abs_weight'],[[r['feature'],fmt(r['abs_weight'])] for r in imp[:25]]),'\n## Interpretation\n\nIf the surrogate reproduces ParticleNet isolation-bin confusion rates and closes confused/correct behavior, the lepton-isolation mechanism is mostly decoded. If not, inspect the residual events for additional b-like, pairwise, or subjet geometry.\n']
    Path(args.out_md).parent.mkdir(parents=True,exist_ok=True); Path(args.out_md).write_text(''.join(md),encoding='utf-8')
    print(json.dumps({'ok':True,'n_events':len(meta),'out_md':args.out_md},indent=2))
if __name__=='__main__': main()
