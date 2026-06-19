#!/usr/bin/env bash
set -euo pipefail
cd "$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
mkdir -p reports/latest/tables manifests/latest runs

PYTHONUNBUFFERED=1 python tools/matrix_program_full_trace_v1.py \
  --events reports/latest/tables/internal_activation_contrast_v2_events.csv \
  --particles reports/latest/tables/internal_activation_contrast_v2_1_top_particles_annotated.csv \
  --head-summary reports/latest/tables/internal_activation_contrast_v2_head_summary.csv \
  --out-md reports/latest/MATRIX_PROGRAM_FULL_TRACE_V1.md \
  --out-db reports/latest/tables/matrix_program_database_v1.csv \
  --out-flow reports/latest/tables/matrix_program_particle_role_flow_v1.csv \
  --out-paths reports/latest/tables/matrix_program_paths_v1.csv \
  --out-json manifests/latest/matrix_program_full_trace_v1.json \
  2>&1 | tee runs/matrix_program_full_trace_v1.log

git add tools/matrix_program_full_trace_v1.py scripts/RUN_MATRIX_PROGRAM_FULL_TRACE_V1.sh \
  reports/latest/MATRIX_PROGRAM_FULL_TRACE_V1.md \
  reports/latest/tables/matrix_program_database_v1.csv \
  reports/latest/tables/matrix_program_particle_role_flow_v1.csv \
  reports/latest/tables/matrix_program_paths_v1.csv \
  manifests/latest/matrix_program_full_trace_v1.json || true

git commit -m "Update matrix program full trace v1" || true
git push

echo "DONE matrix program full trace v1. Main report: reports/latest/MATRIX_PROGRAM_FULL_TRACE_V1.md"
