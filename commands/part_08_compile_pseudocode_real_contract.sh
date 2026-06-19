#!/usr/bin/env bash
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"
python tools/part_real_contract_pseudocode_compiler_v1.py
echo "===== REAL CONTRACT PSEUDOCODE REPORT ====="
sed -n '1,260p' reports/latest/PART_REAL_CONTRACT_PSEUDOCODE_COMPILER_V1.md
