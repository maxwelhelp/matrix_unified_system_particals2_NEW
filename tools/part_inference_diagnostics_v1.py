#!/usr/bin/env python3
import argparse, csv, importlib.util, itertools, json, sys
from pathlib import Path
import torch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools.part_inference_v1 import build_model, load_checkpoint, one_batch
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


def forward_variants(model, b):
    pts, feat, mask = b['points'], b['features'], b['mask']
    vec = b.get('vectors', None)
    variants = []
    if vec is not None:
        variants += [
            ('points_features_vectors_mask', lambda: model(pts, feat, vec, mask)),
            ('features_vectors_mask', lambda: model(feat, vec, mask)),
            ('features_points_vectors_mask', lambda: model(feat, pts, vec, mask)),
            ('points_vectors_features_mask', lambda: model(pts, vec, feat, mask)),
        ]
    variants += [
        ('points_features_mask', lambda: model(pts, feat, mask)),
        ('features_mask', lambda: model(feat, mask)),
    ]
    return variants


def run_variant(model, batch, name, fn_builder, batch_size):
    outs = []
    with torch.no_grad():
        for s in range(0, int(batch['y'].shape[0]), batch_size):
            b = one_batch(batch, list(range(s, min(int(batch['y'].shape[0]), s + batch_size))))
            fn = dict(forward_variants(model, b))[name]
            out = fn()
            if isinstance(out, (tuple, list)):
                out = out[0]
            outs.append(out.detach().cpu())
    return torch.cat(outs, 0)


def confusion(y, pred, n=10):
    m = [[0 for _ in range(n)] for __ in range(n)]
    for a, b in zip(y.tolist(), pred.tolist()):
        m[int(a)][int(b)] += 1
    return m


def best_perm_acc(cm):
    n = len(cm)
    # dp over true classes assigning unique pred labels maximizing diagonal after remap true->pred.
    dp = {0: (0, [])}
    for i in range(n):
        ndp = {}
        for mask, (score, perm) in dp.items():
            for j in range(n):
                if mask & (1 << j):
                    continue
                nm = mask | (1 << j)
                ns = score + cm[i][j]
                if nm not in ndp or ns > ndp[nm][0]:
                    ndp[nm] = (ns, perm + [j])
        dp = ndp
    score, perm = dp[(1 << n) - 1]
    total = sum(sum(r) for r in cm)
    return score / max(1, total), perm, score


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--network-file', default='external/particle_transformer/networks/example_ParticleTransformer.py')
    ap.add_argument('--checkpoint', default='external/particle_transformer/models/ParT_kinpid.pt')
    ap.add_argument('--data-dir', default=str(Path.home()/'Рабочий стол/jetclass_tiny_balanced'))
    ap.add_argument('--mode', default='kinpid')
    ap.add_argument('--samples-per-file', type=int, default=256)
    ap.add_argument('--max-files', type=int, default=100)
    ap.add_argument('--batch-size', type=int, default=32)
    ap.add_argument('--device', default='cuda' if torch.cuda.is_available() else 'cpu')
    ap.add_argument('--out-md', default='reports/latest/PART_INFERENCE_DIAGNOSTICS_V1.md')
    ap.add_argument('--out-csv', default='reports/latest/tables/part_inference_diagnostics_v1_variants.csv')
    ap.add_argument('--out-json', default='manifests/latest/part_inference_diagnostics_v1.json')
    args = ap.parse_args()

    batch = load_balanced(args.data_dir, mode=args.mode, samples_per_file=args.samples_per_file, max_files=args.max_files, device=args.device)
    model, build_info = build_model(Path(args.network_file), batch, args.device)
    load_info = load_checkpoint(model, args.checkpoint, args.device)
    model.eval()
    y = batch['y'].detach().cpu().long()

    # Probe which variants execute on one batch.
    b0 = one_batch(batch, list(range(min(int(batch['y'].shape[0]), args.batch_size))))
    executable = []
    errors = []
    for name, fn in forward_variants(model, b0):
        try:
            out = fn()
            if isinstance(out, (tuple, list)):
                out = out[0]
            executable.append(name)
        except Exception as e:
            errors.append({'variant': name, 'error': repr(e)[:500]})

    rows = []
    for name in executable:
        try:
            logits = run_variant(model, batch, name, None, args.batch_size)
            pred = logits.argmax(1)
            acc = float((pred == y).float().mean())
            cm = confusion(y, pred, len(LABELS))
            pacc, perm, pscore = best_perm_acc(cm)
            pred_counts = torch.bincount(pred, minlength=len(LABELS)).tolist()
            rows.append({
                'variant': name,
                'ok': True,
                'accuracy': acc,
                'best_label_permutation_accuracy': pacc,
                'best_label_permutation_score': pscore,
                'best_true_to_pred_perm': json.dumps({LABELS[i]: LABELS[perm[i]] for i in range(len(LABELS))}, ensure_ascii=False),
                'pred_counts': json.dumps({LABELS[i]: pred_counts[i] for i in range(len(LABELS))}, ensure_ascii=False),
            })
        except Exception as e:
            rows.append({'variant': name, 'ok': False, 'error': repr(e)[:500]})

    wcsv(args.out_csv, rows)
    result = {
        'ok': True,
        'n': int(y.numel()),
        'build_info': build_info,
        'load_info': load_info,
        'executable_variants': executable,
        'variant_errors': errors,
        'rows': rows,
        'diagnosis': 'If all variants have ~0.10 accuracy and best permutation accuracy is also low, issue is input preprocessing/data mapping/config, not label order only.',
    }
    wjson(args.out_json, result)

    md = ['# PART_INFERENCE_DIAGNOSTICS_V1\n\n']
    md.append('Diagnostic for low ParT inference accuracy. Tests all executable forward signatures and label-permutation upper bound.\n\n')
    md.append(f'- events: **{int(y.numel())}**\n')
    md.append(f'- missing keys: **{len(load_info["missing"])}**\n')
    md.append(f'- unexpected keys: **{len(load_info["unexpected"])}**\n')
    md.append(f'- executable variants: `{", ".join(executable)}`\n\n')
    md.append('## Variant results\n')
    md.append(mdtab(['variant','acc','perm_acc','pred_counts'], [[r.get('variant'), f"{r.get('accuracy',0):.4f}" if r.get('ok') else 'ERR', f"{r.get('best_label_permutation_accuracy',0):.4f}" if r.get('ok') else '', r.get('pred_counts', r.get('error',''))] for r in rows]))
    md.append('\n## Interpretation\n\n')
    md.append('- If raw accuracy is low but permutation accuracy is high, label order is wrong.\n')
    md.append('- If both raw and permutation accuracy are low, input preprocessing/model config/data split is wrong.\n')
    md.append('- If another forward variant is much better, update PART_INFERENCE_V1 to use that signature.\n')
    Path(args.out_md).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out_md).write_text(''.join(md), encoding='utf-8')
    print(json.dumps({'ok': True, 'n': int(y.numel()), 'rows': rows, 'out_md': args.out_md}, indent=2))

if __name__ == '__main__':
    main()
