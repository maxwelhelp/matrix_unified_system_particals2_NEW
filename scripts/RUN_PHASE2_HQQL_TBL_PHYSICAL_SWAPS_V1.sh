#!/usr/bin/env bash
set -euo pipefail
cd "$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
mkdir -p reports/latest/tables manifests/latest runs

STAGE="${PHASE2_STAGE:-medium}"
case "$STAGE" in
  small)
    SPF="${SAMPLES_PER_FILE:-256}"
    MF="${MAX_FILES:-20}"
    MB="${MICRO_BATCH:-64}"
    MT="${MAX_TARGETS:-30}"
    ;;
  medium)
    SPF="${SAMPLES_PER_FILE:-1024}"
    MF="${MAX_FILES:-100}"
    MB="${MICRO_BATCH:-64}"
    MT="${MAX_TARGETS:-80}"
    ;;
  large)
    SPF="${SAMPLES_PER_FILE:-4096}"
    MF="${MAX_FILES:-1000}"
    MB="${MICRO_BATCH:-32}"
    MT="${MAX_TARGETS:-150}"
    ;;
  *)
    echo "Unknown PHASE2_STAGE=$STAGE. Use small|medium|large" >&2
    exit 2
    ;;
esac

export PYTORCH_CUDA_ALLOC_CONF="${PYTORCH_CUDA_ALLOC_CONF:-expandable_segments:True}"
echo "PHASE2 stage=$STAGE samples_per_file=$SPF max_files=$MF micro_batch=$MB max_targets=$MT patch_k=${PATCH_K:-8}"

PYTHONUNBUFFERED=1 python tools/phase2_hqql_tbl_physical_swaps_v1.py \
  --checkpoint "${CHECKPOINT:-local_checkpoints/part/ParticleNet_kinpid.pt}" \
  --data-dir "${JETCLASS_TINY:-$HOME/Рабочий стол/jetclass_tiny_balanced}" \
  --mode "${MODE:-kinpid}" \
  --samples-per-file "$SPF" \
  --max-files "$MF" \
  --micro-batch "$MB" \
  --max-targets "$MT" \
  --patch-k "${PATCH_K:-8}" \
  --seed "${SEED:-123}" \
  --device "${DEVICE:-cuda}" \
  --out-csv reports/latest/tables/phase2_hqql_tbl_physical_swaps.csv \
  --out-summary reports/latest/tables/phase2_hqql_tbl_physical_swaps_summary.csv \
  --out-json manifests/latest/phase2_hqql_tbl_physical_swaps_v1.json \
  --out-md reports/latest/PHASE2_HQQL_TBL_PHYSICAL_SWAPS_V1.md \
  2>&1 | tee "runs/phase2_hqql_tbl_physical_swaps_${STAGE}.log"

git add docs/02_physics/PHASE2_HQQL_TBL_PHYSICAL_SWAPS_v1.md \
  tools/phase2_hqql_tbl_physical_swaps_v1.py scripts/RUN_PHASE2_HQQL_TBL_PHYSICAL_SWAPS_V1.sh \
  reports/latest/PHASE2_HQQL_TBL_PHYSICAL_SWAPS_V1.md reports/latest/tables/phase2_hqql_tbl_physical_swaps.csv reports/latest/tables/phase2_hqql_tbl_physical_swaps_summary.csv manifests/latest/phase2_hqql_tbl_physical_swaps_v1.json

git commit -m "Update Phase 2 Hqql Tbl physical swaps" || true
git push

echo "DONE Phase 2 Hqql/Tbl physical swaps. Main report: reports/latest/PHASE2_HQQL_TBL_PHYSICAL_SWAPS_V1.md"
