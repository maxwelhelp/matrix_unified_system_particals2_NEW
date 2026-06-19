#!/usr/bin/env bash
set -euo pipefail
cd "$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
mkdir -p reports/latest/tables manifests/latest runs

PYTHONUNBUFFERED=1 python tools/known_observable_residual_v2_1_behavior.py \
  --phase1-events reports/latest/tables/hqql_tbl_confusion_physics_events.csv \
  --seed "${SEED:-123}" \
  --lr "${LR:-0.05}" \
  --steps "${STEPS:-3000}" \
  --l2 "${L2:-0.001}" \
  --pos-weight "${POS_WEIGHT:-8.0}" \
  --out-md reports/latest/KNOWN_OBSERVABLE_RESIDUAL_V2_1_BEHAVIOR.md \
  --out-json manifests/latest/known_observable_residual_v2_1_behavior.json \
  --out-bins reports/latest/tables/known_observable_residual_v2_1_behavior_bins.csv \
  --out-importance reports/latest/tables/known_observable_residual_v2_1_behavior_importance.csv \
  2>&1 | tee runs/known_observable_residual_v2_1_behavior.log

git add docs/02_physics/KNOWN_OBSERVABLE_RESIDUAL_V2_1_BEHAVIOR_SURROGATE.md \
  tools/known_observable_residual_v2_1_behavior.py scripts/RUN_KNOWN_OBSERVABLE_RESIDUAL_V2_1_BEHAVIOR.sh \
  reports/latest/KNOWN_OBSERVABLE_RESIDUAL_V2_1_BEHAVIOR.md \
  reports/latest/tables/known_observable_residual_v2_1_behavior_bins.csv \
  reports/latest/tables/known_observable_residual_v2_1_behavior_importance.csv \
  manifests/latest/known_observable_residual_v2_1_behavior.json

git commit -m "Update known observable residual v2.1 behavior" || true
git push

echo "DONE known observable residual v2.1 behavior. Main report: reports/latest/KNOWN_OBSERVABLE_RESIDUAL_V2_1_BEHAVIOR.md"
