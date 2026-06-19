#!/usr/bin/env bash
set -euo pipefail
cd "$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
mkdir -p reports/latest/tables manifests/latest runs

PYTHONUNBUFFERED=1 python tools/part_weaver_output_analyzer_v1.py \
  --glob "${ROOT_GLOB:-reports/latest/part_weaver_predict_smoke_v3*.root}" \
  --out-md reports/latest/PART_WEAVER_OUTPUT_ANALYZER_V1.md \
  --out-summary reports/latest/tables/part_weaver_output_analyzer_v1_summary.csv \
  --out-pairs reports/latest/tables/part_weaver_output_analyzer_v1_pairs.csv \
  --out-counts reports/latest/tables/part_weaver_output_analyzer_v1_counts.csv \
  --out-json manifests/latest/part_weaver_output_analyzer_v1.json \
  2>&1 | tee runs/part_weaver_output_analyzer_v1.log

git add tools/part_weaver_output_analyzer_v1.py scripts/RUN_PART_WEAVER_OUTPUT_ANALYZER_V1.sh \
  reports/latest/PART_WEAVER_OUTPUT_ANALYZER_V1.md \
  reports/latest/tables/part_weaver_output_analyzer_v1_summary.csv \
  reports/latest/tables/part_weaver_output_analyzer_v1_pairs.csv \
  reports/latest/tables/part_weaver_output_analyzer_v1_counts.csv \
  manifests/latest/part_weaver_output_analyzer_v1.json || true

git commit -m "Update ParT Weaver output analyzer" || true
git push || true

echo "DONE ParT Weaver output analyzer. Main report: reports/latest/PART_WEAVER_OUTPUT_ANALYZER_V1.md"
