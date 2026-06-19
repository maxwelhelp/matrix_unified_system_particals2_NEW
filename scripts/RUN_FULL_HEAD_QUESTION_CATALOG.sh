#!/usr/bin/env bash
set -euo pipefail
cd "$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
mkdir -p reports/latest/tables manifests/latest runs
PYTHONUNBUFFERED=1 python tools/export_full_head_question_catalog_v1.py \
  --heads reports/latest/tables/head_projection_question_map.csv \
  --out-md reports/latest/FULL_HEAD_QUESTION_CATALOG.md \
  --out-csv reports/latest/tables/full_head_question_catalog.csv \
  --out-json manifests/latest/full_head_question_catalog.json \
  2>&1 | tee runs/full_head_question_catalog.log
git add docs/FULL_HEAD_QUESTION_CATALOG_SPEC_v1.md tools/export_full_head_question_catalog_v1.py scripts/RUN_FULL_HEAD_QUESTION_CATALOG.sh reports/latest/FULL_HEAD_QUESTION_CATALOG.md reports/latest/tables/full_head_question_catalog.csv manifests/latest/full_head_question_catalog.json
git commit -m "Update full head question catalog" || true
git push

echo "DONE full head question catalog. Main file: reports/latest/FULL_HEAD_QUESTION_CATALOG.md"
