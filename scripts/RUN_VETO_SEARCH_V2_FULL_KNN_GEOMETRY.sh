#!/usr/bin/env bash
set -euo pipefail
cd "$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
mkdir -p reports/latest/tables manifests/latest runs

PYTHONUNBUFFERED=1 python tools/veto_search_v2_full_knn_geometry.py \
  --phase1-events reports/latest/tables/hqql_tbl_confusion_physics_events.csv \
  --data-dir "${JETCLASS_TINY:-$HOME/Рабочий стол/jetclass_tiny_balanced}" \
  --mode "${MODE:-kinpid}" \
  --samples-per-file "${SAMPLES_PER_FILE:-4096}" \
  --max-files "${MAX_FILES:-1000}" \
  --isolation-threshold "${ISOLATION_THRESHOLD:-0.30}" \
  --p0-lepton-dr-threshold "${P0_LEPTON_DR_THRESHOLD:-0.05}" \
  --patch-k "${PATCH_K:-16}" \
  --device "${DEVICE:-cpu}" \
  --out-md reports/latest/VETO_SEARCH_V2_FULL_KNN_GEOMETRY.md \
  --out-events reports/latest/tables/veto_search_v2_full_knn_events.csv \
  --out-contrasts reports/latest/tables/veto_search_v2_full_knn_contrasts.csv \
  --out-json manifests/latest/veto_search_v2_full_knn_geometry.json \
  2>&1 | tee runs/veto_search_v2_full_knn_geometry.log

git add tools/veto_search_v2_full_knn_geometry.py scripts/RUN_VETO_SEARCH_V2_FULL_KNN_GEOMETRY.sh \
  reports/latest/VETO_SEARCH_V2_FULL_KNN_GEOMETRY.md \
  reports/latest/tables/veto_search_v2_full_knn_events.csv \
  reports/latest/tables/veto_search_v2_full_knn_contrasts.csv \
  manifests/latest/veto_search_v2_full_knn_geometry.json

git commit -m "Update VETO search v2 full KNN geometry" || true
git push

echo "DONE VETO search v2 full KNN geometry. Main report: reports/latest/VETO_SEARCH_V2_FULL_KNN_GEOMETRY.md"
