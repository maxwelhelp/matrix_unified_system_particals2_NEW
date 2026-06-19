#!/usr/bin/env bash
set -euo pipefail
cd "$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
mkdir -p external reports/latest manifests/latest runs

PART_REPO_URL="${PART_REPO_URL:-https://github.com/jet-universe/particle_transformer.git}"
PART_REPO_DIR="${PART_REPO_DIR:-external/particle_transformer}"

if [ ! -d "$PART_REPO_DIR/.git" ]; then
  echo "Cloning Particle Transformer into $PART_REPO_DIR"
  git clone --depth 1 "$PART_REPO_URL" "$PART_REPO_DIR"
else
  echo "Particle Transformer repo already exists: $PART_REPO_DIR"
  git -C "$PART_REPO_DIR" pull --ff-only || true
fi

if [ -f "$PART_REPO_DIR/requirements.txt" ]; then
  echo "requirements.txt found. Install manually if needed:"
  echo "  pip install -r $PART_REPO_DIR/requirements.txt"
else
  echo "No requirements.txt found in $PART_REPO_DIR"
fi

echo "DONE setup Particle Transformer. Next: bash scripts/RUN_PART_BOOTSTRAP_PROBE_V1.sh"
