#!/usr/bin/env bash
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"
mkdir -p reports/latest/tables manifests/latest

EVENTS_LIST="${BUNDLE_SWEEP_EVENTS_LIST:-64 128}"
STRENGTH_LIST="${BUNDLE_SWEEP_STRENGTH_LIST:-20 40 80}"
MICRO_BATCH="${BUNDLE_SWEEP_MICRO_BATCH:-8}"
TOP_ROUTES="${BUNDLE_SWEEP_TOP_ROUTES:-8}"

for E in $EVENTS_LIST; do
  for S in $STRENGTH_LIST; do
    TAG="e${E}_s${S}"
    echo "===== bundle sweep $TAG ====="
    python tools/part_bundle_causal_patch_real_contract_v1.py \
      --events-per-group "$E" \
      --micro-batch "$MICRO_BATCH" \
      --top-routes "$TOP_ROUTES" \
      --patch-strength "$S" \
      --out-md "reports/latest/PART_BUNDLE_CAUSAL_PATCH_REAL_CONTRACT_V1_${TAG}.md" \
      --out-csv "reports/latest/tables/part_bundle_causal_patch_real_contract_v1_${TAG}.csv" \
      --out-json "manifests/latest/part_bundle_causal_patch_real_contract_v1_${TAG}.json"
  done
done

python - <<'PY'
import csv
from pathlib import Path

rows=[]
for p in sorted(Path('reports/latest/tables').glob('part_bundle_causal_patch_real_contract_v1_e*_s*.csv')):
    tag=p.stem.replace('part_bundle_causal_patch_real_contract_v1_','')
    with p.open(newline='', encoding='utf-8') as f:
        for r in csv.DictReader(f):
            r=dict(r)
            r['tag']=tag
            rows.append(r)

def f(x):
    try: return float(x)
    except Exception: return 0.0

# Pick stable useful bundles: reduce B confusion, avoid destroying A/C too much.
summary=[]
by_bundle={}
for r in rows:
    by_bundle.setdefault(r['bundle'], []).append(r)
for b, xs in by_bundle.items():
    n=len(xs)
    b_mean=sum(f(x.get('B_Hqql_to_Tbl_delta_margin')) for x in xs)/max(1,n)
    b_flip=sum(f(x.get('B_Hqql_to_Tbl_delta_tbl_pred')) for x in xs)/max(1,n)
    a_mean=sum(f(x.get('A_Hqql_correct_delta_margin')) for x in xs)/max(1,n)
    c_mean=sum(f(x.get('C_Tbl_correct_delta_margin')) for x in xs)/max(1,n)
    helpful=sum(1 for x in xs if f(x.get('B_Hqql_to_Tbl_delta_margin')) < 0)
    flips=sum(1 for x in xs if f(x.get('B_Hqql_to_Tbl_delta_tbl_pred')) < 0)
    summary.append({
        'bundle': b,
        'runs': n,
        'helpful_runs': helpful,
        'flip_runs': flips,
        'mean_B_delta_margin': b_mean,
        'mean_B_delta_tbl_pred': b_flip,
        'mean_A_delta_margin': a_mean,
        'mean_C_delta_margin': c_mean,
        'kind': xs[0].get('kind',''),
        'n_rules': xs[0].get('n_rules',''),
    })
summary.sort(key=lambda r: (r['flip_runs'], -r['mean_B_delta_margin'] if r['mean_B_delta_margin'] < 0 else -999), reverse=True)

out_csv=Path('reports/latest/tables/part_bundle_causal_sweep_summary_v1.csv')
out_csv.parent.mkdir(parents=True, exist_ok=True)
fields=['bundle','kind','n_rules','runs','helpful_runs','flip_runs','mean_B_delta_margin','mean_B_delta_tbl_pred','mean_A_delta_margin','mean_C_delta_margin']
with out_csv.open('w', newline='', encoding='utf-8') as fcsv:
    w=csv.DictWriter(fcsv, fieldnames=fields)
    w.writeheader()
    for r in summary:
        w.writerow({k:r.get(k,'') for k in fields})

lines=['# PART_BUNDLE_CAUSAL_SWEEP_V1','', 'Stability sweep for bundle/head causal patches over direct-replay Hqql/Tbl groups.', '', '| bundle | kind | runs | helpful_runs | flip_runs | mean_B_delta_margin | mean_B_delta_tbl_pred | mean_A_delta_margin | mean_C_delta_margin |', '| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |']
for r in summary:
    lines.append(f"| {r['bundle']} | {r['kind']} | {r['runs']} | {r['helpful_runs']} | {r['flip_runs']} | {r['mean_B_delta_margin']:.6e} | {r['mean_B_delta_tbl_pred']:.6e} | {r['mean_A_delta_margin']:.6e} | {r['mean_C_delta_margin']:.6e} |")
lines.append('')
lines.append('## Reading')
lines.append('')
lines.append('- `helpful_runs`: runs where B Tbl-like margin decreased.')
lines.append('- `flip_runs`: runs where at least some B mistakes flipped away from Tbl.')
lines.append('- Strong candidate = high helpful_runs/flip_runs with moderate A/C damage.')
Path('reports/latest/PART_BUNDLE_CAUSAL_SWEEP_V1.md').write_text('\n'.join(lines)+'\n', encoding='utf-8')
print('\n'.join(lines))
PY

sed -n '1,220p' reports/latest/PART_BUNDLE_CAUSAL_SWEEP_V1.md
