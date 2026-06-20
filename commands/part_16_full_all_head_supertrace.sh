#!/usr/bin/env bash
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"

python tools/part_full_all_head_supertrace_real_contract_v1.py \
  --events-per-group "${FULL_SUPERTRACE_EVENTS_PER_GROUP:-64}" \
  --micro-batch "${FULL_SUPERTRACE_MICRO_BATCH:-8}" \
  --objectives "${FULL_SUPERTRACE_OBJECTIVES:-pred_logit,signed_hqql_tbl}" \
  --top-events "${FULL_SUPERTRACE_TOP_EVENTS:-80}" \
  --top-particles "${FULL_SUPERTRACE_TOP_PARTICLES:-8}"

sed -n '1,260p' reports/latest/PART_FULL_ALL_HEAD_SUPERTRACE_REAL_CONTRACT_V1.md
