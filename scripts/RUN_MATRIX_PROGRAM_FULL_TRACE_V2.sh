#!/usr/bin/env bash
set -euo pipefail
cd "$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
mkdir -p reports/latest/tables reports/latest/particle_flow_graphs_v2 manifests/latest runs
export PYTORCH_CUDA_ALLOC_CONF="${PYTORCH_CUDA_ALLOC_CONF:-expandable_segments:True}"

PYTHONUNBUFFERED=1 python tools/matrix_program_full_trace_v2.py \
  --phase1-events reports/latest/tables/hqql_tbl_confusion_physics_events.csv \
  --checkpoint "${CHECKPOINT:-local_checkpoints/part/ParticleNet_kinpid.pt}" \
  --data-dir "${JETCLASS_TINY:-$HOME/Рабочий стол/jetclass_tiny_balanced}" \
  --mode "${MODE:-kinpid}" \
  --samples-per-file "${SAMPLES_PER_FILE:-4096}" \
  --max-files "${MAX_FILES:-1000}" \
  --max-tbl-correct "${MAX_TBL_CORRECT:-128}" \
  --isolation-threshold "${ISOLATION_THRESHOLD:-0.30}" \
  --head-step "${HEAD_STEP:-32}" \
  --top-particles "${TOP_PARTICLES:-3}" \
  --max-graphs "${MAX_GRAPHS:-200}" \
  --device "${DEVICE:-cuda}" \
  --out-dir reports/latest/particle_flow_graphs_v2 \
  --out-md reports/latest/MATRIX_PROGRAM_FULL_TRACE_V2.md \
  --out-db reports/latest/tables/matrix_program_database_v2.csv \
  --out-flow reports/latest/tables/matrix_program_particle_role_flow_v2.csv \
  --out-trig reports/latest/tables/top_confusion_triggers_v2.csv \
  --out-loss reports/latest/tables/top_hqql_loss_paths_v2.csv \
  --out-anom reports/latest/tables/top_anomalous_paths_v2.csv \
  --out-json manifests/latest/matrix_program_full_trace_v2.json \
  2>&1 | tee runs/matrix_program_full_trace_v2.log

git add docs/что_считает_нейронка/00_ВАЖНО_МЕТОД_АНАЛИЗА/MATRIX_PROGRAM_FULL_TRACE_V2.md \
  tools/matrix_program_full_trace_v2.py scripts/RUN_MATRIX_PROGRAM_FULL_TRACE_V2.sh \
  reports/latest/MATRIX_PROGRAM_FULL_TRACE_V2.md \
  reports/latest/tables/matrix_program_database_v2.csv \
  reports/latest/tables/matrix_program_particle_role_flow_v2.csv \
  reports/latest/tables/top_confusion_triggers_v2.csv \
  reports/latest/tables/top_hqql_loss_paths_v2.csv \
  reports/latest/tables/top_anomalous_paths_v2.csv \
  reports/latest/particle_flow_graphs_v2 manifests/latest/matrix_program_full_trace_v2.json

git commit -m "Update matrix program full trace v2" || true
git push

echo "DONE matrix program full trace v2. Main report: reports/latest/MATRIX_PROGRAM_FULL_TRACE_V2.md"
