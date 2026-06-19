#!/usr/bin/env bash
set -euo pipefail
cd "$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
mkdir -p runs reports/latest/tables manifests/latest
PYTHONUNBUFFERED=1 python tools/particle_order_control_v1.py \
  --checkpoint "${CHECKPOINT:-local_checkpoints/part/ParticleNet_kinpid.pt}" \
  --data-dir "${JETCLASS_TINY:-$HOME/Рабочий стол/jetclass_tiny_balanced}" \
  --mode "${MODE:-kinpid}" \
  --samples-per-file "${SAMPLES_PER_FILE:-256}" \
  --max-files "${MAX_FILES:-20}" \
  --micro-batch "${MICRO_BATCH:-128}" \
  --random-repeats "${RANDOM_REPEATS:-3}" \
  --seed "${SEED:-123}" \
  --device "${DEVICE:-cuda}" \
  --out-dir runs/particle_order_control_v1 \
  2>&1 | tee runs/particle_order_control_v1.log

cp -f runs/particle_order_control_v1/PARTICLE_ORDER_CONTROL_V1.md reports/latest/PARTICLE_ORDER_CONTROL_V1.md
cp -f runs/particle_order_control_v1/particle_order_control_v1.json manifests/latest/particle_order_control_v1.json
cp -f runs/particle_order_control_v1/tables/particle_order_control_summary.csv reports/latest/tables/particle_order_control.csv
cp -f runs/particle_order_control_v1/tables/particle_order_control_by_class.csv reports/latest/tables/particle_order_control_by_class.csv

git add tools/particle_order_control_v1.py \
  scripts/RUN_PARTICLE_ORDER_CONTROL_V1.sh \
  reports/latest/PARTICLE_ORDER_CONTROL_V1.md \
  reports/latest/tables/particle_order_control.csv \
  reports/latest/tables/particle_order_control_by_class.csv \
  manifests/latest/particle_order_control_v1.json

git commit -m "Update particle order control" || true
git push

echo "DONE particle order control. Main report: reports/latest/PARTICLE_ORDER_CONTROL_V1.md"
