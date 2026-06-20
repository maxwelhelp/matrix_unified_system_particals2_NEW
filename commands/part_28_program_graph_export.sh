#!/usr/bin/env bash
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"

python tools/part_program_graph_export_v1.py

sed -n '1,320p' reports/latest/PART_PROGRAM_GRAPH_EXPORT_V1.md
