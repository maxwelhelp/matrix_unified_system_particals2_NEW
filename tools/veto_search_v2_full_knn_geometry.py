#!/usr/bin/env python3
import argparse, csv, json, math, sys
from pathlib import Path
from collections import Counter
import torch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools.particlenet_real_patch_controls_v1 import load_balanced
from tools.particle0_topk_controls_v2 import pt_values, real_mask


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


def fnum(x, default=0.0):
    try:
        v = float(x)
        return v if math.isfinite(v) else default
    except Exception:
        return default


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


def is_lep(feat, ei, idx):
    return feat.shape[1] >= 11 and bool((feat[ei, 9, idx] > 0.5) or (feat[ei, 10, idx] > 0.5))


def is_had(feat, ei, idx):
    return feat.shape[1] >= 8 and bool((feat[ei, 6, idx] > 0.5) or (feat[ei, 7, idx] > 0.5))


def is_charged(feat, ei, idx):
    return feat.shape[1] >= 7 and bool(feat[ei, 6, idx] > 0.5)


def pid_name(feat, ei, idx):
    if feat.shape[1] < 11:
        return 'no_pid'
    vals = {
        'charged_hadron': float(feat[ei, 6, idx]),
        'neutral_hadron': float(feat[ei, 7, idx]),
        'photon': float(feat[ei, 8, idx]),
        'electron': float(feat[ei, 9, idx]),
        'muon': float(feat[ei, 10, idx]),
    }
    return max(vals.items(), key=lambda kv: kv[1])[0]


def dist(a, b):
    return float(torch.sqrt(((a - b) ** 2).sum() + 1e-9))


def pairwise(coords):
    out = []
    for i in range(len(coords)):
        for j in range(i + 1, len(coords)):
            out.append(dist(coords[i], coords[j]))
    return out


def summarize_knn(prefix, ei, center_idx, nb, feat, points, pt, hard_q=0.70):
    nb = [int(x) for x in nb if int(x) != int(center_idx)]
    nb_pt = [float(pt[ei, j]) for j in nb]
    hard_thr = sorted(nb_pt)[int(len(nb_pt) * hard_q)] if nb_pt else 0.0
    coords = [points[ei, :, j].float().cpu() for j in nb]
    center = points[ei, :, center_idx].float().cpu()
    drs = [dist(c, center) for c in coords]
    pdr = pairwise(coords)
    had = [j for j in nb if is_had(feat, ei, j)]
    ch = [j for j in nb if is_charged(feat, ei, j)]
    lep = [j for j in nb if is_lep(feat, ei, j)]
    hard = [j for j in nb if float(pt[ei, j]) >= hard_thr]
    hard_had = [j for j in hard if is_had(feat, ei, j)]
    hard_ch = [j for j in hard if is_charged(feat, ei, j)]
    out = {
        prefix + '_knn_size': len(nb),
        prefix + '_knn_sum_pt': sum(nb_pt),
        prefix + '_knn_mean_pt': sum(nb_pt) / len(nb_pt) if nb_pt else 0.0,
        prefix + '_knn_max_pt': max(nb_pt) if nb_pt else 0.0,
        prefix + '_knn_hadron_count': len(had),
        prefix + '_knn_charged_count': len(ch),
        prefix + '_knn_lepton_count': len(lep),
        prefix + '_knn_hadron_frac': len(had) / len(nb) if nb else 0.0,
        prefix + '_knn_charged_frac': len(ch) / len(nb) if nb else 0.0,
        prefix + '_knn_lepton_frac': len(lep) / len(nb) if nb else 0.0,
        prefix + '_knn_hard_neighbor_count': len(hard),
        prefix + '_knn_hard_hadron_count': len(hard_had),
        prefix + '_knn_hard_charged_count': len(hard_ch),
        prefix + '_knn_deltaR_to_center_mean': sum(drs) / len(drs) if drs else 0.0,
        prefix + '_knn_deltaR_to_center_min': min(drs) if drs else 0.0,
        prefix + '_knn_pairwise_deltaR_mean': sum(pdr) / len(pdr) if pdr else 0.0,
        prefix + '_knn_pairwise_deltaR_min': min(pdr) if pdr else 0.0,
        prefix + '_knn_pairwise_deltaR_max': max(pdr) if pdr else 0.0,
    }
    for j, nm in [(6, 'charged_hadron'), (7, 'neutral_hadron'), (8, 'photon'), (9, 'electron'), (10, 'muon')]:
        out[prefix + '_knn_' + nm + '_frac'] = float(feat[ei, j, nb].float().mean()) if feat.shape[1] > j and nb else 0.0
    return out


def event_features(ei, group, phase_row, batch, local_knn_idx, patch_k, align_thr):
    feat = batch['features']
    points = batch['points']
    pt = pt_values(batch)
    mask = real_mask(batch)
    p0 = 0
    p0_nb = [int(x) for x in local_knn_idx[0, p0].tolist() if int(x) != p0][:patch_k]

    leps = [j for j in range(pt.shape[1]) if bool(mask[ei, j]) and is_lep(feat, ei, j)]
    leps_sorted = sorted(leps, key=lambda j: float(pt[ei, j]), reverse=True)
    lep_idx = leps_sorted[0] if leps_sorted else p0
    lep_nb = [int(x) for x in local_knn_idx[0, lep_idx].tolist() if int(x) != lep_idx][:patch_k]

    p0c = points[ei, :, p0].float().cpu()
    lepc = points[ei, :, lep_idx].float().cpu()
    p0_lep_dr = dist(p0c, lepc)

    had_all = [j for j in range(pt.shape[1]) if bool(mask[ei, j]) and is_had(feat, ei, j)]
    had_drs = []
    for j in had_all:
        hc = points[ei, :, j].float().cpu()
        had_drs.append((dist(hc, lepc), j, float(pt[ei, j])))
    had_drs = sorted(had_drs)
    hard_had_drs = sorted(had_drs, key=lambda x: (-x[2], x[0]))

    row = {
        'event_index': ei,
        'group': group,
        'phase1_group': phase_row.get('group', ''),
        'p0_pid': pid_name(feat, ei, p0),
        'best_lepton_pid': pid_name(feat, ei, lep_idx),
        'p0_pt': float(pt[ei, p0]),
        'best_lepton_pt': float(pt[ei, lep_idx]),
        'p0_iso': fnum(phase_row.get('particle0_iso_pt_ratio')),
        'phase1_deltaR_p0_lepton': fnum(phase_row.get('deltaR_p0_lepton')),
        'computed_deltaR_p0_lepton': p0_lep_dr,
        'p0_is_lepton_aligned': int(p0_lep_dr < align_thr),
        'p0_idx_equals_best_lepton': int(p0 == lep_idx),
        'best_lepton_idx': int(lep_idx),
        'second_lepton_present': int(len(leps_sorted) >= 2),
        'second_lepton_pt': float(pt[ei, leps_sorted[1]]) if len(leps_sorted) >= 2 else 0.0,
        'lepton_nearest_hadron_deltaR': had_drs[0][0] if had_drs else 999.0,
        'lepton_hardest_hadron_deltaR': hard_had_drs[0][0] if hard_had_drs else 999.0,
        'lepton_hardest_hadron_pt': hard_had_drs[0][2] if hard_had_drs else 0.0,
    }
    row.update(summarize_knn('p0', ei, p0, p0_nb, feat, points, pt))
    row.update(summarize_knn('lep', ei, lep_idx, lep_nb, feat, points, pt))
    return row


def compare(rows, features):
    prot = [r for r in rows if r['group'] == 'protected_highiso']
    conf = [r for r in rows if r['group'] == 'actual_confused_highiso']
    out = []
    for f in features:
        a = [fnum(r.get(f)) for r in prot]
        b = [fnum(r.get(f)) for r in conf]
        if not a or not b:
            continue
        ma = sum(a) / len(a)
        mb = sum(b) / len(b)
        sa = math.sqrt(sum((x - ma) ** 2 for x in a) / max(1, len(a) - 1))
        sb = math.sqrt(sum((x - mb) ** 2 for x in b) / max(1, len(b) - 1))
        pooled = math.sqrt((sa * sa + sb * sb) / 2) + 1e-9
        diff = ma - mb
        out.append({
            'feature': f,
            'protected_mean': ma,
            'confused_mean': mb,
            'diff_protected_minus_confused': diff,
            'ratio_protected_over_confused': (ma + 1e-9) / (mb + 1e-9) if abs(mb) > 1e-9 else 999.0,
            'std_effect': diff / pooled,
            'direction': 'protected_higher_veto_candidate' if diff > 0 else 'confused_higher_trigger_candidate',
        })
    return sorted(out, key=lambda r: abs(r['std_effect']), reverse=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--phase1-events', default='reports/latest/tables/hqql_tbl_confusion_physics_events.csv')
    ap.add_argument('--data-dir', default=str(Path.home() / 'Рабочий стол/jetclass_tiny_balanced'))
    ap.add_argument('--mode', default='kinpid')
    ap.add_argument('--samples-per-file', type=int, default=4096)
    ap.add_argument('--max-files', type=int, default=1000)
    ap.add_argument('--isolation-threshold', type=float, default=0.30)
    ap.add_argument('--p0-lepton-dr-threshold', type=float, default=0.05)
    ap.add_argument('--patch-k', type=int, default=16)
    ap.add_argument('--device', default='cpu')
    ap.add_argument('--out-md', default='reports/latest/VETO_SEARCH_V2_FULL_KNN_GEOMETRY.md')
    ap.add_argument('--out-events', default='reports/latest/tables/veto_search_v2_full_knn_events.csv')
    ap.add_argument('--out-contrasts', default='reports/latest/tables/veto_search_v2_full_knn_contrasts.csv')
    ap.add_argument('--out-json', default='manifests/latest/veto_search_v2_full_knn_geometry.json')
    args = ap.parse_args()

    phase = readcsv(args.phase1_events)
    protected = [r for r in phase if r.get('true_label') == 'label_Hqql' and r.get('group') == 'Hqql_correct' and fnum(r.get('particle0_iso_pt_ratio')) >= args.isolation_threshold]
    confused = [r for r in phase if r.get('true_label') == 'label_Hqql' and r.get('group') == 'Hqql_to_Tbl' and fnum(r.get('particle0_iso_pt_ratio')) >= args.isolation_threshold]
    wanted = {int(fnum(r.get('event_index'), -1)): (r, 'protected_highiso') for r in protected}
    wanted.update({int(fnum(r.get('event_index'), -1)): (r, 'actual_confused_highiso') for r in confused})

    batch = load_balanced(args.data_dir, mode=args.mode, samples_per_file=args.samples_per_file, max_files=args.max_files, device=args.device)
    pts = batch['points']
    max_e = max(wanted) if wanted else -1
    if max_e >= pts.shape[0]:
        raise RuntimeError(f'Phase1 event_index max {max_e} exceeds loaded dataset B={pts.shape[0]}; increase SAMPLES_PER_FILE/MAX_FILES')

    from weaver.nn.model.ParticleNet import knn
    rows = []
    with torch.no_grad():
        for ei, (phase_row, group) in sorted(wanted.items()):
            local_idx = knn(pts[ei:ei+1], args.patch_k).detach().cpu()
            rows.append(event_features(ei, group, phase_row, batch, local_idx, args.patch_k, args.p0_lepton_dr_threshold))

    exclude = {'event_index', 'group', 'phase1_group', 'p0_pid', 'best_lepton_pid'}
    features = [k for k in rows[0].keys() if k not in exclude] if rows else []
    contrasts = compare(rows, features)
    wcsv(args.out_events, rows)
    wcsv(args.out_contrasts, contrasts)

    pidp = Counter(r['p0_pid'] for r in rows if r['group'] == 'protected_highiso')
    pidc = Counter(r['p0_pid'] for r in rows if r['group'] == 'actual_confused_highiso')
    np = sum(1 for r in rows if r['group'] == 'protected_highiso')
    nc = sum(1 for r in rows if r['group'] == 'actual_confused_highiso')
    ap_rate = sum(r.get('p0_is_lepton_aligned', 0) for r in rows if r['group'] == 'protected_highiso') / max(1, np)
    ac_rate = sum(r.get('p0_is_lepton_aligned', 0) for r in rows if r['group'] == 'actual_confused_highiso') / max(1, nc)

    veto = [r for r in contrasts if r['direction'] == 'protected_higher_veto_candidate'][:15]
    trig = [r for r in contrasts if r['direction'] == 'confused_higher_trigger_candidate'][:15]
    wjson(args.out_json, {
        'ok': True,
        'protected_highiso_n': len(protected),
        'actual_confused_highiso_n': len(confused),
        'rows': len(rows),
        'p0_lepton_dr_threshold': args.p0_lepton_dr_threshold,
        'protected_alignment_rate': ap_rate,
        'confused_alignment_rate': ac_rate,
        'top_contrasts': contrasts[:30],
    })

    md = [
        '# VETO_SEARCH_V2_FULL_KNN_GEOMETRY\n\n',
        'Full KNN geometry contrast for high-isolation Hqql protected vs actual-confused events. This version tests the core-lepton alignment hypothesis.\n\n',
        '## Groups\n',
        mdtab(['group', 'n', 'p0_pid_modes', 'p0_is_lepton_aligned_rate'], [
            ['protected_highiso', len(protected), ', '.join(f'{k}:{v}' for k, v in pidp.most_common()), fmt(ap_rate)],
            ['actual_confused_highiso', len(confused), ', '.join(f'{k}:{v}' for k, v in pidc.most_common()), fmt(ac_rate)],
        ]),
        '\n## Protected-higher candidates / possible veto\n',
        mdtab(['feature', 'protected_mean', 'confused_mean', 'diff', 'ratio', 'std_effect'], [[r['feature'], fmt(r['protected_mean']), fmt(r['confused_mean']), fmt(r['diff_protected_minus_confused']), fmt(r['ratio_protected_over_confused']), fmt(r['std_effect'])] for r in veto]),
        '\n## Confused-higher candidates / possible false-Tbl trigger\n',
        mdtab(['feature', 'protected_mean', 'confused_mean', 'diff', 'ratio', 'std_effect'], [[r['feature'], fmt(r['protected_mean']), fmt(r['confused_mean']), fmt(r['diff_protected_minus_confused']), fmt(r['ratio_protected_over_confused']), fmt(r['std_effect'])] for r in trig]),
        '\n## Interpretation\n\nPrimary hypothesis: high isolation creates Tbl-risk; p0-lepton alignment and lepton-centric hard/charged/hadronic KNN geometry may veto false Tbl-readout. If confused-higher `computed_deltaR_p0_lepton` or lower `p0_is_lepton_aligned` dominates, the next mechanism is core/lepton mismatch rather than muon/electron PID alone.\n'
    ]
    Path(args.out_md).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out_md).write_text(''.join(md), encoding='utf-8')
    print(json.dumps({'ok': True, 'rows': len(rows), 'out_md': args.out_md}, indent=2, ensure_ascii=False))


if __name__ == '__main__':
    main()
