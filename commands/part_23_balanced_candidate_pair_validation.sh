#!/usr/bin/env bash
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"
mkdir -p reports/latest/tables manifests/latest

python - <<'PY'
import csv, os
from pathlib import Path
from collections import Counter

def f(x):
    try: return float(x)
    except Exception: return 0.0

per_diag = int(os.environ.get('PAIR_VAL_BALANCED_PER_DIAG', '8'))
total = int(os.environ.get('PAIR_VAL_BALANCED_TOTAL', '32'))

src = Path('reports/latest/tables/part_discovery_candidates_real_contract_v1.csv')
out = Path('reports/latest/tables/part_discovery_candidates_balanced_v1.csv')
rows = list(csv.DictReader(src.open(newline='', encoding='utf-8')))
order = [
    'causal_candidate',
    'B_Tbl_push_read_write',
    'B_Tbl_resist_or_protective_read_write',
    'high_gradient_write_node',
]
selected = []
seen = set()
for diag in order:
    xs = [r for r in rows if r.get('diagnosis') == diag and '<-' in r.get('pair_role','')]
    xs.sort(key=lambda r: f(r.get('evidence_score')), reverse=True)
    n = 0
    for r in xs:
        k = (r.get('head_id',''), r.get('pair_role',''))
        if not k[0] or k in seen:
            continue
        selected.append(r)
        seen.add(k)
        n += 1
        if n >= per_diag:
            break
# top-up with overall best if needed
for r in sorted(rows, key=lambda r: f(r.get('evidence_score')), reverse=True):
    k = (r.get('head_id',''), r.get('pair_role',''))
    if not k[0] or '<-' not in k[1] or k in seen:
        continue
    selected.append(r)
    seen.add(k)
    if len(selected) >= total:
        break
fields = list(rows[0].keys()) if rows else []
out.parent.mkdir(parents=True, exist_ok=True)
selected = selected[:total]
with out.open('w', newline='', encoding='utf-8') as fcsv:
    w = csv.DictWriter(fcsv, fieldnames=fields)
    w.writeheader()
    for r in selected:
        w.writerow(r)
print('balanced_candidates', len(selected), '->', out)
print('diagnosis_counts', dict(Counter(r.get('diagnosis','') for r in selected)))
PY

python tools/part_candidate_pair_validation_v1.py \
  --candidates-csv reports/latest/tables/part_discovery_candidates_balanced_v1.csv \
  --events-per-group "${PAIR_VAL_EVENTS_PER_GROUP:-64}" \
  --micro-batch "${PAIR_VAL_MICRO_BATCH:-8}" \
  --max-candidates "${PAIR_VAL_BALANCED_TOTAL:-32}" \
  --strengths "${PAIR_VAL_STRENGTHS:-20,40,80}" \
  --out-md reports/latest/PART_CANDIDATE_PAIR_VALIDATION_BALANCED_V1.md \
  --out-rows reports/latest/tables/part_candidate_pair_validation_balanced_v1_rows.csv \
  --out-summary reports/latest/tables/part_candidate_pair_validation_balanced_v1_summary.csv \
  --out-json manifests/latest/part_candidate_pair_validation_balanced_v1.json

sed -n '1,320p' reports/latest/PART_CANDIDATE_PAIR_VALIDATION_BALANCED_V1.md
