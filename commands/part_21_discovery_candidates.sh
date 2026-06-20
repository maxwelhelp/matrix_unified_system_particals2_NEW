#!/usr/bin/env bash
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"

python tools/part_discovery_candidates_real_contract_v1.py

sed -n '1,320p' reports/latest/PART_DISCOVERY_CANDIDATES_REAL_CONTRACT_V1.md
