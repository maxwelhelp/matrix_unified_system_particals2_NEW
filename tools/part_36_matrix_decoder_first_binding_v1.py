#!/usr/bin/env python3
import argparse, csv, json, re
from pathlib import Path
from collections import Counter, defaultdict


def fnum(x, d=0.0):
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
    with p.open(newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))


def load_json(path):
    p = Path(path)
    if not p.exists():
        return {}
    try:
        return json.loads(p.read_text(encoding='utf-8'))
    except Exception:
        return {}


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
    with p.open('w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=keys)
        w.writeheader()
        w.writerows(rows)


def write_json(path, obj):
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(obj, indent=2, ensure_ascii=False), encoding='utf-8')


def parse_tag_from_edges(path):
    name = Path(path).name
    tag = name.replace('part_pair_program_graph_', '').replace('_edges_v1.csv', '')
    m = re.match(r'rank(\d+)_([^_]+)_to_(.+)', tag)
    if not m:
        return tag, '', '', ''
    return tag, int(m.group(1)), 'label_' + m.group(2), 'label_' + m.group(3)


def parse_attention_pair(source):
    s = (source or '').replace('attention_pair:', '')
    if '|' in s:
        head_id, route = s.split('|', 1)
    else:
        head_id, route = s, ''
    if '<-' in route:
        query_role, key_role = route.split('<-', 1)
    else:
        query_role, key_role = route, ''
    module = head_id
    head = ''
    if '.h' in head_id:
        module, head = head_id.rsplit('.h', 1)
    return head_id, module, head, route, query_role, key_role


def route_family(role):
    if role in ('electron', 'muon'):
        return 'lepton'
    if role in ('charged_hadron', 'neutral_hadron'):
        return 'hadron'
    if role == 'photon':
        return 'photon'
    if role == 'CLS':
        return 'CLS'
    if role == 'pad':
        return 'pad'
    return 'other'


def physics_hypothesis(src_label, tgt_label, route, q, k):
    fq, fk = route_family(q), route_family(k)
    pair = f'{src_label}->{tgt_label}'
    if fq == 'hadron' and fk == 'hadron':
        return (f'{pair}: head reads hadron-hadron topology. Likely computes jet-substructure, neutral/charged energy flow, prong geometry, or fragmentation pattern used to separate hadronic classes.')
    if 'photon' in (fq, fk) and 'hadron' in (fq, fk):
        return (f'{pair}: head reads photon-hadron coupling. Likely uses electromagnetic fraction / neutral pion related shower structure as a class-evidence axis.')
    if fq == 'lepton' or fk == 'lepton':
        return (f'{pair}: head reads lepton-linked route. Likely detects semileptonic decay proxy, heavy-flavor/top contamination, or lepton-in-jet evidence.')
    if fq == 'CLS' or fk == 'CLS':
        return (f'{pair}: route uses CLS aggregation. Likely global event summary/readout rather than a local particle-pair operator.')
    return (f'{pair}: route is mixed/unknown family; keep as hypothesis until route-aware pseudocode and full trace confirm the physical meaning.')


def make_matrix_formula(head_id, route, src_label, tgt_label):
    return (f'PROGRAM[{head_id}, {route}, {src_label}->{tgt_label}] = '
            f'READ_ROUTE({route}) -> WRITE_RESIDUAL(head_slice) -> PROJECT_LOGIT({tgt_label}-{src_label})')


def load_full_trace(paths):
    rows = []
    for p in paths:
        rows.extend(read_csv(p))
    by = defaultdict(list)
    for r in rows:
        hid = r.get('head_id', '')
        if hid:
            by[hid].append(r)
    return by


def load_pseudo_rows(paths):
    rows = []
    for p in paths:
        rows.extend(read_csv(p))
    by = defaultdict(list)
    for r in rows:
        hid = r.get('head_id', '')
        if hid:
            by[hid].append(r)
    return by


def load_compiled_rules(path):
    obj = load_json(path)
    rules = obj.get('rules') or []
    by_head = defaultdict(list)
    by_head_route = defaultdict(list)
    for r in rules:
        module = r.get('module', '')
        head = str(r.get('head', ''))
        head_id = f'{module}.h{head}' if module and head else ''
        if head_id:
            by_head[head_id].append(r)
            by_head_route[(head_id, r.get('pair', ''))].append(r)
    return by_head, by_head_route


def best_full_trace(rows):
    if not rows:
        return {}
    def score(r):
        return abs(fnum(r.get('confusion_support_score'))) + abs(fnum(r.get('gradient_support_score'))) + abs(fnum(r.get('correct_damage_score')))
    return sorted(rows, key=score, reverse=True)[0]


def best_pseudo(rows):
    if not rows:
        return {}
    def score(r):
        vals = [r.get('route_aware_pseudocode', ''), r.get('refined_pseudocode', ''), r.get('pseudocode', '')]
        return max(len(x) for x in vals)
    return sorted(rows, key=score, reverse=True)[0]


def decode_status(full_row, pseudo_row, rule):
    has_full = bool(full_row)
    has_pseudo = bool(pseudo_row.get('route_aware_pseudocode') or pseudo_row.get('refined_pseudocode') or pseudo_row.get('pseudocode'))
    has_rule = bool(rule)
    if has_full and has_pseudo and has_rule:
        return 'DECODED'
    if has_full and (has_pseudo or has_rule):
        return 'PARTIAL_DECODE'
    if has_full:
        return 'PARTIAL_DECODE'
    return 'MISSING_DECODE'


def missing_fields(full_row, pseudo_row, rule):
    miss = []
    if not full_row:
        miss.append('matrix_program_full_trace_row')
    if not rule:
        miss.append('compiled_route_rule')
    if not (pseudo_row.get('route_aware_pseudocode') or pseudo_row.get('refined_pseudocode') or pseudo_row.get('pseudocode')):
        miss.append('route_aware_or_refined_pseudocode')
    return ';'.join(miss)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--edges-glob', default='reports/latest/tables/part_pair_program_graph_rank*_edges_v1.csv')
    ap.add_argument('--min-abs-weight', type=float, default=1e-3)
    ap.add_argument('--full-trace', default='reports/latest/tables/part_matrix_program_full_trace_real_contract_v1_database.csv,reports/latest/tables/part_matrix_program_full_trace_real_contract_v1_ranked.csv')
    ap.add_argument('--pseudo-db', default='reports/latest/tables/pseudocode_operation_database_v3.csv,reports/latest/tables/pseudocode_operation_database_v2.csv,reports/latest/tables/pseudocode_operation_database.csv')
    ap.add_argument('--compiled-rules-json', default='manifests/latest/part_real_contract_pseudocode_compiler_v1.json')
    ap.add_argument('--out-md', default='reports/latest/PART_MATRIX_DECODER_FIRST_ATLAS_V1.md')
    ap.add_argument('--out-csv', default='reports/latest/tables/part_matrix_decoder_first_atlas_v1.csv')
    ap.add_argument('--out-json', default='manifests/latest/part_matrix_decoder_first_atlas_v1.json')
    args = ap.parse_args()

    full_by_head = load_full_trace([x.strip() for x in args.full_trace.split(',') if x.strip()])
    pseudo_by_head = load_pseudo_rows([x.strip() for x in args.pseudo_db.split(',') if x.strip()])
    rules_by_head, rules_by_head_route = load_compiled_rules(args.compiled_rules_json)

    decoded = []
    for edge_path in sorted(Path('.').glob(args.edges_glob)):
        tag, rank, src_label, tgt_label = parse_tag_from_edges(edge_path)
        for e in read_csv(edge_path):
            if e.get('kind') != 'validated_pair_to_residual':
                continue
            weight = fnum(e.get('weight'))
            if abs(weight) < args.min_abs_weight:
                continue
            head_id, module, head, route, q, k = parse_attention_pair(e.get('source', ''))
            full_row = best_full_trace(full_by_head.get(head_id, []))
            pseudo_row = best_pseudo(pseudo_by_head.get(head_id, []))
            rule = None
            exact_rules = rules_by_head_route.get((head_id, route), [])
            if exact_rules:
                rule = exact_rules[0]
            elif rules_by_head.get(head_id):
                rule = rules_by_head[head_id][0]
            status = decode_status(full_row, pseudo_row, rule)
            pseudocode = pseudo_row.get('route_aware_pseudocode') or pseudo_row.get('refined_pseudocode') or pseudo_row.get('pseudocode') or (rule or {}).get('pseudocode', '')
            matrix_route = (rule or {}).get('matrix_route', '') or make_matrix_formula(head_id, route, src_label, tgt_label)
            matrix_summary = full_row.get('matrix_program_summary', '') or make_matrix_formula(head_id, route, src_label, tgt_label)
            physics = physics_hypothesis(src_label, tgt_label, route, q, k)
            decoded.append({
                'pair_rank': rank,
                'pair_tag': tag,
                'src_label': src_label,
                'tgt_label': tgt_label,
                'head_id': head_id,
                'module': module,
                'head': head,
                'route': route,
                'query_role': q,
                'key_role': k,
                'causal_B_delta': weight,
                'causal_B_flip': e.get('B_flip', ''),
                'causal_score': e.get('score', ''),
                'decode_status': status,
                'missing_fields': missing_fields(full_row, pseudo_row, rule),
                'matrix_program_summary': matrix_summary,
                'compiled_matrix_route': matrix_route,
                'pseudocode': pseudocode,
                'route_aware_pseudocode': pseudo_row.get('route_aware_pseudocode', ''),
                'refined_pseudocode': pseudo_row.get('refined_pseudocode', ''),
                'physics_interpretation': physics,
                'hypothesis': physics,
                'full_trace_diagnosis': full_row.get('diagnosis', ''),
                'full_trace_top_roles_B': full_row.get('B_Hqql_to_Tbl_top_roles', ''),
                'operation_db_route_role': pseudo_row.get('route_role', '') or pseudo_row.get('output_role', '') or pseudo_row.get('stage_role', ''),
            })

    decoded.sort(key=lambda r: (r['decode_status'] != 'DECODED', r['decode_status'] != 'PARTIAL_DECODE', -abs(fnum(r['causal_B_delta']))))
    counts = Counter(r['decode_status'] for r in decoded)
    write_csv(args.out_csv, decoded)
    write_json(args.out_json, {'ok': True, 'mechanisms': len(decoded), 'status_counts': dict(counts), 'rows': decoded[:200]})

    md = []
    md.append('# PART_MATRIX_DECODER_FIRST_ATLAS_V1\n\n')
    md.append('Decoder-first interpretation atlas. Pair atlas is used only to select validated mechanisms; final interpretation is the matrix-program / pseudocode / physics binding.\n\n')
    md.append(f'- mechanisms: **{len(decoded)}**\n')
    md.append(f'- status_counts: `{dict(counts)}`\n')
    md.append(f'- min_abs_weight: **{args.min_abs_weight}**\n\n')
    md.append('## Concrete decoded mechanisms\n')
    for i, r in enumerate(decoded[:40], 1):
        md.append(f"\n### {i}. rank{int(r['pair_rank']):03d} {r['src_label']} -> {r['tgt_label']} / `{r['head_id']}` / `{r['route']}`\n\n")
        md.append(f"- decode_status: **{r['decode_status']}**\n")
        if r['missing_fields']:
            md.append(f"- missing: `{r['missing_fields']}`\n")
        md.append(f"- causal_B_delta: **{fmt(r['causal_B_delta'])}**\n")
        md.append(f"- causal_B_flip: **{r['causal_B_flip']}**\n")
        md.append(f"- query_role: `{r['query_role']}`\n")
        md.append(f"- key_role: `{r['key_role']}`\n")
        md.append(f"- full_trace_diagnosis: `{r['full_trace_diagnosis']}`\n")
        md.append(f"- operation_db_role: `{r['operation_db_route_role']}`\n\n")
        md.append('**What it computes**\n\n')
        md.append(r['matrix_program_summary'] + '\n\n')
        md.append('**Compiled matrix route**\n\n```text\n' + r['compiled_matrix_route'] + '\n```\n\n')
        md.append('**Pseudocode**\n\n```python\n' + (r['pseudocode'] or '# MISSING_PSEUDOCODE') + '\n```\n\n')
        md.append('**Physics interpretation / hypothesis**\n\n')
        md.append(r['physics_interpretation'] + '\n')
    md.append('\n## Rule\n\nA mechanism is final only when it is DECODED or explicitly marked with the missing decoder fields. Gradients/patches/residual paths are evidence, not the interpretation itself.\n')
    Path(args.out_md).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out_md).write_text(''.join(md), encoding='utf-8')
    print(json.dumps({'ok': True, 'mechanisms': len(decoded), 'status_counts': dict(counts), 'out_md': args.out_md}, indent=2, ensure_ascii=False))


if __name__ == '__main__':
    main()
