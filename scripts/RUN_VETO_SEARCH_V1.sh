#!/usr/bin/env bash
set -euo pipefail
cd "$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
mkdir -p reports/latest/tables manifests/latest runs

PYTHONUNBUFFERED=1 python tools/veto_search_v1.py \
  --phase1-events reports/latest/tables/hqql_tbl_confusion_physics_events.csv \
  --isolation-threshold "${ISOLATION_THRESHOLD:-0.30}" \
  --out-md reports/latest/VETO_SEARCH_V1.md \
  --out-csv reports/latest/tables/veto_search_v1_feature_contrasts.csv \
  --out-json manifests/latest/veto_search_v1.json \
  2>&1 | tee runs/veto_search_v1.log

git add docs/что_считает_нейронка/00_ВАЖНО_МЕТОД_АНАЛИЗА/README.md \
  docs/что_считает_нейронка/00_ВАЖНО_МЕТОД_АНАЛИЗА/REASONING_FRAMEWORK_V1.md \
  docs/что_считает_нейронка/02_текущая_задача_particlenet_hqql_tbl/06_next_steps/VETO_SEARCH_V1.md \
  tools/veto_search_v1.py scripts/RUN_VETO_SEARCH_V1.sh \
  reports/latest/VETO_SEARCH_V1.md reports/latest/tables/veto_search_v1_feature_contrasts.csv manifests/latest/veto_search_v1.json

git commit -m "Add reasoning framework and VETO search" || true
git push

echo "DONE VETO search. Main report: reports/latest/VETO_SEARCH_V1.md"
