#!/usr/bin/env bash
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"

python tools/part_all_head_route_gradient_real_contract_v1.py \
  --events-per-group "${ROUTE_GRAD_EVENTS_PER_GROUP:-32}" \
  --micro-batch "${ROUTE_GRAD_MICRO_BATCH:-4}" \
  --gate-scale "${ROUTE_GRAD_GATE_SCALE:-1.0}"

sed -n '1,260p' reports/latest/PART_ALL_HEAD_ROUTE_GRADIENT_REAL_CONTRACT_V1.md
