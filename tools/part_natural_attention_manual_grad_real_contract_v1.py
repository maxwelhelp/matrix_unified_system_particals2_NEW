#!/usr/bin/env python3
import argparse, csv, gc, json, math, sys, types
from pathlib import Path
from collections import defaultdict

import torch
import torch.nn.functional as F

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


def is_legacy_mha(m):
    return hasattr(m, 'in_proj_weight') and hasattr(m, 'out_proj') and hasattr(m, 'num_heads') and hasattr(m, 'head_dim')


def to_attn_mask(mask, scores, B, H, T, S):
    if mask is None:
        return scores
    am = mask
    if am.dtype == torch.bool:
        am = torch.zeros_like(am, dtype=scores.dtype).masked_fill(am, float('-inf'))
    else:
        am = am.to(dtype=scores.dtype)
    am = am.to(device=scores.device)
    if am.ndim == 2:
        am = am.view(1, 1, am.shape[-2], am.shape[-1])
    elif am.ndim == 3:
        if am.shape[0] == B * H:
            am = am.view(B, H, am.shape[-2], am.shape[-1])
        elif am.shape[0] == B:
            am = am.view(B, 1, am.shape[-2], am.shape[-1])
        elif am.shape[0] == 1:
            am = am.view(1, 1, am.shape[-2], am.shape[-1])
    elif am.ndim == 4:
        pass
    if am.shape[-2:] == (T, S):
        scores = scores + am
    return scores


class ManualAttentionARecorder:
    def __init__(self):
        self.records = []
        self.original = []

    def patch_model(self, model):
        for name, m in model.named_modules():
            if is_legacy_mha(m):
                old = m.forward
                self.original.append((m, old))
                m.forward = types.MethodType(self._make_forward(name), m)
        if not self.original:
            raise RuntimeError('no legacy MultiheadAttention modules patched')

    def restore(self):
        for m, old in self.original:
            m.forward = old
        self.original = []

    def _make_forward(self, name):
        recorder = self
        def forward(module, query, key, value, key_padding_mask=None, need_weights=True, attn_mask=None, average_attn_weights=True, is_causal=False):
            # Supports legacy seq-first MHA used by ParticleTransformer_legacy.
            batch_first = bool(getattr(module, 'batch_first', False))
            if batch_first:
                q_in = query.transpose(0, 1)
                k_in = key.transpose(0, 1)
                v_in = value.transpose(0, 1)
            else:
                q_in, k_in, v_in = query, key, value
            T, B, E = q_in.shape
            S = k_in.shape[0]
            H = int(module.num_heads)
            D = int(module.head_dim)
            # Packed projection. ParT calls self-attention, but this supports q/k/v generally.
            q_proj, k_proj, v_proj = F._in_projection_packed(q_in, k_in, v_in, module.in_proj_weight, module.in_proj_bias)
            qh = q_proj.contiguous().view(T, B, H, D).permute(1, 2, 0, 3) * (1.0 / math.sqrt(D))
            kh = k_proj.contiguous().view(S, B, H, D).permute(1, 2, 0, 3)
            vh = v_proj.contiguous().view(S, B, H, D).permute(1, 2, 0, 3)
            scores = torch.matmul(qh, kh.transpose(-2, -1))
            scores = to_attn_mask(attn_mask, scores, B, H, T, S)
            if key_padding_mask is not None:
                kpm = key_padding_mask.to(device=scores.device).bool()
                scores = scores.masked_fill(kpm.view(B, 1, 1, S), float('-inf'))
            A = torch.softmax(scores, dim=-1)
            A.retain_grad()
            recorder.records.append({'name': name, 'num_heads': H, 'A': A})
            out_heads = torch.matmul(A, vh)  # [B,H,T,D]
            merged = out_heads.permute(2, 0, 1, 3).contiguous().view(T, B, E)
            out = F.linear(merged, module.out_proj.weight, module.out_proj.bias)
            if batch_first:
                out = out.transpose(0, 1)
            # Preserve original API enough for ParticleTransformer: caller uses [0].
            if average_attn_weights:
                weights = A.mean(dim=1)
            else:
                weights = A
            return out, weights
        return forward


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
        A = rec['A']
        G = A.grad
        if G is None:
            continue
        ww = A.detach().float().cpu()
        gg = G.detach().float().cpu()
        _, H, T, S = ww.shape
        for h in range(H):
            for qr, kr in pairs:
                for bi, meta in enumerate(metas):
                    qpos = role_positions(meta, qr, T, True)
                    kpos = role_positions(meta, kr, S, False)
                    if not qpos or not kpos:
                        continue
                    vals = ww[bi, h][qpos][:, kpos].reshape(-1)
                    grads = gg[bi, h][qpos][:, kpos].reshape(-1)
                    if vals.numel() == 0:
                        continue
                    key = (objective, rec['name'], h, qr + '<-' + kr, meta['analysis_group'])
                    add_stat(acc, key, float(vals.sum()), float(grads.sum()), float((vals * grads).sum()), vals.numel(), weight)
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
    by = defaultdict(dict)
    for r in rows:
        by[(r['objective'], r['head_id'], r['pair_role'])][r['analysis_group']] = r
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
        }
        row['support_score'] = row['abs_B_mean_AxGrad'] + abs(row['B_minus_A_AxGrad']) * 0.5
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
    ap.add_argument('--out-md', default='reports/latest/PART_NATURAL_ATTENTION_MANUAL_GRAD_REAL_CONTRACT_V1.md')
    ap.add_argument('--out-rows', default='reports/latest/tables/part_natural_attention_manual_grad_real_contract_v1_rows.csv')
    ap.add_argument('--out-summary', default='reports/latest/tables/part_natural_attention_manual_grad_real_contract_v1_summary.csv')
    ap.add_argument('--out-json', default='manifests/latest/part_natural_attention_manual_grad_real_contract_v1.json')
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
            recorder = ManualAttentionARecorder()
            recorder.patch_model(model)
            logits = model(pts, fts, vec, msk)
            obj = objective_value(logits, metas, obj_name)
            if obj is not None:
                obj.backward()
                local_acc = aggregate_records(recorder.records, metas, pairs, obj_name, len(sub_events) / max(1, len(events)))
                merge_acc(global_acc, local_acc)
            recorder.restore()
            del pts, fts, vec, msk, logits, obj, recorder
            gc.collect()
            if device.type == 'cuda':
                torch.cuda.empty_cache()

    rows = rows_from_acc(global_acc)
    summary_rows = make_summary_rows(rows)
    wcsv(args.out_rows, rows)
    wcsv(args.out_summary, summary_rows)
    obj = {
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
        'note': 'manual MHA forward, real QK softmax A with retained gradient; no synthetic route gate',
    }
    wjson(args.out_json, obj)

    by_obj = defaultdict(list)
    for r in summary_rows:
        by_obj[r['objective']].append(r)
    md = ['# PART_NATURAL_ATTENTION_MANUAL_GRAD_REAL_CONTRACT_V1\n\n',
          'Natural attention A×grad trace using manual legacy MHA forward. This computes real QK softmax attention `A`, retains `grad_A`, and aggregates `A`, `grad_A`, `A*grad_A` by physical role-pairs. No synthetic route gate is inserted.\n\n',
          f'- events: **{len(events)}**\n', f'- events_per_group: **{args.events_per_group}**\n', f'- micro_batch: **{args.micro_batch}**\n',
          f'- roles: `{roles}`\n', f'- role_pairs: **{len(pairs)}**\n', f'- objectives: `{objectives}`\n', f'- rows: **{len(rows)}**\n\n']
    for obj_name in objectives:
        top = by_obj.get(obj_name, [])[:30]
        md += [f'## Top natural attention role-links: `{obj_name}`\n',
               mdtab(['rank','head','pair','B_A','B_AxGrad','B-A','B-C','support'], [[i+1, r['head_id'], r['pair_role'], fmt(r['B_mean_A']), fmt(r['B_mean_AxGrad']), fmt(r['B_minus_A_AxGrad']), fmt(r['B_minus_C_AxGrad']), fmt(r['support_score'])] for i, r in enumerate(top)]), '\n']
    md += ['## Interpretation\n\n',
           '- `mean_A`: natural attention mass on this role-link.\n',
           '- `mean_AxGrad`: attention mass times objective gradient. Active links with large |A×grad| are real attention links that matter for Hqql/Tbl.\n',
           '- For `B_tbl_minus_hqql`, positive B_AxGrad pushes Hqql mistakes toward Tbl; negative resists Tbl.\n',
           '- This fixes the previous `rows=0` issue by manually computing the attention graph instead of relying on returned PyTorch weights.\n']
    Path(args.out_md).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out_md).write_text(''.join(md), encoding='utf-8')
    print(json.dumps({'ok': True, 'events': len(events), 'rows': len(rows), 'summary_rows': len(summary_rows), 'out_md': args.out_md}, indent=2))


if __name__ == '__main__':
    main()
