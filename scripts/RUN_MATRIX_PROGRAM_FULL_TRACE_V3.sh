#!/usr/bin/env bash
set -euo pipefail
cd "$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
mkdir -p reports/latest/tables manifests/latest runs

export PYTORCH_CUDA_ALLOC_CONF="${PYTORCH_CUDA_ALLOC_CONF:-expandable_segments:True}"

echo "MATRIX_PROGRAM_FULL_TRACE_V3 slice_size=${SLICE_SIZE:-32} max_tbl_correct=${MAX_TBL_CORRECT:-64} device=${DEVICE:-cuda}"

PYTHONUNBUFFERED=1 python tools/matrix_program_full_trace_v3.py \
  --phase1-events reports/latest/tables/hqql_tbl_confusion_physics_events.csv \
  --checkpoint "${CHECKPOINT:-local_checkpoints/part/ParticleNet_kinpid.pt}" \
  --data-dir "${JETCLASS_TINY:-$HOME/Рабочий стол/jetclass_tiny_balanced}" \
  --mode "${MODE:-kinpid}" \
  --samples-per-file "${SAMPLES_PER_FILE:-4096}" \
  --max-files "${MAX_FILES:-1000}" \
  --layers "${LAYERS:-0,1,2}" \
  --slice-size "${SLICE_SIZE:-32}" \
  --max-channels "${MAX_CHANNELS:-256}" \
  --isolation-threshold "${ISOLATION_THRESHOLD:-0.30}" \
  --max-tbl-correct "${MAX_TBL_CORRECT:-64}" \
  --forward-step "${FORWARD_STEP:-128}" \
  --device "${DEVICE:-cuda}" \
  --out-md reports/latest/MATRIX_PROGRAM_FULL_TRACE_V3_SUMMARY.md \
  --out-db reports/latest/tables/matrix_program_full_trace_v3_all_heads_database.csv \
  --out-ranked reports/latest/tables/matrix_program_full_trace_v3_all_heads_ranked.csv \
  --out-roles reports/latest/tables/matrix_program_full_trace_v3_top_particle_roles.csv \
  --out-event-rows reports/latest/tables/matrix_program_full_trace_v3_event_head_rows.csv \
  --out-json manifests/latest/matrix_program_full_trace_v3.json \
  2>&1 | tee runs/matrix_program_full_trace_v3.log

git add docs/что_считает_нейронка/02_текущая_задача_particlenet_hqql_tbl/06_next_steps/MATRIX_PROGRAM_FULL_TRACE_V3.md \
  tools/matrix_program_full_trace_v3.py scripts/RUN_MATRIX_PROGRAM_FULL_TRACE_V3.sh \
  reports/latest/MATRIX_PROGRAM_FULL_TRACE_V3_SUMMARY.md \
  reports/latest/tables/matrix_program_full_trace_v3_all_heads_database.csv \
  reports/latest/tables/matrix_program_full_trace_v3_all_heads_ranked.csv \
  reports/latest/tables/matrix_program_full_trace_v3_top_particle_roles.csv \
  reports/latest/tables/matrix_program_full_trace_v3_event_head_rows.csv \
  manifests/latest/matrix_program_full_trace_v3.json

git commit -m "Update matrix program full trace v3" || true
git push

echo "DONE matrix program full trace v3. Main report: reports/latest/MATRIX_PROGRAM_FULL_TRACE_V3_SUMMARY.md"
