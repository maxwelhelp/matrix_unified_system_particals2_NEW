#!/usr/bin/env python3
import argparse, csv, json, math, random, sys
from pathlib import Path
from collections import defaultdict
import torch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools.particlenet_real_patch_controls_v1 import load_balanced
from tools.particle0_topk_controls_v2 import make_model, pt_values, real_mask
from data.jetclass_tiny_loader_v3_official import LABELS

HQQL = LABELS.index('label_Hqql')
TBL = LABELS.index('label_Tbl')


def readcsv(p):
    p = Path(p)
    if not p.exists():
        return []
    with p.open('r', encoding='utf-8') as f:
        return list(csv.DictReader(f))


def wcsv(p, rows):
    p = Path(p); p.parent.mkdir(parents=True, exist_ok=True)
    keys, seen = [], set()
    for r in rows:
        for k in r:
            if k not in seen:
                keys.append(k); seen.add(k)
    with p.open('w', encoding='utf-8', newline='') as f:
        wr = csv.DictWriter(f, fieldnames=keys); wr.writeheader()
        for r in rows:
            wr.writerow({k: r.get(k, '') for k in keys})


def wjson(p, obj):
    p = Path(p); p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(obj, indent=2, ensure_ascii=False), encoding='utf-8')


def fnum(x, d=0.0):
    try:
        v = float(x); return v if math.isfinite(v) else d
    except Exception:
        return d


def fmt(x):
    try: return f'{float(x):.4f}'
    except Exception: return 'n/a'


def mdtab(h, rs):
    if not rs: return '_No rows._\n'
    out = ['| ' + ' | '.join(h) + ' |', '| ' + ' | '.join(['---'] * len(h)) + ' |']
    out += ['| ' + ' | '.join(str(x).replace('\n', ' ') for x in r) + ' |' for r in rs]
    return '\n'.join(out) + '\n'


def pid_name(feat, ei, idx):
    if feat.shape[1] < 11: return 'no_pid'
    vals = {'charged_hadron': float(feat[ei,6,idx]), 'neutral_hadron': float(feat[ei,7,idx]), 'photon': float(feat[ei,8,idx]), 'electron': float(feat[ei,9,idx]), 'muon': float(feat[ei,10,idx])}
    return max(vals.items(), key=lambda kv: kv[1])[0]


def is_lep(feat, ei, idx):
    return feat.shape[1] >= 11 and bool((feat[ei,9,idx] > 0.5) or (feat[ei,10,idx] > 0.5))


def best_lepton_idx(feat, pt, mask, ei):
    leps = [j for j in range(pt.shape[1]) if bool(mask[ei,j]) and is_lep(feat, ei, j)]
    if not leps: return 0
    return max(leps, key=lambda j: float(pt[ei,j]))


def second_lepton_idx(feat, pt, mask, ei, best):
    leps = [j for j in range(pt.shape[1]) if j != best and bool(mask[ei,j]) and is_lep(feat, ei, j)]
    if not leps: return None
    return max(leps, key=lambda j: float(pt[ei,j]))


def one(batch, ei):
    return {k: (v[ei:ei+1].clone() if torch.is_tensor(v) and v.shape[0] > ei else v) for k, v in batch.items()}


def copy_particle(dst, di, src, si):
    for k in ['points', 'features', 'vectors']:
        if k in dst and k in src and torch.is_tensor(dst[k]) and dst[k].dim() == 3:
            dst[k][0,:,di] = src[k][0,:,si]
    if 'mask' in dst and torch.is_tensor(dst['mask']):
        dst['mask'][0,:,di] = 1


def mask_particle(dst, idx):
    for k in ['points', 'features', 'vectors']:
        if k in dst and torch.is_tensor(dst[k]) and dst[k].dim() == 3:
            dst[k][0,:,idx] = 0
    if 'mask' in dst and torch.is_tensor(dst['mask']):
        dst['mask'][0,:,idx] = 0


def single_forward(model, b):
    with torch.no_grad():
        return model(b['points'], b['features'], b['mask']).detach().cpu()[0]


def margin(logits):
    return float(logits[HQQL] - logits[TBL])


def pred_label(logits):
    return int(logits.argmax())


def match_donor(protected, target_pt, pt):
    best, bd = None, 1e30
    for ei in protected:
        d = abs(math.log((float(pt[ei,0]) + 1e-6) / (target_pt + 1e-6)))
        if d < bd:
            best, bd = ei, d
    return best


def local_knn(points_event, k):
    from weaver.nn.model.ParticleNet import knn
    with torch.no_grad():
        return knn(points_event, k).detach().cpu()


def build_pid_bank(feat, pt, mask, max_events=None):
    bank = defaultdict(list)
    B = pt.shape[0] if max_events is None else min(pt.shape[0], max_events)
    for ei in range(B):
        for j in range(pt.shape[1]):
            if bool(mask[ei,j]):
                bank[pid_name(feat, ei, j)].append((float(pt[ei,j]), ei, j))
    for k in list(bank):
        bank[k].sort(key=lambda x: x[0])
    return bank


def closest_from_bank(bank, pid, target_pt, rng):
    xs = bank.get(pid) or bank.get('charged_hadron') or []
    if not xs: return None
    # sample a small window around closest for speed and randomness
    best_i, bd = 0, 1e30
    for i, (p, ei, j) in enumerate(xs[::max(1, len(xs)//500)]):
        d = abs(math.log((p+1e-6)/(target_pt+1e-6)))
        if d < bd:
            best_i, bd = i * max(1, len(xs)//500), d
    lo, hi = max(0, best_i-20), min(len(xs), best_i+21)
    return rng.choice(xs[lo:hi])


def apply_compact_knn_patch(tb, batch, target_ei, donor_ei, knn_target, knn_donor, feat, pt, mask, patch_k):
    target_lep = best_lepton_idx(feat, pt, mask, target_ei)
    donor_lep = best_lepton_idx(feat, pt, mask, donor_ei)
    tnb = [int(x) for x in knn_target[0,target_lep].tolist() if int(x) != target_lep][:patch_k]
    dnb = [int(x) for x in knn_donor[0,donor_lep].tolist() if int(x) != donor_lep][:patch_k]
    db = one(batch, donor_ei)
    used = []
    for di, si in zip(tnb, dnb):
        copy_particle(tb, di, db, si); used.append(di)
    return used


def apply_same_pid_pt_control(tb, batch, target_ei, donor_ei, knn_target, knn_donor, feat, pt, mask, bank, rng, patch_k):
    target_lep = best_lepton_idx(feat, pt, mask, target_ei)
    donor_lep = best_lepton_idx(feat, pt, mask, donor_ei)
    tnb = [int(x) for x in knn_target[0,target_lep].tolist() if int(x) != target_lep][:patch_k]
    dnb = [int(x) for x in knn_donor[0,donor_lep].tolist() if int(x) != donor_lep][:patch_k]
    used = []
    for di, si in zip(tnb, dnb):
        pid = pid_name(feat, donor_ei, si); p = float(pt[donor_ei, si])
        c = closest_from_bank(bank, pid, p, rng)
        if c is None: continue
        _, cei, cidx = c
        cb = one(batch, cei)
        copy_particle(tb, di, cb, cidx); used.append(di)
    return used


def apply_second_lepton_removal(tb, target_ei, feat, pt, mask):
    best = best_lepton_idx(feat, pt, mask, target_ei)
    second = second_lepton_idx(feat, pt, mask, target_ei, best)
    if second is None: return []
    mask_particle(tb, second)
    return [second]


def apply_random_remove_control(tb, target_ei, feat, pt, mask, rng):
    best = best_lepton_idx(feat, pt, mask, target_ei)
    valid = [j for j in range(pt.shape[1]) if j != best and bool(mask[target_ei,j])]
    if not valid: return []
    idx = rng.choice(valid)
    mask_particle(tb, idx)
    return [idx]


def run_case(model, base_logits, patched, test, target_ei, donor_ei, used):
    out = single_forward(model, patched)
    bp, pp = pred_label(base_logits), pred_label(out)
    return {'test': test, 'target_event': target_ei, 'donor_event': donor_ei, 'baseline_pred': LABELS[bp], 'patched_pred': LABELS[pp], 'success_to_Hqql': int(pp == HQQL), 'flip': int(pp != bp), 'baseline_margin_Hqql_minus_Tbl': margin(base_logits), 'patched_margin_Hqql_minus_Tbl': margin(out), 'delta_margin': margin(out) - margin(base_logits), 'patched_indices': json.dumps(used)}


def summarize(rows):
    by = defaultdict(list)
    for r in rows: by[r['test']].append(r)
    out = []
    for test, xs in by.items():
        n = len(xs)
        out.append({'test': test, 'n': n, 'success_to_Hqql_rate': sum(r['success_to_Hqql'] for r in xs)/n if n else 0, 'flip_rate': sum(r['flip'] for r in xs)/n if n else 0, 'mean_delta_margin': sum(float(r['delta_margin']) for r in xs)/n if n else 0})
    return sorted(out, key=lambda r: r['test'])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--phase1-events', default='reports/latest/tables/hqql_tbl_confusion_physics_events.csv')
    ap.add_argument('--checkpoint', default='local_checkpoints/part/ParticleNet_kinpid.pt')
    ap.add_argument('--data-dir', default=str(Path.home()/'Рабочий стол/jetclass_tiny_balanced'))
    ap.add_argument('--mode', default='kinpid')
    ap.add_argument('--samples-per-file', type=int, default=4096)
    ap.add_argument('--max-files', type=int, default=1000)
    ap.add_argument('--max-targets', type=int, default=80)
    ap.add_argument('--patch-k', type=int, default=16)
    ap.add_argument('--isolation-threshold', type=float, default=0.30)
    ap.add_argument('--seed', type=int, default=123)
    ap.add_argument('--device', default='cuda' if torch.cuda.is_available() else 'cpu')
    ap.add_argument('--out-md', default='reports/latest/GEOMETRY_VETO_PATCH_V1.md')
    ap.add_argument('--out-csv', default='reports/latest/tables/geometry_veto_patch_v1.csv')
    ap.add_argument('--out-summary', default='reports/latest/tables/geometry_veto_patch_v1_summary.csv')
    ap.add_argument('--out-json', default='manifests/latest/geometry_veto_patch_v1.json')
    a = ap.parse_args(); rng = random.Random(a.seed)

    phase = readcsv(a.phase1_events)
    protected = [int(fnum(r['event_index'])) for r in phase if r.get('true_label')=='label_Hqql' and r.get('group')=='Hqql_correct' and fnum(r.get('particle0_iso_pt_ratio')) >= a.isolation_threshold]
    targets = [int(fnum(r['event_index'])) for r in phase if r.get('true_label')=='label_Hqql' and r.get('group')=='Hqql_to_Tbl' and fnum(r.get('particle0_iso_pt_ratio')) >= a.isolation_threshold]
    targets = targets[:a.max_targets]
    model, res = make_model(a.checkpoint, a.mode, a.device)
    batch = load_balanced(a.data_dir, mode=a.mode, samples_per_file=a.samples_per_file, max_files=a.max_files, device=a.device)
    feat = batch['features'].detach().cpu(); pt = pt_values(batch).detach().cpu(); mask = real_mask(batch).detach().cpu()
    max_e = max(targets + protected) if (targets or protected) else -1
    if max_e >= batch['points'].shape[0]: raise RuntimeError(f'event index {max_e} >= loaded B={batch["points"].shape[0]}')
    bank = build_pid_bank(feat, pt, mask, max_events=min(batch['points'].shape[0], 20000))

    rows = []
    for ei in targets:
        donor = match_donor(protected, float(pt[ei, best_lepton_idx(feat, pt, mask, ei)]), pt)
        if donor is None: continue
        base_b = one(batch, ei); base_logits = single_forward(model, base_b)
        knn_t = local_knn(batch['points'][ei:ei+1], a.patch_k)
        knn_d = local_knn(batch['points'][donor:donor+1], a.patch_k)
        has_second = second_lepton_idx(feat, pt, mask, ei, best_lepton_idx(feat, pt, mask, ei)) is not None
        meta = {'target_has_second_lepton': int(has_second)}

        tb = one(batch, ei); used = apply_compact_knn_patch(tb, batch, ei, donor, knn_t, knn_d, feat, pt, mask, a.patch_k)
        rows.append({**run_case(model, base_logits, tb, 'G1_compact_knn_injection', ei, donor, used), **meta})

        tb = one(batch, ei); used = apply_same_pid_pt_control(tb, batch, ei, donor, knn_t, knn_d, feat, pt, mask, bank, rng, a.patch_k)
        rows.append({**run_case(model, base_logits, tb, 'G1_control_same_pid_pt', ei, donor, used), **meta})

        if has_second:
            tb = one(batch, ei); used = apply_second_lepton_removal(tb, ei, feat, pt, mask)
            rows.append({**run_case(model, base_logits, tb, 'G2_second_lepton_removal', ei, donor, used), **meta})
            tb = one(batch, ei); used = apply_random_remove_control(tb, ei, feat, pt, mask, rng)
            rows.append({**run_case(model, base_logits, tb, 'G2_control_random_removal', ei, donor, used), **meta})

            tb = one(batch, ei); u1 = apply_compact_knn_patch(tb, batch, ei, donor, knn_t, knn_d, feat, pt, mask, a.patch_k); u2 = apply_second_lepton_removal(tb, ei, feat, pt, mask)
            rows.append({**run_case(model, base_logits, tb, 'G3_compact_knn_plus_second_lepton_removal', ei, donor, u1+u2), **meta})

    summ = summarize(rows)
    wcsv(a.out_csv, rows); wcsv(a.out_summary, summ)
    wjson(a.out_json, {'ok': True, 'targets': len(targets), 'protected': len(protected), 'rows': len(rows), 'summary': summ, 'model_missing': list(res.missing_keys), 'model_unexpected': list(res.unexpected_keys)})
    md = ['# GEOMETRY_VETO_PATCH_V1\n\nPatch tests for high-isolation Hqql_to_Tbl events.\n\n', '## Summary\n', mdtab(['test','n','success_to_Hqql','flip','delta_margin'], [[r['test'], r['n'], fmt(r['success_to_Hqql_rate']), fmt(r['flip_rate']), fmt(r['mean_delta_margin'])] for r in summ]), '\n## Example rows\n', mdtab(['test','target','donor','base','patched','success','delta_margin','idx'], [[r['test'], r['target_event'], r['donor_event'], r['baseline_pred'], r['patched_pred'], r['success_to_Hqql'], fmt(r['delta_margin']), r['patched_indices']] for r in rows[:80]]), '\n## Interpretation\n\nG1 tests compact lepton-centered KNN geometry. G2 tests second-lepton ambiguity. G3 tests whether the two mechanisms are additive. Compare each targeted test with its control before raising claim level.\n']
    Path(a.out_md).parent.mkdir(parents=True, exist_ok=True); Path(a.out_md).write_text(''.join(md), encoding='utf-8')
    print(json.dumps({'ok': True, 'rows': len(rows), 'out_md': a.out_md}, indent=2, ensure_ascii=False))

if __name__ == '__main__': main()
