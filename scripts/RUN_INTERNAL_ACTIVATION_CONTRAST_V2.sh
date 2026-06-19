#!/usr/bin/env bash
set -euo pipefail
cd "$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
mkdir -p reports/latest/tables manifests/latest runs

export PYTORCH_CUDA_ALLOC_CONF="${PYTORCH_CUDA_ALLOC_CONF:-expandable_segments:True}"

PYTHONUNBUFFERED=1 python tools/internal_activation_contrast_v2.py \
  --phase1-events reports/latest/tables/hqql_tbl_confusion_physics_events.csv \
  --checkpoint "${CHECKPOINT:-local_checkpoints/part/ParticleNet_kinpid.pt}" \
  --data-dir "${JETCLASS_TINY:-$HOME/Рабочий стол/jetclass_tiny_balanced}" \
  --mode "${MODE:-kinpid}" \
  --samples-per-file "${SAMPLES_PER_FILE:-4096}" \
  --max-files "${MAX_FILES:-1000}" \
  --heads "${HEADS:-L2:128:160,L2:160:192,L2:224:256,L1:32:48,L1:80:96,L2:0:32,L2:32:64}" \
  --isolation-threshold "${ISOLATION_THRESHOLD:-0.30}" \
  --max-tbl-correct "${MAX_TBL_CORRECT:-128}" \
  --device "${DEVICE:-cuda}" \
  --out-md reports/latest/INTERNAL_ACTIVATION_CONTRAST_V2.md \
  --out-events reports/latest/tables/internal_activation_contrast_v2_events.csv \
  --out-particles reports/latest/tables/internal_activation_contrast_v2_top_particles.csv \
  --out-heads reports/latest/tables/internal_activation_contrast_v2_head_summary.csv \
  --out-json manifests/latest/internal_activation_contrast_v2.json \
  2>&1 | tee runs/internal_activation_contrast_v2.log

git add docs/что_считает_нейронка/02_текущая_задача_particlenet_hqql_tbl/06_next_steps/INTERNAL_ACTIVATION_CONTRAST_V2.md \
  tools/internal_activation_contrast_v2.py scripts/RUN_INTERNAL_ACTIVATION_CONTRAST_V2.sh \
  reports/latest/INTERNAL_ACTIVATION_CONTRAST_V2.md \
  reports/latest/tables/internal_activation_contrast_v2_events.csv \
  reports/latest/tables/internal_activation_contrast_v2_top_particles.csv \
  reports/latest/tables/internal_activation_contrast_v2_head_summary.csv \
  manifests/latest/internal_activation_contrast_v2.json

git commit -m "Update internal activation contrast v2" || true
git push

echo "DONE internal activation contrast v2. Main report: reports/latest/INTERNAL_ACTIVATION_CONTRAST_V2.md"
