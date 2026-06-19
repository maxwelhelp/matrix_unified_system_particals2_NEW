#!/usr/bin/env bash
set -euo pipefail

cd "$(git rev-parse --show-toplevel)"
mkdir -p reports/latest manifests/latest

python tools/part_pad_control_v1.py

echo "===== PAD CONTROL REPORT ====="
sed -n '1,240p' reports/latest/PART_PAD_CONTROL_V1.md
