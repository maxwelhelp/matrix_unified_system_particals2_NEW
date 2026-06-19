#!/usr/bin/env python3
import argparse, csv, json, re
from pathlib import Path
import numpy as np
import uproot

LABELS = ['label_QCD','label_Hbb','label_Hcc','label_Hgg','label_H4q','label_Hqql','label_Zqq','label_Wqq','label_Tbqq','label_Tbl']
SRC='label_Hqql'; TGT='label_Tbl'

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
        if hasattr(obj,'arrays') and hasattr(obj,'keys'):
            return obj
    raise RuntimeError('no tree found')

def score_branches(keys):
    bs=[]
    for lab in LABELS:
        for cand in [f'score_{lab}', f'score_{lab.replace("label_","")}', f'scores_{lab}']:
            if cand in keys:
                bs.append(cand); break
        else:
            return []
    return bs

def group_from_output_name(path):
    name=Path(path).name
    m=re.match(r'part_weaver_predict_smoke_v3_(.*)\.root$', name)
    return m.group(1) if m else Path(path).stem

def read_manifest(p):
    mp={}
    p=Path(p)
    if not p.exists(): return mp
    for line in p.read_text(encoding='utf-8').splitlines():
        if ':' in line:
            g, f = line.split(':', 1)
            mp[g]=f
    return mp

def read_output(path, manifest):
    g=group_from_output_name(path)
    with uproot.open(path) as rf:
        t=find_tree(rf); keys=list(t.keys())
        labs=[x for x in LABELS if x in keys]
        scores=score_branches(keys)
        if len(labs)!=len(LABELS) or len(scores)!=len(LABELS):
            raise RuntimeError(f'cannot find labels/scores in {path}')
        arr=t.arrays(labs+scores, library='np')
        Y=np.stack([arr[x] for x in labs], axis=1)
        S=np.stack([arr[x] for x in scores], axis=1)
        y=Y.argmax(axis=1); pred=S.argmax(axis=1)
        rows=[]
        for i in range(len(y)):
            rows.append({
                'output_root': str(path), 'source_root': manifest.get(g,''), 'source_group': g,
                'entry_idx': int(i), 'true_label': LABELS[int(y[i])], 'pred_label': LABELS[int(pred[i])],
                'score_Hqql': float(S[i, LABELS.index(SRC)]), 'score_Tbl': float(S[i, LABELS.index(TGT)]),
                'margin_Hqql_minus_Tbl': float(S[i, LABELS.index(SRC)]-S[i, LABELS.index(TGT)]),
                'margin_Tbl_minus_Hqql': float(S[i, LABELS.index(TGT)]-S[i, LABELS.index(SRC)]),
                'pred_score': float(S[i, int(pred[i])])
            })
        return rows

def take(rows, group_name, max_n):
    if group_name=='A_Hqql_correct':
        xs=[r for r in rows if r['source_group']=='HToWW2Q1L' and r['true_label']==SRC and r['pred_label']==SRC]
        xs=sorted(xs, key=lambda r:r['margin_Hqql_minus_Tbl'], reverse=True)
    elif group_name=='B_Hqql_to_Tbl':
        xs=[r for r in rows if r['source_group']=='HToWW2Q1L' and r['true_label']==SRC and r['pred_label']==TGT]
        xs=sorted(xs, key=lambda r:r['margin_Tbl_minus_Hqql'], reverse=True)
    elif group_name=='C_Tbl_correct':
        xs=[r for r in rows if r['source_group']=='TTBarLep' and r['true_label']==TGT and r['pred_label']==TGT]
        xs=sorted(xs, key=lambda r:r['margin_Tbl_minus_Hqql'], reverse=True)
    elif group_name=='D_Tbl_to_Hqql':
        xs=[r for r in rows if r['source_group']=='TTBarLep' and r['true_label']==TGT and r['pred_label']==SRC]
        xs=sorted(xs, key=lambda r:r['margin_Hqql_minus_Tbl'], reverse=True)
    else:
        xs=[]
    for r in xs[:max_n]: r['analysis_group']=group_name
    return xs[:max_n], len(xs)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--root-glob', default='reports/latest/part_weaver_predict_smoke_v3_*.root')
    ap.add_argument('--manifest', default='manifests/latest/part_weaver_predict_smoke_v3_args.txt')
    ap.add_argument('--max-a', type=int, default=128)
    ap.add_argument('--max-b', type=int, default=128)
    ap.add_argument('--max-c', type=int, default=128)
    ap.add_argument('--max-d', type=int, default=128)
    ap.add_argument('--out-md', default='reports/latest/PART_HQQL_TBL_GROUP_BUILDER_V1.md')
    ap.add_argument('--out-csv', default='reports/latest/tables/part_hqql_tbl_groups_v1.csv')
    ap.add_argument('--out-json', default='manifests/latest/part_hqql_tbl_group_builder_v1.json')
    a=ap.parse_args()
    manifest=read_manifest(a.manifest)
    all_rows=[]
    for f in sorted(Path('.').glob(a.root_glob)):
        all_rows += read_output(f, manifest)
    selected=[]; counts={}
    for g,mx in [('A_Hqql_correct',a.max_a),('B_Hqql_to_Tbl',a.max_b),('C_Tbl_correct',a.max_c),('D_Tbl_to_Hqql',a.max_d)]:
        rows,n=take(all_rows,g,mx); selected += rows; counts[g]=n
    wcsv(a.out_csv, selected)
    Path(a.out_json).parent.mkdir(parents=True, exist_ok=True)
    Path(a.out_json).write_text(json.dumps({'ok':True,'counts_total':counts,'selected':len(selected),'root_glob':a.root_glob}, indent=2, ensure_ascii=False), encoding='utf-8')
    md='# PART_HQQL_TBL_GROUP_BUILDER_V1\n\n'
    md+='Builds A/B/C groups for ParT attention tracing from Weaver prediction ROOT outputs.\n\n'
    md+='## Counts\n'+mdtab(['group','total_available','selected_limit'], [[k,counts[k], {'A_Hqql_correct':a.max_a,'B_Hqql_to_Tbl':a.max_b,'C_Tbl_correct':a.max_c,'D_Tbl_to_Hqql':a.max_d}[k]] for k in counts])
    md+='\n## Selected preview\n'+mdtab(['group','source_group','entry','true','pred','score_Hqql','score_Tbl','margin'], [[r['analysis_group'],r['source_group'],r['entry_idx'],r['true_label'],r['pred_label'],round(r['score_Hqql'],5),round(r['score_Tbl'],5),round(r['margin_Tbl_minus_Hqql'] if r['analysis_group'].startswith(('B','C')) else r['margin_Hqql_minus_Tbl'],5)] for r in selected[:40]])
    md+='\n## Next\nUse `part_hqql_tbl_groups_v1.csv` as the event index list for `PART_ATTENTION_TRACE_V1`.\n'
    Path(a.out_md).parent.mkdir(parents=True, exist_ok=True); Path(a.out_md).write_text(md, encoding='utf-8')
    print(json.dumps({'ok':True,'counts':counts,'selected':len(selected),'out_md':a.out_md}, indent=2))
if __name__=='__main__': main()
