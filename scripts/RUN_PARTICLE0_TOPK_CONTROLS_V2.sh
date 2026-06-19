#!/usr/bin/env bash
set -euo pipefail
cd "$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
mkdir -p runs reports/latest/tables manifests/latest
PYTHONUNBUFFERED=1 python tools/particle0_topk_controls_v2.py \
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
  --out-dir runs/particle0_topk_controls_v2 \
  2>&1 | tee runs/particle0_topk_controls_v2.log

cp -f runs/particle0_topk_controls_v2/PARTICLE0_TOPK_CONTROLS_V2.md reports/latest/PARTICLE0_TOPK_CONTROLS_V2.md
cp -f runs/particle0_topk_controls_v2/particle0_topk_controls_v2.json manifests/latest/particle0_topk_controls_v2.json
cp -f runs/particle0_topk_controls_v2/tables/particle0_topk_control_summary_v2.csv reports/latest/tables/particle0_topk_control_summary_v2.csv
cp -f runs/particle0_topk_controls_v2/tables/particle0_topk_control_by_class_v2.csv reports/latest/tables/particle0_topk_control_by_class_v2.csv
cp -f runs/particle0_topk_controls_v2/tables/particle0_topk_random_baselines_v2.csv reports/latest/tables/particle0_topk_random_baselines_v2.csv

# Compatibility marker for comparison engine v2: it checks v1 names to know the control exists.
cp -f reports/latest/PARTICLE0_TOPK_CONTROLS_V2.md reports/latest/PARTICLE0_TOPK_CONTROLS_V1.md
cp -f manifests/latest/particle0_topk_controls_v2.json manifests/latest/particle0_topk_controls_v1.json
cp -f reports/latest/tables/particle0_topk_control_summary_v2.csv reports/latest/tables/particle0_topk_controls.csv

git add tools/particle0_topk_controls_v2.py \
  scripts/RUN_PARTICLE0_TOPK_CONTROLS_V2.sh \
  reports/latest/PARTICLE0_TOPK_CONTROLS_V2.md reports/latest/PARTICLE0_TOPK_CONTROLS_V1.md \
  reports/latest/tables/particle0_topk_control_summary_v2.csv \
  reports/latest/tables/particle0_topk_control_by_class_v2.csv \
  reports/latest/tables/particle0_topk_random_baselines_v2.csv \
  reports/latest/tables/particle0_topk_controls.csv \
  manifests/latest/particle0_topk_controls_v2.json manifests/latest/particle0_topk_controls_v1.json

git commit -m "Update particle0 top-k controls v2" || true
git push

echo "DONE particle0 top-k controls v2. Main report: reports/latest/PARTICLE0_TOPK_CONTROLS_V2.md"
