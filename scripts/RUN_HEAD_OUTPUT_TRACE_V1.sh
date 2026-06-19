#!/usr/bin/env bash
set -euo pipefail
cd "$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
mkdir -p reports/latest/tables manifests/latest runs
PYTHONUNBUFFERED=1 python tools/head_output_trace_v1.py \
  --pseudocode reports/latest/tables/pseudocode_operation_database.csv \
  --checkpoint "${CHECKPOINT:-local_checkpoints/part/ParticleNet_kinpid.pt}" \
  --data-dir "${JETCLASS_TINY:-$HOME/Рабочий стол/jetclass_tiny_balanced}" \
  --mode "${MODE:-kinpid}" \
  --samples-per-file "${SAMPLES_PER_FILE:-128}" \
  --max-files "${MAX_FILES:-20}" \
  --device "${DEVICE:-cuda}" \
  --out-csv reports/latest/tables/head_output_trace.csv \
  --out-events reports/latest/tables/head_output_top_events.csv \
  --out-json manifests/latest/head_output_trace_v1.json \
  --out-md reports/latest/HEAD_OUTPUT_TRACE_V1.md \
  2>&1 | tee runs/head_output_trace_v1.log

git add docs/01_method/HEAD_OUTPUT_INTERPRETATION_v1.md \
  tools/head_output_trace_v1.py scripts/RUN_HEAD_OUTPUT_TRACE_V1.sh \
  reports/latest/HEAD_OUTPUT_TRACE_V1.md reports/latest/tables/head_output_trace.csv reports/latest/tables/head_output_top_events.csv manifests/latest/head_output_trace_v1.json

git commit -m "Update head output trace" || true
git push

echo "DONE head output trace. Main report: reports/latest/HEAD_OUTPUT_TRACE_V1.md"
