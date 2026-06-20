#!/usr/bin/env bash
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"

python tools/part_residual_path_trace_real_contract_v2.py \
  --events-per-group "${RESIDUAL_TRACE_EVENTS_PER_GROUP:-32}" \
  --micro-batch "${RESIDUAL_TRACE_MICRO_BATCH:-8}" \
  --objectives "${RESIDUAL_TRACE_OBJECTIVES:-signed_hqql_tbl,B_tbl_minus_hqql}"

sed -n '1,360p' reports/latest/PART_RESIDUAL_PATH_TRACE_REAL_CONTRACT_V2.md
