#!/usr/bin/env bash
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"

python tools/part_natural_attention_manual_grad_real_contract_v1.py \
  --events-per-group "${NAT_MANUAL_EVENTS_PER_GROUP:-32}" \
  --micro-batch "${NAT_MANUAL_MICRO_BATCH:-4}" \
  --objectives "${NAT_MANUAL_OBJECTIVES:-signed_hqql_tbl,B_tbl_minus_hqql}"

sed -n '1,260p' reports/latest/PART_NATURAL_ATTENTION_MANUAL_GRAD_REAL_CONTRACT_V1.md
