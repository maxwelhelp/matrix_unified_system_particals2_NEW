#!/usr/bin/env bash
set -euo pipefail
cd "$(git rev-parse --show-toplevel 2>/dev/null || pwd)"

echo "[cycle] repo=$(pwd)"
echo "[cycle] RUN_MODEL=${RUN_MODEL:-1} SAMPLES_PER_FILE=${SAMPLES_PER_FILE:-64} MICRO_BATCH=${MICRO_BATCH:-32}"

if [[ "${RUN_MODEL:-1}" != "0" ]]; then
  echo "[cycle] step 1/4: all-head supertrace"
  PYTORCH_CUDA_ALLOC_CONF="${PYTORCH_CUDA_ALLOC_CONF:-expandable_segments:True}" \
  MICRO_BATCH="${MICRO_BATCH:-32}" \
  SAMPLES_PER_FILE="${SAMPLES_PER_FILE:-64}" \
  TOP_EVENTS="${TOP_EVENTS:-80}" \
  TOP_PARTICLES="${TOP_PARTICLES:-12}" \
  CHECKPOINT="${CHECKPOINT:-local_checkpoints/part/ParticleNet_kinpid.pt}" \
  MODE="${MODE:-kinpid}" \
  JETCLASS_TINY="${JETCLASS_TINY:-$HOME/Рабочий стол/jetclass_tiny_balanced}" \
  bash scripts/RUN_PARTICLENET_ALL_HEAD_SUPERTRACE_V1.sh
else
  echo "[cycle] step 1/4: skipped model run (RUN_MODEL=0)"
fi

echo "[cycle] step 2/4: evidence graph history"
HISTORY_COPY=1 bash scripts/RUN_RESEARCH_EVIDENCE_GRAPH_V1.sh

echo "[cycle] step 3/4: dynamics"
bash scripts/RUN_RESEARCH_DYNAMICS_V1.sh

echo "[cycle] step 4/4: stream index"
bash scripts/RUN_RESEARCH_STREAM_INDEX_V1.sh

echo "[cycle] DONE"
echo "[cycle] Read: reports/latest/RESEARCH_STREAM_INDEX_V1.md"
echo "[cycle] Query examples:"
echo "  python tools/query_research_stream_v1.py --event-type HEAD_GATE --top 20"
echo "  python tools/query_research_stream_v1.py --query particle0 --top 30"
echo "  python tools/query_research_stream_v1.py --class-label label_Hqql --top 30"
