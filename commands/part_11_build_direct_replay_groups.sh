#!/usr/bin/env bash
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"

python tools/part_direct_replay_group_builder_v1.py \
  --scan-limit "${DIRECT_SCAN_LIMIT:-20000}" \
  --batch-size "${DIRECT_BATCH_SIZE:-64}" \
  --max-per-group "${DIRECT_MAX_PER_GROUP:-256}"

sed -n '1,220p' reports/latest/PART_DIRECT_REPLAY_GROUP_BUILDER_V1.md
