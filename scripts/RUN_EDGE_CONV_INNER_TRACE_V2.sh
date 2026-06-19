#!/usr/bin/env bash
set -euo pipefail
cd "$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
mkdir -p reports/latest/tables manifests/latest runs
PYTHONUNBUFFERED=1 python tools/edgeconv_inner_trace_v2.py \
  --rankings reports/latest/tables/question_driven_head_rankings.csv \
  --checkpoint "${CHECKPOINT:-local_checkpoints/part/ParticleNet_kinpid.pt}" \
  --data-dir "${JETCLASS_TINY:-$HOME/Рабочий стол/jetclass_tiny_balanced}" \
  --mode "${MODE:-kinpid}" \
  --questions "${QUESTIONS:-Q1_core_readout,Q3_residual_axis,Q4_trace_priority}" \
  --top-heads "${TOP_HEADS:-10}" \
  --samples-per-file "${SAMPLES_PER_FILE:-64}" \
  --max-files "${MAX_FILES:-20}" \
  --top-events-per-head "${TOP_EVENTS_PER_HEAD:-8}" \
  --device "${DEVICE:-cuda}" \
  --out-heads reports/latest/tables/edgeconv_inner_trace_v2_heads.csv \
  --out-events reports/latest/tables/edgeconv_inner_trace_v2_events.csv \
  --out-json manifests/latest/edgeconv_inner_trace_v2.json \
  --out-md reports/latest/EDGE_CONV_INNER_TRACE_V2.md \
  2>&1 | tee runs/edgeconv_inner_trace_v2.log

git add tools/edgeconv_inner_trace_v2.py scripts/RUN_EDGE_CONV_INNER_TRACE_V2.sh \
  reports/latest/EDGE_CONV_INNER_TRACE_V2.md reports/latest/tables/edgeconv_inner_trace_v2_heads.csv reports/latest/tables/edgeconv_inner_trace_v2_events.csv manifests/latest/edgeconv_inner_trace_v2.json

git commit -m "Update EdgeConv inner trace v2" || true
git push

echo "DONE EdgeConv inner trace v2. Main report: reports/latest/EDGE_CONV_INNER_TRACE_V2.md"
