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
GROUPS = ['A_Hqql_correct', 'B_Hqql_to_Tbl', 'C_Tbl_correct', 'D_Tbl_to_Hqql']


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
    for g in GROUPS:
        out += by[g][:n_per_group]
    return out


def role_pairs(roles):
    return [(q, k) for q in roles for k in roles]


def is_attention_module(m):
    return hasattr(m, 'num_heads') and hasattr(m, 'head_dim') and (hasattr(m, 'in_proj_weight') or hasattr(m, 'in_proj'))


class NaturalAttentionTracer:
    """Capture real per-head attention weights and gradients.

    This is NOT a synthetic route-gate. It forces nn.MultiheadAttention to return
    per-head attention weights, retains grad on those weights, and later aggregates
    A, grad_A, and A*grad_A by physical particle roles.
    """
    def __init__(self):
        self.records = []
        self.handles = []

    def _pre_hook(self, name):
        def fn(module, args, kwargs):
            # Keep output behavior the same for callers using [0], but ask PyTorch to
            # keep per-head weights instead of averaged weights.
            kwargs['need_weights'] = True
            kwargs['average_attn_weights'] = False
            return args, kwargs
        return fn

    def _fwd_hook(self, name):
        def fn(module, args, kwargs, out):
            if not isinstance(out, tuple) or len(out) < 2:
                return
            weights = out[1]
            if not torch.is_tensor(weights):
                return
            # Expected with average_attn_weights=False: [B,H,T,S]. Some PyTorch paths
            # may return [B*H,T,S]; normalize at aggregation time.
            if weights.requires_grad:
                weights.retain_grad()
            self.records.append({'name': name, 'num_heads': int(module.num_heads), 'weights': weights})
        return fn

    def attach(self, model):
        for name, m in model.named_modules():
            if is_attention_module(m):
                self.handles.append(m.register_forward_pre_hook(self._pre_hook(name), with_kwargs=True))
                self.handles.append(m.register_forward_hook(self._fwd_hook(name), with_kwargs=True))
        if not self.handles:
            raise RuntimeError('no attention modules hooked')

    def close(self):
        for h in self.handles:
            h.remove()
        self.handles = []


def objective_value(logits, metas, mode):
    vals = []
    for i, m in enumerate(metas):
        g = m['analysis_group']
        if mode == 'signed_hqql_tbl':
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


def normalize_weights(w, B, H):
    # Return [B,H,T,S]
    if w.ndim == 4:
        if w.shape[0] == B:
            return w
        # sometimes [H,B,T,S]
        if w.shape[1] == B:
            return w.permute(1, 0, 2, 3)
    if w.ndim == 3 and w.shape[0] == B * H:
        return w.view(B, H, w.shape[-2], w.shape[-1])
    if w.ndim == 3 and w.shape[0] == B:
        # averaged heads. Keep as one pseudo-head if this happens.
        return w.view(B, 1, w.shape[-2], w.shape[-1])
    return None


def add_stat(acc, key, a_sum, g_sum, ag_sum, n, weight):
    if key not in acc:
        acc[key] = {'A_sum': 0.0, 'grad_sum': 0.0, 'Agrad_sum': 0.0, 'n': 0.0}
    acc[key]['A_sum'] += float(a_sum) * weight
    acc[key]['grad_sum'] += float(g_sum) * weight
    acc[key]['Agrad_sum'] += float(ag_sum) * weight
    acc[key]['n'] += float(n) * weight


def aggregate_records(records, metas, pairs, objective, weight):
    acc = {}
    B = len(metas)
    for rec in records:
        H = int(rec['num_heads'])
        w = rec['weights']
        grad = w.grad
        if grad is None:
            continue
        ww = normalize_weights(w.detach().float().cpu(), B, H)
        gg = normalize_weights(grad.detach().float().cpu(), B, H)
        if ww is None or gg is None:
            continue
        B2, H2, T, S = ww.shape
        for h in range(H2):
            for pi, (qr, kr) in enumerate(pairs):
                for bi, meta in enumerate(metas):
                    qpos = role_positions(meta, qr, T, True)
                    kpos = role_positions(meta, kr, S, False)
                    if not qpos or not kpos:
                        continue
                    vals = ww[bi, h][qpos][:, kpos].reshape(-1)
                    grads = gg[bi, h][qpos][:, kpos].reshape(-1)
                    if vals.numel() == 0:
                        continue
                    a_sum = float(vals.sum())
                    g_sum = float(grads.sum())
                    ag_sum = float((vals * grads).sum())
                    key = (objective, rec['name'], h, qr + '<-' + kr, meta['analysis_group'])
                    add_stat(acc, key, a_sum, g_sum, ag_sum, vals.numel(), weight)
    return acc


def merge_acc(dst, src):
    for k, v in src.items():
        if k not in dst:
            dst[k] = dict(v)
        else:
            for kk in ['A_sum', 'grad_sum', 'Agrad_sum', 'n']:
                dst[k][kk] += v[kk]


def rows_from_acc(acc):
    rows = []
    for (objective, module, head, pair, group), v in acc.items():
        n = max(1e-12, float(v['n']))
        mean_A = v['A_sum'] / n
        mean_grad = v['grad_sum'] / n
        mean_Agrad = v['Agrad_sum'] / n
        rows.append({
            'objective': objective,
            'module': module,
            'head': head,
            'head_id': f'{module}.h{head}',
            'pair_role': pair,
            'analysis_group': group,
            'mean_A': mean_A,
            'mean_grad_A': mean_grad,
            'mean_AxGrad': mean_Agrad,
            'abs_mean_AxGrad': abs(mean_Agrad),
            'n_links': v['n'],
        })
    return sorted(rows, key=lambda r: r['abs_mean_AxGrad'], reverse=True)


def make_summary_rows(rows):
    # Pivot by objective/head/pair: keep group-specific Agrad and useful contrasts.
    by = defaultdict(dict)
    for r in rows:
        key = (r['objective'], r['head_id'], r['pair_role'])
        by[key][r['analysis_group']] = r
    out = []
    for (objective, hid, pair), d in by.items():
        b = d.get('B_Hqql_to_Tbl', {})
        a = d.get('A_Hqql_correct', {})
        c = d.get('C_Tbl_correct', {})
        dd = d.get('D_Tbl_to_Hqql', {})
        row = {
            'objective': objective,
            'head_id': hid,
            'pair_role': pair,
            'B_mean_A': b.get('mean_A', 0.0),
            'B_mean_AxGrad': b.get('mean_AxGrad', 0.0),
            'A_mean_AxGrad': a.get('mean_AxGrad', 0.0),
            'C_mean_AxGrad': c.get('mean_AxGrad', 0.0),
            'D_mean_AxGrad': dd.get('mean_AxGrad', 0.0),
            'B_minus_A_AxGrad': b.get('mean_AxGrad', 0.0) - a.get('mean_AxGrad', 0.0),
            'B_minus_C_AxGrad': b.get('mean_AxGrad', 0.0) - c.get('mean_AxGrad', 0.0),
            'abs_B_mean_AxGrad': abs(b.get('mean_AxGrad', 0.0)),
            'support_score': abs(b.get('mean_AxGrad', 0.0)) + abs(b.get('mean_AxGrad', 0.0) - a.get('mean_AxGrad', 0.0)) * 0.5,
        }
        out.append(row)
    return sorted(out, key=lambda r: r['support_score'], reverse=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--groups-csv', default='reports/latest/tables/part_hqql_tbl_groups_direct_replay_v1.csv')
    ap.add_argument('--network-file', default='external/particle_transformer/networks/example_ParticleTransformer_legacy.py')
    ap.add_argument('--checkpoint', default='external/particle_transformer/models/ParT_kinpid.pt')
    ap.add_argument('--data-config', default='external/particle_transformer/data/JetClass/JetClass_kinpid.yaml')
    ap.add_argument('--events-per-group', type=int, default=32)
    ap.add_argument('--micro-batch', type=int, default=4)
    ap.add_argument('--roles', default=','.join(DEFAULT_ROLES))
    ap.add_argument('--objectives', default='signed_hqql_tbl,B_tbl_minus_hqql')
    ap.add_argument('--device', default='cuda' if torch.cuda.is_available() else 'cpu')
    ap.add_argument('--out-md', default='reports/latest/PART_NATURAL_ATTENTION_GRAD_REAL_CONTRACT_V1.md')
    ap.add_argument('--out-rows', default='reports/latest/tables/part_natural_attention_grad_real_contract_v1_rows.csv')
    ap.add_argument('--out-summary', default='reports/latest/tables/part_natural_attention_grad_real_contract_v1_summary.csv')
    ap.add_argument('--out-json', default='manifests/latest/part_natural_attention_grad_real_contract_v1.json')
    args = ap.parse_args()

    roles = [x.strip() for x in args.roles.split(',') if x.strip()]
    pairs = role_pairs(roles)
    objectives = [x.strip() for x in args.objectives.split(',') if x.strip()]
    events = select_events(args.groups_csv, args.events_per_group)
    device = torch.device(args.device)
    model, dc = load_model(args.network_file, args.checkpoint, args.data_config, device)

    global_acc = {}
    mb = max(1, args.micro_batch)
    for obj_name in objectives:
        for s in range(0, len(events), mb):
            sub_events = events[s:s + mb]
            pts, fts, vec, msk, metas = build_batch(sub_events, device, dc)
            model.zero_grad(set_to_none=True)
            tracer = NaturalAttentionTracer()
            tracer.attach(model)
            logits = model(pts, fts, vec, msk)
            obj = objective_value(logits, metas, obj_name)
            if obj is not None:
                obj.backward()
                local_acc = aggregate_records(tracer.records, metas, pairs, obj_name, len(sub_events) / max(1, len(events)))
                merge_acc(global_acc, local_acc)
            tracer.close()
            del pts, fts, vec, msk, logits, obj, tracer
            gc.collect()
            if device.type == 'cuda':
                torch.cuda.empty_cache()

    rows = rows_from_acc(global_acc)
    summary_rows = make_summary_rows(rows)
    wcsv(args.out_rows, rows)
    wcsv(args.out_summary, summary_rows)
    summary = {
        'ok': True,
        'events': len(events),
        'events_per_group': args.events_per_group,
        'micro_batch': args.micro_batch,
        'roles': roles,
        'role_pairs': len(pairs),
        'objectives': objectives,
        'rows': len(rows),
        'summary_rows': len(summary_rows),
        'top': summary_rows[:30],
    }
    wjson(args.out_json, summary)

    by_obj = defaultdict(list)
    for r in summary_rows:
        by_obj[r['objective']].append(r)
    md = ['# PART_NATURAL_ATTENTION_GRAD_REAL_CONTRACT_V1\n\n',
          'Natural attention A×grad trace over current direct-replay ParT groups. This captures real per-head attention weights from nn.MultiheadAttention, retains gradients on them, and aggregates A, grad_A, and A*grad_A by physical role-pairs. No synthetic route gate is inserted.\n\n',
          f'- events: **{len(events)}**\n', f'- events_per_group: **{args.events_per_group}**\n', f'- micro_batch: **{args.micro_batch}**\n',
          f'- roles: `{roles}`\n', f'- role_pairs: **{len(pairs)}**\n', f'- objectives: `{objectives}`\n', f'- rows: **{len(rows)}**\n\n']
    for obj_name in objectives:
        top = by_obj.get(obj_name, [])[:30]
        md += [f'## Top natural attention role-links: `{obj_name}`\n',
               mdtab(['rank','head','pair','B_A','B_AxGrad','B-A','B-C','support'], [[i+1, r['head_id'], r['pair_role'], fmt(r['B_mean_A']), fmt(r['B_mean_AxGrad']), fmt(r['B_minus_A_AxGrad']), fmt(r['B_minus_C_AxGrad']), fmt(r['support_score'])] for i, r in enumerate(top)]), '\n']
    md += ['## Interpretation\n\n',
           '- `mean_A`: how much natural attention mass uses this role-link.\n',
           '- `mean_AxGrad`: attention mass weighted by objective gradient. This is the important one: active links that also matter for Hqql/Tbl.\n',
           '- For `B_tbl_minus_hqql`, positive B_AxGrad means the natural link pushes Hqql mistakes toward Tbl; negative means it resists that margin.\n',
           '- This is the missing bridge between attention visualization and matrix-program evidence: real A, real grad_A, physical role-pair aggregation.\n']
    Path(args.out_md).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out_md).write_text(''.join(md), encoding='utf-8')
    print(json.dumps({'ok': True, 'events': len(events), 'rows': len(rows), 'summary_rows': len(summary_rows), 'out_md': args.out_md}, indent=2))


if __name__ == '__main__':
    main()
