#!/usr/bin/env python3
import argparse, importlib, json, os, sys
from pathlib import Path


def rel(path, root):
    try:
        return str(Path(path).resolve().relative_to(Path(root).resolve()))
    except Exception:
        return str(path)


def find_files(root, patterns):
    out = []
    root = Path(root)
    if not root.exists():
        return out
    for pat in patterns:
        out.extend(root.rglob(pat))
    return sorted(set(out))


def try_imports(repo_dir):
    sys.path.insert(0, str(Path(repo_dir).resolve()))
    candidates = [
        'weaver',
        'weaver.nn',
        'weaver.nn.model',
        'weaver.nn.model.ParticleTransformer',
        'weaver.nn.model.ParticleTransformer2023',
    ]
    rows = []
    for name in candidates:
        try:
            mod = importlib.import_module(name)
            rows.append({'module': name, 'ok': True, 'file': getattr(mod, '__file__', '')})
        except Exception as e:
            rows.append({'module': name, 'ok': False, 'error': repr(e)})
    return rows


def md_table(headers, rows):
    if not rows:
        return '_No rows._\n'
    out = ['| ' + ' | '.join(headers) + ' |', '| ' + ' | '.join(['---'] * len(headers)) + ' |']
    for row in rows:
        out.append('| ' + ' | '.join(str(x).replace('\n', ' ') for x in row) + ' |')
    return '\n'.join(out) + '\n'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--repo-dir', default='external/particle_transformer')
    ap.add_argument('--out-md', default='reports/latest/PART_BOOTSTRAP_PROBE_V1.md')
    ap.add_argument('--out-json', default='manifests/latest/part_bootstrap_probe_v1.json')
    args = ap.parse_args()

    repo = Path(args.repo_dir)
    exists = repo.exists()
    py_model_files = find_files(repo, ['*Particle*Transformer*.py', '*part*transform*.py', '*ParT*.py'])
    yaml_files = find_files(repo, ['*.yaml', '*.yml', '*.json'])
    ckpt_files = find_files(repo, ['*.pt', '*.pth', '*.ckpt', '*.onnx'])
    imports = try_imports(repo) if exists else []

    result = {
        'ok': bool(exists),
        'repo_dir': str(repo),
        'exists': exists,
        'model_files': [rel(p, repo) for p in py_model_files[:80]],
        'config_files': [rel(p, repo) for p in yaml_files[:80]],
        'checkpoint_files': [rel(p, repo) for p in ckpt_files[:80]],
        'imports': imports,
        'next': 'If imports fail, install ParT/weaver requirements or run from the ParT repo environment before writing attention trace.',
    }

    Path(args.out_json).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out_json).write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding='utf-8')

    md = []
    md.append('# PART_BOOTSTRAP_PROBE_V1\n\n')
    md.append('Bootstrap probe for Particle Transformer / ParT integration. This does not train or run inference yet.\n\n')
    md.append(f'- repo_dir: `{repo}`\n')
    md.append(f'- exists: **{exists}**\n')
    md.append(f'- model files found: **{len(py_model_files)}**\n')
    md.append(f'- config/json files found: **{len(yaml_files)}**\n')
    md.append(f'- checkpoint files found: **{len(ckpt_files)}**\n\n')
    md.append('## Import checks\n')
    md.append(md_table(['module', 'ok', 'file/error'], [[r.get('module'), r.get('ok'), r.get('file') or r.get('error')] for r in imports]))
    md.append('\n## Candidate model files\n')
    md.append(md_table(['path'], [[rel(p, repo)] for p in py_model_files[:40]]))
    md.append('\n## Candidate config files\n')
    md.append(md_table(['path'], [[rel(p, repo)] for p in yaml_files[:40]]))
    md.append('\n## Candidate checkpoints inside repo\n')
    md.append(md_table(['path'], [[rel(p, repo)] for p in ckpt_files[:40]]))
    md.append('\n## Next\n\n')
    md.append('If the ParticleTransformer module imports, write `PART_INFERENCE_V1`. If import fails, install requirements and rerun this probe.\n')

    Path(args.out_md).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out_md).write_text(''.join(md), encoding='utf-8')
    print(json.dumps({'ok': exists, 'out_md': args.out_md, 'model_files': len(py_model_files), 'imports_ok': sum(1 for r in imports if r.get('ok'))}, indent=2))


if __name__ == '__main__':
    main()
