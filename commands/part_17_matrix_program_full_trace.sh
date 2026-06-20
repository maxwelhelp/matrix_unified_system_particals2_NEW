#!/usr/bin/env bash
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"

python tools/part_matrix_program_full_trace_real_contract_v1.py \
  --events-per-group "${MATRIX_TRACE_EVENTS_PER_GROUP:-64}" \
  --micro-batch "${MATRIX_TRACE_MICRO_BATCH:-8}" \
  --role-topk "${MATRIX_TRACE_ROLE_TOPK:-3}"

sed -n '1,260p' reports/latest/PART_MATRIX_PROGRAM_FULL_TRACE_REAL_CONTRACT_V1.md
