#!/usr/bin/env bash
set -euo pipefail

cd "$(git rev-parse --show-toplevel)"

MSG="${1:-Update lightweight interpretability reports}"
MAX_BYTES="${MAX_BYTES:-50000000}"

echo "=== stage lightweight outputs only ==="
mkdir -p reports/latest manifests/latest reports/latest/tables

# Stage reports/manifests that are useful for development.
find reports/latest manifests/latest \
  -type f \( -name '*.md' -o -name '*.json' -o -name '*.csv' \) \
  ! -name '*pair_flows*.csv' \
  ! -name '*path_summary*.csv' \
  ! -name '*trace*.csv' \
  -size -${MAX_BYTES}c \
  -print0 2>/dev/null | xargs -0 -r git add

# Never stage heavy artifacts.
git reset -q -- '*.root' '*.pt' '*.pth' '*.ckpt' '*.safetensors' '*.npy' '*.npz' '*.zip' '*.tar' '*.tar.gz' '*.tgz' 2>/dev/null || true

echo "=== status ==="
git status --short

echo "=== forbidden tracked files check ==="
if git ls-files | grep -Ei '\.(pt|pth|ckpt|safetensors|onnx|bin|pkl|pickle|root|h5|hdf5|npy|npz|parquet|arrow|tar|tgz|zip|7z|rar)$'; then
  echo "ERROR: forbidden heavy files are tracked"
  exit 1
fi

echo "=== tracked files over 50MB ==="
if git ls-files -z | xargs -0 du -b 2>/dev/null | awk '$1 > 50000000 {print $0}' | grep .; then
  echo "ERROR: tracked files over 50MB"
  exit 1
else
  echo "OK: no tracked files over 50MB"
fi

if git diff --cached --quiet; then
  echo "Nothing staged. No commit needed."
  exit 0
fi

git commit -m "$MSG"
git push origin main
