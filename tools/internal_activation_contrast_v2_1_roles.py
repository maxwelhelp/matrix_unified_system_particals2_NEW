#!/usr/bin/env python3
import argparse, csv, json, math, sys
from pathlib import Path
from collections import defaultdict
import torch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools.particlenet_real_patch_controls_v1 import load_balanced
from tools.particle0_topk_controls_v2 import pt_values, real_mask


def readcsv(p):
    p = Path(p)
    if not p.exists(): return []
    with p.open('r', encoding='utf-8') as f: return list(csv.DictReader(f))

def wcsv(p, rows):
    p = Path(p); p.parent.mkdir(parents=True, exist_ok=True)
    keys, seen = [], set()
    for r in rows:
        for k in r:
            if k not in seen: keys.append(k); seen.add(k)
    with p.open('w', encoding='utf-8', newline='') as f:
        wr = csv.DictWriter(f, fieldnames=keys); wr.writeheader()
        for r in rows: wr.writerow({k: r.get(k, '') for k in keys})

def wjson(p, obj):
    p = Path(p); p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(obj, indent=2, ensure_ascii=False), encoding='utf-8')

def fnum(x, d=0.0):
    try:
        v = float(x); return v if math.isfinite(v) else d
    except Exception: return d

def fmt(x):
    try: return f'{float(x):.4f}'
    except Exception: return 'n/a'

def mdtab(h, rows):
    if not rows: return '_No rows._\n'
    out = ['| ' + ' | '.join(h) + ' |', '| ' + ' | '.join(['---'] * len(h)) + ' |']
    out += ['| ' + ' | '.join(str(x).replace('\n', ' ') for x in r) + ' |' for r in rows]
    return '\n'.join(out) + '\n'

def is_lep(feat, ei, idx):
    return feat.shape[1] >= 11 and bool((feat[ei,9,idx] > 0.5) or (feat[ei,10,idx] > 0.5))

def is_had(feat, ei, idx):
    return feat.shape[1] >= 8 and bool((feat[ei,6,idx] > 0.5) or (feat[ei,7,idx] > 0.5))

def is_photon(feat, ei, idx):
    return feat.shape[1] >= 9 and bool(feat[ei,8,idx] > 0.5)

def pid_name(feat, ei, idx):
    if feat.shape[1] < 11: return 'no_pid'
    vals = {'charged_hadron': float(feat[ei,6,idx]), 'neutral_hadron': float(feat[ei,7,idx]), 'photon': float(feat[ei,8,idx]), 'electron': float(feat[ei,9,idx]), 'muon': float(feat[ei,10,idx])}
    return max(vals.items(), key=lambda kv: kv[1])[0]

def dist(a, b): return float(torch.sqrt(((a-b)**2).sum()+1e-9))

def event_roles(batch, event_idx):
    feat = batch['features'].detach().cpu(); pts = batch['points'].detach().cpu(); pt = pt_values(batch).detach().cpu(); mask = real_mask(batch).detach().cpu()
    ei = event_idx; p0 = 0
    valid = [j for j in range(pt.shape[1]) if bool(mask[ei,j])]
    leps = [j for j in valid if is_lep(feat, ei, j)]
    leps = sorted(leps, key=lambda j: float(pt[ei,j]), reverse=True)
    best = leps[0] if leps else None
    second = leps[1] if len(leps) > 1 else None
    hads = [j for j in valid if is_had(feat, ei, j)]
    nearest_had = None; hardest_had = None; hard_thr = 0.0
    if hads:
        if best is not None:
            bc = pts[ei,:,best].float()
            nearest_had = min(hads, key=lambda j: dist(pts[ei,:,j].float(), bc))
        hardest_had = max(hads, key=lambda j: float(pt[ei,j]))
        hp = sorted([float(pt[ei,j]) for j in hads])
        hard_thr = hp[int(0.70 * (len(hp)-1))] if hp else 0.0
    return {'p0': p0, 'best_lepton': best, 'second_lepton': second, 'nearest_hadron_to_best_lepton': nearest_had, 'hardest_hadron': hardest_had, 'hard_thr': hard_thr, 'feat': feat, 'pt': pt, 'points': pts}

def role_for(info, event_idx, pi):
    feat, pt = info['feat'], info['pt']
    p0, best, second = info['p0'], info['best_lepton'], info['second_lepton']
    if pi == p0 and best is not None and pi == best: return 'particle0_best_lepton'
    if pi == p0: return 'particle0'
    if best is not None and pi == best: return 'best_lepton'
    if second is not None and pi == second: return 'second_lepton'
    if info['nearest_hadron_to_best_lepton'] is not None and pi == info['nearest_hadron_to_best_lepton']: return 'nearest_hadron_to_best_lepton'
    if info['hardest_hadron'] is not None and pi == info['hardest_hadron']: return 'hardest_hadron'
    if is_had(feat, event_idx, pi) and float(pt[event_idx,pi]) >= info['hard_thr']: return 'hard_hadron'
    if is_had(feat, event_idx, pi): return 'hadron_neighbor'
    if is_photon(feat, event_idx, pi): return 'photon_neighbor'
    if is_lep(feat, event_idx, pi): return 'other_lepton'
    return 'other'

def summarize(rows):
    evs = defaultdict(set)
    role_top1 = defaultdict(int); role_top3 = defaultdict(int); role_act = defaultdict(float); role_rows = defaultdict(int)
    for r in rows:
        key = (r['head_id'], r['group'])
        evs[key].add(r['event_idx'])
        rk = int(fnum(r['rank'], 99)); role = r['particle_role']
        if rk == 1: role_top1[key, role] += 1
        if rk <= 3: role_top3[key, role] += 1
        role_act[key, role] += fnum(r['particle_activation_norm']); role_rows[key, role] += 1
    out = []
    for key, ids in sorted(evs.items()):
        n = max(1, len(ids))
        roles = sorted({r for (k,r) in role_rows if k == key})
        for role in roles:
            denom3 = 3*n
            out.append({'head_id': key[0], 'group': key[1], 'role': role, 'events': len(ids), 'top1_count': role_top1[key,role], 'top1_rate': role_top1[key,role]/n, 'top3_count': role_top3[key,role], 'top3_rate': role_top3[key,role]/denom3, 'mean_activation_norm': role_act[key,role]/max(1, role_rows[key,role])})
    return sorted(out, key=lambda r: (r['head_id'], r['group'], -r['top1_rate'], -r['top3_rate']))

def contrast(summary, focus_heads):
    by = {(r['head_id'], r['group'], r['role']): r for r in summary}
    roles = sorted(set(r['role'] for r in summary))
    out = []
    for head in focus_heads:
        for role in roles:
            A = by.get((head,'A_protected_highiso',role), {})
            B = by.get((head,'B_confused_highiso',role), {})
            C = by.get((head,'C_Tbl_correct',role), {})
            out.append({'head_id': head, 'role': role, 'A_top1_rate': fnum(A.get('top1_rate')), 'B_top1_rate': fnum(B.get('top1_rate')), 'C_top1_rate': fnum(C.get('top1_rate')), 'B_minus_A_top1_rate': fnum(B.get('top1_rate'))-fnum(A.get('top1_rate')), 'B_minus_C_top1_rate': fnum(B.get('top1_rate'))-fnum(C.get('top1_rate')), 'A_top3_rate': fnum(A.get('top3_rate')), 'B_top3_rate': fnum(B.get('top3_rate')), 'C_top3_rate': fnum(C.get('top3_rate')), 'B_minus_A_top3_rate': fnum(B.get('top3_rate'))-fnum(A.get('top3_rate')), 'B_minus_C_top3_rate': fnum(B.get('top3_rate'))-fnum(C.get('top3_rate'))})
    return sorted(out, key=lambda r: abs(r['B_minus_A_top1_rate']) + abs(r['B_minus_A_top3_rate']), reverse=True)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--top-particles', default='reports/latest/tables/internal_activation_contrast_v2_top_particles.csv')
    ap.add_argument('--data-dir', default=str(Path.home()/'Рабочий стол/jetclass_tiny_balanced'))
    ap.add_argument('--mode', default='kinpid')
    ap.add_argument('--samples-per-file', type=int, default=4096)
    ap.add_argument('--max-files', type=int, default=1000)
    ap.add_argument('--focus-heads', default='L1_ch80:96,L1_ch32:48,L2_ch128:160')
    ap.add_argument('--device', default='cpu')
    ap.add_argument('--out-md', default='reports/latest/INTERNAL_ACTIVATION_CONTRAST_V2_1.md')
    ap.add_argument('--out-annotated', default='reports/latest/tables/internal_activation_contrast_v2_1_top_particles_annotated.csv')
    ap.add_argument('--out-summary', default='reports/latest/tables/internal_activation_contrast_v2_1_role_summary.csv')
    ap.add_argument('--out-contrast', default='reports/latest/tables/internal_activation_contrast_v2_1_role_contrast.csv')
    ap.add_argument('--out-json', default='manifests/latest/internal_activation_contrast_v2_1.json')
    args = ap.parse_args()
    rows = readcsv(args.top_particles)
    if not rows: raise RuntimeError('missing top-particles table; run INTERNAL_ACTIVATION_CONTRAST_V2 first')
    batch = load_balanced(args.data_dir, mode=args.mode, samples_per_file=args.samples_per_file, max_files=args.max_files, device=args.device)
    cache = {}; annotated = []
    for r in rows:
        ei = int(fnum(r['event_idx'], -1)); pi = int(fnum(r['particle_idx'], -1))
        if ei < 0 or pi < 0: continue
        if ei not in cache: cache[ei] = event_roles(batch, ei)
        info = cache[ei]
        rr = dict(r); rr['particle_role'] = role_for(info, ei, pi)
        rr['best_lepton_idx'] = '' if info['best_lepton'] is None else info['best_lepton']
        rr['second_lepton_idx'] = '' if info['second_lepton'] is None else info['second_lepton']
        rr['nearest_hadron_to_best_lepton_idx'] = '' if info['nearest_hadron_to_best_lepton'] is None else info['nearest_hadron_to_best_lepton']
        rr['hardest_hadron_idx'] = '' if info['hardest_hadron'] is None else info['hardest_hadron']
        annotated.append(rr)
    summ = summarize(annotated)
    focus = [x.strip() for x in args.focus_heads.split(',') if x.strip()]
    cont = contrast(summ, focus)
    wcsv(args.out_annotated, annotated); wcsv(args.out_summary, summ); wcsv(args.out_contrast, cont)
    focus_rows = [r for r in cont if r['head_id'] in focus and (r['role'] in ('second_lepton','particle0_best_lepton','best_lepton','nearest_hadron_to_best_lepton','hardest_hadron','hard_hadron','hadron_neighbor'))][:40]
    wjson(args.out_json, {'ok': True, 'rows': len(annotated), 'events': len(cache), 'focus_heads': focus, 'top_contrasts': focus_rows[:30]})
    md = ['# INTERNAL_ACTIVATION_CONTRAST_V2_1\n\nParticle-role annotation for V2 top activations.\n\n', '## Focus role contrasts\n', mdtab(['head','role','A top1','B top1','C top1','B-A top1','A top3','B top3','C top3','B-A top3'], [[r['head_id'], r['role'], fmt(r['A_top1_rate']), fmt(r['B_top1_rate']), fmt(r['C_top1_rate']), fmt(r['B_minus_A_top1_rate']), fmt(r['A_top3_rate']), fmt(r['B_top3_rate']), fmt(r['C_top3_rate']), fmt(r['B_minus_A_top3_rate'])] for r in focus_rows]), '\n## Interpretation\n\nIf `second_lepton` is high in B for L1_ch80:96, the second-lepton trigger directly drives the Tbl-like route. If hadron roles dominate, the L1 route is more geometry-driven. If particle0/best_lepton dominates in both A and B, the same core is read differently due to context.\n']
    Path(args.out_md).parent.mkdir(parents=True, exist_ok=True); Path(args.out_md).write_text(''.join(md), encoding='utf-8')
    print(json.dumps({'ok': True, 'rows': len(annotated), 'events': len(cache), 'out_md': args.out_md}, indent=2))

if __name__ == '__main__': main()
