#!/usr/bin/env bash
set -euo pipefail
cd "$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
echo "=== Particle Stage 0/1: dummy probe ==="
bash scripts/RUN_PARTICLE_DUMMY_PROBE_V1.sh
echo "=== Particle Stage 0/1: dummy patch controls ==="
bash scripts/RUN_PARTICLE_DUMMY_PATCH_V2.sh
echo "=== Particle Stage 1: model/checkpoint loader ==="
bash scripts/RUN_PARTICLE_LOAD_PART_MODEL_V1.sh
echo "DONE Particle Stage 0/1. Check reports/latest/*.md and manifests/latest/*.json"
