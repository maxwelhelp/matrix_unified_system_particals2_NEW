#!/usr/bin/env bash
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"

python tools/part_candidate_pair_validation_v1.py \
  --events-per-group "${PAIR_VAL_EVENTS_PER_GROUP:-64}" \
  --micro-batch "${PAIR_VAL_MICRO_BATCH:-8}" \
  --max-candidates "${PAIR_VAL_MAX_CANDIDATES:-24}" \
  --strengths "${PAIR_VAL_STRENGTHS:-20,40,80}"

sed -n '1,260p' reports/latest/PART_CANDIDATE_PAIR_VALIDATION_V1.md
