#!/usr/bin/env bash
set -euo pipefail
cd "$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
mkdir -p runs reports/latest manifests/latest
PYTHONUNBUFFERED=1 python tools/particle_load_part_model_v1.py \
  --device "${DEVICE:-cuda}" \
  --checkpoint "${CHECKPOINT:-}" \
  --input-dim "${INPUT_DIM:-16}" \
  --classes "${CLASSES:-10}" \
  --particles "${PARTICLES:-32}" \
  --embed-dim "${EMBED_DIM:-64}" \
  --heads "${HEADS:-4}" \
  --layers "${LAYERS:-2}" \
  --cls-layers "${CLS_LAYERS:-1}" \
  --out-dir runs/particle_load_part_model_v1 \
  2>&1 | tee runs/particle_load_part_model_v1.log
cp -f runs/particle_load_part_model_v1/PART_MODEL_LOAD_REPORT.md reports/latest/PART_MODEL_LOAD_REPORT.md
cp -f runs/particle_load_part_model_v1/part_model_load_report.json manifests/latest/part_model_load_report.json
git add tools/particle_load_part_model_v1.py scripts/RUN_PARTICLE_LOAD_PART_MODEL_V1.sh reports/latest manifests/latest
git commit -m "Update particle model loader report" || true
git push
