#!/usr/bin/env bash
set -euo pipefail

cd "$(git rev-parse --show-toplevel)"

RUN_SYNC="${RUN_SYNC:-0}"
RUN_ANALYZE="${RUN_ANALYZE:-1}"

echo "=== Matrix Unified System Particles: all lightweight checks ==="
echo "repo: $(pwd)"
echo "RUN_SYNC=$RUN_SYNC RUN_ANALYZE=$RUN_ANALYZE"

if [ "$RUN_SYNC" = "1" ]; then
  echo
  echo "=== 00 sync ==="
  bash commands/part_00_sync_repo.sh
fi

echo
echo "=== 01 sanity contract ==="
bash commands/part_01_sanity_contract.sh

if [ "$RUN_ANALYZE" = "1" ]; then
  echo
  echo "=== 02 analyze existing Weaver outputs ==="
  bash commands/part_02_analyze_weaver_outputs.sh || true
fi

echo
echo "=== 03 report index ==="
bash commands/part_03_report_index.sh

echo
echo "=== done ==="
echo "Inspect first: reports/latest/PART_SANITY_CONTRACT.md"
echo "Then: reports/latest/PART_WEAVER_OUTPUT_ANALYZER_V1.md"
echo "Then: reports/latest/PART_INTERPRETABILITY_INDEX.md"
