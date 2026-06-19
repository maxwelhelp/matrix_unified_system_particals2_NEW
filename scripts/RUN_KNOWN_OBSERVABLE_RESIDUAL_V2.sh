#!/usr/bin/env bash
set -euo pipefail
cd "$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
mkdir -p reports/latest/tables manifests/latest runs

PYTHONUNBUFFERED=1 python tools/known_observable_residual_v2.py \
  --phase1-events reports/latest/tables/hqql_tbl_confusion_physics_events.csv \
  --seed "${SEED:-123}" \
  --lr "${LR:-0.05}" \
  --steps "${STEPS:-2000}" \
  --l2 "${L2:-0.001}" \
  --out-md reports/latest/KNOWN_OBSERVABLE_RESIDUAL_V2.md \
  --out-json manifests/latest/known_observable_residual_v2.json \
  --out-summary reports/latest/tables/known_observable_residual_v2_summary.csv \
  --out-bins reports/latest/tables/known_observable_residual_v2_isolation_bins.csv \
  --out-importance reports/latest/tables/known_observable_residual_v2_feature_importance.csv \
  2>&1 | tee runs/known_observable_residual_v2.log

git add docs/02_physics/MECHANISTIC_FINDING_LEPTON_ISOLATION_HQQL_TBL_v1.md \
  tools/known_observable_residual_v2.py scripts/RUN_KNOWN_OBSERVABLE_RESIDUAL_V2.sh \
  reports/latest/KNOWN_OBSERVABLE_RESIDUAL_V2.md \
  reports/latest/tables/known_observable_residual_v2_summary.csv \
  reports/latest/tables/known_observable_residual_v2_isolation_bins.csv \
  reports/latest/tables/known_observable_residual_v2_feature_importance.csv \
  manifests/latest/known_observable_residual_v2.json

git commit -m "Update known observable residual v2" || true
git push

echo "DONE known observable residual v2. Main report: reports/latest/KNOWN_OBSERVABLE_RESIDUAL_V2.md"
