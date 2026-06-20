#!/usr/bin/env bash
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"

python tools/part_natural_attention_grad_real_contract_v1.py \
  --events-per-group "${NAT_ATTN_EVENTS_PER_GROUP:-32}" \
  --micro-batch "${NAT_ATTN_MICRO_BATCH:-4}" \
  --objectives "${NAT_ATTN_OBJECTIVES:-signed_hqql_tbl,B_tbl_minus_hqql}"

sed -n '1,260p' reports/latest/PART_NATURAL_ATTENTION_GRAD_REAL_CONTRACT_V1.md
