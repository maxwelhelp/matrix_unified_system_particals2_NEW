#!/usr/bin/env python3
import argparse, csv, json, re
from pathlib import Path
from collections import defaultdict
import numpy as np
import uproot

LABELS = ['label_QCD','label_Hbb','label_Hcc','label_Hgg','label_H4q','label_Hqql','label_Zqq','label_Wqq','label_Tbqq','label_Tbl']

def wcsv(p, rows):
    p=Path(p); p.parent.mkdir(parents=True, exist_ok=True)
    keys=[]
    for r in rows:
        for k in r:
            if k not in keys: keys.append(k)
    with p.open('w', encoding='utf-8', newline='') as f:
        wr=csv.DictWriter(f, fieldnames=keys); wr.writeheader(); wr.writerows(rows)

def mdtab(h, rows):
    if not rows: return '_No rows._\n'
    return '\n'.join(['| '+' | '.join(h)+' |','| '+' | '.join(['---']*len(h))+' |']+['| '+' | '.join(str(x) for x in r)+' |' for r in rows])+'\n'

def find_tree(rf):
    for k in rf.keys():
        obj=rf[k]
        if hasattr(obj, 'keys') and hasattr(obj, 'arrays'):
            return k, obj
    return None, None

def score_branches(keys):
    patterns=[]
    for pref in ['score_', 'scores_', 'output_', 'prob_', 'cls_', 'predict_']:
        bs=[]
        for lab in LABELS:
            for cand in [pref+lab, pref+lab.replace('label_','')]:
                if cand in keys: bs.append(cand); break
        if len(bs)==len(LABELS): return bs, pref
    # fallback: branches ending label names
    bs=[]
    for lab in LABELS:
        hits=[k for k in keys if k.endswith(lab) and k not in LABELS]
        bs.append(hits[0] if hits else '')
    if all(bs): return bs, 'suffix_label_fallback'
    return [], ''

def label_branches(keys):
    if all(l in keys for l in LABELS): return LABELS
    return []

def analyze_file(path):
    out={'file':str(path)}
    with uproot.open(path) as rf:
        tname,t=find_tree(rf)
        out['tree']=tname or ''
        if t is None:
            out['error']='no tree found'; return out, [], []
        keys=list(t.keys()); out['branches_n']=len(keys); out['branches_sample']=';'.join(keys[:30])
        labs=label_branches(keys); scores,spref=score_branches(keys)
        out['label_branches_found']=len(labs); out['score_branches_found']=len(scores); out['score_prefix']=spref
        if not labs or not scores:
            out['error']='could not find labels or score branches'; return out, [], []
        arr=t.arrays(labs+scores, library='np')
        Y=np.stack([arr[x] for x in labs], axis=1)
        S=np.stack([arr[x] for x in scores], axis=1)
        y=Y.argmax(axis=1); pred=S.argmax(axis=1)
        out['n']=int(len(y)); out['accuracy']=float((y==pred).mean()) if len(y) else 0.0
        cm=defaultdict(int)
        pred_counts=defaultdict(int); true_counts=defaultdict(int)
        for a,b in zip(y,pred):
            cm[(LABELS[int(a)],LABELS[int(b)])]+=1; pred_counts[LABELS[int(b)]]+=1; true_counts[LABELS[int(a)]]+=1
        pairs=[{'file':str(path),'true_label':k[0],'pred_label':k[1],'n':v} for k,v in sorted(cm.items(), key=lambda kv:-kv[1])]
        counts=[]
        for lab in LABELS: counts.append({'file':str(path),'label':lab,'true_n':true_counts[lab],'pred_n':pred_counts[lab]})
        return out,pairs,counts

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--glob', default='reports/latest/part_weaver_predict_smoke_v3*.root')
    ap.add_argument('--out-md', default='reports/latest/PART_WEAVER_OUTPUT_ANALYZER_V1.md')
    ap.add_argument('--out-summary', default='reports/latest/tables/part_weaver_output_analyzer_v1_summary.csv')
    ap.add_argument('--out-pairs', default='reports/latest/tables/part_weaver_output_analyzer_v1_pairs.csv')
    ap.add_argument('--out-counts', default='reports/latest/tables/part_weaver_output_analyzer_v1_counts.csv')
    ap.add_argument('--out-json', default='manifests/latest/part_weaver_output_analyzer_v1.json')
    a=ap.parse_args()
    files=sorted(Path('.').glob(a.glob))
    summary=[]; pairs=[]; counts=[]
    for f in files:
        try:
            s,p,c=analyze_file(f); summary.append(s); pairs+=p; counts+=c
        except Exception as e:
            summary.append({'file':str(f),'error':repr(e)[:500]})
    wcsv(a.out_summary, summary); wcsv(a.out_pairs, pairs); wcsv(a.out_counts, counts)
    Path(a.out_json).parent.mkdir(parents=True, exist_ok=True)
    Path(a.out_json).write_text(json.dumps({'ok':True,'files':len(files),'summary':summary}, indent=2, ensure_ascii=False), encoding='utf-8')
    md='# PART_WEAVER_OUTPUT_ANALYZER_V1\n\n'
    md+=f'- glob: `{a.glob}`\n- files: **{len(files)}**\n\n'
    md+='## Summary\n'+mdtab(['file','n','accuracy','labels','scores','prefix','error'], [[s.get('file'),s.get('n',''),s.get('accuracy',''),s.get('label_branches_found',''),s.get('score_branches_found',''),s.get('score_prefix',''),s.get('error','')] for s in summary])
    md+='\n## Top confusion pairs\n'+mdtab(['file','true','pred','n'], [[p['file'],p['true_label'],p['pred_label'],p['n']] for p in pairs[:60]])
    Path(a.out_md).parent.mkdir(parents=True, exist_ok=True); Path(a.out_md).write_text(md, encoding='utf-8')
    print(json.dumps({'ok':True,'files':len(files),'out_md':a.out_md}, indent=2))
if __name__=='__main__': main()
