#!/usr/bin/env bash
set -euo pipefail
cd "$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
mkdir -p reports/latest/tables manifests/latest runs
PYTHONUNBUFFERED=1 python tools/build_layer_code_alignment_v1.py \
  --pseudocode reports/latest/tables/pseudocode_operation_database.csv \
  --checkpoint "${CHECKPOINT:-local_checkpoints/part/ParticleNet_kinpid.pt}" \
  --data-dir "${JETCLASS_TINY:-$HOME/Рабочий стол/jetclass_tiny_balanced}" \
  --mode "${MODE:-kinpid}" \
  --samples-per-file "${SAMPLES_PER_FILE:-16}" \
  --max-files "${MAX_FILES:-10}" \
  --device "${DEVICE:-cuda}" \
  --out-csv reports/latest/tables/layer_code_alignment.csv \
  --out-json manifests/latest/layer_code_alignment_v1.json \
  --out-md reports/latest/LAYER_CODE_ALIGNMENT_V1.md \
  2>&1 | tee runs/layer_code_alignment_v1.log

git add docs/01_method/LAYER_CODE_ALIGNMENT_v1.md \
  tools/build_layer_code_alignment_v1.py \
  scripts/RUN_LAYER_CODE_ALIGNMENT_V1.sh \
  reports/latest/LAYER_CODE_ALIGNMENT_V1.md \
  reports/latest/tables/layer_code_alignment.csv \
  manifests/latest/layer_code_alignment_v1.json

git commit -m "Update layer code alignment" || true
git push

echo "DONE layer code alignment. Main report: reports/latest/LAYER_CODE_ALIGNMENT_V1.md"
