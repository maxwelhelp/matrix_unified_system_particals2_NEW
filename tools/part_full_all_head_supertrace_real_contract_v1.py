#!/usr/bin/env python3
import argparse, csv, gc, json, sys
from pathlib import Path
from collections import defaultdict, Counter

import torch
import torch.nn.functional as F

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from tools.part_attention_supertrace_real_contract_v1 import LABELS, load_model, build_batch, wcsv, wjson

HQQL = LABELS.index('label_Hqql')
TBL = LABELS.index('label_Tbl')


def fmt(x):
    try:
        x = float(x)
    except Exception:
        return 'n/a'
    return f'{x:.3e}' if abs(x) > 0 and (abs(x) < 1e-3 or abs(x) > 1e4) else f'{x:.4f}'


def mdtab(headers, rows):
    if not rows:
        return '_No rows._\n'
    return '\n'.join(['| ' + ' | '.join(headers) + ' |', '| ' + ' | '.join(['---'] * len(headers)) + ' |'] + ['| ' + ' | '.join(str(x) for x in r) + ' |' for r in rows]) + '\n'


def read_csv(path):
    with open(path, newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))


def select_events(path, n_per_group):
    rows = read_csv(path)
    by = defaultdict(list)
    for r in rows:
        by[r['analysis_group']].append(r)
    out = []
    for g in ['A_Hqql_correct', 'B_Hqql_to_Tbl', 'C_Tbl_correct', 'D_Tbl_to_Hqql']:
        out += by[g][:n_per_group]
    return out


def tensor_batch(batch, start, end):
    pts, fts, vec, msk = batch
    return (pts[start:end], fts[start:end], vec[start:end], msk[start:end])


def baseline_logits(model, batch):
    pts, fts, vec, msk = batch
    with torch.no_grad():
        return model(pts, fts, vec, msk).detach()


def split_head_ranges(C, H):
    return [(h, (C*h)//H, (C*(h+1))//H) for h in range(H) if (C*h)//H < (C*(h+1))//H]


def is_attention_module(m):
    return hasattr(m, 'num_heads') and hasattr(m, 'head_dim') and (hasattr(m, 'in_proj_weight') or hasattr(m, 'in_proj'))


class HeadGateTracer:
    def __init__(self):
        self.gates = {}
        self.meta = {}
        self.handles = []

    def _hook(self, name):
        def hook(module, args, out):
            x = out[0] if isinstance(out, tuple) else out
            if not torch.is_tensor(x) or x.ndim != 3:
                return out
            H = int(module.num_heads)
            C = int(x.shape[-1])
            ranges = split_head_ranges(C, H)
            if name not in self.gates:
                self.gates[name] = torch.ones((len(ranges),), device=x.device, dtype=x.dtype, requires_grad=True)
                self.meta[name] = {'ranges': ranges, 'num_heads': H, 'channels': C}
            gate = self.gates[name]
            # No in-place slice writes: legacy MultiheadAttention returns views that autograd
            # needs unchanged for backward. Build the gated tensor by concatenation instead.
            parts = []
            last = 0
            for idx, (_, a, b) in enumerate(ranges):
                if a > last:
                    parts.append(x[..., last:a])
                parts.append(x[..., a:b] * gate[idx])
                last = b
            if last < C:
                parts.append(x[..., last:C])
            y = torch.cat(parts, dim=-1)
            if isinstance(out, tuple):
                return (y,) + out[1:]
            return y
        return hook

    def attach(self, model):
        for name, m in model.named_modules():
            if is_attention_module(m):
                self.handles.append(m.register_forward_hook(self._hook(name)))
        if not self.handles:
            raise RuntimeError('no attention modules found for HeadGateTracer')

    def close(self):
        for h in self.handles:
            h.remove()
        self.handles = []

    def grad_rows(self, objective, weight):
        rows = []
        for name, gate in self.gates.items():
            grad = gate.grad.detach().float().cpu() if gate.grad is not None else torch.zeros_like(gate.detach().float().cpu())
            for idx, (head, a, b) in enumerate(self.meta[name]['ranges']):
                g = float(grad[idx]) * weight
                rows.append({
                    'objective': objective,
                    'module': name,
                    'head': head,
                    'head_id': f'{name}.h{head}',
                    'channels': f'ch{a}:{b}',
                    'grad': g,
                    'abs_grad': abs(g),
                    'positive_grad': max(0.0, g),
                    'negative_grad': min(0.0, g),
                })
        return rows


class HeadEnergyCapture:
    def __init__(self, metas):
        self.metas = metas
        self.handles = []
        self.rows = []

    def _align_energy_to_particles(self, energy, mask_len):
        # energy: [B,T] or [T,B] already converted to [B,T]
        B, T = energy.shape
        if T == mask_len + 1:
            return energy[:, 1:]
        if T == mask_len:
            return energy
        n = min(T, mask_len)
        return energy[:, :n]

    def _hook(self, name):
        def hook(module, args, out):
            x = out[0] if isinstance(out, tuple) else out
            if not torch.is_tensor(x) or x.ndim != 3:
                return
            B = len(self.metas)
            # Legacy MHA is [T,B,C]; batch-first variants are [B,T,C].
            if x.shape[1] == B:
                xb = x.permute(1, 0, 2).detach()
            elif x.shape[0] == B:
                xb = x.detach()
            else:
                return
            H = int(module.num_heads)
            C = int(xb.shape[-1])
            ranges = split_head_ranges(C, H)
            for head, a, b in ranges:
                en = torch.sqrt((xb[..., a:b].float() ** 2).sum(dim=-1) + 1e-12)  # [B,T]
                self.rows.append({'module': name, 'head': head, 'head_id': f'{name}.h{head}', 'energy': en.cpu()})
        return hook

    def attach(self, model):
        for name, m in model.named_modules():
            if is_attention_module(m):
                self.handles.append(m.register_forward_hook(self._hook(name)))
        if not self.handles:
            raise RuntimeError('no attention modules found for HeadEnergyCapture')

    def close(self):
        for h in self.handles:
            h.remove()
        self.handles = []


def add_grad(acc, rows):
    for r in rows:
        k = (r['objective'], r['module'], str(r['head']), r['head_id'], r['channels'])
        if k not in acc:
            acc[k] = dict(r)
        else:
            acc[k]['grad'] += float(r['grad'])
            acc[k]['abs_grad'] = abs(acc[k]['grad'])
            acc[k]['positive_grad'] = max(0.0, acc[k]['grad'])
            acc[k]['negative_grad'] = min(0.0, acc[k]['grad'])


def grad_list(acc):
    out = list(acc.values())
    for r in out:
        r['abs_grad'] = abs(float(r['grad']))
    return sorted(out, key=lambda r: r['abs_grad'], reverse=True)


def objective_value(logits, metas, base_pred, objective):
    if objective == 'pred_logit':
        return logits.gather(1, base_pred[:, None]).mean()
    vals = []
    for i, m in enumerate(metas):
        g = m['analysis_group']
        if objective == 'signed_hqql_tbl':
            # Supports current prediction regime: A/D Hqql-like, B/C Tbl-like.
            if g in ('B_Hqql_to_Tbl', 'C_Tbl_correct'):
                vals.append(logits[i, TBL] - logits[i, HQQL])
            else:
                vals.append(logits[i, HQQL] - logits[i, TBL])
        elif objective == 'B_tbl_minus_hqql':
            if g == 'B_Hqql_to_Tbl':
                vals.append(logits[i, TBL] - logits[i, HQQL])
        elif objective == 'A_hqql_minus_tbl':
            if g == 'A_Hqql_correct':
                vals.append(logits[i, HQQL] - logits[i, TBL])
        else:
            raise ValueError('unknown objective ' + objective)
    if not vals:
        return None
    return torch.stack(vals).mean()


def role_for(meta, pi):
    roles = meta.get('roles') or []
    if 0 <= pi < len(roles):
        return roles[pi]
    return 'unknown'


def build_super_scores(energy_rows, metas, mask, grad_lookup):
    # returns event rows + particle rows for a microbatch
    B = len(metas)
    mask_cpu = mask.detach().cpu().bool()
    if mask_cpu.ndim == 3:
        mask_cpu = mask_cpu[:, 0, :]
    mask_len = int(mask_cpu.shape[1])
    super_score = torch.zeros((B, mask_len), dtype=torch.float32)
    contribs = []
    for er in energy_rows:
        hid = er['head_id']
        w = float(grad_lookup.get(hid, 0.0))
        if abs(w) < 1e-12:
            continue
        en = er['energy'].float()
        # Convert [B,T] to [B,N_particles]
        if en.shape[0] != B:
            continue
        if en.shape[1] == mask_len + 1:
            en = en[:, 1:]
        elif en.shape[1] != mask_len:
            n = min(en.shape[1], mask_len)
            tmp = torch.zeros((B, mask_len), dtype=en.dtype)
            tmp[:, :n] = en[:, :n]
            en = tmp
        en = en / (en.amax(dim=1, keepdim=True) + 1e-9)
        super_score += w * en
        contribs.append((hid, w))
    super_score = super_score.masked_fill(~mask_cpu, -1e9)
    return super_score, contribs


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--groups-csv', default='reports/latest/tables/part_hqql_tbl_groups_direct_replay_v1.csv')
    ap.add_argument('--network-file', default='external/particle_transformer/networks/example_ParticleTransformer_legacy.py')
    ap.add_argument('--checkpoint', default='external/particle_transformer/models/ParT_kinpid.pt')
    ap.add_argument('--data-config', default='external/particle_transformer/data/JetClass/JetClass_kinpid.yaml')
    ap.add_argument('--events-per-group', type=int, default=64)
    ap.add_argument('--micro-batch', type=int, default=8)
    ap.add_argument('--objectives', default='pred_logit,signed_hqql_tbl')
    ap.add_argument('--top-events', type=int, default=80)
    ap.add_argument('--top-particles', type=int, default=8)
    ap.add_argument('--device', default='cuda' if torch.cuda.is_available() else 'cpu')
    ap.add_argument('--out-md', default='reports/latest/PART_FULL_ALL_HEAD_SUPERTRACE_REAL_CONTRACT_V1.md')
    ap.add_argument('--out-json', default='manifests/latest/part_full_all_head_supertrace_real_contract_v1.json')
    ap.add_argument('--out-grad', default='reports/latest/tables/part_full_all_head_supertrace_head_gradients_v1.csv')
    ap.add_argument('--out-events', default='reports/latest/tables/part_full_all_head_supertrace_events_v1.csv')
    ap.add_argument('--out-particles', default='reports/latest/tables/part_full_all_head_supertrace_particles_v1.csv')
    ap.add_argument('--out-classes', default='reports/latest/tables/part_full_all_head_supertrace_class_summary_v1.csv')
    args = ap.parse_args()

    objectives = [x.strip() for x in args.objectives.split(',') if x.strip()]
    events = select_events(args.groups_csv, args.events_per_group)
    device = torch.device(args.device)
    model, dc = load_model(args.network_file, args.checkpoint, args.data_config, device)

    # Build one tensor batch for the selected direct replay events.
    pts, fts, vec, msk, metas = build_batch(events, device, dc)
    batch = (pts, fts, vec, msk)
    B = int(pts.shape[0])
    mb = max(1, int(args.micro_batch))

    base_chunks = []
    for s in range(0, B, mb):
        base_chunks.append(baseline_logits(model, tensor_batch(batch, s, min(B, s + mb))).cpu())
        if device.type == 'cuda':
            torch.cuda.empty_cache()
    base = torch.cat(base_chunks, dim=0)
    pred = base.argmax(dim=1)
    prob = F.softmax(base.float(), dim=1)

    # Differentiable all-head gate gradients.
    grad_acc = {}
    objective_means = {}
    for obj_name in objectives:
        weighted_obj = 0.0
        for s in range(0, B, mb):
            e = min(B, s + mb)
            sub = tensor_batch(batch, s, e)
            sub_metas = metas[s:e]
            sub_pred = pred[s:e].to(device)
            model.zero_grad(set_to_none=True)
            tracer = HeadGateTracer()
            tracer.attach(model)
            logits = model(*sub)
            obj = objective_value(logits, sub_metas, sub_pred, obj_name)
            if obj is not None:
                obj.backward()
                weight = (e - s) / max(1, B)
                add_grad(grad_acc, tracer.grad_rows(obj_name, weight))
                weighted_obj += float(obj.detach().cpu()) * weight
            tracer.close()
            del logits, obj, tracer
            gc.collect()
            if device.type == 'cuda':
                torch.cuda.empty_cache()
        objective_means[obj_name] = weighted_obj

    grad_rows = grad_list(grad_acc)
    # Use positive pred_logit grads as old supertrace weights; fallback abs.
    pred_grad = [r for r in grad_rows if r['objective'] == 'pred_logit']
    if sum(max(0.0, float(r['grad'])) for r in pred_grad) > 1e-12:
        grad_lookup = {r['head_id']: max(0.0, float(r['grad'])) for r in pred_grad}
        weight_note = 'positive pred_logit gate gradient'
    else:
        grad_lookup = {r['head_id']: abs(float(r['grad'])) for r in pred_grad}
        weight_note = 'abs pred_logit gate gradient fallback'

    # Capture natural head energies and build all-head particle super-score.
    event_rows = []
    particle_rows = []
    class_acc = defaultdict(lambda: {'n': 0, 'correct': 0, 'score_sum': 0.0, 'scores': []})
    for s in range(0, B, mb):
        e = min(B, s + mb)
        sub = tensor_batch(batch, s, e)
        sub_metas = metas[s:e]
        cap = HeadEnergyCapture(sub_metas)
        cap.attach(model)
        with torch.no_grad():
            _ = model(*sub)
        cap.close()
        score, contribs = build_super_scores(cap.rows, sub_metas, sub[3], grad_lookup)
        score_cpu = score.cpu()
        mask_cpu = sub[3].detach().cpu().bool()
        if mask_cpu.ndim == 3:
            mask_cpu = mask_cpu[:, 0, :]
        for i, meta in enumerate(sub_metas):
            gi = s + i
            real_n = int(mask_cpu[i].sum()) if mask_cpu.numel() else int(score_cpu.shape[1])
            k = min(args.top_particles, max(1, real_n), int(score_cpu.shape[1]))
            top_idx = torch.topk(score_cpu[i], k).indices.tolist()
            pred_i = int(pred[gi])
            true_label = meta.get('true_label', '')
            pred_label = LABELS[pred_i]
            correct = int(true_label == pred_label)
            ev_score = float(score_cpu[i].max())
            event_rows.append({
                'event_local': gi,
                'analysis_group': meta.get('analysis_group', ''),
                'source_group': meta.get('source_group', ''),
                'entry_idx': meta.get('entry_idx', ''),
                'true_label': true_label,
                'pred_label': pred_label,
                'conf': float(prob[gi, pred_i]),
                'pred_logit': float(base[gi, pred_i]),
                'super_max_particle_score': ev_score,
                'real_particles': real_n,
                'top_particle_indices': json.dumps(top_idx),
            })
            class_acc[pred_label]['n'] += 1
            class_acc[pred_label]['correct'] += correct
            class_acc[pred_label]['score_sum'] += ev_score
            class_acc[pred_label]['scores'].append(ev_score)
            for rank, pi in enumerate(top_idx, 1):
                particle_rows.append({
                    'event_local': gi,
                    'rank': rank,
                    'particle_idx': pi,
                    'particle_role': role_for(meta, pi),
                    'super_score': float(score_cpu[i, pi]),
                    'analysis_group': meta.get('analysis_group', ''),
                    'true_label': true_label,
                    'pred_label': pred_label,
                })
        del cap, score
        gc.collect()
        if device.type == 'cuda':
            torch.cuda.empty_cache()

    event_rows = sorted(event_rows, key=lambda r: float(r['super_max_particle_score']), reverse=True)
    top_event_ids = set(r['event_local'] for r in event_rows[:args.top_events])
    particle_rows = [r for r in particle_rows if r['event_local'] in top_event_ids]
    particle_rows = sorted(particle_rows, key=lambda r: (r['event_local'], r['rank']))

    class_rows = []
    for lbl, d in sorted(class_acc.items()):
        scores = torch.tensor(d['scores'], dtype=torch.float32) if d['scores'] else torch.tensor([0.0])
        class_rows.append({
            'pred_label': lbl,
            'n_pred': d['n'],
            'super_score_mean': d['score_sum'] / max(1, d['n']),
            'super_score_p90': float(torch.quantile(scores, 0.9)),
            'acc_within_pred': d['correct'] / max(1, d['n']),
        })

    wcsv(args.out_grad, grad_rows)
    wcsv(args.out_events, event_rows[:args.top_events])
    wcsv(args.out_particles, particle_rows)
    wcsv(args.out_classes, class_rows)

    summary = {
        'ok': True,
        'events': B,
        'events_per_group': args.events_per_group,
        'micro_batch': mb,
        'objectives': objectives,
        'objective_means': objective_means,
        'weight_note': weight_note,
        'n_head_grad_rows': len(grad_rows),
        'top_heads_by_abs_grad': grad_rows[:30],
        'top_events': event_rows[:20],
        'class_summary': class_rows,
        'network_file': args.network_file,
        'checkpoint': args.checkpoint,
        'data_config': args.data_config,
        'groups_csv': args.groups_csv,
    }
    wjson(args.out_json, summary)

    by_obj = defaultdict(list)
    for r in grad_rows:
        by_obj[r['objective']].append(r)

    md = ['# PART_FULL_ALL_HEAD_SUPERTRACE_REAL_CONTRACT_V1\n\n',
          'ParT port of the old ParticleNet all-head differentiable supertrace. It gates every attention head output slice simultaneously, backpropagates objectives through all gates, then builds an all-head particle super-score from natural head-output energies weighted by gate gradients.\n\n',
          f'- events: **{B}**\n', f'- events_per_group: **{args.events_per_group}**\n', f'- micro_batch: **{mb}**\n',
          f'- objectives: `{objectives}`\n', f'- weight_note: `{weight_note}`\n', f'- head_grad_rows: **{len(grad_rows)}**\n',
          f'- groups_csv: `{args.groups_csv}`\n\n']
    for obj_name in objectives:
        rows = by_obj.get(obj_name, [])[:30]
        md += [f'## Top differentiable head gates: `{obj_name}`\n',
               mdtab(['rank', 'head', 'grad', 'abs_grad', 'channels'], [[i+1, r['head_id'], fmt(r['grad']), fmt(r['abs_grad']), r['channels']] for i, r in enumerate(rows)]), '\n']
    md += ['## Class summary by predicted class\n',
           mdtab(['pred_label','n_pred','super_mean','super_p90','acc_within_pred'], [[r['pred_label'], r['n_pred'], fmt(r['super_score_mean']), fmt(r['super_score_p90']), fmt(r['acc_within_pred'])] for r in class_rows]),
           '\n## Top events by all-head super-score\n',
           mdtab(['event','group','true','pred','conf','super_max','real_particles','top_particle_indices'], [[r['event_local'], r['analysis_group'], r['true_label'], r['pred_label'], fmt(r['conf']), fmt(r['super_max_particle_score']), r['real_particles'], r['top_particle_indices']] for r in event_rows[:args.top_events]]),
           '\n## Top particles inside top events\n',
           mdtab(['event','rank','particle','role','super_score','group','pred'], [[r['event_local'], r['rank'], r['particle_idx'], r['particle_role'], fmt(r['super_score']), r['analysis_group'], r['pred_label']] for r in particle_rows[:200]]),
           '\n## Interpretation\n\nThis is the full all-head map for current ParT replay groups. Read it like the old supertrace: all heads are active together, gradients rank which head slices support the objective, and particle super-score shows where the weighted multi-head computation concentrates. Use this before single-route/bundle probes.\n']
    Path(args.out_md).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out_md).write_text(''.join(md), encoding='utf-8')
    print(json.dumps({'ok': True, 'events': B, 'head_grad_rows': len(grad_rows), 'out_md': args.out_md}, indent=2))


if __name__ == '__main__':
    main()
