#!/usr/bin/env python3
import argparse, csv, json, re
from pathlib import Path
from collections import defaultdict, Counter


def fnum(x, default=0.0):
    try:
        if x is None or x == '':
            return default
        return float(x)
    except Exception:
        return default


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


def write_csv(path, rows):
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        p.write_text('', encoding='utf-8')
        return
    fields = []
    for r in rows:
        for k in r.keys():
            if k not in fields:
                fields.append(k)
    with p.open('w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for r in rows:
            w.writerow(r)


def write_json(path, obj):
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(obj, indent=2, ensure_ascii=False), encoding='utf-8')


def mdtab(headers, rows):
    if not rows:
        return '_No rows._\n'
    lines = ['| ' + ' | '.join(headers) + ' |', '| ' + ' | '.join(['---'] * len(headers)) + ' |']
    for r in rows:
        lines.append('| ' + ' | '.join(str(x) for x in r) + ' |')
    return '\n'.join(lines) + '\n'


def head_from_bundle_name(bundle):
    # head_output_zero_mod.blocks.7.attn_h3 -> mod.blocks.7.attn.h3
    if not bundle.startswith('head_output_zero_'):
        return ''
    rest = bundle.replace('head_output_zero_', '')
    if '_h' not in rest:
        return ''
    mod, h = rest.rsplit('_h', 1)
    return f'{mod}.h{h}'


def module_head_from_id(head_id):
    if '.h' not in head_id:
        return head_id, ''
    mod, h = head_id.rsplit('.h', 1)
    return mod, h


def rule_head_id(r):
    mod = r.get('module', '')
    head = r.get('head', '')
    if mod == '' or head == '':
        return ''
    return f'{mod}.h{head}'


def rule_pair(r):
    return r.get('pair_role') or r.get('route') or r.get('pair') or ''


def classify(row):
    bw = fnum(row.get('B_write_dot_grad'))
    ba = fnum(row.get('B_AxGrad'))
    bundle_dm = fnum(row.get('bundle_best_B_delta_margin'), 999.0)
    bundle_flip = fnum(row.get('bundle_best_B_delta_tbl_pred'), 0.0)
    grad = fnum(row.get('head_grad_signed_abs'))
    if bundle_dm < -0.03 or bundle_flip < 0:
        return 'causal_candidate'
    if bw > 0.02 or ba > 0.02:
        return 'B_Tbl_push_read_write'
    if bw < -0.02 or ba < -0.02:
        return 'B_Tbl_resist_or_protective_read_write'
    if grad > 0.05 and fnum(row.get('B_abs_write_dot_grad')) > 0.02:
        return 'high_gradient_write_node'
    if fnum(row.get('compiled_rule_count')) > 0:
        return 'rule_supported_weak_write'
    return 'weak_or_distributed'


def mechanism_text(row):
    head = row['head_id']
    pair = row['pair_role']
    bw = fnum(row.get('B_write_dot_grad'))
    ba = fnum(row.get('B_AxGrad'))
    sign = 'pushes B toward Tbl' if (bw > 0 or ba > 0) else 'resists Tbl / protective' if (bw < 0 or ba < 0) else 'mixed/weak'
    routes = row.get('compiled_routes', '')
    causal = ''
    if row.get('bundle_best_B_delta_margin', '') != '':
        causal = f" bundle_B_delta_margin={fmt(row.get('bundle_best_B_delta_margin'))}, bundle_B_delta_tbl_pred={fmt(row.get('bundle_best_B_delta_tbl_pred'))}."
    return f"{head} uses {pair}; natural A×grad={fmt(ba)}, value/write={fmt(bw)} so it {sign}.{causal} Routes: {routes[:160]}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--nat-summary', default='reports/latest/tables/part_natural_attention_manual_grad_real_contract_v1_summary.csv')
    ap.add_argument('--write-summary', default='reports/latest/tables/part_value_write_grad_real_contract_v1_summary.csv')
    ap.add_argument('--head-grad', default='reports/latest/tables/part_full_all_head_supertrace_head_gradients_v1.csv')
    ap.add_argument('--rules-csv', default='reports/latest/tables/part_rule_gate_join_real_contract_v1.csv')
    ap.add_argument('--bundle-csv', default='reports/latest/tables/part_bundle_causal_patch_real_contract_v1.csv')
    ap.add_argument('--bundle-sweep-csv', default='reports/latest/tables/part_bundle_causal_sweep_summary_v1.csv')
    ap.add_argument('--out-md', default='reports/latest/PART_DISCOVERY_CANDIDATES_REAL_CONTRACT_V1.md')
    ap.add_argument('--out-csv', default='reports/latest/tables/part_discovery_candidates_real_contract_v1.csv')
    ap.add_argument('--out-json', default='manifests/latest/part_discovery_candidates_real_contract_v1.json')
    args = ap.parse_args()

    nat_rows = read_csv(args.nat_summary)
    write_rows = read_csv(args.write_summary)
    head_grad_rows = read_csv(args.head_grad)
    rule_rows = read_csv(args.rules_csv)
    bundle_rows = read_csv(args.bundle_csv)
    sweep_rows = read_csv(args.bundle_sweep_csv)

    nat = {}
    for r in nat_rows:
        if r.get('objective') in ('B_tbl_minus_hqql', 'signed_hqql_tbl'):
            key = (r.get('objective'), r.get('head_id'), r.get('pair_role'))
            nat[key] = r

    # Start candidates from value/write rows; this is the strongest read->write evidence.
    candidates = {}
    for r in write_rows:
        obj = r.get('objective')
        if obj not in ('B_tbl_minus_hqql', 'signed_hqql_tbl'):
            continue
        head_id = r.get('head_id', '')
        pair = r.get('pair_role', '')
        if not head_id or not pair:
            continue
        key = (head_id, pair)
        # Prefer direct B objective, fallback signed.
        if key in candidates and candidates[key].get('objective') == 'B_tbl_minus_hqql':
            continue
        if key in candidates and obj != 'B_tbl_minus_hqql':
            continue
        c = {
            'head_id': head_id,
            'pair_role': pair,
            'objective': obj,
            'B_mean_A': r.get('B_mean_A', ''),
            'B_write_dot_grad': r.get('B_write_dot_grad', ''),
            'B_abs_write_dot_grad': r.get('B_abs_write_dot_grad', ''),
            'B_value_norm': r.get('B_value_norm', ''),
            'B_context_grad_norm': r.get('B_context_grad_norm', ''),
            'B_minus_A_write': r.get('B_minus_A_write', ''),
            'B_minus_C_write': r.get('B_minus_C_write', ''),
            'write_support_score': r.get('support_score', ''),
        }
        nr = nat.get((obj, head_id, pair)) or nat.get(('B_tbl_minus_hqql', head_id, pair)) or nat.get(('signed_hqql_tbl', head_id, pair)) or {}
        c.update({
            'B_AxGrad': nr.get('B_mean_AxGrad', ''),
            'B_minus_A_AxGrad': nr.get('B_minus_A_AxGrad', ''),
            'B_minus_C_AxGrad': nr.get('B_minus_C_AxGrad', ''),
            'attention_support_score': nr.get('support_score', ''),
        })
        candidates[key] = c

    # Head-level gradients from full all-head supertrace.
    grad_by_head = defaultdict(dict)
    for r in head_grad_rows:
        hid = r.get('head_id', '')
        obj = r.get('objective', '')
        if hid and obj:
            grad_by_head[hid][obj] = r

    # Compiled pseudocode/rules.
    rules_by_head = defaultdict(list)
    for r in rule_rows:
        hid = rule_head_id(r)
        if hid:
            rules_by_head[hid].append(r)

    # Bundle causal evidence.
    bundle_by_head = defaultdict(list)
    for r in bundle_rows:
        hid = head_from_bundle_name(r.get('bundle', ''))
        if hid:
            bundle_by_head[hid].append(r)
    sweep_by_bundle = {r.get('bundle', ''): r for r in sweep_rows}

    out = []
    for (hid, pair), c in candidates.items():
        g_signed = grad_by_head.get(hid, {}).get('signed_hqql_tbl', {})
        g_pred = grad_by_head.get(hid, {}).get('pred_logit', {})
        rs = rules_by_head.get(hid, [])
        exact_pair_rules = [r for r in rs if rule_pair(r) == pair]
        bundles = bundle_by_head.get(hid, [])
        best_dm = ''
        best_flip = ''
        if bundles:
            best_dm = min(fnum(r.get('B_Hqql_to_Tbl_delta_margin')) for r in bundles)
            best_flip = min(fnum(r.get('B_Hqql_to_Tbl_delta_tbl_pred')) for r in bundles)
        c['module'], c['head'] = module_head_from_id(hid)
        c['head_grad_signed'] = g_signed.get('grad', '')
        c['head_grad_signed_abs'] = g_signed.get('abs_grad', '')
        c['head_grad_pred_logit'] = g_pred.get('grad', '')
        c['head_grad_pred_logit_abs'] = g_pred.get('abs_grad', '')
        c['compiled_rule_count'] = len(rs)
        c['exact_pair_rule_count'] = len(exact_pair_rules)
        c['compiled_routes'] = ';'.join((rule_pair(r) or '') for r in rs[:10])
        c['bundle_evidence_count'] = len(bundles)
        c['bundle_best_B_delta_margin'] = best_dm
        c['bundle_best_B_delta_tbl_pred'] = best_flip
        # scoring: evidence agreement, not just one metric.
        abs_write = fnum(c.get('B_abs_write_dot_grad'))
        abs_attn = abs(fnum(c.get('B_AxGrad')))
        grad = fnum(c.get('head_grad_signed_abs'))
        rule_bonus = min(0.15, 0.02 * len(rs)) + min(0.10, 0.05 * len(exact_pair_rules))
        causal_bonus = 0.0
        if best_dm != '':
            causal_bonus += max(0.0, -fnum(best_dm)) * 3.0
        if best_flip != '':
            causal_bonus += max(0.0, -fnum(best_flip)) * 3.0
        c['evidence_score'] = abs_write + abs_attn + 0.25 * grad + rule_bonus + causal_bonus
        c['diagnosis'] = classify(c)
        c['mechanism_summary'] = mechanism_text(c)
        out.append(c)

    out.sort(key=lambda r: fnum(r.get('evidence_score')), reverse=True)
    write_csv(args.out_csv, out)
    counts = Counter(r['diagnosis'] for r in out)
    summary = {
        'ok': True,
        'candidates': len(out),
        'diagnosis_counts': dict(counts),
        'inputs': {
            'nat_summary': args.nat_summary,
            'write_summary': args.write_summary,
            'head_grad': args.head_grad,
            'rules_csv': args.rules_csv,
            'bundle_csv': args.bundle_csv,
            'bundle_sweep_csv': args.bundle_sweep_csv,
        },
        'top': out[:40],
    }
    write_json(args.out_json, summary)

    top_causal = [r for r in out if r['diagnosis'] == 'causal_candidate'][:20]
    top_push = [r for r in out if r['diagnosis'] == 'B_Tbl_push_read_write'][:20]
    top_resist = [r for r in out if r['diagnosis'] == 'B_Tbl_resist_or_protective_read_write'][:20]
    top_all = out[:30]

    md = ['# PART_DISCOVERY_CANDIDATES_REAL_CONTRACT_V1\n\n',
          'End-to-end discovery candidates for ParT Hqql/Tbl. This report joins natural attention `A×grad`, value/write contribution, all-head gate gradients, compiled pseudocode routes, and bundle/zero-head causal evidence into one ranked mechanism table.\n\n',
          f'- candidates: **{len(out)}**\n',
          f'- diagnosis_counts: `{dict(counts)}`\n',
          f'- natural_attention: `{args.nat_summary}`\n',
          f'- value_write: `{args.write_summary}`\n',
          f'- all_head_grad: `{args.head_grad}`\n',
          f'- rules: `{args.rules_csv}`\n',
          f'- bundle: `{args.bundle_csv}`\n\n']

    headers = ['rank','diagnosis','head','pair','score','B_AxGrad','B_write','abs_write','grad_signed','rules','bundle_dm','bundle_flip','summary']
    def row_pack(rows):
        return [[i+1, r['diagnosis'], r['head_id'], r['pair_role'], fmt(r['evidence_score']), fmt(r.get('B_AxGrad')), fmt(r.get('B_write_dot_grad')), fmt(r.get('B_abs_write_dot_grad')), fmt(r.get('head_grad_signed')), r.get('compiled_rule_count'), fmt(r.get('bundle_best_B_delta_margin')), fmt(r.get('bundle_best_B_delta_tbl_pred')), r.get('mechanism_summary','')[:220]] for i, r in enumerate(rows)]

    md += ['## Top candidates overall\n', mdtab(headers, row_pack(top_all)), '\n']
    md += ['## Causal candidates\n', mdtab(headers, row_pack(top_causal)), '\n']
    md += ['## B→Tbl push candidates\n', mdtab(headers, row_pack(top_push)), '\n']
    md += ['## B→Tbl resist/protect candidates\n', mdtab(headers, row_pack(top_resist)), '\n']
    md += ['## Reading\n\n',
           '- `B_AxGrad`: real natural attention mass times gradient. This is read-side importance.\n',
           '- `B_write`: `A[q,k] * dot(V[k], grad_context[q])`. This is write-side contribution.\n',
           '- `rules`: compiled pseudocode/route evidence attached to the same head.\n',
           '- `bundle_dm` / `bundle_flip`: causal intervention evidence when available.\n',
           '- Strong mechanism = same head/pair has read-side evidence, write-side evidence, head gradient, route/pseudocode support, and causal/bundle effect.\n']
    Path(args.out_md).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out_md).write_text(''.join(md), encoding='utf-8')
    print(json.dumps({'ok': True, 'candidates': len(out), 'out_md': args.out_md}, indent=2))


if __name__ == '__main__':
    main()
