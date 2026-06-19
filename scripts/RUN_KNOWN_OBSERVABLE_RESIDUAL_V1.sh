#!/usr/bin/env bash
set -euo pipefail
cd "$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
mkdir -p runs reports/latest/tables manifests/latest
PYTHONUNBUFFERED=1 python tools/known_observable_residual_v1.py \
  --checkpoint "${CHECKPOINT:-local_checkpoints/part/ParticleNet_kinpid.pt}" \
  --data-dir "${JETCLASS_TINY:-$HOME/Рабочий стол/jetclass_tiny_balanced}" \
  --mode "${MODE:-kinpid}" \
  --samples-per-file "${SAMPLES_PER_FILE:-256}" \
  --max-files "${MAX_FILES:-20}" \
  --micro-batch "${MICRO_BATCH:-128}" \
  --seed "${SEED:-123}" \
  --ridge-lambda "${RIDGE_LAMBDA:-0.01}" \
  --device "${DEVICE:-cuda}" \
  --out-dir runs/known_observable_residual_v1 \
  2>&1 | tee runs/known_observable_residual_v1.log

cp -f runs/known_observable_residual_v1/KNOWN_OBSERVABLE_RESIDUAL_V1.md reports/latest/KNOWN_OBSERVABLE_RESIDUAL_V1.md
cp -f runs/known_observable_residual_v1/known_observable_residual_v1.json manifests/latest/known_observable_residual_v1.json
cp -f runs/known_observable_residual_v1/tables/known_observable_residual_by_class.csv reports/latest/tables/known_observable_residual_by_class.csv
cp -f runs/known_observable_residual_v1/tables/known_observable_feature_importance.csv reports/latest/tables/known_observable_feature_importance.csv
cp -f runs/known_observable_residual_v1/tables/known_observable_residual_top_events.csv reports/latest/tables/known_observable_residual_top_events.csv

git add tools/known_observable_residual_v1.py \
  scripts/RUN_KNOWN_OBSERVABLE_RESIDUAL_V1.sh \
  reports/latest/KNOWN_OBSERVABLE_RESIDUAL_V1.md \
  reports/latest/tables/known_observable_residual_by_class.csv \
  reports/latest/tables/known_observable_feature_importance.csv \
  reports/latest/tables/known_observable_residual_top_events.csv \
  manifests/latest/known_observable_residual_v1.json

git commit -m "Update known observable residual" || true
git push

echo "DONE known observable residual. Main report: reports/latest/KNOWN_OBSERVABLE_RESIDUAL_V1.md"
