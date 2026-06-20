#!/usr/bin/env python3
import argparse, csv, gc, json, sys
from pathlib import Path
from collections import defaultdict, Counter

import torch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from tools.part_attention_supertrace_real_contract_v1 import LABELS, load_model, build_batch, wcsv, wjson
from tools.part_exact_route_patch_real_contract_v1 import split_pair, role_positions

HQQL = LABELS.index('label_Hqql')
TBL = LABELS.index('label_Tbl')


def fnum(x, default=0.0):
    try:
        return float(x)
    except Exception:
        return default


def read_csv(path):
    with open(path, newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))


def load_groups(path, n_per_group):
    rows = read_csv(path)
    by = defaultdict(list)
    for r in rows:
        by[r['analysis_group']].append(r)
    out = []
    for g in ['A_Hqql_correct', 'B_Hqql_to_Tbl', 'C_Tbl_correct', 'D_Tbl_to_Hqql']:
        out += by[g][:n_per_group]
    return out


def rule_name(r):
    return r.get('rule') or r.get('id') or r.get('rule_id') or ''


def rule_route(r):
    return r.get('route') or r.get('pair') or r.get('pair_role') or ''


def rule_strength(r):
    return fnum(r.get('rule_strength', r.get('strength', 0.0)))


def rule_gate(r):
    return fnum(r.get('gate_grad', 0.0))


def clean_rules(rows):
    out = []
    seen = set()
    for r in rows:
        route = rule_route(r)
        if '<-' not in route or 'pad' in route:
            continue
        module = r.get('module', '')
        head = str(r.get('head', ''))
        if not module or head == '':
            continue
        name = rule_name(r)
        key = (name, module, head, route)
        if key in seen:
            continue
        seen.add(key)
        rr = dict(r)
        rr['rule'] = name
        rr['route'] = route
        rr['head'] = head
        rr['_score'] = abs(rule_gate(rr)) * max(1e-6, rule_strength(rr))
        out.append(rr)
    return out


def choose_bundles(rules, top_routes=8):
    b = [r for r in rules if 'B_to_Tbl' in rule_name(r)]
    a = [r for r in rules if 'A_protect' in rule_name(r)]
    anom = [r for r in rules if 'anomaly' in rule_name(r)]
    key = lambda r: r['_score']
    bundles = []

    def add(name, kind, rs, note=''):
        rs = list(rs)
        if rs:
            bundles.append({'bundle': name, 'kind': kind, 'rules': rs, 'note': note})

    add('route_bundle_B_top8_gate_weighted', 'route_bundle', sorted(b, key=key, reverse=True)[:top_routes], 'top B_to_Tbl routes by abs(gate_grad)*rule_strength')
    add('route_bundle_A_top8_gate_weighted', 'route_bundle', sorted(a, key=key, reverse=True)[:top_routes], 'top A_protect routes by abs(gate_grad)*rule_strength')
    add('route_bundle_anomaly_top8_gate_weighted', 'route_bundle', sorted(anom, key=key, reverse=True)[:top_routes], 'top anomaly routes by abs(gate_grad)*rule_strength')

    add('route_bundle_blocks7_head4_B', 'route_bundle', [r for r in b if r.get('module') == 'mod.blocks.7.attn' and str(r.get('head')) == '4'], 'all B_to_Tbl routes in mod.blocks.7.attn head 4')
    add('route_bundle_blocks6_head0_B', 'route_bundle', [r for r in b if r.get('module') == 'mod.blocks.6.attn' and str(r.get('head')) == '0'], 'all B_to_Tbl routes in mod.blocks.6.attn head 0')
    add('route_bundle_blocks6_head4_mixed', 'route_bundle', [r for r in rules if r.get('module') == 'mod.blocks.6.attn' and str(r.get('head')) == '4'], 'all compiled routes in mod.blocks.6.attn head 4')

    # Full output head zero controls for strong heads.
    head_specs = []
    for module, head in [('mod.blocks.7.attn', '4'), ('mod.blocks.6.attn', '0'), ('mod.blocks.6.attn', '4'), ('mod.blocks.5.attn', '6'), ('mod.blocks.7.attn', '3')]:
        refs = [r for r in rules if r.get('module') == module and str(r.get('head')) == head]
        if refs:
            head_specs.append({'bundle': f'head_output_zero_{module}_h{head}', 'kind': 'head_output_zero', 'module': module, 'head': head, 'rules': refs, 'note': 'zero output slice for this attention head'})
    bundles.extend(head_specs)
    return bundles


class MultiRoutePatch:
    def __init__(self, rules, metas, strength=40.0):
        self.rules = rules
        self.metas = metas
        self.strength = float(strength)
        self.handles = []
        by = defaultdict(list)
        for r in rules:
            by[r['module']].append(r)
        self.by_module = dict(by)

    def _hook(self, module_name):
        rules = self.by_module[module_name]
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
            hits = 0
            for r in rules:
                head = int(r['head'])
                if head < 0 or head >= H:
                    continue
                qr, kr = split_pair(r['route'])
                for bi, meta in enumerate(self.metas):
                    qpos = role_positions(meta, qr, T, True)
                    kpos = role_positions(meta, kr, S, False)
                    for qi in qpos:
                        for ki in kpos:
                            if legacy:
                                patch[bi * H + head, qi, ki] -= self.strength
                            else:
                                patch[bi, head, qi, ki] -= self.strength
                            hits += 1
            if hits == 0:
                return args, kwargs
            base = kwargs.get('attn_mask', None)
            if base is None:
                kwargs['attn_mask'] = patch
                return args, kwargs
            basef = torch.zeros_like(base, dtype=q.dtype).masked_fill(base, -self.strength) if base.dtype == torch.bool else base.to(dtype=q.dtype)
            if legacy:
                if basef.ndim == 2:
                    basef = basef.view(1, basef.shape[-2], basef.shape[-1]).expand(B * H, T, S)
                elif basef.ndim == 4:
                    basef = basef.reshape(B * H, basef.shape[-2], basef.shape[-1])
                kwargs['attn_mask'] = basef + patch if basef.shape == patch.shape else base
            else:
                if basef.ndim == 2:
                    basef = basef.view(1, 1, basef.shape[-2], basef.shape[-1]).expand(B, H, T, S)
                elif basef.ndim == 3 and basef.shape[0] == B * H:
                    basef = basef.view(B, H, basef.shape[-2], basef.shape[-1])
                elif basef.ndim == 4 and basef.shape[0] == B and basef.shape[1] == 1:
                    basef = basef.expand(B, H, T, S)
                kwargs['attn_mask'] = basef + patch if basef.shape == patch.shape else base
            return args, kwargs
        return fn

    def attach(self, model):
        for name, m in model.named_modules():
            if name in self.by_module:
                self.handles.append(m.register_forward_pre_hook(self._hook(name), with_kwargs=True))
        if not self.handles:
            raise RuntimeError('no route bundle hooks attached')

    def close(self):
        for h in self.handles:
            h.remove()
        self.handles = []


class HeadOutputZeroPatch:
    def __init__(self, module, head):
        self.module = module
        self.head = int(head)
        self.handle = None

    def _hook(self, module, args, out):
        x = out[0] if isinstance(out, tuple) else out
        if not torch.is_tensor(x) or x.ndim != 3:
            return out
        H = int(module.num_heads)
        C = x.shape[-1]
        a = (C * self.head) // H
        b = (C * (self.head + 1)) // H
        y = x.clone()
        y[..., a:b] = 0
        if isinstance(out, tuple):
            return (y,) + out[1:]
        return y

    def attach(self, model):
        for name, m in model.named_modules():
            if name == self.module:
                self.handle = m.register_forward_hook(self._hook)
                return
        raise RuntimeError(f'head module not found: {self.module}')

    def close(self):
        if self.handle is not None:
            self.handle.remove()
            self.handle = None


def forward_model(model, batch, patch=None):
    if patch is not None:
        patch.attach(model)
    pts, fts, vec, msk = batch
    with torch.no_grad():
        out = model(pts, fts, vec, msk).detach().cpu()
    if patch is not None:
        patch.close()
    return out


def metrics(outputs, metas):
    pred = outputs.argmax(dim=1).tolist()
    h = outputs[:, HQQL].float()
    t = outputs[:, TBL].float()
    d = defaultdict(lambda: {'n': 0, 'tbl_minus_hqql': 0.0, 'tbl_pred': 0, 'hqql_pred': 0})
    for i, m in enumerate(metas):
        g = m['analysis_group']
        d[g]['n'] += 1
        d[g]['tbl_minus_hqql'] += float(t[i] - h[i])
        d[g]['tbl_pred'] += int(pred[i] == TBL)
        d[g]['hqql_pred'] += int(pred[i] == HQQL)
    out = {}
    for g, x in d.items():
        n = max(1, x['n'])
        out[g] = {
            'n': x['n'],
            'tbl_minus_hqql': x['tbl_minus_hqql'] / n,
            'tbl_pred_rate': x['tbl_pred'] / n,
            'hqql_pred_rate': x['hqql_pred'] / n,
        }
    return out


def mdtab(headers, rows):
    if not rows:
        return '_No rows._\n'
    return '\n'.join(['| ' + ' | '.join(headers) + ' |', '| ' + ' | '.join(['---'] * len(headers)) + ' |'] + ['| ' + ' | '.join(str(x) for x in r) + ' |' for r in rows]) + '\n'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--groups-csv', default='reports/latest/tables/part_hqql_tbl_groups_direct_replay_v1.csv')
    ap.add_argument('--rules-csv', default='reports/latest/tables/part_rule_gate_join_real_contract_v1.csv')
    ap.add_argument('--network-file', default='external/particle_transformer/networks/example_ParticleTransformer_legacy.py')
    ap.add_argument('--checkpoint', default='external/particle_transformer/models/ParT_kinpid.pt')
    ap.add_argument('--data-config', default='external/particle_transformer/data/JetClass/JetClass_kinpid.yaml')
    ap.add_argument('--events-per-group', type=int, default=64)
    ap.add_argument('--micro-batch', type=int, default=8)
    ap.add_argument('--top-routes', type=int, default=8)
    ap.add_argument('--patch-strength', type=float, default=40.0)
    ap.add_argument('--device', default='cuda' if torch.cuda.is_available() else 'cpu')
    ap.add_argument('--out-md', default='reports/latest/PART_BUNDLE_CAUSAL_PATCH_REAL_CONTRACT_V1.md')
    ap.add_argument('--out-csv', default='reports/latest/tables/part_bundle_causal_patch_real_contract_v1.csv')
    ap.add_argument('--out-json', default='manifests/latest/part_bundle_causal_patch_real_contract_v1.json')
    a = ap.parse_args()

    events = load_groups(a.groups_csv, a.events_per_group)
    rules = clean_rules(read_csv(a.rules_csv))
    bundles = choose_bundles(rules, a.top_routes)
    if not bundles:
        raise RuntimeError('no bundles selected')

    device = torch.device(a.device)
    model, dc = load_model(a.network_file, a.checkpoint, a.data_config, device)
    mb = max(1, a.micro_batch)
    base_chunks = []
    patched_chunks = {i: [] for i in range(len(bundles))}
    meta_all = []

    for s in range(0, len(events), mb):
        sub = events[s:s + mb]
        pts, fts, vec, msk, metas = build_batch(sub, device, dc)
        batch = (pts, fts, vec, msk)
        base_chunks.append(forward_model(model, batch))
        meta_all += metas
        for bi, b in enumerate(bundles):
            if b['kind'] == 'route_bundle':
                patch = MultiRoutePatch(b['rules'], metas, strength=a.patch_strength)
            else:
                patch = HeadOutputZeroPatch(b['module'], b['head'])
            patched_chunks[bi].append(forward_model(model, batch, patch=patch))
        del pts, fts, vec, msk
        if device.type == 'cuda':
            torch.cuda.empty_cache()
        gc.collect()

    base_out = torch.cat(base_chunks, dim=0)
    base_m = metrics(base_out, meta_all)
    rows = []
    for bi, bundle in enumerate(bundles):
        out = torch.cat(patched_chunks[bi], dim=0)
        pm = metrics(out, meta_all)
        r = {
            'bundle': bundle['bundle'],
            'kind': bundle['kind'],
            'n_rules': len(bundle.get('rules', [])),
            'rules': ';'.join(rule_name(x) for x in bundle.get('rules', [])[:12]),
            'routes': ';'.join(rule_route(x) for x in bundle.get('rules', [])[:12]),
            'note': bundle.get('note', ''),
        }
        for g in ['A_Hqql_correct', 'B_Hqql_to_Tbl', 'C_Tbl_correct', 'D_Tbl_to_Hqql']:
            bm = base_m.get(g, {})
            xm = pm.get(g, {})
            r[f'{g}_n'] = bm.get('n', 0)
            r[f'{g}_base_margin'] = bm.get('tbl_minus_hqql', 0.0)
            r[f'{g}_patch_margin'] = xm.get('tbl_minus_hqql', 0.0)
            r[f'{g}_delta_margin'] = xm.get('tbl_minus_hqql', 0.0) - bm.get('tbl_minus_hqql', 0.0)
            r[f'{g}_base_tbl_pred'] = bm.get('tbl_pred_rate', 0.0)
            r[f'{g}_patch_tbl_pred'] = xm.get('tbl_pred_rate', 0.0)
            r[f'{g}_delta_tbl_pred'] = xm.get('tbl_pred_rate', 0.0) - bm.get('tbl_pred_rate', 0.0)
        r['B_reduce_confusion_score'] = -r['B_Hqql_to_Tbl_delta_margin']
        r['A_damage_score'] = abs(r['A_Hqql_correct_delta_margin'])
        rows.append(r)

    rows.sort(key=lambda r: abs(r['B_Hqql_to_Tbl_delta_margin']), reverse=True)
    wcsv(a.out_csv, rows)
    summary = {
        'ok': True,
        'events': len(events),
        'events_per_group': a.events_per_group,
        'bundles': len(bundles),
        'patch_strength': a.patch_strength,
        'top': rows[:5],
    }
    wjson(a.out_json, summary)

    md = []
    md.append('# PART_BUNDLE_CAUSAL_PATCH_REAL_CONTRACT_V1\n\n')
    md.append('Bundle/head causal patch over direct-replay ParT Hqql/Tbl groups. This tests algorithmic nodes, not only one attention route.\n\n')
    md.append(f'- events: **{len(events)}**\n')
    md.append(f'- events_per_group: **{a.events_per_group}**\n')
    md.append(f'- bundles tested: **{len(bundles)}**\n')
    md.append(f'- patch_strength: **{a.patch_strength}**\n')
    md.append(f'- groups_csv: `{a.groups_csv}`\n')
    md.append(f'- rules_csv: `{a.rules_csv}`\n\n')
    md.append('## Top bundle effects\n')
    md.append(mdtab(['bundle', 'kind', 'n_rules', 'B_delta_margin', 'B_delta_tbl_pred', 'A_delta_margin', 'C_delta_margin', 'D_delta_margin'], [[r['bundle'], r['kind'], r['n_rules'], f"{r['B_Hqql_to_Tbl_delta_margin']:.5e}", f"{r['B_Hqql_to_Tbl_delta_tbl_pred']:.5e}", f"{r['A_Hqql_correct_delta_margin']:.5e}", f"{r['C_Tbl_correct_delta_margin']:.5e}", f"{r['D_Tbl_to_Hqql_delta_margin']:.5e}"] for r in rows]))
    md.append('\n## Reading rule\n\n')
    md.append('- Negative `B_delta_margin`: patch reduces Tbl-like margin in Hqql→Tbl mistakes; bundle supports confusion.\n')
    md.append('- Positive `B_delta_margin`: patch increases Tbl-like margin; bundle may be protective/suppressive.\n')
    md.append('- Nonzero `B_delta_tbl_pred` means the bundle can flip some class decisions, not just margins.\n')
    md.append('- Compare with `A_delta_margin/C_delta_margin` to see damage to correct regimes.\n')
    Path(a.out_md).write_text(''.join(md), encoding='utf-8')
    print(json.dumps(summary, indent=2, ensure_ascii=False))


if __name__ == '__main__':
    main()
