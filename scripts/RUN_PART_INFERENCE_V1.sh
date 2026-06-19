#!/usr/bin/env bash
set -euo pipefail
cd "$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
mkdir -p reports/latest/tables manifests/latest runs
export PYTORCH_CUDA_ALLOC_CONF="${PYTORCH_CUDA_ALLOC_CONF:-expandable_segments:True}"

PYTHONUNBUFFERED=1 python tools/part_inference_v1.py \
  --repo-dir "${PART_REPO_DIR:-external/particle_transformer}" \
  --network-file "${PART_NETWORK_FILE:-external/particle_transformer/networks/example_ParticleTransformer.py}" \
  --checkpoint "${PART_CHECKPOINT:-external/particle_transformer/models/ParT_kinpid.pt}" \
  --data-dir "${JETCLASS_TINY:-$HOME/Рабочий стол/jetclass_tiny_balanced}" \
  --mode "${MODE:-kinpid}" \
  --samples-per-file "${SAMPLES_PER_FILE:-512}" \
  --max-files "${MAX_FILES:-100}" \
  --batch-size "${BATCH_SIZE:-32}" \
  --device "${DEVICE:-cuda}" \
  --out-md reports/latest/PART_INFERENCE_V1.md \
  --out-pred reports/latest/tables/part_inference_v1_predictions.csv \
  --out-conf reports/latest/tables/part_inference_v1_confusion_pairs.csv \
  --out-json manifests/latest/part_inference_v1.json \
  2>&1 | tee runs/part_inference_v1.log

git add tools/part_inference_v1.py scripts/RUN_PART_INFERENCE_V1.sh \
  reports/latest/PART_INFERENCE_V1.md \
  reports/latest/tables/part_inference_v1_predictions.csv \
  reports/latest/tables/part_inference_v1_confusion_pairs.csv \
  manifests/latest/part_inference_v1.json || true

git commit -m "Update ParT inference v1" || true
git push

echo "DONE ParT inference v1. Main report: reports/latest/PART_INFERENCE_V1.md"
