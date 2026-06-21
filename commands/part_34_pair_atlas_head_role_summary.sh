#!/usr/bin/env bash
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"

python tools/part_pair_atlas_head_role_summary_v1.py \
  --edges-glob "${PAIR_ATLAS_EDGES_GLOB:-reports/latest/tables/part_pair_program_graph_rank*_edges_v1.csv}"

sed -n '1,320p' reports/latest/PART_PAIR_ATLAS_HEAD_ROLE_SUMMARY_V1.md
