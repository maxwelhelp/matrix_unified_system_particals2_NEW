#!/usr/bin/env bash
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"

python tools/part_mechanism_discovery_final_v1.py

sed -n '1,360p' reports/latest/PART_MECHANISM_DISCOVERY_FINAL_V1.md
