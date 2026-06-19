#!/usr/bin/env python3
import argparse, csv, importlib.util, inspect, json, sys
from pathlib import Path
from types import SimpleNamespace
import torch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools.particlenet_real_patch_controls_v1 import load_balanced
from data.jetclass_tiny_loader_v3_official import LABELS


def wcsv(path, rows):
    path = Path(path); path.parent.mkdir(parents=True, exist_ok=True)
    keys, seen = [], set()
    for r in rows:
        for k in r:
            if k not in seen:
                keys.append(k); seen.add(k)
    with path.open('w', encoding='utf-8', newline='') as f:
        wr = csv.DictWriter(f, fieldnames=keys); wr.writeheader()
        for r in rows:
            wr.writerow({k: r.get(k, '') for k in keys})


def wjson(path, obj):
    path = Path(path); path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, ensure_ascii=False), encoding='utf-8')


def mdtab(headers, rows):
    if not rows:
        return '_No rows._\n'
    out = ['| ' + ' | '.join(headers) + ' |', '| ' + ' | '.join(['---'] * len(headers)) + ' |']
    out += ['| ' + ' | '.join(str(x).replace('\n', ' ') for x in r) + ' |' for r in rows]
    return '\n'.join(out) + '\n'


def load_network_module(path):
    spec = importlib.util.spec_from_file_location('part_network_example', str(path))
    if spec is None or spec.loader is None:
        raise RuntimeError(f'Cannot load network file: {path}')
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def make_data_config(batch):
    c_feat = int(batch['features'].shape[1])
    c_pts = int(batch['points'].shape[1])
    c_vec = int(batch.get('vectors', torch.zeros(1,4,1)).shape[1]) if 'vectors' in batch else 4
    return SimpleNamespace(
        input_names=['pf_points', 'pf_features', 'pf_vectors', 'pf_mask'],
        input_shapes={
            'pf_points': (1, c_pts, None),
            'pf_features': (1, c_feat, None),
            'pf_vectors': (1, c_vec, None),
            'pf_mask': (1, 1, None),
        },
        input_dicts={
            'pf_points': [f'point_{i}' for i in range(c_pts)],
            'pf_features': [f'feature_{i}' for i in range(c_feat)],
            'pf_vectors': [f'vector_{i}' for i in range(c_vec)],
            'pf_mask': ['mask'],
        },
        label_value=list(range(len(LABELS))),
        label_names=LABELS,
    )


def build_model(network_file, batch, device):
    mod = load_network_module(network_file)
    dc = make_data_config(batch)
    attempts = []
    if hasattr(mod, 'get_model'):
        for kwargs in ({}, {'data_config': dc}):
            try:
                if kwargs:
                    obj = mod.get_model(**kwargs)
                else:
                    obj = mod.get_model(dc)
                if isinstance(obj, tuple):
                    return obj[0].to(device), {'builder': 'network.get_model', 'model_info': str(obj[1])[:500]}
                return obj.to(device), {'builder': 'network.get_model', 'model_info': ''}
            except Exception as e:
                attempts.append(f'get_model {kwargs}: {repr(e)}')
    # fallback direct import
    try:
        from weaver.nn.model.ParticleTransformer import ParticleTransformer
        sig = inspect.signature(ParticleTransformer)
        kw = {'input_dim': int(batch['features'].shape[1]), 'num_classes': len(LABELS)}
        if 'pair_input_dim' in sig.parameters:
            kw['pair_input_dim'] = 4
        filt = {k: v for k, v in kw.items() if k in sig.parameters}
        return ParticleTransformer(**filt).to(device), {'builder': 'direct ParticleTransformer', 'kwargs': filt, 'attempts': attempts}
    except Exception as e:
        attempts.append(f'direct ParticleTransformer: {repr(e)}')
    raise RuntimeError('Could not build ParT model:\n' + '\n'.join(attempts))


def extract_state(obj):
    if isinstance(obj, dict):
        for k in ['model_state_dict', 'state_dict', 'model', 'net']:
            if k in obj and isinstance(obj[k], dict):
                return obj[k]
        if all(isinstance(k, str) for k in obj.keys()):
            return obj
    return obj


def clean_state_dict(sd):
    out = {}
    for k, v in sd.items():
        kk = k
        for pref in ['module.', 'model.', 'net.']:
            if kk.startswith(pref):
                kk = kk[len(pref):]
        out[kk] = v
    return out


def load_checkpoint(model, ckpt_path, device):
    ckpt = torch.load(ckpt_path, map_location=device)
    sd = clean_state_dict(extract_state(ckpt))
    res = model.load_state_dict(sd, strict=False)
    return {'missing': list(res.missing_keys), 'unexpected': list(res.unexpected_keys), 'ckpt_keys': list(ckpt.keys())[:20] if isinstance(ckpt, dict) else []}


def one_batch(batch, ids):
    idx = torch.as_tensor(ids, dtype=torch.long, device=batch['y'].device)
    B = batch['y'].shape[0]
    out = {}
    for k, v in batch.items():
        if torch.is_tensor(v) and v.shape and v.shape[0] == B:
            out[k] = v.index_select(0, idx)
        else:
            out[k] = v
    return out


def forward_try(model, b):
    pts, feat, mask = b['points'], b['features'], b['mask']
    vec = b.get('vectors', None)
    attempts = []
    calls = []
    if vec is not None:
        calls.append(('points,features,vectors,mask', lambda: model(pts, feat, vec, mask)))
        calls.append(('features,vectors,mask', lambda: model(feat, vec, mask)))
    calls.append(('points,features,mask', lambda: model(pts, feat, mask)))
    calls.append(('features,mask', lambda: model(feat, mask)))
    if vec is not None:
        calls.append(('kwargs x/v/mask', lambda: model(x=feat, v=vec, mask=mask)))
    for name, fn in calls:
        try:
            out = fn()
            if isinstance(out, (tuple, list)):
                out = out[0]
            return out, name
        except Exception as e:
            attempts.append(f'{name}: {repr(e)}')
    raise RuntimeError('No forward signature worked:\n' + '\n'.join(attempts))


def run_logits(model, batch, batch_size):
    outs, sig = [], None
    with torch.no_grad():
        for s in range(0, int(batch['y'].shape[0]), batch_size):
            b = one_batch(batch, list(range(s, min(int(batch['y'].shape[0]), s + batch_size))))
            out, used = forward_try(model, b)
            sig = sig or used
            outs.append(out.detach().cpu())
    return torch.cat(outs, 0), sig


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--repo-dir', default='external/particle_transformer')
    ap.add_argument('--network-file', default='external/particle_transformer/networks/example_ParticleTransformer.py')
    ap.add_argument('--checkpoint', default='external/particle_transformer/models/ParT_kinpid.pt')
    ap.add_argument('--data-dir', default=str(Path.home()/'Рабочий стол/jetclass_tiny_balanced'))
    ap.add_argument('--mode', default='kinpid')
    ap.add_argument('--samples-per-file', type=int, default=1024)
    ap.add_argument('--max-files', type=int, default=100)
    ap.add_argument('--batch-size', type=int, default=64)
    ap.add_argument('--device', default='cuda' if torch.cuda.is_available() else 'cpu')
    ap.add_argument('--out-md', default='reports/latest/PART_INFERENCE_V1.md')
    ap.add_argument('--out-pred', default='reports/latest/tables/part_inference_v1_predictions.csv')
    ap.add_argument('--out-conf', default='reports/latest/tables/part_inference_v1_confusion_pairs.csv')
    ap.add_argument('--out-json', default='manifests/latest/part_inference_v1.json')
    args = ap.parse_args()

    batch = load_balanced(args.data_dir, mode=args.mode, samples_per_file=args.samples_per_file, max_files=args.max_files, device=args.device)
    model, build_info = build_model(Path(args.network_file), batch, args.device)
    load_info = load_checkpoint(model, args.checkpoint, args.device)
    model.eval()
    logits, forward_signature = run_logits(model, batch, args.batch_size)
    probs = torch.softmax(logits.float(), dim=1)
    pred = logits.argmax(1)
    y = batch['y'].detach().cpu().long()

    rows = []
    for i in range(len(y)):
        rows.append({
            'event_idx': i,
            'true_idx': int(y[i]), 'true_label': LABELS[int(y[i])],
            'pred_idx': int(pred[i]), 'pred_label': LABELS[int(pred[i])],
            'conf': float(probs[i, pred[i]]),
            'logit_true': float(logits[i, y[i]]),
            'logit_pred': float(logits[i, pred[i]]),
            'logit_Hqql': float(logits[i, LABELS.index('label_Hqql')]),
            'logit_Tbl': float(logits[i, LABELS.index('label_Tbl')]),
        })

    pair_counts = {}
    correct = 0
    for r in rows:
        correct += int(r['true_idx'] == r['pred_idx'])
        k = (r['true_label'], r['pred_label'])
        pair_counts[k] = pair_counts.get(k, 0) + 1
    conf_rows = [{'true_label': k[0], 'pred_label': k[1], 'n': v} for k, v in sorted(pair_counts.items(), key=lambda kv: kv[1], reverse=True)]
    acc = correct / max(1, len(rows))

    hqql_tbl = [r for r in rows if r['true_label'] == 'label_Hqql' and r['pred_label'] == 'label_Tbl']
    tbl_hqql = [r for r in rows if r['true_label'] == 'label_Tbl' and r['pred_label'] == 'label_Hqql']

    wcsv(args.out_pred, rows)
    wcsv(args.out_conf, conf_rows)
    wjson(args.out_json, {
        'ok': True,
        'n': len(rows),
        'accuracy': acc,
        'checkpoint': args.checkpoint,
        'builder': build_info,
        'load_info': load_info,
        'forward_signature': forward_signature,
        'Hqql_to_Tbl': len(hqql_tbl),
        'Tbl_to_Hqql': len(tbl_hqql),
    })

    md = ['# PART_INFERENCE_V1\n\n']
    md.append('ParT inference smoke test on local JetClass balanced sample. No training.\n\n')
    md.append(f'- checkpoint: `{args.checkpoint}`\n')
    md.append(f'- events: **{len(rows)}**\n')
    md.append(f'- accuracy: **{acc:.4f}**\n')
    md.append(f'- forward signature: `{forward_signature}`\n')
    md.append(f'- missing keys: **{len(load_info["missing"])}**\n')
    md.append(f'- unexpected keys: **{len(load_info["unexpected"])}**\n')
    md.append(f'- Hqql_to_Tbl: **{len(hqql_tbl)}**\n')
    md.append(f'- Tbl_to_Hqql: **{len(tbl_hqql)}**\n\n')
    md.append('## Top confusion pairs\n')
    md.append(mdtab(['true', 'pred', 'n'], [[r['true_label'], r['pred_label'], r['n']] for r in conf_rows[:30]]))
    md.append('\n## Next\n\nIf accuracy/logits are sane and Hqql/Tbl events exist, build `PART_ATTENTION_TRACE_V1` to export attention heads and pairwise particle flows for A/B/C.\n')
    Path(args.out_md).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out_md).write_text(''.join(md), encoding='utf-8')
    print(json.dumps({'ok': True, 'n': len(rows), 'accuracy': acc, 'Hqql_to_Tbl': len(hqql_tbl), 'Tbl_to_Hqql': len(tbl_hqql), 'out_md': args.out_md}, indent=2))

if __name__ == '__main__':
    main()
