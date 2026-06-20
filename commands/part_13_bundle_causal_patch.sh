#!/usr/bin/env bash
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"

python tools/part_bundle_causal_patch_real_contract_v1.py \
  --events-per-group "${BUNDLE_EVENTS_PER_GROUP:-64}" \
  --micro-batch "${BUNDLE_MICRO_BATCH:-8}" \
  --top-routes "${BUNDLE_TOP_ROUTES:-8}" \
  --patch-strength "${BUNDLE_PATCH_STRENGTH:-40}"

sed -n '1,220p' reports/latest/PART_BUNDLE_CAUSAL_PATCH_REAL_CONTRACT_V1.md
