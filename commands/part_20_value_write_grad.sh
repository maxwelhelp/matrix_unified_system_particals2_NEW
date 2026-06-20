#!/usr/bin/env bash
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"

python tools/part_value_write_grad_real_contract_v1.py \
  --events-per-group "${VALUE_WRITE_EVENTS_PER_GROUP:-32}" \
  --micro-batch "${VALUE_WRITE_MICRO_BATCH:-4}" \
  --objectives "${VALUE_WRITE_OBJECTIVES:-signed_hqql_tbl,B_tbl_minus_hqql}"

sed -n '1,260p' reports/latest/PART_VALUE_WRITE_GRAD_REAL_CONTRACT_V1.md
