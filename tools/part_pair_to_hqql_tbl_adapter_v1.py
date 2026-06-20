#!/usr/bin/env python3
import argparse, csv, json, re
from pathlib import Path


def safe(x):
    return re.sub(r'[^A-Za-z0-9]+', '_', x.replace('label_', '')).strip('_')


def read_csv(path):
    with open(path, newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))


def wcsv(path, rows):
    p = Path(path); p.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        p.write_text('', encoding='utf-8'); return
    keys=[]
    for r in rows:
        for k in r:
            if k not in keys: keys.append(k)
    with p.open('w', newline='', encoding='utf-8') as f:
        w=csv.DictWriter(f, fieldnames=keys); w.writeheader(); w.writerows(rows)


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--pair-groups', required=True)
    ap.add_argument('--out-csv', default='')
    ap.add_argument('--out-json', default='')
    ap.add_argument('--out-md', default='')
    a=ap.parse_args()
    rows=read_csv(a.pair_groups)
    if not rows:
        raise RuntimeError('empty pair groups: '+a.pair_groups)
    src=rows[0].get('src_label','')
    tgt=rows[0].get('tgt_label','')
    tag=f"{safe(src)}_to_{safe(tgt)}"
    out_csv=a.out_csv or f'reports/latest/tables/part_pair_as_hqql_tbl_{tag}_v1.csv'
    out_json=a.out_json or f'manifests/latest/part_pair_as_hqql_tbl_{tag}_v1.json'
    out_md=a.out_md or f'reports/latest/PART_PAIR_AS_HQQL_TBL_{tag}_V1.md'
    mapping={
        'A_src_correct':'A_Hqql_correct',
        'B_src_to_tgt':'B_Hqql_to_Tbl',
        'C_tgt_correct':'C_Tbl_correct',
        'D_tgt_to_src':'D_Tbl_to_Hqql',
    }
    out=[]
    for r in rows:
        nr=dict(r)
        nr['pair_original_analysis_group']=r.get('analysis_group','')
        nr['analysis_group']=mapping.get(r.get('analysis_group',''), r.get('analysis_group',''))
        nr['score_Hqql']=r.get('score_src','')
        nr['score_Tbl']=r.get('score_tgt','')
        nr['margin_Tbl_minus_Hqql']=r.get('margin_tgt_minus_src','')
        nr['margin_Hqql_minus_Tbl']=r.get('margin_src_minus_tgt','')
        nr['adapter_src_label']=src
        nr['adapter_tgt_label']=tgt
        out.append(nr)
    wcsv(out_csv,out)
    counts={g:sum(1 for r in out if r['analysis_group']==g) for g in sorted(set(r['analysis_group'] for r in out))}
    obj={'ok':True,'src_label':src,'tgt_label':tgt,'in_csv':a.pair_groups,'out_csv':out_csv,'counts':counts,'network_file':'external/particle_transformer/networks/example_ParticleTransformer_pair_adapter.py'}
    Path(out_json).parent.mkdir(parents=True, exist_ok=True); Path(out_json).write_text(json.dumps(obj,indent=2,ensure_ascii=False),encoding='utf-8')
    md=['# PART_PAIR_AS_HQQL_TBL_ADAPTER_V1\n\n',f'- src_label: `{src}` mapped to `label_Hqql` slot\n',f'- tgt_label: `{tgt}` mapped to `label_Tbl` slot\n',f'- input: `{a.pair_groups}`\n',f'- output: `{out_csv}`\n',f'- counts: `{counts}`\n\n','Use with `PART_PAIR_SRC_LABEL` and `PART_PAIR_TGT_LABEL` plus `example_ParticleTransformer_pair_adapter.py`.\n']
    Path(out_md).parent.mkdir(parents=True, exist_ok=True); Path(out_md).write_text(''.join(md),encoding='utf-8')
    print(json.dumps({'ok':True,'out_csv':out_csv,'src_label':src,'tgt_label':tgt,'counts':counts},indent=2))

if __name__=='__main__': main()
