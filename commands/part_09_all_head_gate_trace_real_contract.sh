#!/usr/bin/env bash
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"
python tools/part_all_head_gate_trace_real_contract_v1.py
sed -n '1,220p' reports/latest/PART_ALL_HEAD_GATE_TRACE_REAL_CONTRACT_V1.md
