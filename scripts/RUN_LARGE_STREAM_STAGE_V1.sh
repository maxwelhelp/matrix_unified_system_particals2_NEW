#!/usr/bin/env bash
set -euo pipefail
cd "$(git rev-parse --show-toplevel 2>/dev/null || pwd)"

STAGE="${STAGE:-medium}"
case "$STAGE" in
  smoke)
    export SAMPLES_PER_FILE="${SAMPLES_PER_FILE:-64}"
    export MICRO_BATCH="${MICRO_BATCH:-32}"
    ;;
  medium)
    export SAMPLES_PER_FILE="${SAMPLES_PER_FILE:-256}"
    export MICRO_BATCH="${MICRO_BATCH:-32}"
    ;;
  large)
    export SAMPLES_PER_FILE="${SAMPLES_PER_FILE:-512}"
    export MICRO_BATCH="${MICRO_BATCH:-16}"
    ;;
  xlarge)
    export SAMPLES_PER_FILE="${SAMPLES_PER_FILE:-1024}"
    export MICRO_BATCH="${MICRO_BATCH:-8}"
    ;;
  *)
    echo "Unknown STAGE=$STAGE. Use smoke|medium|large|xlarge" >&2
    exit 2
    ;;
esac

export RUN_MODEL=1
export TOP_EVENTS="${TOP_EVENTS:-120}"
export TOP_PARTICLES="${TOP_PARTICLES:-16}"
export CHECKPOINT="${CHECKPOINT:-local_checkpoints/part/ParticleNet_kinpid.pt}"
export MODE="${MODE:-kinpid}"
export JETCLASS_TINY="${JETCLASS_TINY:-$HOME/Рабочий стол/jetclass_tiny_balanced}"
export PYTORCH_CUDA_ALLOC_CONF="${PYTORCH_CUDA_ALLOC_CONF:-expandable_segments:True}"

echo "[large-stage] STAGE=$STAGE SAMPLES_PER_FILE=$SAMPLES_PER_FILE MICRO_BATCH=$MICRO_BATCH TOP_EVENTS=$TOP_EVENTS TOP_PARTICLES=$TOP_PARTICLES"
echo "[large-stage] data=$JETCLASS_TINY checkpoint=$CHECKPOINT mode=$MODE"

bash scripts/RUN_STREAM_CYCLE_V1.sh
bash scripts/RUN_STREAM_TASK_WATCHER_V1.sh
bash scripts/RUN_RELATION_SIGNAL_GRAPH_V1.sh
bash scripts/RUN_AUTOMATIC_COMPARISON_ENGINE_V1.sh
bash scripts/RUN_AUTOMATIC_COMPARISON_ENGINE_V2.sh

echo "[large-stage] DONE stage=$STAGE"
echo "[large-stage] Read: reports/latest/AUTOMATIC_COMPARISON_ENGINE_V2.md"
echo "[large-stage] Read: reports/latest/RESEARCH_STREAM_INDEX_V1.md"
