#!/usr/bin/env bash
set -euo pipefail
cd "$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
mkdir -p reports/latest/tables manifests/latest runs
PYTHONUNBUFFERED=1 python tools/build_pseudocode_operation_database_v2.py \
  --pseudo reports/latest/tables/pseudocode_operation_database.csv \
  --trace reports/latest/tables/head_output_trace.csv \
  --align reports/latest/tables/layer_code_alignment_v2.csv \
  --out-csv reports/latest/tables/pseudocode_operation_database_v2.csv \
  --out-jsonl reports/latest/tables/pseudocode_operation_database_v2.jsonl \
  --out-json manifests/latest/pseudocode_operation_database_v2.json \
  --out-md reports/latest/PSEUDOCODE_OPERATION_DATABASE_V2.md \
  2>&1 | tee runs/pseudocode_operation_database_v2.log

git add tools/build_pseudocode_operation_database_v2.py scripts/RUN_PSEUDOCODE_OPERATION_DATABASE_V2.sh \
  reports/latest/PSEUDOCODE_OPERATION_DATABASE_V2.md reports/latest/tables/pseudocode_operation_database_v2.csv reports/latest/tables/pseudocode_operation_database_v2.jsonl manifests/latest/pseudocode_operation_database_v2.json

git commit -m "Update output-aware pseudocode operation database" || true
git push

echo "DONE pseudocode operation database v2. Main report: reports/latest/PSEUDOCODE_OPERATION_DATABASE_V2.md"
