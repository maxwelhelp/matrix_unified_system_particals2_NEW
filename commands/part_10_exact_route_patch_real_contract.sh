#!/usr/bin/env bash
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"

python tools/part_exact_route_patch_real_contract_v1.py \
  --events-per-group "${PATCH_EVENTS_PER_GROUP:-32}" \
  --micro-batch "${PATCH_MICRO_BATCH:-8}" \
  --top-rules "${PATCH_TOP_RULES:-8}" \
  --patch-strength "${PATCH_STRENGTH:-40}"

sed -n '1,220p' reports/latest/PART_EXACT_ROUTE_PATCH_REAL_CONTRACT_V1.md
