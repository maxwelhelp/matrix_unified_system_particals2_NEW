#!/usr/bin/env python3
import argparse, csv, json, math, sys
from pathlib import Path
from collections import defaultdict
import torch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools.particlenet_real_patch_controls_v1 import load_balanced
from tools.particle0_topk_controls_v2 import make_model, real_mask, pt_values
from data.jetclass_tiny_loader_v3_official import LABELS

HQQL = LABELS.index('label_Hqql')
TBL = LABELS.index('label_Tbl')


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


def mdtab(h, rs):
    if not rs: return '_No rows._\n'
    out = ['| ' + ' | '.join(h) + ' |', '| ' + ' | '.join(['---'] * len(h)) + ' |']
    for r in rs: out.append('| ' + ' | '.join(str(x).replace('\n', ' ') for x in r) + ' |')
    return '\n'.join(out) + '\n'


def parse_heads(s):
    heads = []
    for item in str(s).split(','):
        item = item.strip()
        if not item: continue
        # L2:128:160 or L2_ch128:160
        item = item.replace('_ch', ':')
        parts = item.split(':')
        if len(parts) != 3 or not parts[0].startswith('L'):
            raise ValueError(f'Bad head spec: {item}; use L2:128:160')
        layer = int(parts[0][1:]); start = int(parts[1]); end = int(parts[2])
        heads.append({'head_id': f'L{layer}_ch{start}:{end}', 'layer': layer, 'start': start, 'end': end})
    return heads


def slice_batch(batch, idx):
    idx = torch.as_tensor(idx, dtype=torch.long, device=batch['y'].device)
    out = {}
    B = batch['y'].shape[0]
    for k, v in batch.items():
        if torch.is_tensor(v) and v.shape and v.shape[0] == B:
            out[k] = v.index_select(0, idx)
        else:
            out[k] = v
    return out


def pid_name(feat, bi, pi):
    if feat.shape[1] < 11: return 'no_pid'
    vals = {'charged_hadron': float(feat[bi,6,pi]), 'neutral_hadron': float(feat[bi,7,pi]), 'photon': float(feat[bi,8,pi]), 'electron': float(feat[bi,9,pi]), 'muon': float(feat[bi,10,pi])}
    return max(vals.items(), key=lambda kv: kv[1])[0]


def get_effective_classifier_direction(model):
    # Approximate effective class direction from pooled final EdgeConv channels to logits.
    # Works for common ParticleNet fc: Linear(C->H) ... Linear(H->num_classes).
    linears = []
    for m in getattr(model, 'fc', model).modules():
        if isinstance(m, torch.nn.Linear):
            linears.append(m)
    if not linears:
        return None, 'no_linear_layers_found'
    try:
        W = linears[0].weight.detach().float().cpu()  # [H, C]
        for lin in linears[1:]:
            W = lin.weight.detach().float().cpu() @ W
        return W, f'effective_linear_approx_from_{len(linears)}_linear_layers'
    except Exception as e:
        return None, f'failed_effective_classifier_direction:{e}'


def capture_activations(model, batch, heads):
    captures = {}
    hooks = []
    target_layers = sorted(set(h['layer'] for h in heads))
    def mk(layer):
        def hook(module, inp, out):
            x = out[0] if isinstance(out, (tuple, list)) else out
            captures[layer] = x.detach().float().cpu()
        return hook
    for layer in target_layers:
        hooks.append(model.edge_convs[layer].register_forward_hook(mk(layer)))
    with torch.no_grad(): logits = model(batch['points'], batch['features'], batch['mask']).detach().cpu()
    for h in hooks: h.remove()
    return logits, captures


def logits_with_zeroed_head(model, batch, head):
    hooks = []
    layer, s, e = head['layer'], head['start'], head['end']
    def hook(module, inp, out):
        if isinstance(out, (tuple, list)):
            x = out[0].clone(); x[:, s:e, :] = 0
            return (x,) + tuple(out[1:])
        x = out.clone(); x[:, s:e, :] = 0
        return x
    hooks.append(model.edge_convs[layer].register_forward_hook(hook))
    with torch.no_grad(): logits = model(batch['points'], batch['features'], batch['mask']).detach().cpu()
    for h in hooks: h.remove()
    return logits


def masked_mean_act(act, mask, s, e):
    # act [B,C,N], mask [B,N]
    x = act[:, s:e, :]
    m = mask.float().unsqueeze(1)
    return (x * m).sum(dim=2) / m.sum(dim=2).clamp_min(1.0)


def group_ids_from_phase(phase, iso_thr):
    A, B = [], []
    for r in phase:
        if r.get('true_label') != 'label_Hqql': continue
        if fnum(r.get('particle0_iso_pt_ratio')) < iso_thr: continue
        ei = int(fnum(r.get('event_index'), -1))
        if r.get('group') == 'Hqql_correct': A.append(ei)
        elif r.get('group') == 'Hqql_to_Tbl': B.append(ei)
    return sorted(set(A)), sorted(set(B))


def select_tbl_correct(batch, logits, max_c):
    y = batch['y'].detach().cpu().long(); pred = logits.argmax(1).long()
    ids = [i for i in range(len(y)) if int(y[i]) == TBL and int(pred[i]) == TBL]
    return ids[:max_c]


def mean(xs, k):
    vals = [float(x[k]) for x in xs if k in x and x[k] != '']
    return sum(vals)/len(vals) if vals else 0.0


def dist2(a, b):
    return math.sqrt(sum((a[i]-b[i])**2 for i in range(len(a))))


def diagnose(row):
    # Uses projection means, not final proof.
    B = [row['B_score_hqql_mean'], row['B_score_tbl_mean']]
    A = [row['A_score_hqql_mean'], row['A_score_tbl_mean']]
    C = [row['C_score_hqql_mean'], row['C_score_tbl_mean']]
    dba, dbc = dist2(B, A), dist2(B, C)
    if dbc < dba and row['B_score_tbl_mean'] >= row['A_score_tbl_mean']:
        return 'active_tbl_like_readout_candidate'
    if row['B_score_hqql_mean'] < row['A_score_hqql_mean'] and row['B_score_tbl_mean'] <= row['C_score_tbl_mean']:
        return 'lost_hqql_evidence_candidate'
    return 'mixed_or_unclear'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--phase1-events', default='reports/latest/tables/hqql_tbl_confusion_physics_events.csv')
    ap.add_argument('--checkpoint', default='local_checkpoints/part/ParticleNet_kinpid.pt')
    ap.add_argument('--data-dir', default=str(Path.home()/'Рабочий стол/jetclass_tiny_balanced'))
    ap.add_argument('--mode', default='kinpid')
    ap.add_argument('--samples-per-file', type=int, default=4096)
    ap.add_argument('--max-files', type=int, default=1000)
    ap.add_argument('--heads', default='L2:128:160,L2:160:192,L2:224:256,L1:32:48,L1:80:96,L2:0:32,L2:32:64')
    ap.add_argument('--isolation-threshold', type=float, default=0.30)
    ap.add_argument('--max-tbl-correct', type=int, default=128)
    ap.add_argument('--device', default='cuda' if torch.cuda.is_available() else 'cpu')
    ap.add_argument('--out-md', default='reports/latest/INTERNAL_ACTIVATION_CONTRAST_V2.md')
    ap.add_argument('--out-events', default='reports/latest/tables/internal_activation_contrast_v2_events.csv')
    ap.add_argument('--out-particles', default='reports/latest/tables/internal_activation_contrast_v2_top_particles.csv')
    ap.add_argument('--out-heads', default='reports/latest/tables/internal_activation_contrast_v2_head_summary.csv')
    ap.add_argument('--out-json', default='manifests/latest/internal_activation_contrast_v2.json')
    args = ap.parse_args()

    heads = parse_heads(args.heads)
    phase = readcsv(args.phase1_events)
    Aids, Bids = group_ids_from_phase(phase, args.isolation_threshold)

    model, res = make_model(args.checkpoint, args.mode, args.device)
    batch = load_balanced(args.data_dir, mode=args.mode, samples_per_file=args.samples_per_file, max_files=args.max_files, device=args.device)
    # Baseline logits over full loaded batch only to select C.
    with torch.no_grad():
        full_logits = []
        step = 256 if args.device.startswith('cuda') else 128
        for s in range(0, batch['y'].shape[0], step):
            sub = slice_batch(batch, list(range(s, min(batch['y'].shape[0], s+step))))
            full_logits.append(model(sub['points'], sub['features'], sub['mask']).detach().cpu())
        full_logits = torch.cat(full_logits, 0)
    Cids = select_tbl_correct(batch, full_logits, args.max_tbl_correct)

    all_ids = Aids + Bids + Cids
    groups = ['A_protected_highiso']*len(Aids) + ['B_confused_highiso']*len(Bids) + ['C_Tbl_correct']*len(Cids)
    if not all_ids:
        raise RuntimeError('No A/B/C events selected')
    max_e = max(all_ids)
    if max_e >= batch['y'].shape[0]:
        raise RuntimeError(f'event index {max_e} >= loaded B={batch["y"].shape[0]}; increase SAMPLES_PER_FILE/MAX_FILES')

    sub = slice_batch(batch, all_ids)
    base_logits, caps = capture_activations(model, sub, heads)
    mask = real_mask(sub).detach().cpu().bool()
    pt = pt_values(sub).detach().cpu()
    feat = sub['features'].detach().cpu()
    W, W_note = get_effective_classifier_direction(model)

    event_rows, particle_rows = [], []
    group_by_local = {i: groups[i] for i in range(len(all_ids))}
    id_by_local = {i: all_ids[i] for i in range(len(all_ids))}

    # Precompute ablation logits per head.
    ablated = {h['head_id']: logits_with_zeroed_head(model, sub, h) for h in heads}

    for h in heads:
        hid, layer, s, e = h['head_id'], h['layer'], h['start'], h['end']
        act = caps[layer]
        if e > act.shape[1]:
            continue
        ev = masked_mean_act(act, mask, s, e)  # [B, width]
        # Projection direction. If effective W unavailable or incompatible, leave 0 and note.
        if W is not None and W.shape[1] >= e:
            wh = W[HQQL, s:e]
            wt = W[TBL, s:e]
            proj_h = (ev @ wh).tolist()
            proj_t = (ev @ wt).tolist()
        else:
            proj_h = [0.0] * ev.shape[0]
            proj_t = [0.0] * ev.shape[0]
        norms = ev.norm(dim=1).tolist()
        zero_logits = ablated[hid]
        for bi in range(len(all_ids)):
            base = base_logits[bi]
            zl = zero_logits[bi]
            event_rows.append({
                'event_idx': id_by_local[bi], 'group': group_by_local[bi], 'head_id': hid, 'layer': layer, 'channels': f'{s}:{e}',
                'score_hqql_proj': float(proj_h[bi]), 'score_tbl_proj': float(proj_t[bi]), 'activation_norm': float(norms[bi]),
                'base_logit_hqql': float(base[HQQL]), 'base_logit_tbl': float(base[TBL]),
                'zero_logit_hqql': float(zl[HQQL]), 'zero_logit_tbl': float(zl[TBL]),
                'contrib_hqql_logit_drop_when_zeroed': float(base[HQQL] - zl[HQQL]),
                'contrib_tbl_logit_drop_when_zeroed': float(base[TBL] - zl[TBL]),
                'base_pred': LABELS[int(base.argmax())], 'zero_pred': LABELS[int(zl.argmax())],
                'projection_note': W_note,
            })
            # top particles by slice norm
            x = act[bi, s:e, :].transpose(0,1)  # [N,width]
            pn = x.norm(dim=1)
            valid = torch.where(mask[bi])[0]
            if len(valid) > 0:
                vals = pn[valid]
                topk = torch.topk(vals, min(3, len(vals))).indices
                for rank, rel in enumerate(topk.tolist(), 1):
                    pi = int(valid[rel])
                    particle_rows.append({
                        'event_idx': id_by_local[bi], 'group': group_by_local[bi], 'head_id': hid, 'rank': rank,
                        'particle_idx': pi, 'particle_activation_norm': float(pn[pi]), 'pid': pid_name(feat, bi, pi),
                        'pt': float(pt[bi, pi]), 'charge': float(feat[bi,5,pi]) if feat.shape[1] > 5 else 0.0,
                        'is_second_lepton_like': '',
                    })

    # Head summary.
    rows_by_head = defaultdict(list)
    for r in event_rows: rows_by_head[r['head_id']].append(r)
    head_rows = []
    for hid, xs in rows_by_head.items():
        by = {g: [r for r in xs if r['group'] == g] for g in ['A_protected_highiso','B_confused_highiso','C_Tbl_correct']}
        row = {'head_id': hid, 'n_A': len(by['A_protected_highiso']), 'n_B': len(by['B_confused_highiso']), 'n_C': len(by['C_Tbl_correct'])}
        for prefix, group in [('A','A_protected_highiso'),('B','B_confused_highiso'),('C','C_Tbl_correct')]:
            row[prefix+'_score_hqql_mean'] = mean(by[group], 'score_hqql_proj')
            row[prefix+'_score_tbl_mean'] = mean(by[group], 'score_tbl_proj')
            row[prefix+'_activation_norm_mean'] = mean(by[group], 'activation_norm')
            row[prefix+'_contrib_hqql_drop_mean'] = mean(by[group], 'contrib_hqql_logit_drop_when_zeroed')
            row[prefix+'_contrib_tbl_drop_mean'] = mean(by[group], 'contrib_tbl_logit_drop_when_zeroed')
        Bv = [row['B_score_hqql_mean'], row['B_score_tbl_mean']]
        Av = [row['A_score_hqql_mean'], row['A_score_tbl_mean']]
        Cv = [row['C_score_hqql_mean'], row['C_score_tbl_mean']]
        row['dist_BA_projection'] = dist2(Bv, Av)
        row['dist_BC_projection'] = dist2(Bv, Cv)
        row['B_closer_to_C_score'] = row['dist_BA_projection'] - row['dist_BC_projection']
        row['B_minus_A_hqql_projection'] = row['B_score_hqql_mean'] - row['A_score_hqql_mean']
        row['B_minus_A_tbl_projection'] = row['B_score_tbl_mean'] - row['A_score_tbl_mean']
        row['B_minus_A_hqql_contrib_drop'] = row['B_contrib_hqql_drop_mean'] - row['A_contrib_hqql_drop_mean']
        row['B_minus_A_tbl_contrib_drop'] = row['B_contrib_tbl_drop_mean'] - row['A_contrib_tbl_drop_mean']
        row['diagnosis'] = diagnose(row)
        head_rows.append(row)
    head_rows = sorted(head_rows, key=lambda r: abs(r['B_closer_to_C_score']) + abs(r['B_minus_A_hqql_contrib_drop']) + abs(r['B_minus_A_tbl_contrib_drop']), reverse=True)

    wcsv(args.out_events, event_rows)
    wcsv(args.out_particles, particle_rows)
    wcsv(args.out_heads, head_rows)
    wjson(args.out_json, {'ok': True, 'A': len(Aids), 'B': len(Bids), 'C': len(Cids), 'heads': [h['head_id'] for h in heads], 'projection_note': W_note, 'missing': list(res.missing_keys), 'unexpected': list(res.unexpected_keys)})

    md = ['# INTERNAL_ACTIVATION_CONTRAST_V2\n\n',
          'Direct hook-based A/B/C activation contrast. Includes approximate class-direction projection and safer zero-slice ablation contribution.\n\n',
          f'- A protected_highiso: **{len(Aids)}**\n', f'- B confused_highiso: **{len(Bids)}**\n', f'- C Tbl_correct: **{len(Cids)}**\n', f'- projection: `{W_note}`\n\n',
          '## Head diagnosis summary\n',
          mdtab(['head','diag','B_close_C','B-A hqql_proj','B-A tbl_proj','B-A hqql_contrib','B-A tbl_contrib','A hqql/tbl','B hqql/tbl','C hqql/tbl'], [[r['head_id'], r['diagnosis'], fmt(r['B_closer_to_C_score']), fmt(r['B_minus_A_hqql_projection']), fmt(r['B_minus_A_tbl_projection']), fmt(r['B_minus_A_hqql_contrib_drop']), fmt(r['B_minus_A_tbl_contrib_drop']), f"{fmt(r['A_score_hqql_mean'])}/{fmt(r['A_score_tbl_mean'])}", f"{fmt(r['B_score_hqql_mean'])}/{fmt(r['B_score_tbl_mean'])}", f"{fmt(r['C_score_hqql_mean'])}/{fmt(r['C_score_tbl_mean'])}"] for r in head_rows]),
          '\n## Interpretation guide\n\n',
          '- `active_tbl_like_readout_candidate`: B is closer to C than A in projected class-evidence space.\n',
          '- `lost_hqql_evidence_candidate`: B loses Hqql projection/contribution without clean Tbl-like activation.\n',
          '- `mixed_or_unclear`: inspect event rows and top particles.\n',
          '\nUse `internal_activation_contrast_v2_top_particles.csv` to check whether top activations in B land on second leptons, particle0/lepton, or hadronic neighbors.\n']
    Path(args.out_md).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out_md).write_text(''.join(md), encoding='utf-8')
    print(json.dumps({'ok': True, 'A': len(Aids), 'B': len(Bids), 'C': len(Cids), 'out_md': args.out_md}, indent=2))


if __name__ == '__main__':
    main()
