#!/usr/bin/env bash
set -euo pipefail
cd "$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
mkdir -p runs reports/latest/tables manifests/latest
PYTHONUNBUFFERED=1 python tools/particle0_topk_controls_v1.py \
  --checkpoint "${CHECKPOINT:-local_checkpoints/part/ParticleNet_kinpid.pt}" \
  --data-dir "${JETCLASS_TINY:-$HOME/Рабочий стол/jetclass_tiny_balanced}" \
  --mode "${MODE:-kinpid}" \
  --samples-per-file "${SAMPLES_PER_FILE:-256}" \
  --max-files "${MAX_FILES:-20}" \
  --micro-batch "${MICRO_BATCH:-128}" \
  --top-k "${TOP_K:-1,2,4,8,16}" \
  --random-repeats "${RANDOM_REPEATS:-3}" \
  --seed "${SEED:-123}" \
  --device "${DEVICE:-cuda}" \
  --out-dir runs/particle0_topk_controls_v1 \
  2>&1 | tee runs/particle0_topk_controls_v1.log

cp -f runs/particle0_topk_controls_v1/PARTICLE0_TOPK_CONTROLS_V1.md reports/latest/PARTICLE0_TOPK_CONTROLS_V1.md
cp -f runs/particle0_topk_controls_v1/particle0_topk_controls_v1.json manifests/latest/particle0_topk_controls_v1.json
cp -f runs/particle0_topk_controls_v1/tables/particle0_topk_control_summary.csv reports/latest/tables/particle0_topk_control_summary.csv
cp -f runs/particle0_topk_controls_v1/tables/particle0_topk_control_by_class.csv reports/latest/tables/particle0_topk_control_by_class.csv
cp -f runs/particle0_topk_controls_v1/tables/particle0_topk_random_baselines.csv reports/latest/tables/particle0_topk_random_baselines.csv

git add tools/particle0_topk_controls_v1.py \
  scripts/RUN_PARTICLE0_TOPK_CONTROLS_V1.sh \
  reports/latest/PARTICLE0_TOPK_CONTROLS_V1.md \
  reports/latest/tables/particle0_topk_control_summary.csv \
  reports/latest/tables/particle0_topk_control_by_class.csv \
  reports/latest/tables/particle0_topk_random_baselines.csv \
  manifests/latest/particle0_topk_controls_v1.json

git commit -m "Update particle0 top-k controls" || true
git push

echo "DONE particle0 top-k controls. Main report: reports/latest/PARTICLE0_TOPK_CONTROLS_V1.md"
