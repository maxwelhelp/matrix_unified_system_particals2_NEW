#!/usr/bin/env bash
set -euo pipefail
cd "$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
mkdir -p reports/latest/tables manifests/latest runs

PYTHONUNBUFFERED=1 python tools/internal_activation_contrast_v1.py \
  --phase1-events reports/latest/tables/hqql_tbl_confusion_physics_events.csv \
  --super-events reports/latest/tables/all_head_supertrace_events.csv \
  --super-particles reports/latest/tables/all_head_supertrace_particles.csv \
  --head-gradients reports/latest/tables/all_head_gate_gradients.csv \
  --class-gradients reports/latest/tables/class_specific_head_gradients.csv \
  --head-trace reports/latest/tables/head_output_trace.csv \
  --isolation-threshold "${ISOLATION_THRESHOLD:-0.30}" \
  --out-md reports/latest/INTERNAL_ACTIVATION_CONTRAST_V1.md \
  --out-groups reports/latest/tables/internal_activation_contrast_v1_group_inventory.csv \
  --out-particles reports/latest/tables/internal_activation_contrast_v1_particle_contrasts.csv \
  --out-heads reports/latest/tables/internal_activation_contrast_v1_head_priorities.csv \
  --out-json manifests/latest/internal_activation_contrast_v1.json \
  2>&1 | tee runs/internal_activation_contrast_v1.log

git add docs/что_считает_нейронка/00_ВАЖНО_МЕТОД_АНАЛИЗА/DIRECT_INTERNAL_ACTIVATION_PROBE_V1.md \
  docs/что_считает_нейронка/02_текущая_задача_particlenet_hqql_tbl/06_next_steps/INTERNAL_ACTIVATION_CONTRAST_V1.md \
  docs/что_считает_нейронка/02_текущая_задача_particlenet_hqql_tbl/06_next_steps/INTERNAL_DATA_INVENTORY_FOR_CONTRAST.md \
  tools/internal_activation_contrast_v1.py scripts/RUN_INTERNAL_ACTIVATION_CONTRAST_V1.sh \
  reports/latest/INTERNAL_ACTIVATION_CONTRAST_V1.md \
  reports/latest/tables/internal_activation_contrast_v1_group_inventory.csv \
  reports/latest/tables/internal_activation_contrast_v1_particle_contrasts.csv \
  reports/latest/tables/internal_activation_contrast_v1_head_priorities.csv \
  manifests/latest/internal_activation_contrast_v1.json

git commit -m "Update internal activation contrast v1" || true
git push

echo "DONE internal activation contrast v1. Main report: reports/latest/INTERNAL_ACTIVATION_CONTRAST_V1.md"
