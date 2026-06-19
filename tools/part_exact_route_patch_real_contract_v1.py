#!/usr/bin/env python3
import argparse, csv, json, math, gc, sys
from pathlib import Path
from collections import defaultdict, Counter

import torch
import torch.nn.functional as F

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from tools.part_attention_supertrace_real_contract_v1 import (
    LABELS, SRC, TGT, load_groups, load_model, build_batch, wcsv, wjson
)

HQQL = LABELS.index(SRC)
TBL = LABELS.index(TGT)


def fnum(x, d=0.0):
    try:
        return float(x)
    except Exception:
        return d


def read_csv(path):
    with open(path, newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))


def split_pair(pair):
    if '<-' not in pair:
        return pair, ''
    return pair.split('<-', 1)


def pick_rules(path, topn):
    rows = read_csv(path)
    usable = []
    seen = set()
    for r in rows:
        key = (r.get('module'), str(r.get('head')), r.get('route') or r.get('pair'))
        if key in seen:
            continue
        seen.add(key)
        pair = r.get('route') or r.get('pair') or r.get('pair_role') or ''
        if '<-' not in pair or 'pad' in pair:
            continue
        r['pair'] = pair
        r['score'] = abs(fnum(r.get('gate_grad', 0.0))) * max(1e-6, fnum(r.get('rule_strength', r.get('strength', 1.0))))
        usable.append(r)
    usable.sort(key=lambda x: x['score'], reverse=True)
    return usable[:topn]


def select_events(rows, n):
    by = defaultdict(list)
    for r in rows:
        by[r['analysis_group']].append(r)
    out = []
    for g in ['A_Hqql_correct', 'B_Hqql_to_Tbl', 'C_Tbl_correct', 'D_Tbl_to_Hqql']:
        out += by[g][:n]
    return out


def role_positions(meta, role, seq_len, is_query):
    if role == 'CLS':
        return [0] if seq_len == 1 or seq_len == 129 else []
    offset = 1 if (seq_len == 129 and not is_query) else 0
    pos = []
    for i, r in enumerate(meta['roles']):
        j = i + offset
        if j >= seq_len:
            continue
        if r == role:
            pos.append(j)
    return pos


class ExactRoutePatch:
    def __init__(self, module_name, head, pair, metas, strength=40.0):
        self.module_name = module_name
        self.head = int(head)
        self.q_role, self.k_role = split_pair(pair)
        self.metas = metas
        self.strength = float(strength)
        self.handle = None

    def pre_hook(self, module, args, kwargs):
        q, k, v = args[0], args[1], args[2]
        B, T, _ = q.shape
        S = k.shape[1]
        H = int(module.num_heads)
        if self.head < 0 or self.head >= H:
            return args, kwargs
        patch = torch.zeros((B, H, T, S), device=q.device, dtype=q.dtype)
        hits = 0
        for bi, meta in enumerate(self.metas):
            qpos = role_positions(meta, self.q_role, T, True)
            kpos = role_positions(meta, self.k_role, S, False)
            if not qpos or not kpos:
                continue
            patch[bi, self.head, :, :] += 0.0
            for qi in qpos:
                for ki in kpos:
                    patch[bi, self.head, qi, ki] -= self.strength
                    hits += 1
        if hits == 0:
            return args, kwargs
        base = kwargs.get('attn_mask', None)
        if base is None:
            kwargs['attn_mask'] = patch
        else:
            if base.dtype == torch.bool:
                basef = torch.zeros_like(base, dtype=q.dtype).masked_fill(base, -self.strength)
            else:
                basef = base.to(dtype=q.dtype)
            # Weaver ParticleTransformer expects attn_mask as (B, H, T, S), not PyTorch MHA (B*H, T, S).
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
            if basef.shape == patch.shape:
                kwargs['attn_mask'] = basef + patch
            else:
                # Shape mismatch fallback: do not patch instead of corrupting attention.
                kwargs['attn_mask'] = base
        return args, kwargs

    def attach(self, model):
        found = False
        for name, m in model.named_modules():
            if name == self.module_name:
                self.handle = m.register_forward_pre_hook(self.pre_hook, with_kwargs=True)
                found = True
                break
        if not found:
            raise RuntimeError(f'module not found: {self.module_name}')

    def close(self):
        if self.handle is not None:
            self.handle.remove()
            self.handle = None


def forward_logits(model, batch, metas=None, rule=None, strength=40.0):
    pts, fts, vec, msk = batch
    hook = None
    if rule is not None:
        hook = ExactRoutePatch(rule['module'], rule['head'], rule['pair'], metas, strength=strength)
        hook.attach(model)
    with torch.no_grad():
        logits = model(pts, fts, vec, msk).detach().cpu()
    if hook is not None:
        hook.close()
    return logits


def metrics(logits, metas):
    pred = logits.argmax(dim=1).tolist()
    h = logits[:, HQQL].float()
    t = logits[:, TBL].float()
    out = defaultdict(lambda: {'n': 0, 'tbl_minus_hqql': 0.0, 'hqql_minus_tbl': 0.0, 'tbl_pred': 0, 'hqql_pred': 0})
    for i, meta in enumerate(metas):
        g = meta['analysis_group']
        out[g]['n'] += 1
        out[g]['tbl_minus_hqql'] += float(t[i] - h[i])
        out[g]['hqql_minus_tbl'] += float(h[i] - t[i])
        out[g]['tbl_pred'] += 1 if pred[i] == TBL else 0
        out[g]['hqql_pred'] += 1 if pred[i] == HQQL else 0
    rows = {}
    for g, d in out.items():
        n = max(1, d['n'])
        rows[g] = {
            'n': d['n'],
            'tbl_minus_hqql': d['tbl_minus_hqql'] / n,
            'hqql_minus_tbl': d['hqql_minus_tbl'] / n,
            'tbl_pred_rate': d['tbl_pred'] / n,
            'hqql_pred_rate': d['hqql_pred'] / n,
        }
    return rows


def mdtab(headers, rows):
    if not rows:
        return '_No rows._\n'
    return '\n'.join(['| ' + ' | '.join(headers) + ' |', '| ' + ' | '.join(['---'] * len(headers)) + ' |'] + ['| ' + ' | '.join(str(x) for x in r) + ' |' for r in rows]) + '\n'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--rules', default='reports/latest/tables/part_rule_gate_join_real_contract_v1.csv')
    ap.add_argument('--groups-csv', default='reports/latest/tables/part_hqql_tbl_groups_real_contract_v1.csv')
    ap.add_argument('--data-config', default='external/particle_transformer/data/JetClass/JetClass_kinpid.yaml')
    ap.add_argument('--checkpoint', default='external/particle_transformer/models/ParT_kinpid.pt')
    ap.add_argument('--network-file', default='external/particle_transformer/networks/example_ParticleTransformer.py')
    ap.add_argument('--manifest', default='manifests/latest/part_weaver_predict_smoke_v3_args.txt')
    ap.add_argument('--events-per-group', type=int, default=32)
    ap.add_argument('--micro-batch', type=int, default=8)
    ap.add_argument('--top-rules', type=int, default=8)
    ap.add_argument('--patch-strength', type=float, default=40.0)
    ap.add_argument('--device', default='cuda' if torch.cuda.is_available() else 'cpu')
    ap.add_argument('--out-md', default='reports/latest/PART_EXACT_ROUTE_PATCH_REAL_CONTRACT_V1.md')
    ap.add_argument('--out-csv', default='reports/latest/tables/part_exact_route_patch_real_contract_v1.csv')
    ap.add_argument('--out-json', default='manifests/latest/part_exact_route_patch_real_contract_v1.json')
    a = ap.parse_args()

    rules = pick_rules(a.rules, a.top_rules)
    if not rules:
        raise RuntimeError('no rules selected')
    groups, _ = load_groups(a.groups_csv, 'reports/latest/part_weaver_predict_smoke_v3_*.root', a.manifest, a.events_per_group, a.events_per_group, a.events_per_group, a.events_per_group)
    events = select_events(groups, a.events_per_group)
    if not events:
        raise RuntimeError('no events selected')

    device = torch.device(a.device)
    model, dc = load_model(a.network_file, a.checkpoint, a.data_config, device)
    mb = max(1, int(a.micro_batch))

    base_all = []
    meta_all = []
    patch_by_rule = {i: [] for i in range(len(rules))}

    for s in range(0, len(events), mb):
        sub = events[s:s + mb]
        pts, fts, vec, msk, metas = build_batch(sub, device, dc)
        batch = (pts, fts, vec, msk)
        base = forward_logits(model, batch)
        base_all.append(base)
        meta_all += metas
        for ri, rule in enumerate(rules):
            patched = forward_logits(model, batch, metas=metas, rule=rule, strength=a.patch_strength)
            patch_by_rule[ri].append(patched)
        del pts, fts, vec, msk
        if a.device.startswith('cuda'):
            torch.cuda.empty_cache()
        gc.collect()

    base_logits = torch.cat(base_all, dim=0)
    base_m = metrics(base_logits, meta_all)
    rows = []
    for ri, rule in enumerate(rules):
        patched_logits = torch.cat(patch_by_rule[ri], dim=0)
        pm = metrics(patched_logits, meta_all)
        row = {
            'rule': rule.get('rule') or rule.get('id') or f'R{ri+1:03d}',
            'module': rule['module'],
            'head': rule['head'],
            'route': rule['pair'],
            'type': rule.get('type', ''),
            'rule_strength': rule.get('rule_strength', rule.get('strength', '')),
            'gate_grad': rule.get('gate_grad', ''),
            'patch_strength': a.patch_strength,
        }
        for g in ['A_Hqql_correct', 'B_Hqql_to_Tbl', 'C_Tbl_correct', 'D_Tbl_to_Hqql']:
            b = base_m.get(g, {})
            p = pm.get(g, {})
            row[f'{g}_n'] = b.get('n', 0)
            row[f'{g}_base_tbl_minus_hqql'] = b.get('tbl_minus_hqql', 0.0)
            row[f'{g}_patch_tbl_minus_hqql'] = p.get('tbl_minus_hqql', 0.0)
            row[f'{g}_delta_tbl_minus_hqql'] = p.get('tbl_minus_hqql', 0.0) - b.get('tbl_minus_hqql', 0.0)
            row[f'{g}_base_tbl_pred_rate'] = b.get('tbl_pred_rate', 0.0)
            row[f'{g}_patch_tbl_pred_rate'] = p.get('tbl_pred_rate', 0.0)
            row[f'{g}_delta_tbl_pred_rate'] = p.get('tbl_pred_rate', 0.0) - b.get('tbl_pred_rate', 0.0)
        row['causal_score_B_abs_delta_margin'] = abs(row['B_Hqql_to_Tbl_delta_tbl_minus_hqql'])
        row['causal_score_B_reduce_confusion'] = -row['B_Hqql_to_Tbl_delta_tbl_minus_hqql']
        rows.append(row)

    rows = sorted(rows, key=lambda r: abs(r['B_Hqql_to_Tbl_delta_tbl_minus_hqql']), reverse=True)
    wcsv(a.out_csv, rows)
    summary = {
        'ok': True,
        'events': len(events),
        'events_per_group': a.events_per_group,
        'top_rules': len(rules),
        'patch_strength': a.patch_strength,
        'checkpoint': a.checkpoint,
        'data_config': a.data_config,
        'top_by_B_abs_delta': rows[:10],
    }
    wjson(a.out_json, summary)

    md = []
    md.append('# PART_EXACT_ROUTE_PATCH_REAL_CONTRACT_V1\n\n')
    md.append('Exact route patch over real-contract ParT attention. This suppresses one role-route inside one attention head/module and measures Hqql/Tbl margin changes.\n\n')
    md.append(f'- events: **{len(events)}**\n')
    md.append(f'- events_per_group: **{a.events_per_group}**\n')
    md.append(f'- rules tested: **{len(rules)}**\n')
    md.append(f'- patch_strength: **{a.patch_strength}**\n')
    md.append(f'- checkpoint: `{a.checkpoint}`\n')
    md.append(f'- data_config: `{a.data_config}`\n\n')
    md.append('## Interpretation rule\n\n')
    md.append('- Negative `B_delta_tbl_minus_hqql`: patch reduced Tbl-like margin in Hqql→Tbl mistakes, so this route supports confusion.\n')
    md.append('- Positive `B_delta_tbl_minus_hqql`: patch increased Tbl-like margin, so this route was protective or suppressive.\n')
    md.append('- Large absolute delta means stronger causal effect candidate.\n\n')
    md.append('## Top exact route effects\n')
    md.append(mdtab(['rule','module','head','route','type','gate_grad','B_delta_margin','B_delta_tbl_pred','A_delta_margin'], [[r['rule'], r['module'], r['head'], r['route'], r['type'], r.get('gate_grad',''), f"{r['B_Hqql_to_Tbl_delta_tbl_minus_hqql']:.5e}", f"{r['B_Hqql_to_Tbl_delta_tbl_pred_rate']:.5e}", f"{r['A_Hqql_correct_delta_tbl_minus_hqql']:.5e}"] for r in rows]))
    md.append('\n## Validity notes\n\n')
    md.append('This is stronger than route visibility and gate gradient: it changes the actual attention mask for the chosen route and measures model-output change. It is still a v1 exact-route patch; if an attention mask shape is incompatible, that micro-call skips corruption rather than forcing an invalid mask.\n')
    Path(a.out_md).write_text(''.join(md), encoding='utf-8')
    print(json.dumps(summary, indent=2, ensure_ascii=False))


if __name__ == '__main__':
    main()
