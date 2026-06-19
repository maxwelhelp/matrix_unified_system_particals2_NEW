#!/usr/bin/env python3
import argparse
import csv
import importlib.util
import json
import math
from collections import defaultdict
from pathlib import Path

import awkward as ak
import numpy as np
import torch
import torch.nn.functional as F
import uproot
from weaver.utils.data.config import DataConfig

LABELS = ['label_QCD','label_Hbb','label_Hcc','label_Hgg','label_H4q','label_Hqql','label_Zqq','label_Wqq','label_Tbqq','label_Tbl']
SRC = 'label_Hqql'
TGT = 'label_Tbl'
BASE_BRANCHES = [
    'part_px','part_py','part_pz','part_energy','part_deta','part_dphi','part_charge',
    'part_isChargedHadron','part_isNeutralHadron','part_isPhoton','part_isElectron','part_isMuon',
    'part_d0val','part_d0err','part_dzval','part_dzerr','jet_pt','jet_energy'
]


def wcsv(path, rows):
    path = Path(path); path.parent.mkdir(parents=True, exist_ok=True)
    keys = []
    for r in rows:
        for k in r:
            if k not in keys:
                keys.append(k)
    with path.open('w', encoding='utf-8', newline='') as f:
        wr = csv.DictWriter(f, fieldnames=keys)
        wr.writeheader()
        wr.writerows(rows)


def wjson(path, obj):
    path = Path(path); path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, ensure_ascii=False), encoding='utf-8')


def mdtab(headers, rows):
    if not rows:
        return '_No rows._\n'
    return '\n'.join([
        '| ' + ' | '.join(headers) + ' |',
        '| ' + ' | '.join(['---'] * len(headers)) + ' |',
        *['| ' + ' | '.join(str(x) for x in r) + ' |' for r in rows],
    ]) + '\n'


def read_manifest(path):
    out = {}
    p = Path(path)
    if not p.exists():
        return out
    for line in p.read_text(encoding='utf-8', errors='replace').splitlines():
        line = line.strip()
        if not line or line.startswith('#') or ':' not in line:
            continue
        k, v = line.split(':', 1)
        out[k.strip()] = v.strip()
    return out


def find_tree(rf):
    for k in rf.keys():
        obj = rf[k]
        if hasattr(obj, 'arrays') and hasattr(obj, 'keys'):
            return obj
    raise RuntimeError('no tree found')


def group_from_output_name(path):
    n = Path(path).name
    if n.startswith('part_weaver_predict_smoke_v3_') and n.endswith('.root'):
        return n[len('part_weaver_predict_smoke_v3_'):-5]
    if n.startswith('pred_') and n.endswith('.root'):
        return n[len('pred_'):-5]
    return Path(path).stem


def score_branches(keys):
    out = []
    for lab in LABELS:
        found = None
        for cand in [f'score_{lab}', f'score_{lab.replace("label_", "")}', f'scores_{lab}', f'prob_{lab}']:
            if cand in keys:
                found = cand
                break
        if found is None:
            return []
        out.append(found)
    return out


def build_groups_from_outputs(root_glob, manifest_path, max_a, max_b, max_c, max_d):
    manifest = read_manifest(manifest_path)
    rows = []
    for f in sorted(Path('.').glob(root_glob)):
        g = group_from_output_name(f)
        with uproot.open(f) as rf:
            t = find_tree(rf)
            keys = list(t.keys())
            scores = score_branches(keys)
            if not scores:
                raise RuntimeError(f'could not find score branches in {f}')
            arr = t.arrays(LABELS + scores, library='np')
            y = np.stack([arr[x] for x in LABELS], axis=1).argmax(axis=1)
            s = np.stack([arr[x] for x in scores], axis=1)
            pred = s.argmax(axis=1)
        source_root = manifest.get(g, '')
        if not source_root:
            resolved = Path(f).resolve()
            with uproot.open(resolved) as rf:
                pred_keys = set(find_tree(rf).keys())
            if 'part_px' in pred_keys:
                source_root = str(resolved)
            else:
                raise RuntimeError(
                    f'missing source_root for group {g}. Need manifest mapping like "{g}:/path/to/original_input.root"; prediction ROOT does not contain particle branches.'
                )
        for i in range(len(y)):
            tl, pl = LABELS[int(y[i])], LABELS[int(pred[i])]
            group = None
            if g == 'HToWW2Q1L' and tl == SRC and pl == SRC:
                group = 'A_Hqql_correct'
            elif g == 'HToWW2Q1L' and tl == SRC and pl == TGT:
                group = 'B_Hqql_to_Tbl'
            elif g == 'TTBarLep' and tl == TGT and pl == TGT:
                group = 'C_Tbl_correct'
            elif g == 'TTBarLep' and tl == TGT and pl == SRC:
                group = 'D_Tbl_to_Hqql'
            if group:
                rows.append({
                    'analysis_group': group,
                    'source_group': g,
                    'source_root': source_root,
                    'entry_idx': i,
                    'true_label': tl,
                    'pred_label': pl,
                    'score_Hqql': float(s[i, LABELS.index(SRC)]),
                    'score_Tbl': float(s[i, LABELS.index(TGT)]),
                    'margin_Tbl_minus_Hqql': float(s[i, LABELS.index(TGT)] - s[i, LABELS.index(SRC)]),
                    'margin_Hqql_minus_Tbl': float(s[i, LABELS.index(SRC)] - s[i, LABELS.index(TGT)]),
                })

    def pick(group, n):
        xs = [r for r in rows if r['analysis_group'] == group]
        key = 'margin_Tbl_minus_Hqql' if group.startswith(('B', 'C')) else 'margin_Hqql_minus_Tbl'
        return sorted(xs, key=lambda r: r[key], reverse=True)[:n], len(xs)

    selected = []
    counts = {}
    for g, n in [('A_Hqql_correct', max_a), ('B_Hqql_to_Tbl', max_b), ('C_Tbl_correct', max_c), ('D_Tbl_to_Hqql', max_d)]:
        xs, c = pick(g, n)
        selected += xs
        counts[g] = c
    return selected, counts


def load_groups(path, root_glob, manifest, max_a, max_b, max_c, max_d):
    p = Path(path) if path else None
    if p and p.exists():
        rows = []
        with p.open(newline='', encoding='utf-8') as f:
            for r in csv.DictReader(f):
                r['entry_idx'] = int(r['entry_idx'])
                rows.append(r)
        counts = {g: sum(1 for r in rows if r.get('analysis_group') == g) for g in sorted({r.get('analysis_group') for r in rows})}
        return rows, counts
    return build_groups_from_outputs(root_glob, manifest, max_a, max_b, max_c, max_d)


def pad_array(x, length, mode='constant', value=0.0):
    x = np.asarray(x, dtype=np.float32)
    n = len(x)
    if n >= length:
        return x[:length].astype(np.float32), min(n, length)
    if mode == 'wrap' and n > 0:
        reps = int(math.ceil(length / n))
        return np.tile(x, reps)[:length].astype(np.float32), n
    y = np.full(length, value, dtype=np.float32)
    if n > 0:
        y[:n] = x.astype(np.float32)
    return y, n


def standardize(var_name, x, dc):
    info = dc.preprocess_params[var_name]
    y = np.asarray(x, dtype=np.float32)
    center = info.get('center')
    if center is not None:
        y = (y - float(center)) * float(info.get('scale', 1.0))
        y = np.clip(y, float(info.get('min', -5)), float(info.get('max', 5)))
    return y.astype(np.float32)


def pid_role(values, i):
    if values['part_isElectron'][i] > 0.5:
        return 'electron'
    if values['part_isMuon'][i] > 0.5:
        return 'muon'
    if values['part_isPhoton'][i] > 0.5:
        return 'photon'
    if values['part_isChargedHadron'][i] > 0.5:
        return 'charged_hadron'
    if values['part_isNeutralHadron'][i] > 0.5:
        return 'neutral_hadron'
    return 'other'


def event_values(arr, idx):
    values = {}
    for k in BASE_BRANCHES:
        if k in ('jet_pt', 'jet_energy'):
            values[k] = float(arr[k][idx])
        elif k in arr.fields:
            values[k] = np.asarray(arr[k][idx], dtype=np.float32)
    px = values['part_px']; py = values['part_py']; e = values['part_energy']
    pt = np.hypot(px, py).clip(min=1e-8)
    ee = e.clip(min=1e-8)
    values['part_pt'] = pt
    values['part_pt_log'] = np.log(pt)
    values['part_e_log'] = np.log(ee)
    values['part_logptrel'] = np.log(pt / max(values['jet_pt'], 1e-8))
    values['part_logerel'] = np.log(ee / max(values['jet_energy'], 1e-8))
    values['part_deltaR'] = np.hypot(values['part_deta'], values['part_dphi'])
    if 'part_d0val' in values:
        values['part_d0'] = np.tanh(values['part_d0val'])
    if 'part_dzval' in values:
        values['part_dz'] = np.tanh(values['part_dzval'])
    values['part_mask'] = np.ones_like(e, dtype=np.float32)
    return values


def event_to_inputs(arr, idx, dc):
    values = event_values(arr, idx)
    tensors = {}
    real = min(len(values['part_px']), 128)
    for input_name in dc.input_names:
        cols = []
        for var_name in dc.input_dicts[input_name]:
            if var_name not in values:
                raise RuntimeError(f'missing variable {var_name}; mode/YAML expects it')
            info = dc.preprocess_params[var_name]
            length = int(info.get('length', 128))
            mode = str(info.get('pad_mode', 'constant')).lower()
            pad_value = float(info.get('pad_value', 0))
            x = standardize(var_name, values[var_name], dc)
            y, _ = pad_array(x, length, mode=mode, value=pad_value)
            cols.append(y)
        tensors[input_name] = np.stack(cols, axis=0).astype(np.float32)

    roles, pts, detas, dphis = [], [], [], []
    n = len(values['part_px'])
    for i in range(128):
        j = i % max(n, 1) if n > 0 else 0
        if i < real and n > 0:
            roles.append(pid_role(values, j))
            pts.append(float(values['part_pt'][j]))
            detas.append(float(values['part_deta'][j]))
            dphis.append(float(values['part_dphi'][j]))
        else:
            roles.append('pad'); pts.append(0.0); detas.append(0.0); dphis.append(0.0)
    meta = {'roles': roles, 'pt': pts, 'deta': detas, 'dphi': dphis, 'n_real': real}
    return tensors['pf_points'], tensors['pf_features'], tensors['pf_vectors'], tensors['pf_mask'], meta


def needed_branches(dc):
    need = set(BASE_BRANCHES)
    return sorted(need)


def build_batch(rows, device, dc):
    byfile = defaultdict(list)
    for n, r in enumerate(rows):
        byfile[r['source_root']].append((n, r))
    out = [None] * len(rows)
    meta = [None] * len(rows)
    branches = needed_branches(dc)
    for f, items in byfile.items():
        if not f or not Path(f).exists():
            raise RuntimeError(f'missing source_root: {f}')
        with uproot.open(f) as rf:
            t = find_tree(rf)
            keys = set(t.keys())
            read = [b for b in branches if b in keys]
            missing = [b for b in ['part_px','part_py','part_pz','part_energy','part_deta','part_dphi','jet_pt','jet_energy'] if b not in keys]
            if missing:
                raise RuntimeError(f'{f} misses required branches: {missing}')
            arr = t.arrays(read, library='ak')
        for n, r in items:
            p, x, v, m, mm = event_to_inputs(arr, int(r['entry_idx']), dc)
            out[n] = (p, x, v, m)
            meta[n] = {**r, **mm}
    pts = torch.tensor(np.stack([o[0] for o in out]), device=device)
    fts = torch.tensor(np.stack([o[1] for o in out]), device=device)
    vec = torch.tensor(np.stack([o[2] for o in out]), device=device)
    msk = torch.tensor(np.stack([o[3] for o in out]), device=device)
    return pts, fts, vec, msk, meta


def unwrap_state_dict(obj):
    sd = obj
    if isinstance(sd, dict):
        for key in ['model_state_dict', 'state_dict', 'model']:
            if key in sd and isinstance(sd[key], dict):
                sd = sd[key]
                break
    if isinstance(sd, dict):
        sd = {k.replace('module.', '', 1): v for k, v in sd.items()}
    return sd


def load_model(network_file, checkpoint, data_config, device):
    dc = DataConfig.load(data_config)
    spec = importlib.util.spec_from_file_location('part_net', network_file)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    model, _ = mod.get_model(dc)
    model.to(device)
    sd = unwrap_state_dict(torch.load(checkpoint, map_location=device))
    model.load_state_dict(sd, strict=True)
    model.eval()
    return model, dc


class AttentionTap:
    def __init__(self, topk=4):
        self.topk = topk
        self.records = []
        self.handles = []
    def hook(self, name):
        def fn(module, args, kwargs):
            q, k, v = args[0], args[1], args[2]
            kpm = kwargs.get('key_padding_mask', None)
            am = kwargs.get('attn_mask', None)
            b, t, _ = q.shape
            s = k.shape[1]
            nh = module.num_heads
            hd = module.head_dim
            qq, kk, _ = F._in_projection_packed(q, k, v, module.in_proj.weight, module.in_proj.bias)
            qq = module.q_norm(qq.view(b, t, nh, hd)).transpose(1, 2) * math.sqrt(1.0 / hd)
            kk = module.k_norm(kk.view(b, s, nh, hd)).transpose(1, 2)
            w = qq @ kk.transpose(-2, -1)
            if am is not None:
                w = w + am
            if kpm is not None:
                w = w.masked_fill(kpm.view(b, 1, 1, s).bool(), float('-inf'))
            a = torch.softmax(w, dim=-1).detach()
            flat = a.reshape(b, nh, -1)
            val, idx = torch.topk(flat, k=min(self.topk, flat.shape[-1]), dim=-1)
            self.records.append({'name': name, 'tgt': t, 'src': s, 'val': val.cpu(), 'idx': idx.cpu()})
        return fn
    def attach(self, model):
        for name, m in model.named_modules():
            if hasattr(m, 'in_proj') and hasattr(m, 'num_heads') and hasattr(m, 'head_dim'):
                self.handles.append(m.register_forward_pre_hook(self.hook(name), with_kwargs=True))
    def clear(self):
        self.records = []
    def close(self):
        for h in self.handles:
            h.remove()


def pair_dist(meta, q, k):
    if q < 0 or k < 0:
        return 0.0
    return float(math.hypot(meta['deta'][q] - meta['deta'][k], meta['dphi'][q] - meta['dphi'][k]))


def process_records(records, meta_batch, rows_out):
    for rec in records:
        name = rec['name']
        is_cls = rec['tgt'] == 1
        for bi, meta in enumerate(meta_batch):
            for h in range(rec['val'].shape[1]):
                for kk in range(rec['val'].shape[2]):
                    flat = int(rec['idx'][bi, h, kk])
                    w = float(rec['val'][bi, h, kk])
                    q = flat // rec['src']
                    k = flat % rec['src']
                    qi = -1 if is_cls else q
                    ki = k - 1 if is_cls and rec['src'] == 129 else k
                    qr = 'CLS' if qi < 0 else meta['roles'][qi]
                    kr = 'CLS' if ki < 0 else meta['roles'][ki]
                    rows_out.append({
                        'group': meta['analysis_group'],
                        'event_source_group': meta['source_group'],
                        'module': name,
                        'head': h,
                        'query_idx': qi,
                        'key_idx': ki,
                        'query_role': qr,
                        'key_role': kr,
                        'pair_role': qr + '<-' + kr,
                        'attn_weight': w,
                        'deltaR': pair_dist(meta, qi, ki),
                        'query_pt': 0 if qi < 0 else round(meta['pt'][qi], 5),
                        'key_pt': 0 if ki < 0 else round(meta['pt'][ki], 5),
                    })


def aggregate(rows):
    d = defaultdict(lambda: defaultdict(list))
    for r in rows:
        key = (r['module'], r['head'], r['pair_role'])
        d[key][r['group']].append(float(r['attn_weight']))
    out = []
    for (m, h, p), g in d.items():
        A = np.mean(g.get('A_Hqql_correct', [0]))
        B = np.mean(g.get('B_Hqql_to_Tbl', [0]))
        C = np.mean(g.get('C_Tbl_correct', [0]))
        D = np.mean(g.get('D_Tbl_to_Hqql', [0]))
        out.append({
            'module': m, 'head': h, 'pair_role': p,
            'A': A, 'B': B, 'C': C, 'D': D,
            'trigger_B_minus_A': B - A,
            'loss_A_minus_B': A - B,
            'tbl_like_B_close_C': B - abs(B - C),
            'anomaly_B_not_A_not_C': abs(B - A) * abs(B - C),
            'n': sum(len(v) for v in g.values()),
        })
    return sorted(out, key=lambda r: abs(r['trigger_B_minus_A']), reverse=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--groups-csv', default='reports/latest/tables/part_hqql_tbl_groups_real_contract_v1.csv')
    ap.add_argument('--root-glob', default='reports/latest/part_weaver_predict_smoke_v3_*.root')
    ap.add_argument('--manifest', default='manifests/latest/part_weaver_predict_smoke_v3_args.txt')
    ap.add_argument('--network-file', default='external/particle_transformer/networks/example_ParticleTransformer.py')
    ap.add_argument('--data-config', default='external/particle_transformer/data/JetClass/JetClass_kinpid.yaml')
    ap.add_argument('--checkpoint', default='external/particle_transformer/models/ParT_kinpid.pt')
    ap.add_argument('--device', default='cuda' if torch.cuda.is_available() else 'cpu')
    ap.add_argument('--batch-size', type=int, default=8)
    ap.add_argument('--topk', type=int, default=4)
    ap.add_argument('--max-a', type=int, default=256)
    ap.add_argument('--max-b', type=int, default=256)
    ap.add_argument('--max-c', type=int, default=256)
    ap.add_argument('--max-d', type=int, default=256)
    ap.add_argument('--out-md', default='reports/latest/PART_ATTENTION_SUPERTRACE_REAL_CONTRACT_V1.md')
    ap.add_argument('--out-pairs', default='reports/latest/tables/part_attention_pair_flows_real_contract_v1.csv')
    ap.add_argument('--out-summary', default='reports/latest/tables/part_attention_path_summary_real_contract_v1.csv')
    ap.add_argument('--out-json', default='manifests/latest/part_attention_supertrace_real_contract_v1.json')
    a = ap.parse_args()

    device = torch.device(a.device)
    groups, counts = load_groups(a.groups_csv, a.root_glob, a.manifest, a.max_a, a.max_b, a.max_c, a.max_d)
    if not groups:
        raise RuntimeError('no groups selected; check ROOT outputs and Hqql/Tbl confusion counts')
    model, dc = load_model(a.network_file, a.checkpoint, a.data_config, device)
    tap = AttentionTap(a.topk)
    tap.attach(model)
    pair_rows = []
    with torch.no_grad():
        for s in range(0, len(groups), a.batch_size):
            sub = groups[s:s + a.batch_size]
            pts, fts, vec, msk, meta = build_batch(sub, device, dc)
            tap.clear()
            _ = model(pts, fts, vec, msk)
            process_records(tap.records, meta, pair_rows)
    tap.close()

    summary = aggregate(pair_rows)
    wcsv(a.groups_csv, groups)
    wcsv(a.out_pairs, pair_rows)
    wcsv(a.out_summary, summary)
    wjson(a.out_json, {'ok': True, 'events': len(groups), 'counts': counts, 'pair_rows': len(pair_rows), 'summary_rows': len(summary), 'data_config': a.data_config, 'checkpoint': a.checkpoint})

    top_tr = sorted(summary, key=lambda r: r['trigger_B_minus_A'], reverse=True)[:20]
    top_loss = sorted(summary, key=lambda r: r['loss_A_minus_B'], reverse=True)[:20]
    top_anom = sorted(summary, key=lambda r: r['anomaly_B_not_A_not_C'], reverse=True)[:20]

    md = '# PART_ATTENTION_SUPERTRACE_REAL_CONTRACT_V1\n\n'
    md += 'Real-contract ParT top-K attention-pair supertrace over A/B/C/D Hqql/Tbl groups.\n\n'
    md += f'- data_config: `{a.data_config}`\n- checkpoint: `{a.checkpoint}`\n- events traced: **{len(groups)}**\n- pair rows: **{len(pair_rows)}**\n- summary rows: **{len(summary)}**\n- topk per head: **{a.topk}**\n\n'
    md += '## Input counts\n' + mdtab(['group', 'available/selected'], [[k, v] for k, v in counts.items()])
    md += '\n## Top B>A trigger paths\n' + mdtab(['module','head','pair_role','A','B','C','B-A'], [[r['module'], r['head'], r['pair_role'], round(r['A'],5), round(r['B'],5), round(r['C'],5), round(r['trigger_B_minus_A'],5)] for r in top_tr])
    md += '\n## Top A>B Hqql-loss paths\n' + mdtab(['module','head','pair_role','A','B','C','A-B'], [[r['module'], r['head'], r['pair_role'], round(r['A'],5), round(r['B'],5), round(r['C'],5), round(r['loss_A_minus_B'],5)] for r in top_loss])
    md += '\n## Top anomaly paths B!=A and B!=C\n' + mdtab(['module','head','pair_role','A','B','C','score'], [[r['module'], r['head'], r['pair_role'], round(r['A'],5), round(r['B'],5), round(r['C'],5), round(r['anomaly_B_not_A_not_C'],5)] for r in top_anom])
    md += '\n## Validity\nThis report uses real `DataConfig.load(...)` and strict checkpoint loading. It does not use the old fake hardcoded 17-feature SimpleNamespace contract.\n'
    Path(a.out_md).parent.mkdir(parents=True, exist_ok=True)
    Path(a.out_md).write_text(md, encoding='utf-8')
    print(json.dumps({'ok': True, 'events': len(groups), 'pair_rows': len(pair_rows), 'out_md': a.out_md}, indent=2))


if __name__ == '__main__':
    main()
