#!/usr/bin/env python3
import argparse, csv, gc, json, sys
from pathlib import Path
from collections import defaultdict, Counter

import torch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from tools.part_attention_supertrace_real_contract_v1 import LABELS, load_model, build_batch, wcsv, wjson

HQQL = LABELS.index('label_Hqql')
TBL = LABELS.index('label_Tbl')
GROUPS = ['A_Hqql_correct', 'B_Hqql_to_Tbl', 'C_Tbl_correct', 'D_Tbl_to_Hqql']


def fnum(x, default=0.0):
    try:
        return float(x)
    except Exception:
        return default


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
    p = Path(path)
    if not p.exists():
        return []
    with p.open(newline='', encoding='utf-8') as f:
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


def batch_slice(batch, start, end):
    pts, fts, vec, msk = batch
    return (pts[start:end], fts[start:end], vec[start:end], msk[start:end])


def is_attention_module(m):
    return hasattr(m, 'num_heads') and hasattr(m, 'head_dim') and (hasattr(m, 'in_proj_weight') or hasattr(m, 'in_proj'))


def split_head_ranges(C, H):
    return [(h, (C*h)//H, (C*(h+1))//H) for h in range(H) if (C*h)//H < (C*(h+1))//H]


def list_heads(model):
    heads = []
    for name, m in model.named_modules():
        if is_attention_module(m):
            H = int(m.num_heads)
            C = int(H * m.head_dim)
            for h, a, b in split_head_ranges(C, H):
                heads.append({'module': name, 'head': h, 'head_id': f'{name}.h{h}', 'ch_start': a, 'ch_end': b})
    return heads


def role_for(meta, pi):
    roles = meta.get('roles') or []
    if 0 <= pi < len(roles):
        return roles[pi]
    return 'unknown'


def forward_logits(model, batch):
    pts, fts, vec, msk = batch
    with torch.no_grad():
        return model(pts, fts, vec, msk).detach().cpu()


class ZeroHeadPatch:
    def __init__(self, module_name, head):
        self.module_name = module_name
        self.head = int(head)
        self.handle = None

    def _hook(self, module, args, out):
        x = out[0] if isinstance(out, tuple) else out
        if not torch.is_tensor(x) or x.ndim != 3:
            return out
        H = int(module.num_heads)
        C = int(x.shape[-1])
        a = (C * self.head) // H
        b = (C * (self.head + 1)) // H
        parts = []
        if a > 0:
            parts.append(x[..., :a])
        parts.append(torch.zeros_like(x[..., a:b]))
        if b < C:
            parts.append(x[..., b:])
        y = torch.cat(parts, dim=-1)
        if isinstance(out, tuple):
            return (y,) + out[1:]
        return y

    def attach(self, model):
        for name, m in model.named_modules():
            if name == self.module_name:
                self.handle = m.register_forward_hook(self._hook)
                return
        raise RuntimeError(f'module not found: {self.module_name}')

    def close(self):
        if self.handle is not None:
            self.handle.remove()
            self.handle = None


class EnergyCapture:
    def __init__(self, metas):
        self.metas = metas
        self.handles = []
        self.rows = []

    def _hook(self, name):
        def hook(module, args, out):
            x = out[0] if isinstance(out, tuple) else out
            if not torch.is_tensor(x) or x.ndim != 3:
                return
            B = len(self.metas)
            if x.shape[1] == B:
                xb = x.detach().permute(1, 0, 2)  # [B,T,C]
            elif x.shape[0] == B:
                xb = x.detach()
            else:
                return
            H = int(module.num_heads)
            C = int(xb.shape[-1])
            for h, a, b in split_head_ranges(C, H):
                en = torch.sqrt((xb[..., a:b].float() ** 2).sum(dim=-1) + 1e-12).cpu()
                self.rows.append({'module': name, 'head': h, 'head_id': f'{name}.h{h}', 'energy': en})
        return hook

    def attach(self, model):
        for name, m in model.named_modules():
            if is_attention_module(m):
                self.handles.append(m.register_forward_hook(self._hook(name)))
        if not self.handles:
            raise RuntimeError('no attention modules for EnergyCapture')

    def close(self):
        for h in self.handles:
            h.remove()
        self.handles = []


def compute_base(model, batch, mb, device):
    chunks = []
    B = int(batch[0].shape[0])
    for s in range(0, B, mb):
        chunks.append(forward_logits(model, batch_slice(batch, s, min(B, s + mb))))
        if device.type == 'cuda':
            torch.cuda.empty_cache()
    return torch.cat(chunks, dim=0)


def group_metrics(logits, metas):
    pred = logits.argmax(dim=1).tolist()
    h = logits[:, HQQL].float()
    t = logits[:, TBL].float()
    out = defaultdict(lambda: {'n': 0, 'tbl_minus_hqql': 0.0, 'tbl_pred': 0, 'hqql_pred': 0, 'score_hqql': 0.0, 'score_tbl': 0.0})
    for i, m in enumerate(metas):
        g = m['analysis_group']
        out[g]['n'] += 1
        out[g]['tbl_minus_hqql'] += float(t[i] - h[i])
        out[g]['tbl_pred'] += int(pred[i] == TBL)
        out[g]['hqql_pred'] += int(pred[i] == HQQL)
        out[g]['score_hqql'] += float(h[i])
        out[g]['score_tbl'] += float(t[i])
    rows = {}
    for g, d in out.items():
        n = max(1, d['n'])
        rows[g] = {
            'n': d['n'],
            'tbl_minus_hqql': d['tbl_minus_hqql'] / n,
            'tbl_pred_rate': d['tbl_pred'] / n,
            'hqql_pred_rate': d['hqql_pred'] / n,
            'score_hqql': d['score_hqql'] / n,
            'score_tbl': d['score_tbl'] / n,
        }
    return rows


def zero_head_logits(model, batch, head, mb, device):
    out = []
    B = int(batch[0].shape[0])
    patch = ZeroHeadPatch(head['module'], head['head'])
    patch.attach(model)
    for s in range(0, B, mb):
        out.append(forward_logits(model, batch_slice(batch, s, min(B, s + mb))))
        if device.type == 'cuda':
            torch.cuda.empty_cache()
    patch.close()
    return torch.cat(out, dim=0)


def capture_role_stats(model, batch, metas, heads, mb, device, topk=3):
    # Aggregate top particle roles for each head/group from natural head-output energy.
    role_counts = defaultdict(Counter)
    role_top1 = defaultdict(Counter)
    energy_sum = defaultdict(float)
    energy_n = defaultdict(int)
    B = int(batch[0].shape[0])
    head_set = set(h['head_id'] for h in heads)
    for s in range(0, B, mb):
        e = min(B, s + mb)
        sub = batch_slice(batch, s, e)
        sub_metas = metas[s:e]
        cap = EnergyCapture(sub_metas)
        cap.attach(model)
        with torch.no_grad():
            _ = model(*sub)
        cap.close()
        mask = sub[3].detach().cpu().bool()
        if mask.ndim == 3:
            mask = mask[:, 0, :]
        N = int(mask.shape[1])
        for er in cap.rows:
            hid = er['head_id']
            if hid not in head_set:
                continue
            en = er['energy'].float()
            # align CLS+particles to particles
            if en.shape[1] == N + 1:
                en = en[:, 1:]
            elif en.shape[1] != N:
                tmp = torch.zeros((en.shape[0], N), dtype=en.dtype)
                n = min(N, en.shape[1])
                tmp[:, :n] = en[:, :n]
                en = tmp
            en = en.masked_fill(~mask[:en.shape[0]], -1e9)
            for bi, meta in enumerate(sub_metas):
                g = meta['analysis_group']
                real_n = int(mask[bi].sum())
                if real_n <= 0:
                    continue
                vals = en[bi]
                k = min(topk, real_n, int(vals.numel()))
                idx = torch.topk(vals, k).indices.tolist()
                key = (hid, g)
                energy_sum[key] += float(vals[idx[0]])
                energy_n[key] += 1
                for rank, pi in enumerate(idx, 1):
                    role = role_for(meta, int(pi))
                    role_counts[key][role] += 1
                    if rank == 1:
                        role_top1[key][role] += 1
        del cap
        gc.collect()
        if device.type == 'cuda':
            torch.cuda.empty_cache()
    role_rows = []
    for (hid, g), cnt in role_counts.items():
        total = max(1, sum(cnt.values()))
        t1 = role_top1[(hid, g)]
        top_role = cnt.most_common(1)[0][0] if cnt else ''
        top1_role = t1.most_common(1)[0][0] if t1 else ''
        role_rows.append({
            'head_id': hid,
            'group': g,
            'top_role': top_role,
            'top_role_rate_top3': cnt[top_role] / total if top_role else 0.0,
            'top1_role': top1_role,
            'top1_role_rate': t1[top1_role] / max(1, sum(t1.values())) if top1_role else 0.0,
            'mean_top_energy': energy_sum[(hid, g)] / max(1, energy_n[(hid, g)]),
            'role_counts': dict(cnt),
        })
    return role_rows


def role_lookup(role_rows):
    d = {}
    for r in role_rows:
        d[(r['head_id'], r['group'])] = r
    return d


def top_role_text(rlu, hid, group):
    r = rlu.get((hid, group))
    if not r:
        return ''
    return f"top1={r['top1_role']}:{fmt(r['top1_role_rate'])} top3={r['top_role']}:{fmt(r['top_role_rate_top3'])}"


def read_grad_lookup(path):
    rows = read_csv(path)
    d = defaultdict(dict)
    for r in rows:
        hid = r.get('head_id', '')
        obj = r.get('objective', '')
        if hid and obj:
            d[hid][obj] = r
    return d


def read_bundle_lookup(paths):
    out = defaultdict(list)
    for path in paths:
        for r in read_csv(path):
            bundle = r.get('bundle', '')
            for part in bundle.split('_'):
                pass
            # exact head_output_zero bundle name: head_output_zero_mod.blocks.7.attn_h3
            if bundle.startswith('head_output_zero_'):
                rest = bundle.replace('head_output_zero_', '')
                if '_h' in rest:
                    mod, h = rest.rsplit('_h', 1)
                    out[f'{mod}.h{h}'].append(r)
    return out


def read_rule_lookup(path):
    out = defaultdict(list)
    for r in read_csv(path):
        mod = r.get('module', '')
        head = r.get('head', '')
        if mod != '' and head != '':
            out[f'{mod}.h{head}'].append(r)
    return out


def diagnose(row):
    b_dm = fnum(row.get('B_delta_margin_when_zeroed'))
    b_flip = fnum(row.get('B_delta_tbl_pred_when_zeroed'))
    a_damage = abs(fnum(row.get('A_delta_margin_when_zeroed')))
    signed = abs(fnum(row.get('grad_signed_hqql_tbl')))
    pred = abs(fnum(row.get('grad_pred_logit')))
    if b_dm < -0.03 and b_flip < 0:
        return 'causal_tbl_confusion_support'
    if b_dm < -0.02:
        return 'margin_tbl_confusion_support'
    if b_dm > 0.02:
        return 'protective_or_counter_confusion'
    if signed > 0.05 or pred > 0.05:
        return 'high_gradient_weak_ablation'
    if a_damage > 0.05:
        return 'correct_regime_sensitive'
    return 'weak_or_distributed'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--groups-csv', default='reports/latest/tables/part_hqql_tbl_groups_direct_replay_v1.csv')
    ap.add_argument('--head-grad-csv', default='reports/latest/tables/part_full_all_head_supertrace_head_gradients_v1.csv')
    ap.add_argument('--bundle-csv', default='reports/latest/tables/part_bundle_causal_patch_real_contract_v1.csv')
    ap.add_argument('--bundle-sweep-csv', default='reports/latest/tables/part_bundle_causal_sweep_summary_v1.csv')
    ap.add_argument('--rules-csv', default='reports/latest/tables/part_rule_gate_join_real_contract_v1.csv')
    ap.add_argument('--network-file', default='external/particle_transformer/networks/example_ParticleTransformer_legacy.py')
    ap.add_argument('--checkpoint', default='external/particle_transformer/models/ParT_kinpid.pt')
    ap.add_argument('--data-config', default='external/particle_transformer/data/JetClass/JetClass_kinpid.yaml')
    ap.add_argument('--events-per-group', type=int, default=64)
    ap.add_argument('--micro-batch', type=int, default=8)
    ap.add_argument('--role-topk', type=int, default=3)
    ap.add_argument('--device', default='cuda' if torch.cuda.is_available() else 'cpu')
    ap.add_argument('--out-md', default='reports/latest/PART_MATRIX_PROGRAM_FULL_TRACE_REAL_CONTRACT_V1.md')
    ap.add_argument('--out-db', default='reports/latest/tables/part_matrix_program_full_trace_real_contract_v1_database.csv')
    ap.add_argument('--out-ranked', default='reports/latest/tables/part_matrix_program_full_trace_real_contract_v1_ranked.csv')
    ap.add_argument('--out-roles', default='reports/latest/tables/part_matrix_program_full_trace_real_contract_v1_top_roles.csv')
    ap.add_argument('--out-event-rows', default='reports/latest/tables/part_matrix_program_full_trace_real_contract_v1_event_head_ablation.csv')
    ap.add_argument('--out-json', default='manifests/latest/part_matrix_program_full_trace_real_contract_v1.json')
    args = ap.parse_args()

    events = select_events(args.groups_csv, args.events_per_group)
    device = torch.device(args.device)
    model, dc = load_model(args.network_file, args.checkpoint, args.data_config, device)
    pts, fts, vec, msk, metas = build_batch(events, device, dc)
    batch = (pts, fts, vec, msk)
    B = int(pts.shape[0])
    mb = max(1, args.micro_batch)

    heads = list_heads(model)
    base = compute_base(model, batch, mb, device)
    base_m = group_metrics(base, metas)

    role_rows = capture_role_stats(model, batch, metas, heads, mb, device, topk=args.role_topk)
    rlu = role_lookup(role_rows)
    grads = read_grad_lookup(args.head_grad_csv)
    bundles = read_bundle_lookup([args.bundle_csv, args.bundle_sweep_csv])
    rules = read_rule_lookup(args.rules_csv)

    event_rows = []
    db = []
    for hi, head in enumerate(heads, 1):
        zl = zero_head_logits(model, batch, head, mb, device)
        zm = group_metrics(zl, metas)
        hid = head['head_id']
        row = {
            'head_id': hid,
            'module': head['module'],
            'head': head['head'],
            'ch_start': head['ch_start'],
            'ch_end': head['ch_end'],
            'grad_pred_logit': fnum(grads.get(hid, {}).get('pred_logit', {}).get('grad')),
            'grad_pred_logit_abs': fnum(grads.get(hid, {}).get('pred_logit', {}).get('abs_grad')),
            'grad_signed_hqql_tbl': fnum(grads.get(hid, {}).get('signed_hqql_tbl', {}).get('grad')),
            'grad_signed_hqql_tbl_abs': fnum(grads.get(hid, {}).get('signed_hqql_tbl', {}).get('abs_grad')),
            'compiled_rule_count': len(rules.get(hid, [])),
            'compiled_routes': ';'.join((x.get('route') or x.get('pair_role') or '') for x in rules.get(hid, [])[:8]),
        }
        for g in GROUPS:
            bm = base_m.get(g, {})
            xm = zm.get(g, {})
            row[f'{g}_base_margin'] = bm.get('tbl_minus_hqql', 0.0)
            row[f'{g}_zero_margin'] = xm.get('tbl_minus_hqql', 0.0)
            row[f'{g}_delta_margin_when_zeroed'] = xm.get('tbl_minus_hqql', 0.0) - bm.get('tbl_minus_hqql', 0.0)
            row[f'{g}_base_tbl_pred'] = bm.get('tbl_pred_rate', 0.0)
            row[f'{g}_zero_tbl_pred'] = xm.get('tbl_pred_rate', 0.0)
            row[f'{g}_delta_tbl_pred_when_zeroed'] = xm.get('tbl_pred_rate', 0.0) - bm.get('tbl_pred_rate', 0.0)
            row[f'{g}_base_score_hqql'] = bm.get('score_hqql', 0.0)
            row[f'{g}_base_score_tbl'] = bm.get('score_tbl', 0.0)
            row[f'{g}_top_roles'] = top_role_text(rlu, hid, g)
        # direct bundle evidence for same head, if present
        bxs = bundles.get(hid, [])
        row['bundle_evidence_rows'] = len(bxs)
        if bxs:
            row['bundle_B_delta_margin_best'] = min(fnum(x.get('B_Hqql_to_Tbl_delta_margin')) for x in bxs)
            row['bundle_B_delta_tbl_pred_best'] = min(fnum(x.get('B_Hqql_to_Tbl_delta_tbl_pred')) for x in bxs)
        else:
            row['bundle_B_delta_margin_best'] = ''
            row['bundle_B_delta_tbl_pred_best'] = ''
        row['confusion_support_score'] = max(0.0, -fnum(row['B_Hqql_to_Tbl_delta_margin_when_zeroed'])) + max(0.0, -fnum(row['B_Hqql_to_Tbl_delta_tbl_pred_when_zeroed'])) * 2.0
        row['protective_score'] = max(0.0, fnum(row['B_Hqql_to_Tbl_delta_margin_when_zeroed']))
        row['correct_damage_score'] = abs(fnum(row['A_Hqql_correct_delta_margin_when_zeroed'])) + abs(fnum(row['C_Tbl_correct_delta_margin_when_zeroed']))
        row['gradient_support_score'] = fnum(row['grad_signed_hqql_tbl_abs']) + 0.25 * fnum(row['grad_pred_logit_abs'])
        row['diagnosis'] = diagnose(row)
        row['matrix_program_summary'] = 'read particle/context via attention head -> write residual channel slice -> shift Hqql/Tbl margin -> top particle roles/compiled routes/causal ablation evidence'
        db.append(row)

        # event-level ablation rows, lightweight but useful for debugging top heads later
        for i, meta in enumerate(metas):
            event_rows.append({
                'head_id': hid,
                'analysis_group': meta['analysis_group'],
                'source_group': meta.get('source_group', ''),
                'entry_idx': meta.get('entry_idx', ''),
                'base_pred': LABELS[int(base[i].argmax())],
                'zero_pred': LABELS[int(zl[i].argmax())],
                'base_tbl_minus_hqql': float(base[i, TBL] - base[i, HQQL]),
                'zero_tbl_minus_hqql': float(zl[i, TBL] - zl[i, HQQL]),
                'delta_tbl_minus_hqql': float((zl[i, TBL] - zl[i, HQQL]) - (base[i, TBL] - base[i, HQQL])),
                'delta_hqql_score': float(zl[i, HQQL] - base[i, HQQL]),
                'delta_tbl_score': float(zl[i, TBL] - base[i, TBL]),
            })
        del zl
        gc.collect()
        if device.type == 'cuda':
            torch.cuda.empty_cache()

    ranked = sorted(db, key=lambda r: (fnum(r['confusion_support_score']), fnum(r['gradient_support_score'])), reverse=True)
    wcsv(args.out_db, db)
    wcsv(args.out_ranked, ranked)
    wcsv(args.out_roles, role_rows)
    # Keep event rows moderate: top ranked 12 heads only.
    top_heads = set(r['head_id'] for r in ranked[:12])
    wcsv(args.out_event_rows, [r for r in event_rows if r['head_id'] in top_heads])

    counts = Counter(r['diagnosis'] for r in db)
    summary = {
        'ok': True,
        'events': B,
        'events_per_group': args.events_per_group,
        'heads': len(db),
        'diagnosis_counts': dict(counts),
        'top_confusion_support': ranked[:12],
        'groups_csv': args.groups_csv,
        'head_grad_csv': args.head_grad_csv,
        'bundle_csv': args.bundle_csv,
        'bundle_sweep_csv': args.bundle_sweep_csv,
    }
    wjson(args.out_json, summary)

    top_trigger = ranked[:12]
    top_grad = sorted(db, key=lambda r: fnum(r['gradient_support_score']), reverse=True)[:12]
    top_damage = sorted(db, key=lambda r: fnum(r['correct_damage_score']), reverse=True)[:12]

    md = ['# PART_MATRIX_PROGRAM_FULL_TRACE_REAL_CONTRACT_V1\n\n',
          'ParT matrix-program full trace database. This is the ParT port of the old `matrix_program_full_trace_v3`: each attention head is treated as a candidate matrix-program node with all-head gradients, natural role/particle readout, zero-head ablation, compiled route rules, and bundle causal evidence.\n\n',
          f'- events: **{B}**\n', f'- events_per_group: **{args.events_per_group}**\n', f'- heads: **{len(db)}**\n', f'- diagnosis_counts: `{dict(counts)}`\n',
          f'- groups_csv: `{args.groups_csv}`\n', f'- head_grad_csv: `{args.head_grad_csv}`\n\n',
          '## Top Hqql→Tbl confusion-support candidates\n',
          mdtab(['head','diag','conf_support','B_delta_margin','B_delta_tbl_pred','grad_signed','A_damage','C_damage','topA','topB','topC','routes'], [[r['head_id'], r['diagnosis'], fmt(r['confusion_support_score']), fmt(r['B_Hqql_to_Tbl_delta_margin_when_zeroed']), fmt(r['B_Hqql_to_Tbl_delta_tbl_pred_when_zeroed']), fmt(r['grad_signed_hqql_tbl']), fmt(r['A_Hqql_correct_delta_margin_when_zeroed']), fmt(r['C_Tbl_correct_delta_margin_when_zeroed']), r['A_Hqql_correct_top_roles'], r['B_Hqql_to_Tbl_top_roles'], r['C_Tbl_correct_top_roles'], r['compiled_routes']] for r in top_trigger]),
          '\n## Top gradient-supported heads\n',
          mdtab(['head','diag','grad_pred','grad_signed','B_delta_margin','topB','routes'], [[r['head_id'], r['diagnosis'], fmt(r['grad_pred_logit']), fmt(r['grad_signed_hqql_tbl']), fmt(r['B_Hqql_to_Tbl_delta_margin_when_zeroed']), r['B_Hqql_to_Tbl_top_roles'], r['compiled_routes']] for r in top_grad]),
          '\n## Heads with largest correct-regime damage\n',
          mdtab(['head','diag','damage','A_delta','C_delta','B_delta','topA','topC'], [[r['head_id'], r['diagnosis'], fmt(r['correct_damage_score']), fmt(r['A_Hqql_correct_delta_margin_when_zeroed']), fmt(r['C_Tbl_correct_delta_margin_when_zeroed']), fmt(r['B_Hqql_to_Tbl_delta_margin_when_zeroed']), r['A_Hqql_correct_top_roles'], r['C_Tbl_correct_top_roles']] for r in top_damage]),
          '\n## Interpretation\n\nRead each row as a matrix program: attention head reads particle/context roles, writes a residual channel slice, shifts the Hqql/Tbl margin, and can be checked by zero-head ablation plus bundle causal patch evidence. Strong discovery candidates are heads where all-head gradients, B-confusion ablation, role readout, compiled routes, and bundle evidence agree.\n']
    Path(args.out_md).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out_md).write_text(''.join(md), encoding='utf-8')
    print(json.dumps({'ok': True, 'events': B, 'heads': len(db), 'out_md': args.out_md}, indent=2))


if __name__ == '__main__':
    main()
