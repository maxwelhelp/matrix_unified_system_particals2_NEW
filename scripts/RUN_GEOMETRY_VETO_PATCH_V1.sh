#!/usr/bin/env bash
set -euo pipefail
cd "$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
mkdir -p reports/latest/tables manifests/latest runs

export PYTORCH_CUDA_ALLOC_CONF="${PYTORCH_CUDA_ALLOC_CONF:-expandable_segments:True}"

PYTHONUNBUFFERED=1 python tools/geometry_veto_patch_v1.py \
  --phase1-events reports/latest/tables/hqql_tbl_confusion_physics_events.csv \
  --checkpoint "${CHECKPOINT:-local_checkpoints/part/ParticleNet_kinpid.pt}" \
  --data-dir "${JETCLASS_TINY:-$HOME/Рабочий стол/jetclass_tiny_balanced}" \
  --mode "${MODE:-kinpid}" \
  --samples-per-file "${SAMPLES_PER_FILE:-4096}" \
  --max-files "${MAX_FILES:-1000}" \
  --max-targets "${MAX_TARGETS:-80}" \
  --patch-k "${PATCH_K:-16}" \
  --isolation-threshold "${ISOLATION_THRESHOLD:-0.30}" \
  --seed "${SEED:-123}" \
  --device "${DEVICE:-cuda}" \
  --out-md reports/latest/GEOMETRY_VETO_PATCH_V1.md \
  --out-csv reports/latest/tables/geometry_veto_patch_v1.csv \
  --out-summary reports/latest/tables/geometry_veto_patch_v1_summary.csv \
  --out-json manifests/latest/geometry_veto_patch_v1.json \
  2>&1 | tee runs/geometry_veto_patch_v1.log

git add docs/что_считает_нейронка/02_текущая_задача_particlenet_hqql_tbl/06_next_steps/GEOMETRY_VETO_PATCH_V1.md \
  tools/geometry_veto_patch_v1.py scripts/RUN_GEOMETRY_VETO_PATCH_V1.sh \
  reports/latest/GEOMETRY_VETO_PATCH_V1.md reports/latest/tables/geometry_veto_patch_v1.csv \
  reports/latest/tables/geometry_veto_patch_v1_summary.csv manifests/latest/geometry_veto_patch_v1.json

git commit -m "Update geometry veto patch v1" || true
git push

echo "DONE geometry veto patch v1. Main report: reports/latest/GEOMETRY_VETO_PATCH_V1.md"
