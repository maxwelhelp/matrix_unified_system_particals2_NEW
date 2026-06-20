#!/usr/bin/env bash
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"

python tools/part_classifier_logit_decoder_real_contract_v1.py \
  --events-per-group "${CLASSIFIER_DECODER_EVENTS_PER_GROUP:-32}" \
  --micro-batch "${CLASSIFIER_DECODER_MICRO_BATCH:-8}" \
  --objectives "${CLASSIFIER_DECODER_OBJECTIVES:-signed_hqql_tbl,B_tbl_minus_hqql}"

sed -n '1,360p' reports/latest/PART_CLASSIFIER_LOGIT_DECODER_REAL_CONTRACT_V1.md
