#!/usr/bin/env python3
import argparse, csv, json, re, sys
from pathlib import Path
from collections import Counter, defaultdict

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import numpy as np
import uproot

from tools.part_attention_supertrace_real_contract_v1 import LABELS, find_tree, score_branches, group_from_output_name, read_manifest, wcsv, wjson

SOURCE_LABEL_HINTS = {
    'QCD': 'label_QCD',
    'HToBB': 'label_Hbb',
    'HToCC': 'label_Hcc',
    'HToGG': 'label_Hgg',
    'HToWW4Q': 'label_H4q',
    'HToWW2Q1L': 'label_Hqql',
    'ZToQQ': 'label_Zqq',
    'WToQQ': 'label_Wqq',
    'TTBarLep': 'label_Tbl',
    'TTBarHad': 'label_Tbqq',
    'TTBar': 'label_Tbqq',
}


def infer_true_label(group_name):
    for key, lab in SOURCE_LABEL_HINTS.items():
        if key.lower() in group_name.lower():
            return lab
    # fallback: if exact label suffix is in group name
    for lab in LABELS:
        short = lab.replace('label_', '')
        if short.lower() in group_name.lower():
            return lab
    return ''


def mdtab(headers, rows):
    if not rows:
        return '_No rows._\n'
    return '\n'.join(['| ' + ' | '.join(headers) + ' |', '| ' + ' | '.join(['---'] * len(headers)) + ' |'] + ['| ' + ' | '.join(str(x) for x in r) + ' |' for r in rows]) + '\n'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--pred-glob', default='reports/latest/part_weaver_predict_smoke_v3_*.root')
    ap.add_argument('--manifest', default='manifests/latest/part_weaver_predict_smoke_v3_args.txt')
    ap.add_argument('--top-pairs', type=int, default=20)
    ap.add_argument('--min-error', type=int, default=8)
    ap.add_argument('--out-pairs', default='reports/latest/tables/part_all_class_atlas_pairs_v1.csv')
    ap.add_argument('--out-sources', default='reports/latest/tables/part_all_class_atlas_sources_v1.csv')
    ap.add_argument('--out-md', default='reports/latest/PART_ALL_CLASS_ATLAS_PLANNER_V1.md')
    ap.add_argument('--out-json', default='manifests/latest/part_all_class_atlas_planner_v1.json')
    a = ap.parse_args()

    manifest = read_manifest(a.manifest)
    source_rows = []
    pair_counts = Counter()
    pair_margin_sum = defaultdict(float)
    pair_conf_sum = defaultdict(float)
    total_by_true = Counter()
    pred_by_true = defaultdict(Counter)

    files = sorted(Path('.').glob(a.pred_glob))
    for path in files:
        group = group_from_output_name(path)
        source_root = manifest.get(group, '')
        inferred = infer_true_label(group)
        with uproot.open(path) as rf:
            t = find_tree(rf)
            keys = list(t.keys())
            scores = score_branches(keys)
            if not scores:
                continue
            arr = t.arrays([x for x in LABELS if x in keys] + scores, library='np')
            S = np.stack([arr[x] for x in scores], axis=1)
            pred = S.argmax(axis=1)
            # Prefer true label branches when available, otherwise infer from file/group name.
            if all(lab in keys for lab in LABELS):
                Y = np.stack([arr[lab] for lab in LABELS], axis=1).argmax(axis=1)
                true_labels = [LABELS[int(i)] for i in Y]
            elif inferred:
                true_labels = [inferred] * len(pred)
            else:
                true_labels = [''] * len(pred)
        src_ok = bool(source_root)
        source_rows.append({
            'group': group,
            'prediction_root': str(path),
            'source_root': source_root,
            'source_root_available': int(src_ok),
            'inferred_true_label': inferred,
            'events': len(pred),
            'pred_counts': dict(Counter(LABELS[int(i)] for i in pred)),
        })
        for i, pl_idx in enumerate(pred):
            tl = true_labels[i]
            if not tl:
                continue
            pl = LABELS[int(pl_idx)]
            total_by_true[tl] += 1
            pred_by_true[tl][pl] += 1
            if tl == pl:
                continue
            key = (tl, pl)
            pair_counts[key] += 1
            pair_margin_sum[key] += float(S[i, LABELS.index(pl)] - S[i, LABELS.index(tl)])
            pair_conf_sum[key] += float(S[i, LABELS.index(pl)])

    pair_rows = []
    for (src, tgt), n in pair_counts.items():
        if n < a.min_error:
            continue
        src_group_candidates = [r for r in source_rows if r['inferred_true_label'] == src and r['source_root_available']]
        tgt_group_candidates = [r for r in source_rows if r['inferred_true_label'] == tgt and r['source_root_available']]
        pair_rows.append({
            'src_label': src,
            'tgt_label': tgt,
            'error_count': n,
            'src_total': total_by_true.get(src, 0),
            'error_rate_from_src': n / max(1, total_by_true.get(src, 0)),
            'mean_pred_minus_true_margin': pair_margin_sum[(src,tgt)] / max(1, n),
            'mean_tgt_conf': pair_conf_sum[(src,tgt)] / max(1, n),
            'src_source_groups': ';'.join(r['group'] for r in src_group_candidates[:4]),
            'tgt_source_groups': ';'.join(r['group'] for r in tgt_group_candidates[:4]),
            'has_src_root': int(bool(src_group_candidates)),
            'has_tgt_root': int(bool(tgt_group_candidates)),
            'ready_for_direct_pair_builder': int(bool(src_group_candidates and tgt_group_candidates)),
        })
    pair_rows.sort(key=lambda r: (r['ready_for_direct_pair_builder'], r['error_count'], r['mean_pred_minus_true_margin']), reverse=True)

    wcsv(a.out_sources, source_rows)
    wcsv(a.out_pairs, pair_rows)
    obj = {
        'ok': True,
        'prediction_files': len(files),
        'sources': len(source_rows),
        'pairs': len(pair_rows),
        'ready_pairs': sum(int(r['ready_for_direct_pair_builder']) for r in pair_rows),
        'top_pairs': pair_rows[:a.top_pairs],
        'source_rows': source_rows,
    }
    wjson(a.out_json, obj)

    md = []
    md.append('# PART_ALL_CLASS_ATLAS_PLANNER_V1\n\n')
    md.append('All-class atlas planner. It scans available prediction ROOT files, infers true/predicted class transitions, ranks class-pairs, and marks which pairs have enough source ROOT mapping for direct replay / full program graph decoding.\n\n')
    md.append(f'- prediction_files: **{len(files)}**\n')
    md.append(f'- sources: **{len(source_rows)}**\n')
    md.append(f'- candidate_pairs: **{len(pair_rows)}**\n')
    md.append(f'- ready_pairs: **{obj["ready_pairs"]}**\n')
    md.append(f'- min_error: **{a.min_error}**\n\n')
    md.append('## Top class-pair candidates\n')
    md.append(mdtab(['rank','src','tgt','errors','src_total','err_rate','mean_margin','src_groups','tgt_groups','ready'], [[i+1, r['src_label'], r['tgt_label'], r['error_count'], r['src_total'], f"{r['error_rate_from_src']:.4f}", f"{r['mean_pred_minus_true_margin']:.4f}", r['src_source_groups'], r['tgt_source_groups'], r['ready_for_direct_pair_builder']] for i,r in enumerate(pair_rows[:a.top_pairs])]))
    md.append('\n## Available sources\n')
    md.append(mdtab(['group','label','events','source_root_available','prediction_root'], [[r['group'], r['inferred_true_label'], r['events'], r['source_root_available'], r['prediction_root']] for r in source_rows]))
    md.append('\n## Decision\n\n')
    if obj['ready_pairs'] > 0:
        md.append('`ATLAS_PLANNER_OK`: at least one pair has both source and target source roots; next step can build direct replay pair groups.\n')
    else:
        md.append('`ATLAS_PLANNER_NEEDS_MORE_ROOTS`: prediction files exist, but source ROOT mapping is incomplete for direct replay pair groups. Generate/manifest more class source roots first.\n')
    Path(a.out_md).parent.mkdir(parents=True, exist_ok=True)
    Path(a.out_md).write_text(''.join(md), encoding='utf-8')
    print(json.dumps({'ok': True, 'pairs': len(pair_rows), 'ready_pairs': obj['ready_pairs'], 'out_md': a.out_md}, indent=2))

if __name__ == '__main__':
    main()
