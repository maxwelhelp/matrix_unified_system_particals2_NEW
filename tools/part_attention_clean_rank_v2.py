#!/usr/bin/env python3
import argparse, csv, json
from collections import defaultdict
from pathlib import Path

GROUPS = ['A_Hqql_correct','B_Hqql_to_Tbl','C_Tbl_correct','D_Tbl_to_Hqql']

def wcsv(path, rows):
    path=Path(path); path.parent.mkdir(parents=True, exist_ok=True)
    keys=[]
    for r in rows:
        for k in r:
            if k not in keys: keys.append(k)
    with path.open('w', encoding='utf-8', newline='') as f:
        wr=csv.DictWriter(f, fieldnames=keys); wr.writeheader(); wr.writerows(rows)

def mdtab(h, rows):
    if not rows: return '_No rows._\n'
    return '\n'.join(['| '+' | '.join(h)+' |','| '+' | '.join(['---']*len(h))+' |'] + ['| '+' | '.join(str(x) for x in r)+' |' for r in rows])+'\n'

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--pairs', default='reports/latest/tables/part_attention_pair_flows_v1.csv')
    ap.add_argument('--json', default='manifests/latest/part_attention_supertrace_v1.json')
    ap.add_argument('--min-total-n', type=int, default=100)
    ap.add_argument('--min-b-n', type=int, default=20)
    ap.add_argument('--drop-pad', action='store_true', default=True)
    ap.add_argument('--drop-cls-only', action='store_true', default=True)
    ap.add_argument('--out-md', default='reports/latest/PART_ATTENTION_CLEAN_RANK_V2.md')
    ap.add_argument('--out-csv', default='reports/latest/tables/part_attention_clean_rank_v2.csv')
    ap.add_argument('--out-json', default='manifests/latest/part_attention_clean_rank_v2.json')
    a=ap.parse_args()

    counts={g:0 for g in GROUPS}
    if Path(a.json).exists():
        j=json.loads(Path(a.json).read_text(encoding='utf-8'))
        counts.update({k:int(v) for k,v in j.get('counts',{}).items()})

    sums=defaultdict(lambda: defaultdict(float))
    ns=defaultdict(lambda: defaultdict(int))
    event_seen=defaultdict(set)
    raw_rows=0; used_rows=0; dropped_pad=0; dropped_cls=0

    with open(a.pairs, newline='', encoding='utf-8') as f:
        rd=csv.DictReader(f)
        for r in rd:
            raw_rows += 1
            q=r.get('query_role',''); k=r.get('key_role','')
            if a.drop_pad and (q=='pad' or k=='pad'):
                dropped_pad += 1; continue
            if a.drop_cls_only and q=='CLS' and k=='CLS':
                dropped_cls += 1; continue
            g=r['group']
            key=(r['module'], r['head'], r['pair_role'])
            w=float(r['attn_weight'])
            sums[key][g] += w
            ns[key][g] += 1
            event_seen[key].add((g, r.get('entry_idx','')))
            used_rows += 1

    out=[]
    for (module,head,pair), gd in sums.items():
        n_total=sum(ns[(module,head,pair)].values())
        if n_total < a.min_total_n: continue
        if ns[(module,head,pair)].get('B_Hqql_to_Tbl',0) < a.min_b_n: continue
        row={'module':module,'head':int(head),'pair_role':pair,'n_total':n_total}
        for g in GROUPS:
            n=ns[(module,head,pair)].get(g,0)
            mean=(gd.get(g,0.0)/n) if n else 0.0
            freq=(n/max(counts.get(g,1),1)) if counts.get(g,0) else 0.0
            row[g+'_n']=n; row[g+'_mean']=mean; row[g+'_freq']=freq
        A=row['A_Hqql_correct_mean']; B=row['B_Hqql_to_Tbl_mean']; C=row['C_Tbl_correct_mean']
        Af=row['A_Hqql_correct_freq']; Bf=row['B_Hqql_to_Tbl_freq']; Cf=row['C_Tbl_correct_freq']
        row['trigger_score']=(B-A)*Bf
        row['loss_score']=(A-B)*Af
        row['tbl_like_score']=Bf*(B-abs(B-C))
        row['anomaly_score']=Bf*abs(B-A)*abs(B-C)
        row['freq_trigger_score']=Bf-Af
        out.append(row)

    out_sorted=sorted(out, key=lambda r:(r['trigger_score'], r['freq_trigger_score']), reverse=True)
    wcsv(a.out_csv, out_sorted)
    Path(a.out_json).parent.mkdir(parents=True, exist_ok=True)
    Path(a.out_json).write_text(json.dumps({'ok':True,'raw_rows':raw_rows,'used_rows':used_rows,'dropped_pad':dropped_pad,'dropped_cls':dropped_cls,'rows':len(out_sorted),'counts':counts}, indent=2, ensure_ascii=False), encoding='utf-8')

    top_tr=out_sorted[:25]
    top_loss=sorted(out, key=lambda r:r['loss_score'], reverse=True)[:25]
    top_tbl=sorted(out, key=lambda r:r['tbl_like_score'], reverse=True)[:25]
    top_anom=sorted(out, key=lambda r:r['anomaly_score'], reverse=True)[:25]
    md='# PART_ATTENTION_CLEAN_RANK_V2\n\nClean post-rank over existing ParT top-K pair flows. Filters pad pairs and CLS-only paths, adds per-group occurrence counts/frequencies, and reranks trigger/loss/Tbl-like/anomaly paths.\n\n'
    md+=f'- raw rows: **{raw_rows}**\n- used rows: **{used_rows}**\n- dropped pad rows: **{dropped_pad}**\n- dropped CLS-only rows: **{dropped_cls}**\n- clean summary rows: **{len(out_sorted)}**\n\n'
    md+='## Top clean B>A triggers\n'+mdtab(['module','head','pair','A_mean','B_mean','C_mean','A_freq','B_freq','C_freq','score'], [[r['module'],r['head'],r['pair_role'],round(r['A_Hqql_correct_mean'],4),round(r['B_Hqql_to_Tbl_mean'],4),round(r['C_Tbl_correct_mean'],4),round(r['A_Hqql_correct_freq'],4),round(r['B_Hqql_to_Tbl_freq'],4),round(r['C_Tbl_correct_freq'],4),round(r['trigger_score'],6)] for r in top_tr])
    md+='\n## Top clean Hqql-loss paths\n'+mdtab(['module','head','pair','A_mean','B_mean','C_mean','A_freq','B_freq','score'], [[r['module'],r['head'],r['pair_role'],round(r['A_Hqql_correct_mean'],4),round(r['B_Hqql_to_Tbl_mean'],4),round(r['C_Tbl_correct_mean'],4),round(r['A_Hqql_correct_freq'],4),round(r['B_Hqql_to_Tbl_freq'],4),round(r['loss_score'],6)] for r in top_loss])
    md+='\n## Top clean Tbl-like paths\n'+mdtab(['module','head','pair','A_mean','B_mean','C_mean','B_freq','score'], [[r['module'],r['head'],r['pair_role'],round(r['A_Hqql_correct_mean'],4),round(r['B_Hqql_to_Tbl_mean'],4),round(r['C_Tbl_correct_mean'],4),round(r['B_Hqql_to_Tbl_freq'],4),round(r['tbl_like_score'],6)] for r in top_tbl])
    md+='\n## Top clean anomaly paths\n'+mdtab(['module','head','pair','A_mean','B_mean','C_mean','B_freq','score'], [[r['module'],r['head'],r['pair_role'],round(r['A_Hqql_correct_mean'],4),round(r['B_Hqql_to_Tbl_mean'],4),round(r['C_Tbl_correct_mean'],4),round(r['B_Hqql_to_Tbl_freq'],4),round(r['anomaly_score'],6)] for r in top_anom])
    Path(a.out_md).parent.mkdir(parents=True, exist_ok=True); Path(a.out_md).write_text(md, encoding='utf-8')
    print(json.dumps({'ok':True,'rows':len(out_sorted),'out_md':a.out_md}, indent=2))

if __name__=='__main__': main()
