#!/usr/bin/env python3
import argparse, csv, gc, json, sys
from pathlib import Path
from collections import defaultdict, Counter

import torch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from tools.part_attention_supertrace_real_contract_v1 import LABELS, load_model, build_batch, wcsv, wjson
from tools.part_exact_route_patch_real_contract_v1 import role_positions

HQQL = LABELS.index('label_Hqql')
TBL = LABELS.index('label_Tbl')
DEFAULT_ROLES = ['CLS', 'electron', 'muon', 'charged_hadron', 'neutral_hadron', 'photon']


def read_csv(path):
    with open(path, newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))


def load_events(path, n_per_group):
    rows = read_csv(path)
    by = defaultdict(list)
    for r in rows:
        by[r['analysis_group']].append(r)
    out = []
    for g in ['A_Hqql_correct', 'B_Hqql_to_Tbl', 'C_Tbl_correct', 'D_Tbl_to_Hqql']:
        out += by[g][:n_per_group]
    return out


def role_pairs(roles):
    return [(q, k) for q in roles for k in roles]


def normalize_attn_mask(base, patch, q, legacy, B, H, T, S, strength):
    if base is None:
        return patch
    if base.dtype == torch.bool:
        basef = torch.zeros_like(base, dtype=q.dtype).masked_fill(base, -strength)
    else:
        basef = base.to(dtype=q.dtype)
    if legacy:
        if basef.ndim == 2:
            basef = basef.view(1, basef.shape[-2], basef.shape[-1]).expand(B * H, T, S)
        elif basef.ndim == 4:
            basef = basef.reshape(B * H, basef.shape[-2], basef.shape[-1])
        return basef + patch if basef.shape == patch.shape else base
    else:
        if basef.ndim == 2:
            basef = basef.view(1, 1, basef.shape[-2], basef.shape[-1]).expand(B, H, T, S)
        elif basef.ndim == 3:
            if basef.shape[0] == B * H:
                basef = basef.view(B, H, basef.shape[-2], basef.shape[-1])
            elif basef.shape[0] == 1:
                basef = basef.view(1, 1, basef.shape[-2], basef.shape[-1]).expand(B, H, T, S)
        elif basef.ndim == 4:
            if basef.shape[0] == 1 and basef.shape[1] == 1:
                basef = basef.expand(B, H, T, S)
            elif basef.shape[0] == B and basef.shape[1] == 1:
                basef = basef.expand(B, H, T, S)
        return basef + patch if basef.shape == patch.shape else base


class AllHeadRouteGradientTracer:
    def __init__(self, metas, pairs, scale=1.0):
        self.metas = metas
        self.pairs = pairs
        self.scale = float(scale)
        self.handles = []
        self.gates = {}
        self.hit_counts = defaultdict(int)
        self.meta_by_module = {}

    def _hook(self, name):
        def fn(module, args, kwargs):
            q, k, v = args[0], args[1], args[2]
            H = int(module.num_heads)
            legacy = hasattr(module, 'in_proj_weight') and not hasattr(module, 'in_proj')
            if legacy:
                T, B, _ = q.shape
                S = k.shape[0]
                patch = torch.zeros((B * H, T, S), device=q.device, dtype=q.dtype)
            else:
                B, T, _ = q.shape
                S = k.shape[1]
                patch = torch.zeros((B, H, T, S), device=q.device, dtype=q.dtype)

            if name not in self.gates:
                self.gates[name] = torch.zeros((H, len(self.pairs)), device=q.device, dtype=q.dtype, requires_grad=True)
                self.meta_by_module[name] = {'num_heads': H, 'legacy': legacy, 'T': T, 'S': S}
            gates = self.gates[name]

            hits = 0
            for pi, (qr, kr) in enumerate(self.pairs):
                for bi, meta in enumerate(self.metas):
                    qpos = role_positions(meta, qr, T, True)
                    kpos = role_positions(meta, kr, S, False)
                    if not qpos or not kpos:
                        continue
                    for qi in qpos:
                        for ki in kpos:
                            if legacy:
                                patch[bi * H:(bi + 1) * H, qi, ki] = patch[bi * H:(bi + 1) * H, qi, ki] + gates[:, pi] * self.scale
                            else:
                                patch[bi, :, qi, ki] = patch[bi, :, qi, ki] + gates[:, pi] * self.scale
                            hits += H
            self.hit_counts[name] += int(hits)
            if hits == 0:
                return args, kwargs
            kwargs['attn_mask'] = normalize_attn_mask(kwargs.get('attn_mask', None), patch, q, legacy, B, H, T, S, self.scale)
            return args, kwargs
        return fn

    def attach(self, model):
        for name, m in model.named_modules():
            is_new = hasattr(m, 'in_proj') and hasattr(m, 'num_heads') and hasattr(m, 'head_dim')
            is_legacy = hasattr(m, 'in_proj_weight') and hasattr(m, 'num_heads') and hasattr(m, 'head_dim')
            if is_new or is_legacy:
                self.handles.append(m.register_forward_pre_hook(self._hook(name), with_kwargs=True))
        if not self.handles:
            raise RuntimeError('no attention modules hooked')

    def close(self):
        for h in self.handles:
            h.remove()
        self.handles = []

    def rows(self, weight, objective):
        out = []
        for name, gate in self.gates.items():
            grad = gate.grad.detach().cpu() if gate.grad is not None else torch.zeros_like(gate.detach().cpu())
            H, P = grad.shape
            for h in range(H):
                for pi, (qr, kr) in enumerate(self.pairs):
                    val = float(grad[h, pi]) * weight
                    out.append({
                        'objective': objective,
                        'module': name,
                        'head': h,
                        'query_role': qr,
                        'key_role': kr,
                        'pair_role': qr + '<-' + kr,
                        'grad': val,
                        'abs_grad': abs(val),
                        'positive_grad': max(0.0, val),
                        'negative_grad': min(0.0, val),
                        'hit_count_module': self.hit_counts.get(name, 0),
                    })
        return out


def objective_value(logits, metas, mode):
    vals = []
    for i, m in enumerate(metas):
        g = m['analysis_group']
        if mode == 'signed_all':
            if g in ('B_Hqql_to_Tbl', 'C_Tbl_correct'):
                vals.append(logits[i, TBL] - logits[i, HQQL])
            else:
                vals.append(logits[i, HQQL] - logits[i, TBL])
        elif mode == 'B_tbl_minus_hqql':
            if g == 'B_Hqql_to_Tbl':
                vals.append(logits[i, TBL] - logits[i, HQQL])
        elif mode == 'A_hqql_minus_tbl':
            if g == 'A_Hqql_correct':
                vals.append(logits[i, HQQL] - logits[i, TBL])
        elif mode == 'D_hqql_minus_tbl':
            if g == 'D_Tbl_to_Hqql':
                vals.append(logits[i, HQQL] - logits[i, TBL])
        else:
            raise ValueError('unknown objective ' + mode)
    if not vals:
        return None
    return torch.stack(vals).mean()


def add_rows(acc, rows):
    for r in rows:
        k = (r['objective'], r['module'], str(r['head']), r['pair_role'])
        if k not in acc:
            acc[k] = dict(r)
        else:
            acc[k]['grad'] += r['grad']
            acc[k]['abs_grad'] = abs(acc[k]['grad'])
            acc[k]['positive_grad'] = max(0.0, acc[k]['grad'])
            acc[k]['negative_grad'] = min(0.0, acc[k]['grad'])
            acc[k]['hit_count_module'] += r.get('hit_count_module', 0)


def aggregate_from_acc(acc):
    rows = list(acc.values())
    for r in rows:
        r['abs_grad'] = abs(float(r['grad']))
    return sorted(rows, key=lambda r: r['abs_grad'], reverse=True)


def mdtab(headers, rows):
    if not rows:
        return '_No rows._\n'
    return '\n'.join(['| ' + ' | '.join(headers) + ' |', '| ' + ' | '.join(['---'] * len(headers)) + ' |'] + ['| ' + ' | '.join(str(x) for x in r) + ' |' for r in rows]) + '\n'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--groups-csv', default='reports/latest/tables/part_hqql_tbl_groups_direct_replay_v1.csv')
    ap.add_argument('--network-file', default='external/particle_transformer/networks/example_ParticleTransformer_legacy.py')
    ap.add_argument('--checkpoint', default='external/particle_transformer/models/ParT_kinpid.pt')
    ap.add_argument('--data-config', default='external/particle_transformer/data/JetClass/JetClass_kinpid.yaml')
    ap.add_argument('--events-per-group', type=int, default=32)
    ap.add_argument('--micro-batch', type=int, default=4)
    ap.add_argument('--roles', default=','.join(DEFAULT_ROLES))
    ap.add_argument('--objectives', default='signed_all,B_tbl_minus_hqql,A_hqql_minus_tbl,D_hqql_minus_tbl')
    ap.add_argument('--gate-scale', type=float, default=1.0)
    ap.add_argument('--device', default='cuda' if torch.cuda.is_available() else 'cpu')
    ap.add_argument('--out-md', default='reports/latest/PART_ALL_HEAD_ROUTE_GRADIENT_REAL_CONTRACT_V1.md')
    ap.add_argument('--out-csv', default='reports/latest/tables/part_all_head_route_gradient_real_contract_v1.csv')
    ap.add_argument('--out-json', default='manifests/latest/part_all_head_route_gradient_real_contract_v1.json')
    args = ap.parse_args()

    roles = [x.strip() for x in args.roles.split(',') if x.strip()]
    pairs = role_pairs(roles)
    objectives = [x.strip() for x in args.objectives.split(',') if x.strip()]
    events = load_events(args.groups_csv, args.events_per_group)
    device = torch.device(args.device)
    model, dc = load_model(args.network_file, args.checkpoint, args.data_config, device)

    acc = {}
    mb = max(1, args.micro_batch)
    for obj_name in objectives:
        for s in range(0, len(events), mb):
            sub = events[s:s + mb]
            pts, fts, vec, msk, metas = build_batch(sub, device, dc)
            model.zero_grad(set_to_none=True)
            tracer = AllHeadRouteGradientTracer(metas, pairs, scale=args.gate_scale)
            tracer.attach(model)
            logits = model(pts, fts, vec, msk)
            obj = objective_value(logits, metas, obj_name)
            if obj is not None:
                obj.backward()
                tracer.close()
                add_rows(acc, tracer.rows(len(sub) / max(1, len(events)), obj_name))
            else:
                tracer.close()
            del pts, fts, vec, msk, logits, obj
            if device.type == 'cuda':
                torch.cuda.empty_cache()
            gc.collect()

    rows = aggregate_from_acc(acc)
    Path(args.out_csv).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out_json).parent.mkdir(parents=True, exist_ok=True)
    wcsv(args.out_csv, rows)

    by_obj = defaultdict(list)
    for r in rows:
        by_obj[r['objective']].append(r)
    summary = {
        'ok': True,
        'events': len(events),
        'events_per_group': args.events_per_group,
        'micro_batch': args.micro_batch,
        'roles': roles,
        'pairs': len(pairs),
        'objectives': objectives,
        'rows': len(rows),
        'top': rows[:30],
    }
    wjson(args.out_json, summary)

    md = []
    md.append('# PART_ALL_HEAD_ROUTE_GRADIENT_REAL_CONTRACT_V1\n\n')
    md.append('Differentiable all-head all-role-route trace. Each `module/head/role_pair` gets a gate-bias inside attention, all gates are active in the same forward, and backward gives route sensitivity.\n\n')
    md.append(f'- events: **{len(events)}**\n')
    md.append(f'- events_per_group: **{args.events_per_group}**\n')
    md.append(f'- micro_batch: **{args.micro_batch}**\n')
    md.append(f'- roles: `{roles}`\n')
    md.append(f'- role_pairs: **{len(pairs)}**\n')
    md.append(f'- objectives: `{objectives}`\n')
    md.append(f'- rows: **{len(rows)}**\n')
    md.append(f'- gate_scale: **{args.gate_scale}**\n\n')
    for obj_name in objectives:
        top = by_obj.get(obj_name, [])[:25]
        md.append(f'## Top route gradients: `{obj_name}`\n')
        md.append(mdtab(['module', 'head', 'pair', 'grad', 'abs'], [[r['module'], r['head'], r['pair_role'], f"{float(r['grad']):.5e}", f"{float(r['abs_grad']):.5e}"] for r in top]))
        md.append('\n')
    md.append('## Reading\n\n')
    md.append('- Positive grad: increasing attention bias for this role-route increases the objective.\n')
    md.append('- For `B_tbl_minus_hqql`, positive means the route pushes Hqql mistakes toward Tbl; negative means it resists Tbl.\n')
    md.append('- This is the closest current implementation to “all heads simultaneously differentiable” route tracing.\n')
    Path(args.out_md).write_text(''.join(md), encoding='utf-8')
    print(json.dumps(summary, indent=2, ensure_ascii=False))


if __name__ == '__main__':
    main()
