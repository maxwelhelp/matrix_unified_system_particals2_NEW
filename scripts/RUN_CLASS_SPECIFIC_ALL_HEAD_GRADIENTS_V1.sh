#!/usr/bin/env bash
set -euo pipefail
cd "$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
mkdir -p runs reports/latest/tables manifests/latest
PYTHONUNBUFFERED=1 python tools/class_specific_all_head_gradients_v1.py \
  --checkpoint "${CHECKPOINT:-local_checkpoints/part/ParticleNet_kinpid.pt}" \
  --data-dir "${JETCLASS_TINY:-$HOME/Рабочий стол/jetclass_tiny_balanced}" \
  --mode "${MODE:-kinpid}" \
  --samples-per-file "${SAMPLES_PER_FILE:-256}" \
  --max-files "${MAX_FILES:-20}" \
  --head-groups "${HEAD_GROUPS:-8}" \
  --micro-batch "${MICRO_BATCH:-32}" \
  --classes "${CLASSES:-Hqql,Tbl,H4q,QCD,Wqq,Zqq,Hcc}" \
  --device "${DEVICE:-cuda}" \
  --out-dir runs/class_specific_all_head_gradients_v1 \
  2>&1 | tee runs/class_specific_all_head_gradients_v1.log

cp -f runs/class_specific_all_head_gradients_v1/CLASS_SPECIFIC_ALL_HEAD_GRADIENTS_V1.md reports/latest/CLASS_SPECIFIC_ALL_HEAD_GRADIENTS_V1.md
cp -f runs/class_specific_all_head_gradients_v1/class_specific_all_head_gradients_v1.json manifests/latest/class_specific_all_head_gradients_v1.json
cp -f runs/class_specific_all_head_gradients_v1/tables/class_specific_head_gradients.csv reports/latest/tables/class_specific_head_gradients.csv
cp -f runs/class_specific_all_head_gradients_v1/tables/class_specific_head_gradient_summary.csv reports/latest/tables/class_specific_head_gradient_summary.csv

git add tools/class_specific_all_head_gradients_v1.py \
  scripts/RUN_CLASS_SPECIFIC_ALL_HEAD_GRADIENTS_V1.sh \
  reports/latest/CLASS_SPECIFIC_ALL_HEAD_GRADIENTS_V1.md \
  reports/latest/tables/class_specific_head_gradients.csv \
  reports/latest/tables/class_specific_head_gradient_summary.csv \
  manifests/latest/class_specific_all_head_gradients_v1.json

git commit -m "Update class-specific all-head gradients" || true
git push

echo "DONE class-specific all-head gradients. Main report: reports/latest/CLASS_SPECIFIC_ALL_HEAD_GRADIENTS_V1.md"
