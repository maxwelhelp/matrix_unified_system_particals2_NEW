#!/usr/bin/env python3
import argparse, csv, json, sys, math
from pathlib import Path
import numpy as np
import torch
import torch.nn.functional as F

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools.particle0_topk_controls_v2 import make_model, load_balanced, model_logits, real_mask, pt_values
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
            if k not in seen:
                keys.append(k); seen.add(k)
    with p.open('w',encoding='utf-8',newline='') as f:
        wr=csv.DictWriter(f,fieldnames=keys); wr.writeheader()
        for r in rows: wr.writerow({k:r.get(k,'') for k in keys})
def table(headers, rows):
    if not rows: return '_No rows._\n'
    out=['| '+' | '.join(headers)+' |','| '+' | '.join(['---']*len(headers))+' |']
    for r in rows: out.append('| '+' | '.join(str(x) for x in r)+' |')
    return '\n'.join(out)+'\n'


def safe_div(a,b,eps=1e-8):
    return a/(b+eps)

def masked_sum(x,m):
    return (x*m).sum(dim=1)

def masked_mean(x,m):
    return masked_sum(x,m)/m.sum(dim=1).clamp_min(1.0)

def masked_max(x,m):
    return x.masked_fill(~m.bool(),-1e30).max(dim=1).values

def topk_sum(x,m,k):
    xx=x.masked_fill(~m.bool(),-1e30)
    kk=min(k,xx.shape[1])
    vals=torch.topk(xx,kk,dim=1).values.clamp_min(0)
    return vals.sum(dim=1)

def build_known_features(batch, mode='kinpid'):
    # batch: points [B,2,N], features [B,C,N], vectors [B,4,N], mask [B,1,N]
    mask=real_mask(batch).float()
    mb=mask.bool()
    v=batch['vectors'].float()  # [B,4,N] = px,py,pz,E
    px,py,pz,en=v[:,0,:],v[:,1,:],v[:,2,:],v[:,3,:]
    pt=torch.sqrt(px*px+py*py+1e-9)
    sum_px=masked_sum(px,mask); sum_py=masked_sum(py,mask); sum_pz=masked_sum(pz,mask); sum_e=masked_sum(en,mask)
    jet_pt=torch.sqrt(sum_px*sum_px+sum_py*sum_py+1e-9)
    jet_p2=sum_px*sum_px+sum_py*sum_py+sum_pz*sum_pz
    jet_mass=torch.sqrt((sum_e*sum_e-jet_p2).clamp_min(0))
    n=mask.sum(dim=1)
    sum_pt=masked_sum(pt,mask).clamp_min(1e-8)
    lead_pt=masked_max(pt,mb).clamp_min(0)
    lead_e=masked_max(en,mb).clamp_min(0)
    feats=[]; names=[]
    def add(name,t):
        names.append(name); feats.append(t.detach().float().cpu())
    add('log_jet_pt', torch.log1p(jet_pt))
    add('log_jet_energy', torch.log1p(sum_e.clamp_min(0)))
    add('log_jet_mass', torch.log1p(jet_mass))
    add('log_nparticles', torch.log1p(n))
    add('lead_pt_frac', safe_div(lead_pt,sum_pt))
    add('lead_e_frac', safe_div(lead_e,sum_e.clamp_min(1e-8)))
    for k in [2,4,8,16,32]:
        add(f'top{k}_pt_frac', safe_div(topk_sum(pt,mb,k),sum_pt))
    pts=batch['points'].float() # deta,dphi
    deta,dphi=pts[:,0,:],pts[:,1,:]
    dR=torch.sqrt(deta*deta+dphi*dphi+1e-9)
    add('mean_deltaR', masked_mean(dR,mask))
    add('max_deltaR', masked_max(dR,mb).clamp_min(0))
    add('pt_weighted_deltaR', masked_sum(dR*pt,mask)/sum_pt)
    add('pt2_concentration', safe_div(masked_sum(pt*pt,mask),sum_pt*sum_pt))
    # ECF-like cheap moments: pairless approximations / radial energy moments.
    for pwr in [1,2,3]:
        add(f'pt_weighted_dR{pwr}', masked_sum((dR**pwr)*pt,mask)/sum_pt)
    x=batch['features'].float()
    C=x.shape[1]
    # Loader layout: first 5 kin, if kinpid/full then channels 5..10 are charge and PID flags, last2 coords.
    if C >= 11:
        charge=x[:,5,:]
        add('charge_sum', masked_sum(charge,mask))
        add('charge_abs_sum', masked_sum(charge.abs(),mask))
        add('charge_mean', masked_mean(charge,mask))
        pid_names=['charged_hadron','neutral_hadron','photon','electron','muon']
        for off,pn in enumerate(pid_names, start=6):
            if off < C:
                add(f'pid_frac_{pn}', masked_mean(x[:,off,:],mask))
                add(f'pid_pt_frac_{pn}', safe_div(masked_sum(x[:,off,:]*pt,mask),sum_pt))
    # Raw normalized feature summaries as fallback known observables.
    for ci in range(min(C,13)):
        add(f'feat{ci}_mean', masked_mean(x[:,ci,:],mask))
        add(f'feat{ci}_ptw', safe_div(masked_sum(x[:,ci,:]*pt,mask),sum_pt))
    X=torch.stack(feats,dim=1).numpy().astype('float64')
    X=np.nan_to_num(X, nan=0.0, posinf=0.0, neginf=0.0)
    return X,names

def standardize_train_test(X, train_idx, test_idx):
    mu=X[train_idx].mean(axis=0,keepdims=True)
    sd=X[train_idx].std(axis=0,keepdims=True)+1e-6
    return (X[train_idx]-mu)/sd, (X[test_idx]-mu)/sd, mu, sd

def ridge_fit_predict(Xtr,Ytr,Xte,lam=1e-2):
    # Add bias and solve (X^T X + lam I)^-1 X^T Y.
    Xtrb=np.concatenate([Xtr,np.ones((Xtr.shape[0],1))],axis=1)
    Xteb=np.concatenate([Xte,np.ones((Xte.shape[0],1))],axis=1)
    A=Xtrb.T@Xtrb + lam*np.eye(Xtrb.shape[1])
    A[-1,-1] -= lam  # no bias penalty
    W=np.linalg.solve(A, Xtrb.T@Ytr)
    return Xteb@W, W

def r2_score(y,p):
    ss_res=((y-p)**2).sum(axis=0)
    ss_tot=((y-y.mean(axis=0,keepdims=True))**2).sum(axis=0)+1e-9
    return 1.0-ss_res/ss_tot

def split_indices(n,seed=123,train_frac=0.7):
    rng=np.random.default_rng(seed)
    idx=np.arange(n); rng.shuffle(idx)
    ntr=max(1,int(n*train_frac))
    return idx[:ntr], idx[ntr:]

def softmax_np(z):
    z=z-z.max(axis=1,keepdims=True)
    e=np.exp(z); return e/e.sum(axis=1,keepdims=True)


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--checkpoint',default='local_checkpoints/part/ParticleNet_kinpid.pt')
    ap.add_argument('--data-dir',default=str(Path.home()/'Рабочий стол/jetclass_tiny_balanced'))
    ap.add_argument('--mode',default='kinpid',choices=['kin','kinpid','full'])
    ap.add_argument('--samples-per-file',type=int,default=256)
    ap.add_argument('--max-files',type=int,default=20)
    ap.add_argument('--micro-batch',type=int,default=128)
    ap.add_argument('--seed',type=int,default=123)
    ap.add_argument('--ridge-lambda',type=float,default=1e-2)
    ap.add_argument('--device',default='cuda' if torch.cuda.is_available() else 'cpu')
    ap.add_argument('--out-dir',default='runs/known_observable_residual_v1')
    args=ap.parse_args(); out=Path(args.out_dir); mkdir(out/'tables')
    model,res=make_model(args.checkpoint,args.mode,args.device)
    batch=load_balanced(args.data_dir,mode=args.mode,samples_per_file=args.samples_per_file,max_files=args.max_files,device=args.device)
    y=batch['y'].detach().cpu().numpy().astype('int64')
    logits=model_logits(model,batch,args.micro_batch).numpy().astype('float64')
    model_pred=logits.argmax(axis=1)
    model_acc=float((model_pred==y).mean())
    X,names=build_known_features(batch,args.mode)
    train_idx,test_idx=split_indices(len(y),args.seed,0.7)
    Xtr,Xte,mu,sd=standardize_train_test(X,train_idx,test_idx)
    Ytr=logits[train_idx]; Yte=logits[test_idx]
    pred_logits,W=ridge_fit_predict(Xtr,Ytr,Xte,args.ridge_lambda)
    residual=Yte-pred_logits
    r2=r2_score(Yte,pred_logits)
    surrogate_pred=pred_logits.argmax(axis=1)
    test_y=y[test_idx]
    test_model_pred=model_pred[test_idx]
    surrogate_acc=float((surrogate_pred==test_y).mean())
    surrogate_agreement=float((surrogate_pred==test_model_pred).mean())
    residual_norm=np.linalg.norm(residual,axis=1)
    logit_norm=np.linalg.norm(Yte,axis=1)+1e-9
    residual_rel=float(np.mean(residual_norm/logit_norm))
    mse=float(((Yte-pred_logits)**2).mean())
    # One-hot true-label ridge baseline as a sanity check.
    onehot=np.eye(len(LABELS))[y]
    pred_oh,_=ridge_fit_predict(Xtr,onehot[train_idx],Xte,args.ridge_lambda)
    oh_pred=pred_oh.argmax(axis=1)
    observable_label_acc=float((oh_pred==test_y).mean())
    class_rows=[]
    for c,lbl in enumerate(LABELS):
        mask=(test_y==c)
        if mask.sum()==0: continue
        class_rows.append({
            'class_id':c,'class_label':lbl,'n':int(mask.sum()),
            'model_acc':float((test_model_pred[mask]==test_y[mask]).mean()),
            'surrogate_acc':float((surrogate_pred[mask]==test_y[mask]).mean()),
            'surrogate_agreement_with_model':float((surrogate_pred[mask]==test_model_pred[mask]).mean()),
            'logit_r2_class':float(r2[c]),
            'residual_norm_mean':float(residual_norm[mask].mean()),
        })
    # Feature importance proxy: abs coefficient norms per observable.
    coef=W[:-1,:]
    imp=np.linalg.norm(coef,axis=1)
    imp_rows=sorted([{'feature':n,'coef_norm':float(v)} for n,v in zip(names,imp)], key=lambda r:r['coef_norm'], reverse=True)
    event_rows=[]
    top=np.argsort(-residual_norm)[:50]
    for rank,j in enumerate(top,1):
        ii=int(test_idx[j])
        event_rows.append({'rank':rank,'event_index':ii,'true_label':LABELS[int(y[ii])],'model_pred':LABELS[int(model_pred[ii])],'surrogate_pred':LABELS[int(surrogate_pred[j])],'residual_norm':float(residual_norm[j]),'residual_rel':float(residual_norm[j]/logit_norm[j])})
    status='KNOWN_OBSERVABLE_PROXY_STRONG' if surrogate_agreement>=0.85 and np.nanmean(r2)>=0.65 else 'RESIDUAL_SIGNAL_REMAINS' if surrogate_agreement<0.70 or np.nanmean(r2)<0.45 else 'PARTIAL_KNOWN_OBSERVABLE_EXPLANATION'
    summary={
        'ok':True,'checkpoint':args.checkpoint,'mode':args.mode,'n_events':int(len(y)),'train_n':int(len(train_idx)),'test_n':int(len(test_idx)),
        'model_acc_test':float((test_model_pred==test_y).mean()),'model_acc_all':model_acc,
        'known_observable_surrogate_acc':surrogate_acc,
        'known_observable_agreement_with_model':surrogate_agreement,
        'observable_label_acc':observable_label_acc,
        'logit_r2_mean':float(np.nanmean(r2)),'logit_r2_min':float(np.nanmin(r2)),'logit_r2_max':float(np.nanmax(r2)),
        'residual_rel_mean':residual_rel,'logit_mse':mse,'status':status,
        'n_features':len(names),'top_features':imp_rows[:25],
        'missing':list(res.missing_keys),'unexpected':list(res.unexpected_keys),
        'files':batch.get('files',[]),
    }
    wcsv(out/'tables/known_observable_residual_by_class.csv',class_rows)
    wcsv(out/'tables/known_observable_feature_importance.csv',imp_rows)
    wcsv(out/'tables/known_observable_residual_top_events.csv',event_rows)
    wjson(out/'known_observable_residual_v1.json',summary)
    md=['# Known Observable Residual v1\n\n',
        'This report asks whether ParticleNet logits are mostly explainable by simple known observables, or whether a residual model signal remains.\n\n',
        f"n_events={len(y)} train={len(train_idx)} test={len(test_idx)} status={status}\n\n",
        '## Summary\n',
        table(['metric','value'],[
            ['model_acc_test',fmt(summary['model_acc_test'])],
            ['known_observable_surrogate_acc',fmt(surrogate_acc)],
            ['known_observable_agreement_with_model',fmt(surrogate_agreement)],
            ['observable_label_acc',fmt(observable_label_acc)],
            ['logit_r2_mean',fmt(summary['logit_r2_mean'])],
            ['logit_r2_min',fmt(summary['logit_r2_min'])],
            ['residual_rel_mean',fmt(residual_rel)],
            ['n_features',len(names)],
        ]),
        '\n## Per-class surrogate/residual\n',
        table(['class','n','model_acc','surrogate_acc','agreement','logit_r2','residual_norm'],[[r['class_label'],r['n'],fmt(r['model_acc']),fmt(r['surrogate_acc']),fmt(r['surrogate_agreement_with_model']),fmt(r['logit_r2_class']),fmt(r['residual_norm_mean'])] for r in class_rows]),
        '\n## Top known-observable coefficients\n',
        table(['rank','feature','coef_norm'],[[i+1,r['feature'],fmt(r['coef_norm'])] for i,r in enumerate(imp_rows[:30])]),
        '\n## Top residual events\n',
        table(['rank','event','true','model_pred','surrogate_pred','residual_norm','residual_rel'],[[r['rank'],r['event_index'],r['true_label'],r['model_pred'],r['surrogate_pred'],fmt(r['residual_norm']),fmt(r['residual_rel'])] for r in event_rows[:25]]),
        '\n## Interpretation\n\n',
        '- If agreement/R2 are high, the particle0/top-k mechanism may mostly be a known-observable proxy.\n',
        '- If residual remains high, the model contains signal not captured by this simple observable set.\n',
        '- This v1 is a first-pass linear/ridge surrogate, not final physics proof. Next steps: richer ECF/EFP-like features and heldout/per-file stability.\n']
    (out/'KNOWN_OBSERVABLE_RESIDUAL_V1.md').write_text(''.join(md),encoding='utf-8')
    print(json.dumps(summary,indent=2,ensure_ascii=False)[:20000])

if __name__=='__main__': main()
