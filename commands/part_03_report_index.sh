#!/usr/bin/env bash
set -euo pipefail

cd "$(git rev-parse --show-toplevel)"
mkdir -p reports/latest manifests/latest

python - <<'PY'
import json
from pathlib import Path
from datetime import datetime

out_md = Path('reports/latest/PART_INTERPRETABILITY_INDEX.md')
out_json = Path('manifests/latest/part_interpretability_index.json')

def size_h(n):
    x = float(n)
    for u in ['B','KB','MB','GB']:
        if x < 1024 or u == 'GB':
            return f'{x:.1f}{u}' if u != 'B' else f'{int(x)}B'
        x /= 1024

def files(pattern):
    arr = []
    for p in sorted(Path('.').glob(pattern)):
        if p.is_file():
            arr.append({'path': str(p), 'size': p.stat().st_size, 'size_h': size_h(p.stat().st_size)})
    return arr

sections = {
    'commands': files('commands/*.sh'),
    'reports': files('reports/latest/*.md'),
    'manifests': files('manifests/latest/*.json'),
    'tables': files('reports/latest/tables/*.csv')[:80],
    'tools': files('tools/*.py')[:160],
    'configs': files('external/particle_transformer/data/JetClass/*.yaml'),
}

priority = [
    'reports/latest/PART_SANITY_CONTRACT.md',
    'reports/latest/PART_WEAVER_OUTPUT_ANALYZER_V1.md',
    'reports/latest/PART_INTERPRETABILITY_INDEX.md',
    'reports/latest/PART_ATTENTION_SUPERTRACE_V1_RERUN_CLEAN_GROUPS.md',
    'reports/latest/PART_HQQL_TBL_GROUP_BUILDER_V1.md',
]

obj = {'created_at': datetime.now().isoformat(timespec='seconds'), 'priority': priority, **sections}
out_json.write_text(json.dumps(obj, indent=2, ensure_ascii=False), encoding='utf-8')

lines = ['# PART_INTERPRETABILITY_INDEX', '', f'- created_at: `{obj["created_at"]}`', '']
lines += ['## First files to inspect', '']
for p in priority:
    lines.append(f'- `{"OK" if Path(p).exists() else "MISSING"}` `{p}`')
lines.append('')

ana = Path('reports/latest/PART_WEAVER_OUTPUT_ANALYZER_V1.md')
lines += ['## Validity warning', '']
if not Path('reports/latest/PART_SANITY_CONTRACT.md').exists():
    lines.append('- Sanity contract report is missing. Run `bash commands/part_01_sanity_contract.sh` first.')
elif ana.exists():
    txt = ana.read_text(encoding='utf-8', errors='replace')
    if '0.000378' in txt or 'HToGG.root | 500000 | 0.0' in txt:
        lines.append('- Analyzer contains old collapsed smoke numbers. Regenerate predictions before using physics interpretation.')
    else:
        lines.append('- Analyzer exists. Check per-class accuracy before trusting supertrace.')
else:
    lines.append('- Analyzer report is missing. Run `bash commands/part_02_analyze_weaver_outputs.sh` after prediction.')
lines.append('')

for title, arr in sections.items():
    lines += [f'## {title}', '']
    if not arr:
        lines += ['_None found._', '']
        continue
    lines += ['| path | size |', '| --- | ---: |']
    for r in arr:
        lines.append(f"| `{r['path']}` | {r['size_h']} |")
    lines.append('')

out_md.write_text('\n'.join(lines) + '\n', encoding='utf-8')
print('\n'.join(lines[:120]))
PY
