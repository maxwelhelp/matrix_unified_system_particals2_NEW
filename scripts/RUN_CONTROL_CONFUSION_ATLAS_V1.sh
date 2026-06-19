#!/usr/bin/env bash
set -euo pipefail
cd "$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
mkdir -p runs reports/latest/tables manifests/latest
PYTHONUNBUFFERED=1 python tools/control_confusion_atlas_v1.py \
  --checkpoint "${CHECKPOINT:-local_checkpoints/part/ParticleNet_kinpid.pt}" \
  --data-dir "${JETCLASS_TINY:-$HOME/Рабочий стол/jetclass_tiny_balanced}" \
  --mode "${MODE:-kinpid}" \
  --samples-per-file "${SAMPLES_PER_FILE:-256}" \
  --max-files "${MAX_FILES:-20}" \
  --micro-batch "${MICRO_BATCH:-128}" \
  --top-k "${TOP_K:-1,2,4,8,16}" \
  --seed "${SEED:-123}" \
  --device "${DEVICE:-cuda}" \
  --out-dir runs/control_confusion_atlas_v1 \
  2>&1 | tee runs/control_confusion_atlas_v1.log

cp -f runs/control_confusion_atlas_v1/CONTROL_CONFUSION_ATLAS_V1.md reports/latest/CONTROL_CONFUSION_ATLAS_V1.md
cp -f runs/control_confusion_atlas_v1/control_confusion_atlas_v1.json manifests/latest/control_confusion_atlas_v1.json
cp -f runs/control_confusion_atlas_v1/tables/control_confusion_transitions.csv reports/latest/tables/control_confusion_transitions.csv
cp -f runs/control_confusion_atlas_v1/tables/control_confusion_by_class.csv reports/latest/tables/control_confusion_by_class.csv
cp -f runs/control_confusion_atlas_v1/tables/control_confusion_summary.csv reports/latest/tables/control_confusion_summary.csv

git add tools/control_confusion_atlas_v1.py \
  scripts/RUN_CONTROL_CONFUSION_ATLAS_V1.sh \
  reports/latest/CONTROL_CONFUSION_ATLAS_V1.md \
  reports/latest/tables/control_confusion_transitions.csv \
  reports/latest/tables/control_confusion_by_class.csv \
  reports/latest/tables/control_confusion_summary.csv \
  manifests/latest/control_confusion_atlas_v1.json

git commit -m "Update control confusion atlas" || true
git push

echo "DONE control confusion atlas. Main report: reports/latest/CONTROL_CONFUSION_ATLAS_V1.md"
