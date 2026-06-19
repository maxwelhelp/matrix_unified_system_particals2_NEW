#!/usr/bin/env bash
set -euo pipefail
cd "$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
mkdir -p reports/latest/tables manifests/latest runs

# Modes:
#   PHASE3_MODE=only-3c  -> uses Phase 1 CSV only, fastest and cleanest observable test
#   PHASE3_MODE=all      -> runs 3C + 3A matched controls + 3B sweep
MODE3="${PHASE3_MODE:-only-3c}"
RUN_PATCHES=""
if [[ "$MODE3" == "all" ]]; then
  RUN_PATCHES="--run-patches"
elif [[ "$MODE3" != "only-3c" ]]; then
  echo "Unknown PHASE3_MODE=$MODE3. Use only-3c|all" >&2
  exit 2
fi

STAGE="${PHASE3_STAGE:-medium}"
case "$STAGE" in
  small)
    SPF="${SAMPLES_PER_FILE:-256}"
    MF="${MAX_FILES:-20}"
    MB="${MICRO_BATCH:-64}"
    KMB="${KNN_MICRO_BATCH:-128}"
    MT="${MAX_TARGETS:-40}"
    ;;
  medium)
    SPF="${SAMPLES_PER_FILE:-1024}"
    MF="${MAX_FILES:-100}"
    MB="${MICRO_BATCH:-64}"
    KMB="${KNN_MICRO_BATCH:-128}"
    MT="${MAX_TARGETS:-100}"
    ;;
  large)
    SPF="${SAMPLES_PER_FILE:-4096}"
    MF="${MAX_FILES:-1000}"
    MB="${MICRO_BATCH:-32}"
    KMB="${KNN_MICRO_BATCH:-64}"
    MT="${MAX_TARGETS:-150}"
    ;;
  *)
    echo "Unknown PHASE3_STAGE=$STAGE. Use small|medium|large" >&2
    exit 2
    ;;
esac

export PYTORCH_CUDA_ALLOC_CONF="${PYTORCH_CUDA_ALLOC_CONF:-expandable_segments:True}"
echo "PHASE3 mode=$MODE3 stage=$STAGE samples_per_file=$SPF max_files=$MF micro_batch=$MB targets=$MT patch_k=${PATCH_K:-8}"

PYTHONUNBUFFERED=1 python tools/phase3_hqql_tbl_isolation_controls_v1.py \
  --phase1-events reports/latest/tables/hqql_tbl_confusion_physics_events.csv \
  $RUN_PATCHES \
  --checkpoint "${CHECKPOINT:-local_checkpoints/part/ParticleNet_kinpid.pt}" \
  --data-dir "${JETCLASS_TINY:-$HOME/Рабочий стол/jetclass_tiny_balanced}" \
  --mode "${MODEL_MODE:-kinpid}" \
  --samples-per-file "$SPF" \
  --max-files "$MF" \
  --micro-batch "$MB" \
  --knn-micro-batch "$KMB" \
  --max-targets "$MT" \
  --patch-k "${PATCH_K:-8}" \
  --seed "${SEED:-123}" \
  --device "${DEVICE:-cuda}" \
  --out-bins reports/latest/tables/phase3_hqql_tbl_isolation_bins.csv \
  --out-controls reports/latest/tables/phase3_hqql_tbl_matched_controls.csv \
  --out-control-summary reports/latest/tables/phase3_hqql_tbl_matched_controls_summary.csv \
  --out-sweep reports/latest/tables/phase3_hqql_tbl_sweep.csv \
  --out-sweep-summary reports/latest/tables/phase3_hqql_tbl_sweep_summary.csv \
  --out-json manifests/latest/phase3_hqql_tbl_isolation_controls_v1.json \
  --out-md reports/latest/PHASE3_HQQL_TBL_ISOLATION_CONTROLS_V1.md \
  2>&1 | tee "runs/phase3_hqql_tbl_isolation_controls_${MODE3}_${STAGE}.log"

git add docs/02_physics/PHASE3_HQQL_TBL_ISOLATION_CONTROLS_v1.md \
  tools/phase3_hqql_tbl_isolation_controls_v1.py scripts/RUN_PHASE3_HQQL_TBL_ISOLATION_CONTROLS_V1.sh \
  reports/latest/PHASE3_HQQL_TBL_ISOLATION_CONTROLS_V1.md \
  reports/latest/tables/phase3_hqql_tbl_isolation_bins.csv \
  reports/latest/tables/phase3_hqql_tbl_matched_controls.csv reports/latest/tables/phase3_hqql_tbl_matched_controls_summary.csv \
  reports/latest/tables/phase3_hqql_tbl_sweep.csv reports/latest/tables/phase3_hqql_tbl_sweep_summary.csv \
  manifests/latest/phase3_hqql_tbl_isolation_controls_v1.json

git commit -m "Update Phase 3 Hqql Tbl isolation controls" || true
git push

echo "DONE Phase 3 Hqql/Tbl isolation controls. Main report: reports/latest/PHASE3_HQQL_TBL_ISOLATION_CONTROLS_V1.md"
