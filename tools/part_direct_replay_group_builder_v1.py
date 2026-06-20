#!/usr/bin/env python3
import argparse, csv, gc, json, sys
from pathlib import Path
from collections import defaultdict, Counter

import torch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from tools.part_attention_supertrace_real_contract_v1 import LABELS, load_model, build_batch, wcsv, wjson

HQQL = LABELS.index('label_Hqql')
TBL = LABELS.index('label_Tbl')


def read_existing_sources(path):
    src = {}
    with open(path, newline='', encoding='utf-8') as f:
        for r in csv.DictReader(f):
            sg = r.get('source_group')
            sr = r.get('source_root')
            if sg and sr and sg not in src:
                src[sg] = sr
    return src


def enough(out, max_per_group):
    c = Counter(r['analysis_group'] for r in out)
    return all(c.get(g, 0) >= max_per_group for g in ['A_Hqql_correct', 'B_Hqql_to_Tbl', 'C_Tbl_correct', 'D_Tbl_to_Hqql'])


def mdtab(headers, rows):
    if not rows:
        return '_No rows._\n'
    return '\n'.join(['| ' + ' | '.join(headers) + ' |', '| ' + ' | '.join(['---'] * len(headers)) + ' |'] + ['| ' + ' | '.join(str(x) for x in r) + ' |' for r in rows]) + '\n'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--source-csv', default='reports/latest/tables/part_hqql_tbl_groups_real_contract_v1.csv')
    ap.add_argument('--network-file', default='external/particle_transformer/networks/example_ParticleTransformer_legacy.py')
    ap.add_argument('--checkpoint', default='external/particle_transformer/models/ParT_kinpid.pt')
    ap.add_argument('--data-config', default='external/particle_transformer/data/JetClass/JetClass_kinpid.yaml')
    ap.add_argument('--scan-limit', type=int, default=20000)
    ap.add_argument('--batch-size', type=int, default=64)
    ap.add_argument('--max-per-group', type=int, default=256)
    ap.add_argument('--device', default='cuda' if torch.cuda.is_available() else 'cpu')
    ap.add_argument('--out-csv', default='reports/latest/tables/part_hqql_tbl_groups_direct_replay_v1.csv')
    ap.add_argument('--out-json', default='manifests/latest/part_direct_replay_group_builder_v1.json')
    ap.add_argument('--out-md', default='reports/latest/PART_DIRECT_REPLAY_GROUP_BUILDER_V1.md')
    a = ap.parse_args()

    sources = read_existing_sources(a.source_csv)
    needed = ['HToWW2Q1L', 'TTBarLep']
    missing = [x for x in needed if x not in sources]
    if missing:
        raise RuntimeError(f'missing source roots for {missing} in {a.source_csv}')

    device = torch.device(a.device)
    model, dc = load_model(a.network_file, a.checkpoint, a.data_config, device)

    out = []
    scanned = Counter()
    pred_counts = defaultdict(Counter)

    for source_group in needed:
        source_root = sources[source_group]
        for start in range(0, a.scan_limit, a.batch_size):
            if enough(out, a.max_per_group):
                break
            end = min(a.scan_limit, start + a.batch_size)
            probe_rows = []
            for entry_idx in range(start, end):
                probe_rows.append({
                    'analysis_group': 'probe',
                    'source_group': source_group,
                    'source_root': source_root,
                    'entry_idx': entry_idx,
                    'true_label': 'label_Hqql' if source_group == 'HToWW2Q1L' else 'label_Tbl',
                    'pred_label': '',
                })
            pts, fts, vec, msk, meta = build_batch(probe_rows, device, dc)
            with torch.no_grad():
                logits = model(pts, fts, vec, msk).detach().cpu()
                probs = torch.softmax(logits.float(), dim=1)
            pred = probs.argmax(dim=1).tolist()
            for i, entry_idx in enumerate(range(start, end)):
                pred_label = LABELS[pred[i]]
                pred_counts[source_group][pred_label] += 1
                scanned[source_group] += 1
                if source_group == 'HToWW2Q1L':
                    if pred_label == 'label_Hqql':
                        group = 'A_Hqql_correct'
                    elif pred_label == 'label_Tbl':
                        group = 'B_Hqql_to_Tbl'
                    else:
                        continue
                    true_label = 'label_Hqql'
                else:
                    if pred_label == 'label_Tbl':
                        group = 'C_Tbl_correct'
                    elif pred_label == 'label_Hqql':
                        group = 'D_Tbl_to_Hqql'
                    else:
                        continue
                    true_label = 'label_Tbl'
                if sum(1 for r in out if r['analysis_group'] == group) >= a.max_per_group:
                    continue
                h = float(probs[i, HQQL])
                t = float(probs[i, TBL])
                out.append({
                    'analysis_group': group,
                    'source_group': source_group,
                    'source_root': source_root,
                    'entry_idx': entry_idx,
                    'true_label': true_label,
                    'pred_label': pred_label,
                    'score_Hqql': h,
                    'score_Tbl': t,
                    'margin_Tbl_minus_Hqql': t - h,
                    'margin_Hqql_minus_Tbl': h - t,
                    'builder': 'direct_legacy_replay',
                })
            del pts, fts, vec, msk, logits, probs
            if device.type == 'cuda':
                torch.cuda.empty_cache()
            gc.collect()

    counts = Counter(r['analysis_group'] for r in out)
    summary_rows = []
    for g in ['A_Hqql_correct', 'B_Hqql_to_Tbl', 'C_Tbl_correct', 'D_Tbl_to_Hqql']:
        summary_rows.append([g, counts.get(g, 0)])

    Path(a.out_csv).parent.mkdir(parents=True, exist_ok=True)
    Path(a.out_json).parent.mkdir(parents=True, exist_ok=True)
    wcsv(a.out_csv, out)
    obj = {
        'ok': True,
        'out_csv': a.out_csv,
        'scan_limit': a.scan_limit,
        'max_per_group': a.max_per_group,
        'counts': dict(counts),
        'scanned': dict(scanned),
        'pred_counts': {k: dict(v) for k, v in pred_counts.items()},
        'network_file': a.network_file,
        'checkpoint': a.checkpoint,
        'data_config': a.data_config,
    }
    wjson(a.out_json, obj)

    md = []
    md.append('# PART_DIRECT_REPLAY_GROUP_BUILDER_V1\n\n')
    md.append('Builds A/B/C/D Hqql/Tbl groups directly from reproducible legacy-wrapper forward, not from prediction ROOT row indices.\n\n')
    md.append(f'- network_file: `{a.network_file}`\n')
    md.append(f'- checkpoint: `{a.checkpoint}`\n')
    md.append(f'- data_config: `{a.data_config}`\n')
    md.append(f'- scan_limit: **{a.scan_limit}**\n')
    md.append(f'- max_per_group: **{a.max_per_group}**\n')
    md.append(f'- output csv: `{a.out_csv}`\n\n')
    md.append('## Group counts\n')
    md.append(mdtab(['group', 'selected'], summary_rows))
    md.append('\n## Source scan counts\n')
    md.append(mdtab(['source_group', 'scanned', 'pred_counts'], [[k, scanned.get(k, 0), dict(pred_counts[k])] for k in needed]))
    md.append('\n## Decision\n\n')
    if all(counts.get(g, 0) >= min(64, a.max_per_group) for g in ['A_Hqql_correct', 'B_Hqql_to_Tbl', 'C_Tbl_correct', 'D_Tbl_to_Hqql']):
        md.append('`DIRECT_REPLAY_GROUPS_OK`: use this CSV for supertrace/gate/patch. It is internally replay-consistent.\n')
    else:
        md.append('`DIRECT_REPLAY_GROUPS_WEAK`: rare error groups are underfilled; increase `DIRECT_SCAN_LIMIT`.\n')
    Path(a.out_md).write_text(''.join(md), encoding='utf-8')
    print(''.join(md))


if __name__ == '__main__':
    main()
