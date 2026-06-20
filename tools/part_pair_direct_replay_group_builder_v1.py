#!/usr/bin/env python3
import argparse, csv, gc, json, re, sys
from pathlib import Path
from collections import Counter, defaultdict
import torch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from tools.part_attention_supertrace_real_contract_v1 import LABELS, load_model, build_batch, wcsv, wjson


def safe_label(x):
    return re.sub(r'[^A-Za-z0-9]+', '_', x.replace('label_', '')).strip('_')


def read_csv(path):
    with open(path, newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))


def mdtab(headers, rows):
    if not rows:
        return '_No rows._\n'
    return '\n'.join(['| ' + ' | '.join(headers) + ' |', '| ' + ' | '.join(['---'] * len(headers)) + ' |'] + ['| ' + ' | '.join(str(x) for x in r) + ' |' for r in rows]) + '\n'


def pick_pair(rows, rank, src_label, tgt_label):
    if src_label and tgt_label:
        for i, r in enumerate(rows, 1):
            if r.get('src_label') == src_label and r.get('tgt_label') == tgt_label:
                return i, r
        raise RuntimeError(f'pair not found: {src_label}->{tgt_label}')
    if rank < 1 or rank > len(rows):
        raise RuntimeError(f'bad rank {rank}; pairs={len(rows)}')
    return rank, rows[rank - 1]


def first_group(s):
    return (s or '').split(';')[0].strip()


def read_sources(path):
    out = {}
    for r in read_csv(path):
        g = r.get('group', '')
        if g:
            out[g] = r
    return out


def enough(out, groups, max_per_group):
    c = Counter(r['analysis_group'] for r in out)
    return all(c.get(g, 0) >= max_per_group for g in groups)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--atlas-pairs', default='reports/latest/tables/part_all_class_atlas_pairs_v1.csv')
    ap.add_argument('--atlas-sources', default='reports/latest/tables/part_all_class_atlas_sources_v1.csv')
    ap.add_argument('--rank', type=int, default=1)
    ap.add_argument('--src-label', default='')
    ap.add_argument('--tgt-label', default='')
    ap.add_argument('--network-file', default='external/particle_transformer/networks/example_ParticleTransformer_legacy.py')
    ap.add_argument('--checkpoint', default='external/particle_transformer/models/ParT_kinpid.pt')
    ap.add_argument('--data-config', default='external/particle_transformer/data/JetClass/JetClass_kinpid.yaml')
    ap.add_argument('--scan-limit', type=int, default=20000)
    ap.add_argument('--batch-size', type=int, default=64)
    ap.add_argument('--max-per-group', type=int, default=256)
    ap.add_argument('--device', default='cuda' if torch.cuda.is_available() else 'cpu')
    ap.add_argument('--out-prefix', default='')
    a = ap.parse_args()

    pairs = read_csv(a.atlas_pairs)
    sources = read_sources(a.atlas_sources)
    rank, pair = pick_pair(pairs, a.rank, a.src_label, a.tgt_label)
    src_label = pair['src_label']
    tgt_label = pair['tgt_label']
    src_group = first_group(pair.get('src_source_groups'))
    tgt_group = first_group(pair.get('tgt_source_groups'))
    if not src_group or not tgt_group:
        raise RuntimeError(f'pair rank {rank} is not ready: missing source groups')
    if src_group not in sources or tgt_group not in sources:
        raise RuntimeError(f'source groups missing in atlas sources: {src_group}, {tgt_group}')
    src_root = sources[src_group].get('source_root', '')
    tgt_root = sources[tgt_group].get('source_root', '')
    if not src_root or not tgt_root:
        raise RuntimeError(f'missing source roots for groups: {src_group}, {tgt_group}')
    src_idx = LABELS.index(src_label)
    tgt_idx = LABELS.index(tgt_label)

    out_tag = a.out_prefix or f"rank{rank:03d}_{safe_label(src_label)}_to_{safe_label(tgt_label)}"
    out_csv = f'reports/latest/tables/part_pair_groups_{out_tag}_v1.csv'
    out_json = f'manifests/latest/part_pair_groups_{out_tag}_v1.json'
    out_md = f'reports/latest/PART_PAIR_DIRECT_REPLAY_GROUPS_{out_tag}_V1.md'

    groups = ['A_src_correct', 'B_src_to_tgt', 'C_tgt_correct', 'D_tgt_to_src']
    device = torch.device(a.device)
    model, dc = load_model(a.network_file, a.checkpoint, a.data_config, device)
    out = []
    scanned = Counter()
    pred_counts = defaultdict(Counter)

    for source_group, source_root, true_label in [(src_group, src_root, src_label), (tgt_group, tgt_root, tgt_label)]:
        for start in range(0, a.scan_limit, a.batch_size):
            if enough(out, groups, a.max_per_group):
                break
            end = min(a.scan_limit, start + a.batch_size)
            probe_rows = []
            for entry_idx in range(start, end):
                probe_rows.append({
                    'analysis_group': 'probe',
                    'source_group': source_group,
                    'source_root': source_root,
                    'entry_idx': entry_idx,
                    'true_label': true_label,
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
                group = None
                if true_label == src_label:
                    if pred_label == src_label:
                        group = 'A_src_correct'
                    elif pred_label == tgt_label:
                        group = 'B_src_to_tgt'
                else:
                    if pred_label == tgt_label:
                        group = 'C_tgt_correct'
                    elif pred_label == src_label:
                        group = 'D_tgt_to_src'
                if group is None:
                    continue
                if sum(1 for r in out if r['analysis_group'] == group) >= a.max_per_group:
                    continue
                src_score = float(probs[i, src_idx])
                tgt_score = float(probs[i, tgt_idx])
                out.append({
                    'analysis_group': group,
                    'source_group': source_group,
                    'source_root': source_root,
                    'entry_idx': entry_idx,
                    'true_label': true_label,
                    'pred_label': pred_label,
                    'src_label': src_label,
                    'tgt_label': tgt_label,
                    'score_src': src_score,
                    'score_tgt': tgt_score,
                    'margin_tgt_minus_src': tgt_score - src_score,
                    'margin_src_minus_tgt': src_score - tgt_score,
                    'atlas_rank': rank,
                    'builder': 'pair_direct_legacy_replay',
                })
            del pts, fts, vec, msk, logits, probs
            if device.type == 'cuda':
                torch.cuda.empty_cache()
            gc.collect()

    counts = Counter(r['analysis_group'] for r in out)
    wcsv(out_csv, out)
    obj = {
        'ok': True,
        'atlas_rank': rank,
        'src_label': src_label,
        'tgt_label': tgt_label,
        'src_group': src_group,
        'tgt_group': tgt_group,
        'out_csv': out_csv,
        'scan_limit': a.scan_limit,
        'max_per_group': a.max_per_group,
        'counts': dict(counts),
        'scanned': dict(scanned),
        'pred_counts': {k: dict(v) for k, v in pred_counts.items()},
    }
    wjson(out_json, obj)

    rows = [[g, counts.get(g, 0)] for g in groups]
    md = []
    md.append(f'# PART_PAIR_DIRECT_REPLAY_GROUPS_{out_tag}_V1\n\n')
    md.append('Generic direct replay pair groups for all-class atlas. Builds A/B/C/D groups for an arbitrary `src_label -> tgt_label` pair using replay-consistent model forward.\n\n')
    md.append(f'- atlas_rank: **{rank}**\n')
    md.append(f'- src_label: `{src_label}` / src_group: `{src_group}`\n')
    md.append(f'- tgt_label: `{tgt_label}` / tgt_group: `{tgt_group}`\n')
    md.append(f'- scan_limit: **{a.scan_limit}**\n')
    md.append(f'- max_per_group: **{a.max_per_group}**\n')
    md.append(f'- output_csv: `{out_csv}`\n\n')
    md.append('## Group counts\n')
    md.append(mdtab(['group', 'selected'], rows))
    md.append('\n## Source scan counts\n')
    md.append(mdtab(['source_group', 'scanned', 'pred_counts'], [[k, scanned.get(k, 0), dict(pred_counts[k])] for k in [src_group, tgt_group]]))
    md.append('\n## Decision\n\n')
    if all(counts.get(g, 0) >= min(32, a.max_per_group) for g in groups):
        md.append('`PAIR_DIRECT_GROUPS_OK`: enough direct replay events for generic pair decoding.\n')
    else:
        md.append('`PAIR_DIRECT_GROUPS_WEAK`: some groups underfilled; increase scan limit or choose a higher-error pair.\n')
    Path(out_md).parent.mkdir(parents=True, exist_ok=True)
    Path(out_md).write_text(''.join(md), encoding='utf-8')
    print(''.join(md))

if __name__ == '__main__':
    main()
