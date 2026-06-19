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
def fnum(x,d=0.0):
    try:
        v=float(x)
        return v if math.isfinite(v) else d
    except Exception: return d
def fmt(x):
    try: return f'{float(x):.4f}'
    except Exception: return 'n/a'
def mdtab(h,rs):
    if not rs: return '_No rows._\n'
    return '\n'.join(['| '+' | '.join(h)+' |','| '+' | '.join(['---']*len(h))+' |']+['| '+' | '.join(str(x).replace('\n',' ') for x in r)+' |' for r in rs])+'\n'
def features():
    return ['missing_pt_proxy','particle0_pt','particle0_iso_pt_ratio','particle0_is_lepton','particle0_is_electron','particle0_is_muon','particle0_charge','particle0_knn_pt_sum','particle0_knn_charged_hadron_frac','particle0_knn_neutral_hadron_frac','particle0_knn_photon_frac','particle0_knn_electron_frac','particle0_knn_muon_frac','leading_iso_pt_ratio','leading_is_lepton','best_lepton_iso_pt_ratio','deltaR_p0_lepton','deltaR_lead_lepton']
def build(rows,names):
    X=[]; y=[]; meta=[]
    for r in rows:
        if r.get('true_label')!=HQQL: continue
        X.append([fnum(r.get(n)) for n in names])
        y.append(1 if r.get('pred_label')==TBL else 0) # ParticleNet behavior: Hqql->Tbl
        meta.append(r)
    return np.asarray(X,dtype='float64'),np.asarray(y,dtype='int64'),meta
def split(n,seed):
    rng=np.random.default_rng(seed); idx=np.arange(n); rng.shuffle(idx); ntr=int(0.7*n); return idx[:ntr],idx[ntr:]
def std(X,tr):
    mu=X[tr].mean(0,keepdims=True); sd=X[tr].std(0,keepdims=True)+1e-6; return (X-mu)/sd,mu,sd
def fit(X,y,tr,lr,steps,l2,pos_weight=1.0):
    Xb=np.c_[X,np.ones(len(X))]; w=np.zeros(Xb.shape[1])
    for _ in range(steps):
        z=np.clip(Xb[tr]@w,-50,50); p=1/(1+np.exp(-z)); weights=np.where(y[tr]==1,pos_weight,1.0)
        grad=Xb[tr].T@((p-y[tr])*weights)/weights.sum()+l2*np.r_[w[:-1],0]
        w-=lr*grad
    return w
def prob(X,w):
    z=np.clip(np.c_[X,np.ones(len(X))]@w,-50,50); return 1/(1+np.exp(-z))
def auc(y,p):
    pos=p[y==1]; neg=p[y==0]
    if len(pos)==0 or len(neg)==0: return 0.0
    # Mann-Whitney approximation
    vals=np.concatenate([pos,neg]); order=np.argsort(vals); ranks=np.empty_like(order,dtype=float); ranks[order]=np.arange(1,len(vals)+1)
    return float((ranks[:len(pos)].sum()-len(pos)*(len(pos)+1)/2)/(len(pos)*len(neg)))
def choose_threshold(p,y,tr):
    rate=y[tr].mean(); return float(np.quantile(p[tr],1-rate)) if rate>0 else 1.0
def bin_rows(meta,y,p,thr):
    bins=[(0,0.10),(0.10,0.15),(0.15,0.20),(0.20,0.30),(0.30,999)]
    rows=[]; pred=(p>=thr).astype(int)
    for lo,hi in bins:
        idx=[i for i,m in enumerate(meta) if lo<=fnum(m.get('particle0_iso_pt_ratio'))<hi]
        rows.append({'bin':f'{lo:.2f}-{hi:.2f}' if hi<999 else f'{lo:.2f}+','n':len(idx),'ParticleNet_rate':float(y[idx].mean()) if idx else 0.0,'surrogate_prob_mean':float(p[idx].mean()) if idx else 0.0,'surrogate_calibrated_rate':float(pred[idx].mean()) if idx else 0.0,'gap_rate':float(pred[idx].mean()-y[idx].mean()) if idx else 0.0})
    return rows
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--phase1-events',default='reports/latest/tables/hqql_tbl_confusion_physics_events.csv'); ap.add_argument('--seed',type=int,default=123); ap.add_argument('--lr',type=float,default=0.05); ap.add_argument('--steps',type=int,default=3000); ap.add_argument('--l2',type=float,default=1e-3); ap.add_argument('--pos-weight',type=float,default=8.0)
    ap.add_argument('--out-md',default='reports/latest/KNOWN_OBSERVABLE_RESIDUAL_V2_1_BEHAVIOR.md'); ap.add_argument('--out-json',default='manifests/latest/known_observable_residual_v2_1_behavior.json'); ap.add_argument('--out-bins',default='reports/latest/tables/known_observable_residual_v2_1_behavior_bins.csv'); ap.add_argument('--out-importance',default='reports/latest/tables/known_observable_residual_v2_1_behavior_importance.csv')
    a=ap.parse_args(); rows=readcsv(a.phase1_events); names=features(); X,y,meta=build(rows,names); tr,te=split(len(y),a.seed); Xs,mu,sd=std(X,tr); w=fit(Xs,y,tr,a.lr,a.steps,a.l2,a.pos_weight); p=prob(Xs,w); thr=choose_threshold(p,y,tr); pred=(p>=thr).astype(int)
    te_acc=float((pred[te]==y[te]).mean()); te_auc=auc(y[te],p[te]); train_rate=float(y[tr].mean()); test_rate=float(y[te].mean()); agreement=te_acc
    bins=bin_rows(meta,y,p,thr); imp=sorted([{'feature':n,'abs_weight':float(abs(v))} for n,v in zip(names,w[:-1])],key=lambda r:r['abs_weight'],reverse=True)
    wcsv(a.out_bins,bins); wcsv(a.out_importance,imp); summary={'ok':True,'n_hqql':len(y),'train_n':len(tr),'test_n':len(te),'train_particlenet_hqql_to_tbl_rate':train_rate,'test_particlenet_hqql_to_tbl_rate':test_rate,'behavior_surrogate_acc_test':te_acc,'behavior_surrogate_auc_test':te_auc,'calibrated_threshold':thr,'top_features':imp[:20]}; wjson(a.out_json,summary)
    md=['# Known Observable Residual v2.1 — Hqql behavior surrogate\n\n','This report predicts ParticleNet behavior on true Hqql events: whether ParticleNet outputs Tbl. It is better calibrated for the isolation-regime question than V2 true-label surrogate.\n\n','## Summary\n',mdtab(['metric','value'],[[k,fmt(v)] for k,v in summary.items() if k not in ('top_features','ok')]),'\n## Hqql->Tbl behavior by isolation bin\n',mdtab(['bin','n','ParticleNet_rate','surrogate_prob_mean','surrogate_calibrated_rate','gap_rate'],[[r['bin'],r['n'],fmt(r['ParticleNet_rate']),fmt(r['surrogate_prob_mean']),fmt(r['surrogate_calibrated_rate']),fmt(r['gap_rate'])] for r in bins]),'\n## Top features\n',mdtab(['feature','abs_weight'],[[r['feature'],fmt(r['abs_weight'])] for r in imp[:25]]),'\n## Interpretation\n\nIf calibrated surrogate rates follow ParticleNet rates across bins, explicit isolation/core/KNN observables explain model behavior. If not, remaining residual likely needs b-like, pairwise, or subjet geometry.\n']
    Path(a.out_md).parent.mkdir(parents=True,exist_ok=True); Path(a.out_md).write_text(''.join(md),encoding='utf-8')
    print(json.dumps({'ok':True,'out_md':a.out_md,'auc':te_auc,'acc':te_acc},indent=2))
if __name__=='__main__': main()
