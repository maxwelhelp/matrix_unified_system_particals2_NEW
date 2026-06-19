#!/usr/bin/env bash
set -euo pipefail

cd "$(git rev-parse --show-toplevel)"
mkdir -p reports/latest manifests/latest

python - <<'PY'
import importlib.util
import json
import os
import traceback
from pathlib import Path
from datetime import datetime

import torch

try:
    from weaver.utils.data.config import DataConfig
except Exception as e:
    DataConfig = None
    DATA_CONFIG_IMPORT_ERROR = repr(e)
else:
    DATA_CONFIG_IMPORT_ERROR = None

ROOT = Path('.')
NETWORK_FILE = Path(os.environ.get('PART_NETWORK', 'external/particle_transformer/networks/example_ParticleTransformer.py'))
MODES = [x.strip() for x in os.environ.get('PART_MODES', 'full,kinpid').split(',') if x.strip()]


def unwrap_state_dict(obj):
    sd = obj
    if isinstance(sd, dict):
        for key in ('model_state_dict', 'state_dict', 'model'):
            if key in sd and isinstance(sd[key], dict):
                sd = sd[key]
                break
    if isinstance(sd, dict):
        sd = {k.replace('module.', '', 1): v for k, v in sd.items()}
    return sd


def load_network(path):
    spec = importlib.util.spec_from_file_location('part_net', str(path))
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


def inspect_mode(mode):
    row = {
        'mode': mode,
        'yaml': f'external/particle_transformer/data/JetClass/JetClass_{mode}.yaml',
        'checkpoint': f'external/particle_transformer/models/ParT_{mode}.pt',
        'network': str(NETWORK_FILE),
        'ok': False,
        'errors': [],
    }
    yaml_path = Path(row['yaml'])
    ckpt_path = Path(row['checkpoint'])
    try:
        if DATA_CONFIG_IMPORT_ERROR:
            row['errors'].append('DataConfig import failed: ' + DATA_CONFIG_IMPORT_ERROR)
            return row
        if not NETWORK_FILE.exists():
            row['errors'].append('missing network file')
            return row
        if not yaml_path.exists():
            row['errors'].append('missing yaml')
            return row
        if not ckpt_path.exists():
            row['errors'].append('missing checkpoint; weights are intentionally not stored in git')
            return row

        dc = DataConfig.load(str(yaml_path))
        row['input_names'] = list(dc.input_names)
        row['pf_features_n'] = len(dc.input_dicts.get('pf_features', []))
        row['pf_features'] = list(dc.input_dicts.get('pf_features', []))
        row['labels'] = list(dc.label_value)

        mod = load_network(NETWORK_FILE)
        model, _ = mod.get_model(dc)
        raw = torch.load(str(ckpt_path), map_location='cpu')
        sd = unwrap_state_dict(raw)
        missing, unexpected = model.load_state_dict(sd, strict=False)
        row['missing_n'] = len(missing)
        row['unexpected_n'] = len(unexpected)
        row['missing_sample'] = list(missing[:10])
        row['unexpected_sample'] = list(unexpected[:10])
        model.load_state_dict(sd, strict=True)
        row['strict_load'] = True
        row['ok'] = True
    except Exception as e:
        row['errors'].append(repr(e))
        row['traceback_tail'] = traceback.format_exc().splitlines()[-20:]
    return row

rows = [inspect_mode(m) for m in MODES]

supertrace_path = Path('tools/part_attention_supertrace_v1.py')
supertrace_notes = []
if supertrace_path.exists():
    txt = supertrace_path.read_text(encoding='utf-8', errors='replace')
    if 'SimpleNamespace' in txt and "pf_features'" in txt and 'range(17)' in txt:
        supertrace_notes.append('WARNING: supertrace appears to contain a fake hardcoded 17-feature DataConfig. Use it for attention hooks only until it is migrated to real YAML/DataConfig input construction.')
    if 'event_to_arrays' in txt:
        supertrace_notes.append('event_to_arrays exists; verify it uses the same mode/YAML/checkpoint contract before trusting direct-gate predictions.')
else:
    supertrace_notes.append('tools/part_attention_supertrace_v1.py not found')

out = {
    'created_at': datetime.now().isoformat(timespec='seconds'),
    'network_file': str(NETWORK_FILE),
    'modes': rows,
    'supertrace_notes': supertrace_notes,
}
Path('manifests/latest/part_sanity_contract.json').write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding='utf-8')

lines = []
lines.append('# PART_SANITY_CONTRACT')
lines.append('')
lines.append(f'- created_at: `{out["created_at"]}`')
lines.append(f'- network: `{NETWORK_FILE}`')
lines.append('')
lines.append('## Mode contract')
lines.append('| mode | ok | pf_features_n | strict_load | missing | unexpected | errors |')
lines.append('| --- | --- | ---: | --- | ---: | ---: | --- |')
for r in rows:
    errors = '; '.join(r.get('errors', []))[:500]
    lines.append(f"| {r['mode']} | {r.get('ok')} | {r.get('pf_features_n','')} | {r.get('strict_load', False)} | {r.get('missing_n','')} | {r.get('unexpected_n','')} | {errors} |")
lines.append('')
lines.append('## Features')
for r in rows:
    lines.append(f"### {r['mode']}")
    lines.append('')
    lines.append(f"- yaml: `{r['yaml']}`")
    lines.append(f"- checkpoint: `{r['checkpoint']}`")
    lines.append(f"- ok: `{r.get('ok')}`")
    if r.get('pf_features'):
        lines.append('- pf_features:')
        for f in r['pf_features']:
            lines.append(f'  - `{f}`')
    if r.get('errors'):
        lines.append('- errors:')
        for e in r['errors']:
            lines.append(f'  - `{e}`')
    lines.append('')
lines.append('## Supertrace notes')
lines.append('')
for n in supertrace_notes:
    lines.append(f'- {n}')
lines.append('')
lines.append('## Decision')
lines.append('')
if all(r.get('ok') for r in rows):
    lines.append('`CONTRACT_OK`: all requested modes strict-load successfully. Next step: validate prediction outputs before interpretation.')
else:
    lines.append('`CONTRACT_NOT_OK`: fix missing files/imports/checkpoint mismatch before trusting interpretation reports.')

Path('reports/latest/PART_SANITY_CONTRACT.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')
print('\n'.join(lines[:80]))

if not all(r.get('ok') for r in rows):
    raise SystemExit(2)
PY
