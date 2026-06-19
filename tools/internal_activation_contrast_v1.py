#!/usr/bin/env python3
import argparse, csv, json, math
from pathlib import Path
from collections import defaultdict, Counter


def readcsv(path):
    path = Path(path)
    if not path.exists():
        return []
    with path.open('r', encoding='utf-8') as f:
        return list(csv.DictReader(f))


def wcsv(path, rows):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    keys, seen = [], set()
    for r in rows:
        for k in r:
            if k not in seen:
                keys.append(k)
                seen.add(k)
    with path.open('w', encoding='utf-8', newline='') as f:
        wr = csv.DictWriter(f, fieldnames=keys)
        wr.writeheader()
        for r in rows:
            wr.writerow({k: r.get(k, '') for k in keys})


def wjson(path, obj):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, ensure_ascii=False), encoding='utf-8')


def fnum(x, d=0.0):
    try:
        v = float(x)
        return v if math.isfinite(v) else d
    except Exception:
        return d


def fmt(x):
    try:
        return f'{float(x):.4f}'
    except Exception:
        return 'n/a'


def mdtab(headers, rows):
    if not rows:
        return '_No rows._\n'
    out = ['| ' + ' | '.join(headers) + ' |', '| ' + ' | '.join(['---'] * len(headers)) + ' |']
    for r in rows:
        out.append('| ' + ' | '.join(str(x).replace('\n', ' ') for x in r) + ' |')
    return '\n'.join(out) + '\n'


def mean(xs, key):
    vals = [fnum(x.get(key)) for x in xs if x.get(key, '') != '']
    return sum(vals) / len(vals) if vals else 0.0


def std_effect(a, b, key):
    va = [fnum(x.get(key)) for x in a if x.get(key, '') != '']
    vb = [fnum(x.get(key)) for x in b if x.get(key, '') != '']
    if not va or not vb:
        return 0.0
    ma, mb = sum(va)/len(va), sum(vb)/len(vb)
    sa = math.sqrt(sum((x-ma)**2 for x in va) / max(1, len(va)-1))
    sb = math.sqrt(sum((x-mb)**2 for x in vb) / max(1, len(vb)-1))
    return (mb - ma) / (math.sqrt((sa*sa + sb*sb)/2) + 1e-9)


def group_phase1(phase_rows, iso_thr):
    A, B = set(), set()
    for r in phase_rows:
        if r.get('true_label') != 'label_Hqql':
            continue
        if fnum(r.get('particle0_iso_pt_ratio')) < iso_thr:
            continue
        ei = int(fnum(r.get('event_index'), -1))
        if r.get('group') == 'Hqql_correct':
            A.add(ei)
        elif r.get('group') == 'Hqql_to_Tbl':
            B.add(ei)
    return A, B


def group_tbl_correct(super_events):
    C = set()
    for r in super_events:
        if r.get('true_label') == 'label_Tbl' and r.get('pred_label') == 'label_Tbl':
            C.add(int(fnum(r.get('event_idx'), -1)))
    return C


def particle_group_summary(parts, groups):
    rows = []
    for name, ids in groups.items():
        xs = [r for r in parts if int(fnum(r.get('event_idx'), -1)) in ids]
        rows.append({
            'group': name,
            'events': len(ids),
            'particle_rows': len(xs),
            'mean_super_score': mean(xs, 'super_score'),
            'mean_pt': mean(xs, 'pt'),
            'mean_deltaR_from_axis': mean(xs, 'deltaR_from_axis'),
            'mean_isMuon': mean(xs, 'part_isMuon'),
            'mean_isElectron': mean(xs, 'part_isElectron'),
            'mean_isPhoton': mean(xs, 'part_isPhoton'),
            'mean_isChargedHadron': mean(xs, 'part_isChargedHadron'),
            'mean_isNeutralHadron': mean(xs, 'part_isNeutralHadron'),
        })
    return rows


def particle_contrasts(parts, A, B, C):
    groups = {
        'A_protected_highiso': [r for r in parts if int(fnum(r.get('event_idx'), -1)) in A],
        'B_confused_highiso': [r for r in parts if int(fnum(r.get('event_idx'), -1)) in B],
        'C_Tbl_correct': [r for r in parts if int(fnum(r.get('event_idx'), -1)) in C],
    }
    feats = ['super_score','pt','deltaR_from_axis','part_charge','part_isMuon','part_isElectron','part_isPhoton','part_isChargedHadron','part_isNeutralHadron']
    rows = []
    for f in feats:
        rows.append({
            'feature': f,
            'A_mean': mean(groups['A_protected_highiso'], f),
            'B_mean': mean(groups['B_confused_highiso'], f),
            'C_mean': mean(groups['C_Tbl_correct'], f),
            'B_minus_A_effect': std_effect(groups['A_protected_highiso'], groups['B_confused_highiso'], f),
            'B_minus_C_effect': std_effect(groups['C_Tbl_correct'], groups['B_confused_highiso'], f),
            'interpretation': 'particle-level supertrace contrast; not full head activation',
        })
    return sorted(rows, key=lambda r: abs(r['B_minus_A_effect']), reverse=True)


def head_priority(head_grad, class_grad, head_trace):
    rows = []
    trace_by_head = {r.get('head_id'): r for r in head_trace}
    for r in head_grad:
        hid = r.get('head_id')
        tr = trace_by_head.get(hid, {})
        rows.append({
            'head_id': hid,
            'layer': r.get('layer'),
            'channels': r.get('channels'),
            'global_abs_grad': fnum(r.get('abs_grad')),
            'activation_mean_abs': fnum(tr.get('activation_mean_abs')),
            'top_activation_class': tr.get('top_activation_class',''),
            'semantic_axis': tr.get('semantic_axis',''),
            'output_interpretation': tr.get('output_interpretation',''),
            'priority_source': 'all_head_gate_gradients + head_output_trace',
        })
    # Add class-specific rows for Hqql/Tbl as separate signal.
    for r in class_grad:
        if r.get('class_label') in ('label_Hqql','label_Tbl'):
            hid = r.get('head_id')
            tr = trace_by_head.get(hid, {})
            rows.append({
                'head_id': hid,
                'layer': r.get('layer'),
                'channels': r.get('channels'),
                'global_abs_grad': '',
                'class_label': r.get('class_label'),
                'class_rank': r.get('rank'),
                'class_abs_grad': fnum(r.get('abs_grad')),
                'activation_mean_abs': fnum(tr.get('activation_mean_abs')),
                'top_activation_class': tr.get('top_activation_class',''),
                'semantic_axis': tr.get('semantic_axis',''),
                'output_interpretation': tr.get('output_interpretation',''),
                'priority_source': 'class_specific_head_gradients + head_output_trace',
            })
    return sorted(rows, key=lambda r: fnum(r.get('class_abs_grad', r.get('global_abs_grad', 0))), reverse=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--phase1-events', default='reports/latest/tables/hqql_tbl_confusion_physics_events.csv')
    ap.add_argument('--super-events', default='reports/latest/tables/all_head_supertrace_events.csv')
    ap.add_argument('--super-particles', default='reports/latest/tables/all_head_supertrace_particles.csv')
    ap.add_argument('--head-gradients', default='reports/latest/tables/all_head_gate_gradients.csv')
    ap.add_argument('--class-gradients', default='reports/latest/tables/class_specific_head_gradients.csv')
    ap.add_argument('--head-trace', default='reports/latest/tables/head_output_trace.csv')
    ap.add_argument('--isolation-threshold', type=float, default=0.30)
    ap.add_argument('--out-md', default='reports/latest/INTERNAL_ACTIVATION_CONTRAST_V1.md')
    ap.add_argument('--out-groups', default='reports/latest/tables/internal_activation_contrast_v1_group_inventory.csv')
    ap.add_argument('--out-particles', default='reports/latest/tables/internal_activation_contrast_v1_particle_contrasts.csv')
    ap.add_argument('--out-heads', default='reports/latest/tables/internal_activation_contrast_v1_head_priorities.csv')
    ap.add_argument('--out-json', default='manifests/latest/internal_activation_contrast_v1.json')
    args = ap.parse_args()

    phase = readcsv(args.phase1_events)
    super_events = readcsv(args.super_events)
    parts = readcsv(args.super_particles)
    head_grad = readcsv(args.head_gradients)
    class_grad = readcsv(args.class_gradients)
    head_trace = readcsv(args.head_trace)

    A, B = group_phase1(phase, args.isolation_threshold)
    C = group_tbl_correct(super_events)
    groups = {'A_protected_highiso': A, 'B_confused_highiso': B, 'C_Tbl_correct_supertrace': C}
    group_rows = particle_group_summary(parts, groups)
    pcontrasts = particle_contrasts(parts, A, B, C)
    heads = head_priority(head_grad, class_grad, head_trace)

    wcsv(args.out_groups, group_rows)
    wcsv(args.out_particles, pcontrasts)
    wcsv(args.out_heads, heads)
    wjson(args.out_json, {
        'ok': True,
        'mode': 'V0_reader_from_existing_tables',
        'limitation': 'existing tables contain head priorities and particle supertrace, but not full per-event x head activation means',
        'A_protected_highiso_events': len(A),
        'B_confused_highiso_events': len(B),
        'C_Tbl_correct_supertrace_events': len(C),
        'next_required': 'run lightweight extractor for A/B/C event-level L1/L2 activation means if full activation table is absent',
    })

    md = [
        '# INTERNAL_ACTIVATION_CONTRAST_V1\n\n',
        'V0 reader over existing internal trace tables. This is not yet full per-event x head activation contrast. It inventories A/B/C groups, particle-level supertrace contrasts, and head priorities.\n\n',
        '## Group inventory\n',
        mdtab(['group','events','particle_rows','mean_super_score','mean_pt','mean_deltaR','muon','electron','photon','charged_hadron','neutral_hadron'], [[r['group'], r['events'], r['particle_rows'], fmt(r['mean_super_score']), fmt(r['mean_pt']), fmt(r['mean_deltaR_from_axis']), fmt(r['mean_isMuon']), fmt(r['mean_isElectron']), fmt(r['mean_isPhoton']), fmt(r['mean_isChargedHadron']), fmt(r['mean_isNeutralHadron'])] for r in group_rows]),
        '\n## Particle-level contrasts B vs A/C\n',
        mdtab(['feature','A_mean','B_mean','C_mean','B-A effect','B-C effect'], [[r['feature'], fmt(r['A_mean']), fmt(r['B_mean']), fmt(r['C_mean']), fmt(r['B_minus_A_effect']), fmt(r['B_minus_C_effect'])] for r in pcontrasts]),
        '\n## Head priorities for direct extraction\n',
        mdtab(['head','layer','channels','class','class_grad','global_grad','semantic_axis','top_class'], [[r.get('head_id',''), r.get('layer',''), r.get('channels',''), r.get('class_label',''), fmt(r.get('class_abs_grad','')), fmt(r.get('global_abs_grad','')), r.get('semantic_axis',''), r.get('top_activation_class','')] for r in heads[:25]]),
        '\n## Critical limitation\n\nExisting tables are enough to choose heads and event groups, but they do not appear to contain full per-event x head activation means. The next step is a lightweight extractor only for A/B/C events, prioritizing L2_ch128:160, L2_ch160:192, L2_ch224:256 and all L2 groups if cheap.\n',
    ]
    Path(args.out_md).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out_md).write_text(''.join(md), encoding='utf-8')
    print(json.dumps({'ok': True, 'out_md': args.out_md, 'A': len(A), 'B': len(B), 'C': len(C)}, indent=2))


if __name__ == '__main__':
    main()
