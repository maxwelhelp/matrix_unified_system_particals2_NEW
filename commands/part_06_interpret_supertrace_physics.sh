#!/usr/bin/env bash
set -euo pipefail

cd "$(git rev-parse --show-toplevel)"
mkdir -p reports/latest manifests/latest

python tools/part_supertrace_physics_interpreter_v1.py

echo "===== PHYSICS INTERPRETER REPORT ====="
sed -n '1,240p' reports/latest/PART_SUPERTRACE_PHYSICS_INTERPRETER_V1.md
