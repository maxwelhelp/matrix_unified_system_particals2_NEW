#!/usr/bin/env python3
import argparse, glob, json, re
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
    if stem.startswith('pred_'): stem=stem[5:]
    return stem

def find_score_branches(branches):
    # Weaver often writes output names from model_info. Try common names first, then fallback.
    candidates=[]
    for patterns in [
        [f'score_{x}' for x in LABELS],
        [f'score_{x.replace("label_","")}' for x in LABELS],
        [f'prob_{x}' for x in LABELS],
        [f'prob_{x.replace("label_","")}' for x in LABELS],
        [f'softmax_{i}' for i in range(10)],
        [f'output_{i}' for i in range(10)],
    ]:
        if all(p in branches for p in patterns): return patterns
    # fallback: all numeric branches containing softmax/score/prob/output and exactly 10 of them
    for key in ['score','softmax','prob','output']:
        xs=[b for b in branches if key.lower() in b.lower()]
        if len(xs)>=10: return xs[:10]
    return []

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--pred-dir',default='runs/official_weaver_predict_v5_kinpid')
    ap.add_argument('--out-dir',default='runs/official_weaver_pred_probe_v6')
    a=ap.parse_args(); out=Path(a.out_dir); out.mkdir(parents=True,exist_ok=True)
    import uproot
    files=sorted(glob.glob(str(Path(a.pred_dir)/'pred_*.root')))
    rec={'pred_dir':a.pred_dir,'n_files':len(files),'files':[],'global':{}}
    total=0; correct=0; cm=np.zeros((10,10),dtype=np.int64)
    for fp in files:
        f=uproot.open(fp); tname,tr=pick_tree(f); branches=list(tr.keys()) if tr is not None else []
        sample=sample_from_name(fp); true_label=SAMPLE_TO_LABEL.get(sample); true_idx=LABELS.index(true_label) if true_label in LABELS else None
        score_br=find_score_branches(branches)
        item={'file':fp,'sample':sample,'true_label_from_filename':true_label,'tree':tname,'entries':int(tr.num_entries) if tr is not None else 0,'branches':branches[:80],'score_branches':score_br,'acc_from_filename':None,'pred_counts':None}
        if tr is not None and score_br and true_idx is not None:
            arr=tr.arrays(score_br,library='np')
            scores=np.stack([arr[b] for b in score_br],axis=1)
            pred=scores.argmax(axis=1)
            cnt=np.bincount(pred,minlength=10)
            item['pred_counts']=cnt.tolist()
            item['acc_from_filename']=float((pred==true_idx).mean())
            total += len(pred); correct += int((pred==true_idx).sum())
            for p in pred: cm[true_idx,int(p)] += 1
        rec['files'].append(item)
    rec['global']={'total':int(total),'correct':int(correct),'acc_from_filename':float(correct/max(1,total)),'confusion':cm.tolist()}
    (out/'official_weaver_pred_probe_v6.json').write_text(json.dumps(rec,indent=2,ensure_ascii=False),encoding='utf-8')
    md=['# Official Weaver prediction probe v6\n\n',f"pred_dir={a.pred_dir}\nn_files={len(files)}\nacc_from_filename={rec['global']['acc_from_filename']:.4f}\n\n",'| file | sample | true | entries | acc | score branches | pred_counts |\n| --- | --- | --- | ---: | ---: | --- | --- |\n']
    for it in rec['files']:
        md.append(f"| `{Path(it['file']).name}` | {it['sample']} | {it['true_label_from_filename']} | {it['entries']} | {it['acc_from_filename']} | `{it['score_branches']}` | `{it['pred_counts']}` |\n")
    md.append('\n## First file branches\n\n```json\n'+json.dumps(rec['files'][0]['branches'] if rec['files'] else [],indent=2,ensure_ascii=False)+'\n```\n')
    (out/'OFFICIAL_WEAVER_PRED_PROBE_V6.md').write_text(''.join(md),encoding='utf-8')
    print(json.dumps(rec,indent=2,ensure_ascii=False)[:20000])
if __name__=='__main__': main()
