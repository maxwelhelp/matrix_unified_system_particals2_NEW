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
    KMB="${KNN_MICRO_BATCH:-128}"
    ;;
  medium)
    SPF="${SAMPLES_PER_FILE:-1024}"
    MF="${MAX_FILES:-100}"
    MB="${MICRO_BATCH:-64}"
    KMB="${KNN_MICRO_BATCH:-128}"
    ;;
  large)
    SPF="${SAMPLES_PER_FILE:-4096}"
    MF="${MAX_FILES:-1000}"
    MB="${MICRO_BATCH:-32}"
    KMB="${KNN_MICRO_BATCH:-64}"
    ;;
  *)
    echo "Unknown STREAM_STAGE=$STAGE. Use small|medium|large" >&2
    exit 2
    ;;
esac

export PYTORCH_CUDA_ALLOC_CONF="${PYTORCH_CUDA_ALLOC_CONF:-expandable_segments:True}"
echo "FEATURE_RANKER stage=$STAGE samples_per_file=$SPF max_files=$MF micro_batch=$MB knn_micro_batch=$KMB"

PYTHONUNBUFFERED=1 python tools/feature_ranker_v1.py \
  --signals reports/latest/tables/signal_board_v1.csv \
  --checkpoint "${CHECKPOINT:-local_checkpoints/part/ParticleNet_kinpid.pt}" \
  --data-dir "${JETCLASS_TINY:-$HOME/Рабочий стол/jetclass_tiny_balanced}" \
  --mode "${MODE:-kinpid}" \
  --samples-per-file "$SPF" \
  --max-files "$MF" \
  --micro-batch "$MB" \
  --knn-micro-batch "$KMB" \
  --max-pairs "${MAX_PAIRS:-12}" \
  --top-features-per-pair "${TOP_FEATURES_PER_PAIR:-8}" \
  --device "${DEVICE:-cuda}" \
  --out-md reports/latest/FEATURE_RANKER_V1.md \
  --out-candidates reports/latest/tables/feature_ranker_v1_candidates.csv \
  --out-bins reports/latest/tables/feature_ranker_v1_bins.csv \
  --out-signal-board reports/latest/tables/signal_board_v1_feature_candidates.csv \
  --out-json manifests/latest/feature_ranker_v1.json \
  2>&1 | tee runs/feature_ranker_v1_${STAGE}.log

git add docs/что_считает_нейронка/00_ВАЖНО_МЕТОД_АНАЛИЗА/FEATURE_RANKER_V1.md \
  tools/feature_ranker_v1.py scripts/RUN_FEATURE_RANKER_V1.sh \
  reports/latest/FEATURE_RANKER_V1.md reports/latest/tables/feature_ranker_v1_candidates.csv \
  reports/latest/tables/feature_ranker_v1_bins.csv reports/latest/tables/signal_board_v1_feature_candidates.csv \
  manifests/latest/feature_ranker_v1.json

git commit -m "Update feature ranker v1" || true
git push

echo "DONE feature ranker. Main report: reports/latest/FEATURE_RANKER_V1.md"
