#!/usr/bin/env bash
set -euo pipefail
cd "$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
mkdir -p reports/latest/tables manifests/latest runs
PYTHONUNBUFFERED=1 python tools/edgeconv_inner_trace_v1.py \
  --rankings reports/latest/tables/question_driven_head_rankings.csv \
  --checkpoint "${CHECKPOINT:-local_checkpoints/part/ParticleNet_kinpid.pt}" \
  --data-dir "${JETCLASS_TINY:-$HOME/Рабочий стол/jetclass_tiny_balanced}" \
  --mode "${MODE:-kinpid}" \
  --questions "${QUESTIONS:-Q1_core_readout,Q3_residual_axis,Q4_trace_priority}" \
  --top-heads "${TOP_HEADS:-10}" \
  --samples-per-file "${SAMPLES_PER_FILE:-64}" \
  --max-files "${MAX_FILES:-20}" \
  --top-events-per-head "${TOP_EVENTS_PER_HEAD:-5}" \
  --device "${DEVICE:-cuda}" \
  --out-heads reports/latest/tables/edgeconv_inner_trace_heads.csv \
  --out-events reports/latest/tables/edgeconv_inner_trace_events.csv \
  --out-json manifests/latest/edgeconv_inner_trace_v1.json \
  --out-md reports/latest/EDGE_CONV_INNER_TRACE_V1.md \
  2>&1 | tee runs/edgeconv_inner_trace_v1.log

git add docs/01_method/EDGE_CONV_INNER_TRACE_v1.md tools/edgeconv_inner_trace_v1.py scripts/RUN_EDGE_CONV_INNER_TRACE_V1.sh \
  reports/latest/EDGE_CONV_INNER_TRACE_V1.md reports/latest/tables/edgeconv_inner_trace_heads.csv reports/latest/tables/edgeconv_inner_trace_events.csv manifests/latest/edgeconv_inner_trace_v1.json

git commit -m "Update EdgeConv inner trace" || true
git push

echo "DONE EdgeConv inner trace. Main report: reports/latest/EDGE_CONV_INNER_TRACE_V1.md"
