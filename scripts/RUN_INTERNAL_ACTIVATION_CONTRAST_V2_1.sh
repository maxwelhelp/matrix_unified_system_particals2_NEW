#!/usr/bin/env bash
set -euo pipefail
cd "$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
mkdir -p reports/latest/tables manifests/latest runs

PYTHONUNBUFFERED=1 python tools/internal_activation_contrast_v2_1_roles.py \
  --top-particles reports/latest/tables/internal_activation_contrast_v2_top_particles.csv \
  --data-dir "${JETCLASS_TINY:-$HOME/Рабочий стол/jetclass_tiny_balanced}" \
  --mode "${MODE:-kinpid}" \
  --samples-per-file "${SAMPLES_PER_FILE:-4096}" \
  --max-files "${MAX_FILES:-1000}" \
  --focus-heads "${FOCUS_HEADS:-L1_ch80:96,L1_ch32:48,L2_ch128:160}" \
  --device "${DEVICE:-cpu}" \
  --out-md reports/latest/INTERNAL_ACTIVATION_CONTRAST_V2_1.md \
  --out-annotated reports/latest/tables/internal_activation_contrast_v2_1_top_particles_annotated.csv \
  --out-summary reports/latest/tables/internal_activation_contrast_v2_1_role_summary.csv \
  --out-contrast reports/latest/tables/internal_activation_contrast_v2_1_role_contrast.csv \
  --out-json manifests/latest/internal_activation_contrast_v2_1.json \
  2>&1 | tee runs/internal_activation_contrast_v2_1.log

git add docs/что_считает_нейронка/02_текущая_задача_particlenet_hqql_tbl/06_next_steps/INTERNAL_ACTIVATION_CONTRAST_V2_1.md \
  tools/internal_activation_contrast_v2_1_roles.py scripts/RUN_INTERNAL_ACTIVATION_CONTRAST_V2_1.sh \
  reports/latest/INTERNAL_ACTIVATION_CONTRAST_V2_1.md \
  reports/latest/tables/internal_activation_contrast_v2_1_top_particles_annotated.csv \
  reports/latest/tables/internal_activation_contrast_v2_1_role_summary.csv \
  reports/latest/tables/internal_activation_contrast_v2_1_role_contrast.csv \
  manifests/latest/internal_activation_contrast_v2_1.json

git commit -m "Update internal activation contrast v2.1 roles" || true
git push

echo "DONE internal activation contrast v2.1. Main report: reports/latest/INTERNAL_ACTIVATION_CONTRAST_V2_1.md"
