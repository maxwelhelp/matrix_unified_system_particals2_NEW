#!/usr/bin/env python3
import argparse, csv, json, re
from pathlib import Path
from collections import defaultdict, Counter


def f(x, d=0.0):
    try:
        if x is None or x == '':
            return d
        return float(x)
    except Exception:
        return d


def fmt(x):
    try:
        x = float(x)
    except Exception:
        return 'n/a'
    return f'{x:.3e}' if abs(x) > 0 and (abs(x) < 1e-3 or abs(x) > 1e4) else f'{x:.4f}'


def read_csv(path):
    p = Path(path)
    if not p.exists():
        return []
    with p.open(newline='', encoding='utf-8') as h:
        return list(csv.DictReader(h))


def write_csv(path, rows):
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        p.write_text('', encoding='utf-8')
        return
    keys = []
    for r in rows:
        for k in r:
            if k not in keys:
                keys.append(k)
    with p.open('w', newline='', encoding='utf-8') as h:
        w = csv.DictWriter(h, fieldnames=keys)
        w.writeheader()
        w.writerows(rows)


def mdtab(headers, rows):
    if not rows:
        return '_No rows._\n'
    lines = ['| ' + ' | '.join(headers) + ' |', '| ' + ' | '.join(['---'] * len(headers)) + ' |']
    for r in rows:
        lines.append('| ' + ' | '.join(str(x) for x in r) + ' |')
    return '\n'.join(lines) + '\n'


def parse_tag(path):
    name = Path(path).name
    tag = name.replace('part_pair_program_graph_', '').replace('_edges_v1.csv', '')
    m = re.match(r'rank(\d+)_([^_]+)_to_(.+)', tag)
    if not m:
        return tag, '', '', ''
    return tag, int(m.group(1)), 'label_' + m.group(2), 'label_' + m.group(3)


def parse_attention_source(src):
    src = src.replace('attention_pair:', '')
    if '|' in src:
        head, pair = src.split('|', 1)
    else:
        head, pair = src, ''
    q, k = '', ''
    if '<-' in pair:
        q, k = pair.split('<-', 1)
    return head, pair, q, k


def add_acc(acc, key, pair_tag, src_label, tgt_label, weight, score):
    a = acc[key]
    a['n'] += 1
    a['sum_weight'] += weight
    a['sum_abs_weight'] += abs(weight)
    a['sum_score'] += score
    a['pairs'].add(pair_tag)
    a['labels'].add(f'{src_label}->{tgt_label}')
    if abs(weight) > abs(a.get('best_weight', 0.0)):
        a['best_weight'] = weight
        a['best_pair_tag'] = pair_tag
        a['best_label_pair'] = f'{src_label}->{tgt_label}'


def acc_rows(acc, key_name):
    out = []
    for k, a in acc.items():
        n = max(1, a['n'])
        out.append({
            key_name: k,
            'n_edges': a['n'],
            'pair_graphs': len(a['pairs']),
            'label_pairs': ';'.join(sorted(a['labels'])),
            'mean_weight': a['sum_weight'] / n,
            'mean_abs_weight': a['sum_abs_weight'] / n,
            'mean_score': a['sum_score'] / n,
            'best_weight': a.get('best_weight', 0.0),
            'best_pair_tag': a.get('best_pair_tag', ''),
            'best_label_pair': a.get('best_label_pair', ''),
        })
    out.sort(key=lambda r: (r['pair_graphs'], abs(f(r['mean_abs_weight'])), abs(f(r['best_weight']))), reverse=True)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--edges-glob', default='reports/latest/tables/part_pair_program_graph_rank*_edges_v1.csv')
    ap.add_argument('--min-abs-pair-weight', type=float, default=1e-3,
                    help='Ignore near-zero validated_pair_to_residual edges in head/role summaries.')
    ap.add_argument('--min-abs-linear-weight', type=float, default=1e-6,
                    help='Ignore near-zero classifier linear edges in classifier-dim summary.')
    ap.add_argument('--out-md', default='reports/latest/PART_PAIR_ATLAS_HEAD_ROLE_SUMMARY_V1.md')
    ap.add_argument('--out-json', default='manifests/latest/part_pair_atlas_head_role_summary_v1.json')
    ap.add_argument('--out-heads', default='reports/latest/tables/part_pair_atlas_heads_v1.csv')
    ap.add_argument('--out-roles', default='reports/latest/tables/part_pair_atlas_roles_v1.csv')
    ap.add_argument('--out-queries', default='reports/latest/tables/part_pair_atlas_query_roles_v1.csv')
    ap.add_argument('--out-keys', default='reports/latest/tables/part_pair_atlas_key_roles_v1.csv')
    ap.add_argument('--out-dims', default='reports/latest/tables/part_pair_atlas_classifier_dims_v1.csv')
    a = ap.parse_args()

    head_acc = defaultdict(lambda: {'n':0,'sum_weight':0.0,'sum_abs_weight':0.0,'sum_score':0.0,'pairs':set(),'labels':set()})
    role_acc = defaultdict(lambda: {'n':0,'sum_weight':0.0,'sum_abs_weight':0.0,'sum_score':0.0,'pairs':set(),'labels':set()})
    q_acc = defaultdict(lambda: {'n':0,'sum_weight':0.0,'sum_abs_weight':0.0,'sum_score':0.0,'pairs':set(),'labels':set()})
    k_acc = defaultdict(lambda: {'n':0,'sum_weight':0.0,'sum_abs_weight':0.0,'sum_score':0.0,'pairs':set(),'labels':set()})
    dim_acc = defaultdict(lambda: {'n':0,'sum_weight':0.0,'sum_abs_weight':0.0,'sum_score':0.0,'pairs':set(),'labels':set()})
    pair_counts = Counter()
    skipped_pair_edges = 0
    kept_pair_edges = 0
    skipped_linear_edges = 0
    kept_linear_edges = 0

    edge_files = sorted(Path('.').glob(a.edges_glob))
    for ef in edge_files:
        tag, rank, src_label, tgt_label = parse_tag(ef)
        rows = read_csv(ef)
        pair_counts[f'{src_label}->{tgt_label}'] += 1
        for r in rows:
            kind = r.get('kind', '')
            w = f(r.get('weight'))
            score = f(r.get('score'))
            if kind == 'validated_pair_to_residual':
                if abs(w) < a.min_abs_pair_weight:
                    skipped_pair_edges += 1
                    continue
                kept_pair_edges += 1
                head, role_pair, q, k = parse_attention_source(r.get('source',''))
                if head:
                    add_acc(head_acc, head, tag, src_label, tgt_label, w, score)
                if role_pair:
                    add_acc(role_acc, role_pair, tag, src_label, tgt_label, w, score)
                if q:
                    add_acc(q_acc, q, tag, src_label, tgt_label, w, score)
                if k:
                    add_acc(k_acc, k, tag, src_label, tgt_label, w, score)
            elif kind == 'linear_direction':
                if abs(w) < a.min_abs_linear_weight:
                    skipped_linear_edges += 1
                    continue
                kept_linear_edges += 1
                dim = str(r.get('dim',''))
                if dim:
                    add_acc(dim_acc, dim, tag, src_label, tgt_label, w, 0.0)

    head_rows = acc_rows(head_acc, 'head_id')
    role_rows = acc_rows(role_acc, 'role_pair')
    q_rows = acc_rows(q_acc, 'query_role')
    k_rows = acc_rows(k_acc, 'key_role')
    dim_rows = acc_rows(dim_acc, 'classifier_dim')
    write_csv(a.out_heads, head_rows)
    write_csv(a.out_roles, role_rows)
    write_csv(a.out_queries, q_rows)
    write_csv(a.out_keys, k_rows)
    write_csv(a.out_dims, dim_rows)

    obj = {
        'ok': True,
        'pair_graphs': len(edge_files),
        'min_abs_pair_weight': a.min_abs_pair_weight,
        'min_abs_linear_weight': a.min_abs_linear_weight,
        'kept_pair_edges': kept_pair_edges,
        'skipped_pair_edges': skipped_pair_edges,
        'kept_linear_edges': kept_linear_edges,
        'skipped_linear_edges': skipped_linear_edges,
        'heads': len(head_rows),
        'role_pairs': len(role_rows),
        'classifier_dims': len(dim_rows),
        'top_heads': head_rows[:20],
        'top_role_pairs': role_rows[:20],
        'top_classifier_dims': dim_rows[:20],
    }
    Path(a.out_json).parent.mkdir(parents=True, exist_ok=True)
    Path(a.out_json).write_text(json.dumps(obj, indent=2, ensure_ascii=False), encoding='utf-8')

    md = []
    md.append('# PART_PAIR_ATLAS_HEAD_ROLE_SUMMARY_V1\n\n')
    md.append('Aggregates generated pair program graphs into a head/role/classifier-dimension atlas. This is a model-level summary over pair-specific program graphs, not a new model run. Near-zero pair edges are filtered so numerical no-op routes do not look universal.\n\n')
    md.append(f'- pair_graphs: **{len(edge_files)}**\n')
    md.append(f'- min_abs_pair_weight: **{a.min_abs_pair_weight}**\n')
    md.append(f'- kept_pair_edges: **{kept_pair_edges}**\n')
    md.append(f'- skipped_pair_edges: **{skipped_pair_edges}**\n')
    md.append(f'- unique_heads: **{len(head_rows)}**\n')
    md.append(f'- unique_role_pairs: **{len(role_rows)}**\n')
    md.append(f'- unique_classifier_dims: **{len(dim_rows)}**\n\n')
    md.append('## Universal / repeated heads\n')
    md.append(mdtab(['rank','head','graphs','edges','mean_abs','best_weight','best_pair'], [[i+1,r['head_id'],r['pair_graphs'],r['n_edges'],fmt(r['mean_abs_weight']),fmt(r['best_weight']),r['best_label_pair']] for i,r in enumerate(head_rows[:30])]))
    md.append('\n## Repeated causal role pairs\n')
    md.append(mdtab(['rank','role_pair','graphs','edges','mean_abs','best_weight','best_pair'], [[i+1,r['role_pair'],r['pair_graphs'],r['n_edges'],fmt(r['mean_abs_weight']),fmt(r['best_weight']),r['best_label_pair']] for i,r in enumerate(role_rows[:30])]))
    md.append('\n## Query roles\n')
    md.append(mdtab(['rank','query_role','graphs','edges','mean_abs','best_weight','best_pair'], [[i+1,r['query_role'],r['pair_graphs'],r['n_edges'],fmt(r['mean_abs_weight']),fmt(r['best_weight']),r['best_label_pair']] for i,r in enumerate(q_rows[:20])]))
    md.append('\n## Key roles\n')
    md.append(mdtab(['rank','key_role','graphs','edges','mean_abs','best_weight','best_pair'], [[i+1,r['key_role'],r['pair_graphs'],r['n_edges'],fmt(r['mean_abs_weight']),fmt(r['best_weight']),r['best_label_pair']] for i,r in enumerate(k_rows[:20])]))
    md.append('\n## Shared classifier dimensions\n')
    md.append(mdtab(['rank','dim','graphs','mean_abs_W','best_W','best_pair'], [[i+1,r['classifier_dim'],r['pair_graphs'],fmt(r['mean_abs_weight']),fmt(r['best_weight']),r['best_label_pair']] for i,r in enumerate(dim_rows[:30])]))
    md.append('\n## Interpretation\n\n')
    md.append('- Heads with `graphs > 1` and non-trivial edge weight are reusable mechanisms across multiple class-pairs.\n')
    md.append('- Role pairs with `graphs > 1` are repeated physical read routes after filtering numerical no-op edges.\n')
    md.append('- Classifier dims with `graphs > 1` are shared logit axes reused by multiple pair decisions.\n')
    md.append('- Pair-specific rows with high `best_weight` are local mechanisms, not universal ones.\n')
    Path(a.out_md).parent.mkdir(parents=True, exist_ok=True)
    Path(a.out_md).write_text(''.join(md), encoding='utf-8')
    print(json.dumps({'ok': True, 'pair_graphs': len(edge_files), 'heads': len(head_rows), 'role_pairs': len(role_rows), 'kept_pair_edges': kept_pair_edges, 'skipped_pair_edges': skipped_pair_edges, 'out_md': a.out_md}, indent=2))

if __name__ == '__main__':
    main()
