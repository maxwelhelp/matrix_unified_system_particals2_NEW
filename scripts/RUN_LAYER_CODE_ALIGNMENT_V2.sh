#!/usr/bin/env bash
set -euo pipefail
cd "$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
mkdir -p reports/latest/tables manifests/latest runs
PYTHONUNBUFFERED=1 python tools/build_layer_code_alignment_v2.py \
  --pseudocode reports/latest/tables/pseudocode_operation_database.csv \
  --checkpoint "${CHECKPOINT:-local_checkpoints/part/ParticleNet_kinpid.pt}" \
  --data-dir "${JETCLASS_TINY:-$HOME/Рабочий стол/jetclass_tiny_balanced}" \
  --mode "${MODE:-kinpid}" \
  --samples-per-file "${SAMPLES_PER_FILE:-16}" \
  --max-files "${MAX_FILES:-10}" \
  --device "${DEVICE:-cuda}" \
  --out-csv reports/latest/tables/layer_code_alignment_v2.csv \
  --out-json manifests/latest/layer_code_alignment_v2.json \
  --out-md reports/latest/LAYER_CODE_ALIGNMENT_V2.md \
  2>&1 | tee runs/layer_code_alignment_v2.log

git add tools/build_layer_code_alignment_v2.py scripts/RUN_LAYER_CODE_ALIGNMENT_V2.sh \
  reports/latest/LAYER_CODE_ALIGNMENT_V2.md reports/latest/tables/layer_code_alignment_v2.csv manifests/latest/layer_code_alignment_v2.json

git commit -m "Update layer code alignment v2" || true
git push

echo "DONE layer code alignment v2. Main report: reports/latest/LAYER_CODE_ALIGNMENT_V2.md"
