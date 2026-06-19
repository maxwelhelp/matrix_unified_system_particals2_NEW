#!/usr/bin/env python3
import argparse, glob, json
from pathlib import Path
import numpy as np

LABELS=['label_QCD','label_Hbb','label_Hcc','label_Hgg','label_H4q','label_Hqql','label_Zqq','label_Wqq','label_Tbqq','label_Tbl']
SAMPLE_TO_LABEL={
 'ZJetsToNuNu':'label_QCD','HToBB':'label_Hbb','HToCC':'label_Hcc','HToGG':'label_Hgg','HToWW4Q':'label_H4q','HToWW2Q1L':'label_Hqql','ZToQQ':'label_Zqq','WToQQ':'label_Wqq','TTBar':'label_Tbqq','TTBarLep':'label_Tbl'
}

def pick_tree(f):
    trees=[]
    for k,v in f.items():
        try:
            if hasattr(v,'num_entries') and hasattr(v,'keys'):
                trees.append((k,v))
        except Exception:
            pass
    return sorted(trees,key=lambda kv:getattr(kv[1],'num_entries',0),reverse=True)[0] if trees else (None,None)

def sample_from_name(path):
    stem=Path(path).stem
    return stem[5:] if stem.startswith('pred_') else stem

def score_branches(branches):
    xs=[f'score_{x}' for x in LABELS]
    if all(x in branches for x in xs): return xs
    for key in ['score','softmax','prob','output']:
        cand=[b for b in branches if key in b.lower()]
        if len(cand)>=10: return cand[:10]
    return []

def confusion(y,p,n=10):
    m=np.zeros((n,n),dtype=np.int64)
    for a,b in zip(y.astype(int),p.astype(int)):
        if 0<=a<n and 0<=b<n: m[a,b]+=1
    return m

def safe_acc(y,p):
    y=np.asarray(y); p=np.asarray(p)
    if len(y)==0: return None
    return float((y.astype(int)==p.astype(int)).mean())

def label_from_onehot(arr):
    if not all(x in arr for x in LABELS): return None
    mat=np.stack([arr[x] for x in LABELS],axis=1)
    return mat.argmax(axis=1).astype(np.int64)

def label_from_filename(fp, n):
    s=sample_from_name(fp)
    lab=SAMPLE_TO_LABEL.get(s)
    if lab not in LABELS: return None
    return np.full(n, LABELS.index(lab), dtype=np.int64)

def label_from__label_(arr):
    if '_label_' not in arr: return None
    y=np.asarray(arr['_label_'])
    # Weaver can store int class id or sometimes one-hot-like arrays.
    if y.ndim==1: return y.astype(np.int64)
    if y.ndim==2 and y.shape[1]>=10: return y[:,:10].argmax(axis=1).astype(np.int64)
    return y.reshape(-1).astype(np.int64)

def label_perm_upper(cm):
    # Greedy upper bound if label order is permuted. For exact assignment scipy may not exist; greedy is enough diagnostic.
    cm=cm.copy()
    used_cols=set(); total=0
    for i in range(cm.shape[0]):
        choices=sorted([(cm[i,j],j) for j in range(cm.shape[1]) if j not in used_cols], reverse=True)
        if choices:
            total+=int(choices[0][0]); used_cols.add(choices[0][1])
    return float(total/max(1,int(cm.sum())))

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--pred-dir',default='runs/official_weaver_predict_v5_kinpid')
    ap.add_argument('--out-dir',default='runs/official_weaver_pred_probe_v7_label_branch')
    args=ap.parse_args()
    out=Path(args.out_dir); out.mkdir(parents=True,exist_ok=True)
    import uproot
    files=sorted(glob.glob(str(Path(args.pred_dir)/'pred_*.root')))
    rec={'pred_dir':args.pred_dir,'n_files':len(files),'files':[],'global':{}}
    all_pred=[]; all_y_file=[]; all_y_branch=[]; all_y_label=[]
    first_branches=[]
    for fp in files:
        f=uproot.open(fp); tname,tr=pick_tree(f)
        branches=list(tr.keys()) if tr is not None else []
        if not first_branches: first_branches=branches
        sc=score_branches(branches)
        item={'file':fp,'sample':sample_from_name(fp),'tree':tname,'entries':int(tr.num_entries) if tr else 0,'score_branches':sc,'acc_by_filename':None,'acc_by_label_branches':None,'acc_by__label_':None,'pred_counts':None,'label_branch_counts':None,'_label_counts':None,'filename_label':SAMPLE_TO_LABEL.get(sample_from_name(fp))}
        if tr is None or not sc:
            rec['files'].append(item); continue
        need=list(dict.fromkeys(sc + [x for x in LABELS if x in branches] + (['_label_'] if '_label_' in branches else [])))
        arr=tr.arrays(need,library='np')
        scores=np.stack([arr[x] for x in sc],axis=1)
        pred=scores.argmax(axis=1).astype(np.int64)
        y_file=label_from_filename(fp,len(pred))
        y_branch=label_from_onehot(arr)
        y_label=label_from__label_(arr)
        item['pred_counts']=np.bincount(pred,minlength=10).tolist()
        if y_file is not None:
            item['acc_by_filename']=safe_acc(y_file,pred); all_y_file.append(y_file)
        if y_branch is not None:
            item['acc_by_label_branches']=safe_acc(y_branch,pred); item['label_branch_counts']=np.bincount(y_branch,minlength=10).tolist(); all_y_branch.append(y_branch)
        if y_label is not None:
            item['acc_by__label_']=safe_acc(y_label,pred); item['_label_counts']=np.bincount(y_label,minlength=10).tolist(); all_y_label.append(y_label)
        all_pred.append(pred)
        rec['files'].append(item)
    pred=np.concatenate(all_pred) if all_pred else np.array([],dtype=np.int64)
    def glob_metrics(ys):
        if not ys or len(pred)==0: return None
        y=np.concatenate(ys)
        cm=confusion(y,pred,10)
        return {'acc':safe_acc(y,pred),'counts':np.bincount(y,minlength=10).tolist(),'confusion':cm.tolist(),'label_perm_upper_greedy':label_perm_upper(cm)}
    rec['global']={
        'n':int(len(pred)),
        'pred_counts':np.bincount(pred,minlength=10).tolist() if len(pred) else [],
        'by_filename':glob_metrics(all_y_file),
        'by_label_branches':glob_metrics(all_y_branch),
        'by__label_':glob_metrics(all_y_label),
        'first_branches':first_branches[:120],
    }
    (out/'official_weaver_pred_probe_v7_label_branch.json').write_text(json.dumps(rec,indent=2,ensure_ascii=False),encoding='utf-8')
    md=['# Official Weaver prediction probe v7 label branch\n\n',f"pred_dir={args.pred_dir}\nn_files={len(files)}\n\n"]
    for key,title in [('by_filename','Accuracy by filename mapping'),('by_label_branches','Accuracy by one-hot label_* branches'),('by__label_','Accuracy by _label_ branch')]:
        g=rec['global'].get(key)
        md.append(f"## {title}\n\n")
        if g is None:
            md.append('_Not available._\n\n')
        else:
            md.append(f"acc={g['acc']:.6f} label_perm_upper_greedy={g['label_perm_upper_greedy']:.6f}\n\n")
            md.append(f"true_counts=`{g['counts']}`\n\n")
    md.append('| file | sample | file-label | entries | acc_file | acc_label_* | acc__label_ | pred_counts | _label_counts | label*_counts |\n')
    md.append('| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- |\n')
    for it in rec['files']:
        md.append(f"| `{Path(it['file']).name}` | {it['sample']} | {it['filename_label']} | {it['entries']} | {it['acc_by_filename']} | {it['acc_by_label_branches']} | {it['acc_by__label_']} | `{it['pred_counts']}` | `{it['_label_counts']}` | `{it['label_branch_counts']}` |\n")
    md.append('\n## First output branches\n\n```json\n'+json.dumps(first_branches[:120],indent=2,ensure_ascii=False)+'\n```\n')
    (out/'OFFICIAL_WEAVER_PRED_PROBE_V7_LABEL_BRANCH.md').write_text(''.join(md),encoding='utf-8')
    print(json.dumps(rec,indent=2,ensure_ascii=False)[:20000])
if __name__=='__main__': main()
