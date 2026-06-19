#!/usr/bin/env bash
set -euo pipefail
cd "$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
mkdir -p reports/latest/tables manifests/latest runs
PYTHONUNBUFFERED=1 python tools/hqql_tbl_confusion_physics_regime_v1.py \
  --checkpoint "${CHECKPOINT:-local_checkpoints/part/ParticleNet_kinpid.pt}" \
  --data-dir "${JETCLASS_TINY:-$HOME/Рабочий стол/jetclass_tiny_balanced}" \
  --mode "${MODE:-kinpid}" \
  --samples-per-file "${SAMPLES_PER_FILE:-256}" \
  --max-files "${MAX_FILES:-20}" \
  --device "${DEVICE:-cuda}" \
  --out-events reports/latest/tables/hqql_tbl_confusion_physics_events.csv \
  --out-summary reports/latest/tables/hqql_tbl_confusion_physics_summary.csv \
  --out-json manifests/latest/hqql_tbl_confusion_physics_regime_v1.json \
  --out-md reports/latest/HQQL_TBL_CONFUSION_PHYSICS_REGIME_V1.md \
  2>&1 | tee runs/hqql_tbl_confusion_physics_regime_v1.log

git add docs/02_physics/HQQL_TBL_PHYSICAL_CONFUSION_FRAME_v1.md tools/hqql_tbl_confusion_physics_regime_v1.py scripts/RUN_HQQL_TBL_CONFUSION_PHYSICS_REGIME_V1.sh \
  reports/latest/HQQL_TBL_CONFUSION_PHYSICS_REGIME_V1.md reports/latest/tables/hqql_tbl_confusion_physics_events.csv reports/latest/tables/hqql_tbl_confusion_physics_summary.csv manifests/latest/hqql_tbl_confusion_physics_regime_v1.json

git commit -m "Update Hqql Tbl physical confusion regime" || true
git push

echo "DONE Hqql/Tbl physical confusion regime. Main report: reports/latest/HQQL_TBL_CONFUSION_PHYSICS_REGIME_V1.md"
