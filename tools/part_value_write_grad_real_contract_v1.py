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
GROUP_NAMES = ['A_Hqql_correct', 'B_Hqql_to_Tbl', 'C_Tbl_correct', 'D_Tbl_to_Hqql']


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
    for g in GROUP_NAMES:
        out += by[g][:n_per_group]
    return out


def role_pairs(roles):
    return [(q, k) for q in roles for k in roles]


def is_legacy_mha(m):
    return hasattr(m, 'in_proj_weight') and hasattr(m, 'out_proj') and hasattr(m, 'num_heads') and hasattr(m, 'head_dim')


def apply_attn_mask(mask, scores, B, H, T, S):
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


class ManualValueWriteRecorder:
    """Manual legacy MHA forward that exposes value/write path.

    Records:
    - A: real QK softmax attention [B,H,T,S]
    - V: projected value vectors [B,H,S,D]
    - context: A@V before output projection [B,H,T,D]

    After backward, context.grad tells how each head write vector affects the objective.
    A[q,k] * dot(V[k], grad_context[q]) is the signed write contribution of key-role k
    to query-role q through this attention head.
    """
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
        def forward(module, query, key, value, key_padding_mask=None, need_weights=False, attn_mask=None, average_attn_weights=True, is_causal=False):
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

            q_proj, k_proj, v_proj = F._in_projection_packed(q_in, k_in, v_in, module.in_proj_weight, module.in_proj_bias)
            qh = q_proj.contiguous().view(T, B, H, D).permute(1, 2, 0, 3) * (1.0 / math.sqrt(D))
            kh = k_proj.contiguous().view(S, B, H, D).permute(1, 2, 0, 3)
            vh = v_proj.contiguous().view(S, B, H, D).permute(1, 2, 0, 3)

            scores = torch.matmul(qh, kh.transpose(-2, -1))
            scores = apply_attn_mask(attn_mask, scores, B, H, T, S)
            if key_padding_mask is not None:
                kpm = key_padding_mask.to(device=scores.device).bool()
                scores = scores.masked_fill(kpm.view(B, 1, 1, S), float('-inf'))

            A = torch.softmax(scores, dim=-1)
            context = torch.matmul(A, vh)  # [B,H,T,D]
            A.retain_grad()
            context.retain_grad()
            recorder.records.append({'name': name, 'num_heads': H, 'A': A, 'V': vh, 'context': context})

            merged = context.permute(2, 0, 1, 3).contiguous().view(T, B, E)
            out = F.linear(merged, module.out_proj.weight, module.out_proj.bias)
            if batch_first:
                out = out.transpose(0, 1)
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


def add_stat(acc, key, a_sum, write_sum, abs_write_sum, grad_norm_sum, v_norm_sum, n, weight):
    if key not in acc:
        acc[key] = {'A_sum': 0.0, 'write_sum': 0.0, 'abs_write_sum': 0.0, 'grad_norm_sum': 0.0, 'v_norm_sum': 0.0, 'n': 0.0}
    acc[key]['A_sum'] += float(a_sum) * weight
    acc[key]['write_sum'] += float(write_sum) * weight
    acc[key]['abs_write_sum'] += float(abs_write_sum) * weight
    acc[key]['grad_norm_sum'] += float(grad_norm_sum) * weight
    acc[key]['v_norm_sum'] += float(v_norm_sum) * weight
    acc[key]['n'] += float(n) * weight


def aggregate_records(records, metas, pairs, objective, weight):
    acc = {}
    B = len(metas)
    for rec in records:
        A = rec['A']
        V = rec['V']
        C = rec['context']
        G = C.grad
        if G is None:
            continue
        aa = A.detach().float().cpu()
        vv = V.detach().float().cpu()
        gg = G.detach().float().cpu()
        _, H, T, S = aa.shape
        for h in range(H):
            for qr, kr in pairs:
                for bi, meta in enumerate(metas):
                    qpos = role_positions(meta, qr, T, True)
                    kpos = role_positions(meta, kr, S, False)
                    if not qpos or not kpos:
                        continue
                    a_vals = aa[bi, h][qpos][:, kpos]             # [Q,K]
                    g_vals = gg[bi, h][qpos]                     # [Q,D]
                    v_vals = vv[bi, h][kpos]                     # [K,D]
                    if a_vals.numel() == 0:
                        continue
                    # contribution[q,k] = A[q,k] * dot(V[k], grad_context[q])
                    dot = torch.einsum('qd,kd->qk', g_vals, v_vals)
                    write = a_vals * dot
                    grad_norm = torch.sqrt((g_vals ** 2).sum(dim=-1) + 1e-12).mean()
                    v_norm = torch.sqrt((v_vals ** 2).sum(dim=-1) + 1e-12).mean()
                    key = (objective, rec['name'], h, qr + '<-' + kr, meta['analysis_group'])
                    add_stat(acc, key, float(a_vals.sum()), float(write.sum()), float(write.abs().sum()), float(grad_norm), float(v_norm), a_vals.numel(), weight)
    return acc


def merge_acc(dst, src):
    for k, v in src.items():
        if k not in dst:
            dst[k] = dict(v)
        else:
            for kk in ['A_sum', 'write_sum', 'abs_write_sum', 'grad_norm_sum', 'v_norm_sum', 'n']:
                dst[k][kk] += v[kk]


def rows_from_acc(acc):
    rows = []
    for (objective, module, head, pair, group), v in acc.items():
        n = max(1e-12, float(v['n']))
        rows.append({
            'objective': objective,
            'module': module,
            'head': head,
            'head_id': f'{module}.h{head}',
            'pair_role': pair,
            'analysis_group': group,
            'mean_A': v['A_sum'] / n,
            'mean_write_dot_grad': v['write_sum'] / n,
            'mean_abs_write_dot_grad': v['abs_write_sum'] / n,
            'mean_context_grad_norm': v['grad_norm_sum'] / n,
            'mean_value_norm': v['v_norm_sum'] / n,
            'n_links': v['n'],
        })
    return sorted(rows, key=lambda r: r['mean_abs_write_dot_grad'], reverse=True)


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
            'B_write_dot_grad': b.get('mean_write_dot_grad', 0.0),
            'B_abs_write_dot_grad': b.get('mean_abs_write_dot_grad', 0.0),
            'A_write_dot_grad': a.get('mean_write_dot_grad', 0.0),
            'C_write_dot_grad': c.get('mean_write_dot_grad', 0.0),
            'D_write_dot_grad': dd.get('mean_write_dot_grad', 0.0),
            'B_minus_A_write': b.get('mean_write_dot_grad', 0.0) - a.get('mean_write_dot_grad', 0.0),
            'B_minus_C_write': b.get('mean_write_dot_grad', 0.0) - c.get('mean_write_dot_grad', 0.0),
            'B_value_norm': b.get('mean_value_norm', 0.0),
            'B_context_grad_norm': b.get('mean_context_grad_norm', 0.0),
        }
        row['support_score'] = abs(row['B_write_dot_grad']) + abs(row['B_minus_A_write']) * 0.5 + row['B_abs_write_dot_grad'] * 0.25
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
    ap.add_argument('--out-md', default='reports/latest/PART_VALUE_WRITE_GRAD_REAL_CONTRACT_V1.md')
    ap.add_argument('--out-rows', default='reports/latest/tables/part_value_write_grad_real_contract_v1_rows.csv')
    ap.add_argument('--out-summary', default='reports/latest/tables/part_value_write_grad_real_contract_v1_summary.csv')
    ap.add_argument('--out-json', default='manifests/latest/part_value_write_grad_real_contract_v1.json')
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
            recorder = ManualValueWriteRecorder()
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
        'note': 'manual MHA forward with real A, V, context=A@V; write score is A[q,k] * dot(V[k], grad_context[q])',
    }
    wjson(args.out_json, obj)

    by_obj = defaultdict(list)
    for r in summary_rows:
        by_obj[r['objective']].append(r)
    md = ['# PART_VALUE_WRITE_GRAD_REAL_CONTRACT_V1\n\n',
          'Value/write contribution trace using manual legacy MHA forward. It computes real `A`, projected `V`, and `context=A@V`; after backward it aggregates `A[q,k] * dot(V[k], grad_context[q])` by physical role-pairs. This answers not only where attention looks, but what value/write signal the looked-at particle contributes to the objective.\n\n',
          f'- events: **{len(events)}**\n', f'- events_per_group: **{args.events_per_group}**\n', f'- micro_batch: **{args.micro_batch}**\n',
          f'- roles: `{roles}`\n', f'- role_pairs: **{len(pairs)}**\n', f'- objectives: `{objectives}`\n', f'- rows: **{len(rows)}**\n\n']
    for obj_name in objectives:
        top = by_obj.get(obj_name, [])[:30]
        md += [f'## Top value/write role-links: `{obj_name}`\n',
               mdtab(['rank','head','pair','B_A','B_write','B_abs_write','B-A','B-C','V_norm','grad_norm','support'], [[i+1, r['head_id'], r['pair_role'], fmt(r['B_mean_A']), fmt(r['B_write_dot_grad']), fmt(r['B_abs_write_dot_grad']), fmt(r['B_minus_A_write']), fmt(r['B_minus_C_write']), fmt(r['B_value_norm']), fmt(r['B_context_grad_norm']), fmt(r['support_score'])] for i, r in enumerate(top)]), '\n']
    md += ['## Interpretation\n\n',
           '- `B_write`: signed value/write contribution for B_Hqql_to_Tbl. Positive means the value written through this role-link increases the objective; negative resists it.\n',
           '- `B_abs_write`: magnitude regardless of sign; high values mean the role-link writes a strong signal even if mixed.\n',
           '- `V_norm` and `grad_norm` separate whether the link is strong because the value vector is large or because the downstream objective is sensitive.\n',
           '- This is the missing write-side evidence to connect natural attention routes to matrix-program effects.\n']
    Path(args.out_md).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out_md).write_text(''.join(md), encoding='utf-8')
    print(json.dumps({'ok': True, 'events': len(events), 'rows': len(rows), 'summary_rows': len(summary_rows), 'out_md': args.out_md}, indent=2))


if __name__ == '__main__':
    main()
