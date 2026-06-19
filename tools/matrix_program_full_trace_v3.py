#!/usr/bin/env python3
import argparse, csv, json, math, sys
from pathlib import Path
from collections import defaultdict
import torch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from tools.particlenet_real_patch_controls_v1 import load_balanced
from tools.particle0_topk_controls_v2 import make_model, real_mask, pt_values
from tools.internal_activation_contrast_v2 import (
    readcsv, wcsv, wjson, fnum, fmt, mdtab, slice_batch,
    capture_activations, logits_with_zeroed_head, masked_mean_act,
    group_ids_from_phase, select_tbl_correct, get_effective_classifier_direction,
)
from tools.internal_activation_contrast_v2_1_roles import event_roles, role_for
from data.jetclass_tiny_loader_v3_official import LABELS

HQQL = LABELS.index('label_Hqql')
TBL = LABELS.index('label_Tbl')


def generate_heads(layers, slice_size, max_channels):
    heads = []
    for layer in layers:
        for s in range(0, max_channels, slice_size):
            e = min(max_channels, s + slice_size)
            heads.append({'head_id': f'L{layer}_ch{s}:{e}', 'layer': layer, 'start': s, 'end': e})
    return heads


def mean(xs, key):
    vals = [fnum(x.get(key)) for x in xs if x.get(key, '') != '']
    return sum(vals)/len(vals) if vals else 0.0


def dist2(a, b):
    return math.sqrt(sum((a[i]-b[i])**2 for i in range(len(a))))


def role_summary(particle_rows):
    by = defaultdict(list)
    for r in particle_rows:
        by[(r['head_id'], r['group'], r['particle_role'])].append(r)
    out = []
    events_by_hg = defaultdict(set)
    for r in particle_rows:
        events_by_hg[(r['head_id'], r['group'])].add(r['event_idx'])
    for (hid, group, role), xs in sorted(by.items()):
        n_events = max(1, len(events_by_hg[(hid, group)]))
        top1 = sum(1 for r in xs if int(fnum(r['rank'], 99)) == 1)
        top3 = sum(1 for r in xs if int(fnum(r['rank'], 99)) <= 3)
        out.append({
            'head_id': hid, 'group': group, 'role': role,
            'events': n_events,
            'top1_rate': top1 / n_events,
            'top3_rate': top3 / (3*n_events),
            'mean_activation_norm': sum(fnum(r['particle_activation_norm']) for r in xs)/max(1, len(xs)),
        })
    return out


def top_role_for(role_rows, hid, group):
    xs = [r for r in role_rows if r['head_id'] == hid and r['group'] == group]
    if not xs:
        return ''
    xs = sorted(xs, key=lambda r: (fnum(r['top1_rate']), fnum(r['top3_rate']), fnum(r['mean_activation_norm'])), reverse=True)
    return f"{xs[0]['role']} top1={float(xs[0]['top1_rate']):.3f} top3={float(xs[0]['top3_rate']):.3f}"


def diagnose(row):
    # Conservative automatic labels. Projection is approximate; ablation drives score.
    tbl_gain = fnum(row['B_minus_A_tbl_ablation_contrib'])
    hqql_loss = -fnum(row['B_minus_A_hqql_ablation_contrib'])
    anomaly = fnum(row['B_anomaly_score'])
    b_close_c = fnum(row['B_closer_to_C_score'])
    if tbl_gain > 0.25 and b_close_c > 0:
        return 'active_tbl_trigger_candidate'
    if hqql_loss > 0.20 and tbl_gain <= 0.10:
        return 'hqql_loss_candidate'
    if anomaly > 0.20:
        return 'anomalous_third_topology_candidate'
    return 'neutral_or_weak'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--phase1-events', default='reports/latest/tables/hqql_tbl_confusion_physics_events.csv')
    ap.add_argument('--checkpoint', default='local_checkpoints/part/ParticleNet_kinpid.pt')
    ap.add_argument('--data-dir', default=str(Path.home()/'Рабочий стол/jetclass_tiny_balanced'))
    ap.add_argument('--mode', default='kinpid')
    ap.add_argument('--samples-per-file', type=int, default=4096)
    ap.add_argument('--max-files', type=int, default=1000)
    ap.add_argument('--layers', default='0,1,2')
    ap.add_argument('--slice-size', type=int, default=32)
    ap.add_argument('--max-channels', type=int, default=256)
    ap.add_argument('--isolation-threshold', type=float, default=0.30)
    ap.add_argument('--max-tbl-correct', type=int, default=64)
    ap.add_argument('--forward-step', type=int, default=128)
    ap.add_argument('--device', default='cuda' if torch.cuda.is_available() else 'cpu')
    ap.add_argument('--out-md', default='reports/latest/MATRIX_PROGRAM_FULL_TRACE_V3_SUMMARY.md')
    ap.add_argument('--out-db', default='reports/latest/tables/matrix_program_full_trace_v3_all_heads_database.csv')
    ap.add_argument('--out-ranked', default='reports/latest/tables/matrix_program_full_trace_v3_all_heads_ranked.csv')
    ap.add_argument('--out-roles', default='reports/latest/tables/matrix_program_full_trace_v3_top_particle_roles.csv')
    ap.add_argument('--out-event-rows', default='reports/latest/tables/matrix_program_full_trace_v3_event_head_rows.csv')
    ap.add_argument('--out-json', default='manifests/latest/matrix_program_full_trace_v3.json')
    args = ap.parse_args()

    layers = [int(x) for x in args.layers.split(',') if x.strip()]
    heads = generate_heads(layers, args.slice_size, args.max_channels)

    phase = readcsv(args.phase1_events)
    Aids, Bids = group_ids_from_phase(phase, args.isolation_threshold)

    model, res = make_model(args.checkpoint, args.mode, args.device)
    batch = load_balanced(args.data_dir, mode=args.mode, samples_per_file=args.samples_per_file, max_files=args.max_files, device=args.device)

    # Full logits for C selection.
    full_logits = []
    with torch.no_grad():
        for s in range(0, batch['y'].shape[0], max(1, args.forward_step)):
            sub = slice_batch(batch, list(range(s, min(batch['y'].shape[0], s + args.forward_step))))
            full_logits.append(model(sub['points'], sub['features'], sub['mask']).detach().cpu())
    full_logits = torch.cat(full_logits, 0)
    Cids = select_tbl_correct(batch, full_logits, args.max_tbl_correct)

    all_ids = Aids + Bids + Cids
    groups = ['A_protected_highiso']*len(Aids) + ['B_confused_highiso']*len(Bids) + ['C_Tbl_correct']*len(Cids)
    if not all_ids:
        raise RuntimeError('No A/B/C events selected')
    if max(all_ids) >= batch['y'].shape[0]:
        raise RuntimeError(f'event index {max(all_ids)} >= loaded B={batch["y"].shape[0]}; increase SAMPLES_PER_FILE/MAX_FILES')

    sub = slice_batch(batch, all_ids)
    base_logits, caps = capture_activations(model, sub, heads)
    mask = real_mask(sub).detach().cpu().bool()
    feat = sub['features'].detach().cpu()
    pt = pt_values(sub).detach().cpu()
    W, W_note = get_effective_classifier_direction(model)

    # Drop invalid heads whose channel range exceeds actual activation width.
    valid_heads = []
    for h in heads:
        act = caps.get(h['layer'])
        if act is not None and h['end'] <= act.shape[1]:
            valid_heads.append(h)
    heads = valid_heads

    event_rows = []
    particle_rows = []
    role_cache = {}

    # Ablation per head.
    ablated = {}
    for h in heads:
        ablated[h['head_id']] = logits_with_zeroed_head(model, sub, h)

    for h in heads:
        hid, layer, s, e = h['head_id'], h['layer'], h['start'], h['end']
        act = caps[layer]
        ev = masked_mean_act(act, mask, s, e)
        norms = ev.norm(dim=1).tolist()
        # Approximate class projections for all classes when possible.
        proj = None
        if W is not None and W.shape[1] >= e:
            proj = ev @ W[:, s:e].T
        zero_logits = ablated[hid]
        for bi, real_ei in enumerate(all_ids):
            base = base_logits[bi]
            zl = zero_logits[bi]
            row = {
                'event_idx': real_ei, 'group': groups[bi], 'head_id': hid, 'layer': layer, 'ch_start': s, 'ch_end': e,
                'activation_norm': float(norms[bi]),
                'base_pred': LABELS[int(base.argmax())], 'zero_pred': LABELS[int(zl.argmax())],
                'score_hqql_proj': float(proj[bi, HQQL]) if proj is not None else 0.0,
                'score_tbl_proj': float(proj[bi, TBL]) if proj is not None else 0.0,
                'contrib_hqql_drop_when_zeroed': float(base[HQQL] - zl[HQQL]),
                'contrib_tbl_drop_when_zeroed': float(base[TBL] - zl[TBL]),
            }
            for ci, lab in enumerate(LABELS):
                safe = lab.replace('label_', '')
                if proj is not None:
                    row[f'score_{safe}_proj'] = float(proj[bi, ci])
                row[f'contrib_{safe}_drop_when_zeroed'] = float(base[ci] - zl[ci])
            event_rows.append(row)

            # top particles and roles
            x = act[bi, s:e, :].transpose(0, 1)
            pn = x.norm(dim=1)
            valid = torch.where(mask[bi])[0]
            if real_ei not in role_cache:
                role_cache[real_ei] = event_roles(batch, real_ei)
            info = role_cache[real_ei]
            if len(valid) > 0:
                vals = pn[valid]
                topk = torch.topk(vals, min(3, len(vals))).indices
                for rank, rel in enumerate(topk.tolist(), 1):
                    pi = int(valid[rel])
                    role = role_for(info, real_ei, pi)
                    particle_rows.append({
                        'event_idx': real_ei, 'group': groups[bi], 'head_id': hid, 'rank': rank,
                        'particle_idx': pi, 'particle_role': role,
                        'particle_activation_norm': float(pn[pi]),
                        'pid': 'unknown', 'pt': float(pt[bi, pi]),
                    })

    role_rows = role_summary(particle_rows)

    # Build head database.
    by_head = defaultdict(list)
    for r in event_rows:
        by_head[r['head_id']].append(r)
    db = []
    for h in heads:
        hid = h['head_id']
        xs = by_head[hid]
        by_group = {g: [r for r in xs if r['group'] == g] for g in ['A_protected_highiso', 'B_confused_highiso', 'C_Tbl_correct']}
        row = {'head_id': hid, 'layer': h['layer'], 'ch_start': h['start'], 'ch_end': h['end'], 'slice_size': h['end'] - h['start']}
        for prefix, group in [('A','A_protected_highiso'), ('B','B_confused_highiso'), ('C','C_Tbl_correct')]:
            row[f'n_{prefix}'] = len(by_group[group])
            row[f'activation_norm_{prefix}'] = mean(by_group[group], 'activation_norm')
            row[f'score_hqql_{prefix}'] = mean(by_group[group], 'score_hqql_proj')
            row[f'score_tbl_{prefix}'] = mean(by_group[group], 'score_tbl_proj')
            row[f'ablation_hqql_{prefix}'] = mean(by_group[group], 'contrib_hqql_drop_when_zeroed')
            row[f'ablation_tbl_{prefix}'] = mean(by_group[group], 'contrib_tbl_drop_when_zeroed')
            row[f'top_particle_role_{prefix}'] = top_role_for(role_rows, hid, group)
            for lab in LABELS:
                safe = lab.replace('label_', '')
                row[f'score_{safe}_{prefix}'] = mean(by_group[group], f'score_{safe}_proj')
                row[f'ablation_{safe}_{prefix}'] = mean(by_group[group], f'contrib_{safe}_drop_when_zeroed')
        Av = [row['score_hqql_A'], row['score_tbl_A']]
        Bv = [row['score_hqql_B'], row['score_tbl_B']]
        Cv = [row['score_hqql_C'], row['score_tbl_C']]
        row['dist_BA_hqql_tbl_projection'] = dist2(Bv, Av)
        row['dist_BC_hqql_tbl_projection'] = dist2(Bv, Cv)
        row['B_closer_to_C_score'] = row['dist_BA_hqql_tbl_projection'] - row['dist_BC_hqql_tbl_projection']
        row['confusion_trigger_score'] = max(0.0, row['ablation_tbl_B'] - row['ablation_tbl_A']) + max(0.0, row['B_closer_to_C_score']) * 0.01
        row['hqql_loss_score'] = max(0.0, row['ablation_hqql_A'] - row['ablation_hqql_B']) + max(0.0, row['score_hqql_A'] - row['score_hqql_B']) * 0.02
        row['anomaly_score'] = max(0.0, row['dist_BA_hqql_tbl_projection'] - row['dist_BC_hqql_tbl_projection'] * 0.25)
        row['diagnosis'] = diagnose(row)
        row['matrix_program_summary'] = 'read KNN/source context -> project channel slice -> class-direction/ablation effect -> top-particle role'
        db.append(row)

    ranked = sorted(db, key=lambda r: (r['diagnosis'] != 'active_tbl_trigger_candidate', -fnum(r['confusion_trigger_score']), -fnum(r['hqql_loss_score']), -fnum(r['anomaly_score'])))
    wcsv(args.out_db, db)
    wcsv(args.out_ranked, ranked)
    wcsv(args.out_roles, role_rows)
    wcsv(args.out_event_rows, event_rows)
    counts = defaultdict(int)
    for r in db:
        counts[r['diagnosis']] += 1
    wjson(args.out_json, {
        'ok': True, 'heads': len(db), 'slice_size': args.slice_size,
        'A': len(Aids), 'B': len(Bids), 'C': len(Cids),
        'diagnosis_counts': dict(counts), 'projection_note': W_note,
        'missing': list(res.missing_keys), 'unexpected': list(res.unexpected_keys),
    })

    top_trigger = sorted(db, key=lambda r: fnum(r['confusion_trigger_score']), reverse=True)[:8]
    top_loss = sorted(db, key=lambda r: fnum(r['hqql_loss_score']), reverse=True)[:8]
    top_anom = sorted(db, key=lambda r: fnum(r['anomaly_score']), reverse=True)[:8]
    md = ['# MATRIX_PROGRAM_FULL_TRACE_V3_SUMMARY\n\n',
          'All-head matrix-program trace over A/B/C Hqql/Tbl groups.\n\n',
          f'- heads: **{len(db)}**\n', f'- slice_size: **{args.slice_size}**\n', f'- A protected: **{len(Aids)}**\n', f'- B confused: **{len(Bids)}**\n', f'- C Tbl_correct: **{len(Cids)}**\n', f'- projection: `{W_note}`\n\n',
          '## Diagnosis counts\n', mdtab(['diagnosis','count'], [[k, v] for k, v in sorted(counts.items())]),
          '\n## Top trigger candidates\n', mdtab(['head','diag','trigger','loss','anomaly','topA','topB','topC','abl_tbl A/B/C','abl_hqql A/B/C'], [[r['head_id'], r['diagnosis'], fmt(r['confusion_trigger_score']), fmt(r['hqql_loss_score']), fmt(r['anomaly_score']), r['top_particle_role_A'], r['top_particle_role_B'], r['top_particle_role_C'], f"{fmt(r['ablation_tbl_A'])}/{fmt(r['ablation_tbl_B'])}/{fmt(r['ablation_tbl_C'])}", f"{fmt(r['ablation_hqql_A'])}/{fmt(r['ablation_hqql_B'])}/{fmt(r['ablation_hqql_C'])}"] for r in top_trigger]),
          '\n## Top Hqql-loss candidates\n', mdtab(['head','diag','trigger','loss','anomaly','topA','topB','topC','abl_hqql A/B/C','score_hqql A/B/C'], [[r['head_id'], r['diagnosis'], fmt(r['confusion_trigger_score']), fmt(r['hqql_loss_score']), fmt(r['anomaly_score']), r['top_particle_role_A'], r['top_particle_role_B'], r['top_particle_role_C'], f"{fmt(r['ablation_hqql_A'])}/{fmt(r['ablation_hqql_B'])}/{fmt(r['ablation_hqql_C'])}", f"{fmt(r['score_hqql_A'])}/{fmt(r['score_hqql_B'])}/{fmt(r['score_hqql_C'])}"] for r in top_loss]),
          '\n## Top anomalous-third-topology candidates\n', mdtab(['head','diag','trigger','loss','anomaly','topA','topB','topC','B_close_C'], [[r['head_id'], r['diagnosis'], fmt(r['confusion_trigger_score']), fmt(r['hqql_loss_score']), fmt(r['anomaly_score']), r['top_particle_role_A'], r['top_particle_role_B'], r['top_particle_role_C'], fmt(r['B_closer_to_C_score'])] for r in top_anom]),
          '\n## Interpretation\n\nThis report is the full all-head map. It should replace single-suspect analysis. Read each row as a matrix program: source/KNN context -> channel slice -> class-direction contribution -> particle role. Use ranked heads to decide which mechanisms deserve deeper probes.\n']
    Path(args.out_md).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out_md).write_text(''.join(md), encoding='utf-8')
    print(json.dumps({'ok': True, 'heads': len(db), 'out_md': args.out_md}, indent=2))

if __name__ == '__main__':
    main()
