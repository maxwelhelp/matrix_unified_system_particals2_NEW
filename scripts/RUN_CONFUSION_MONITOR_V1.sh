#!/usr/bin/env bash
set -euo pipefail
cd "$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
mkdir -p reports/latest/tables manifests/latest runs

STAGE="${STREAM_STAGE:-medium}"
case "$STAGE" in
  small)
    SPF="${SAMPLES_PER_FILE:-256}"
    MF="${MAX_FILES:-20}"
    MB="${MICRO_BATCH:-64}"
    ;;
  medium)
    SPF="${SAMPLES_PER_FILE:-1024}"
    MF="${MAX_FILES:-100}"
    MB="${MICRO_BATCH:-64}"
    ;;
  large)
    SPF="${SAMPLES_PER_FILE:-4096}"
    MF="${MAX_FILES:-1000}"
    MB="${MICRO_BATCH:-32}"
    ;;
  full)
    SPF="${SAMPLES_PER_FILE:-999999}"
    MF="${MAX_FILES:-999999}"
    MB="${MICRO_BATCH:-16}"
    ;;
  *)
    echo "Unknown STREAM_STAGE=$STAGE. Use small|medium|large|full" >&2
    exit 2
    ;;
esac

UPDATE_FLAG=""
if [[ "${UPDATE_BASELINE:-0}" == "1" ]]; then
  UPDATE_FLAG="--update-baseline"
fi

export PYTORCH_CUDA_ALLOC_CONF="${PYTORCH_CUDA_ALLOC_CONF:-expandable_segments:True}"
echo "CONFUSION_MONITOR stage=$STAGE samples_per_file=$SPF max_files=$MF micro_batch=$MB update_baseline=${UPDATE_BASELINE:-0}"

PYTHONUNBUFFERED=1 python tools/confusion_monitor_v1.py \
  --checkpoint "${CHECKPOINT:-local_checkpoints/part/ParticleNet_kinpid.pt}" \
  --data-dir "${JETCLASS_TINY:-$HOME/Рабочий стол/jetclass_tiny_balanced}" \
  --mode "${MODE:-kinpid}" \
  --samples-per-file "$SPF" \
  --max-files "$MF" \
  --micro-batch "$MB" \
  --device "${DEVICE:-cuda}" \
  --baseline-json manifests/latest/confusion_monitor_v1_baseline.json \
  $UPDATE_FLAG \
  --watch-rate "${WATCH_RATE:-0.02}" \
  --alert-rate "${ALERT_RATE:-0.05}" \
  --watch-delta "${WATCH_DELTA:-0.01}" \
  --alert-delta "${ALERT_DELTA:-0.03}" \
  --min-pair-count "${MIN_PAIR_COUNT:-10}" \
  --out-md reports/latest/CONFUSION_MONITOR_V1.md \
  --out-json manifests/latest/confusion_monitor_v1.json \
  --out-pairs reports/latest/tables/confusion_monitor_v1_pairs.csv \
  --out-matrix reports/latest/tables/confusion_monitor_v1_matrix.csv \
  --out-signal-board reports/latest/tables/signal_board_v1.csv \
  2>&1 | tee runs/confusion_monitor_v1_${STAGE}.log

git add docs/что_считает_нейронка/00_ВАЖНО_МЕТОД_АНАЛИЗА/STREAM_ARCHITECTURE_V1.md \
  docs/что_считает_нейронка/00_ВАЖНО_МЕТОД_АНАЛИЗА/AUTOMATIC_REASONING_PIPELINE_V1.md \
  tools/confusion_monitor_v1.py scripts/RUN_CONFUSION_MONITOR_V1.sh \
  reports/latest/CONFUSION_MONITOR_V1.md reports/latest/tables/confusion_monitor_v1_pairs.csv \
  reports/latest/tables/confusion_monitor_v1_matrix.csv reports/latest/tables/signal_board_v1.csv \
  manifests/latest/confusion_monitor_v1.json manifests/latest/confusion_monitor_v1_baseline.json || true

git commit -m "Update confusion monitor v1" || true
git push

echo "DONE confusion monitor. Main report: reports/latest/CONFUSION_MONITOR_V1.md"
