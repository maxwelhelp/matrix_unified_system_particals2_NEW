#!/usr/bin/env bash
set -euo pipefail

cd "$(git rev-parse --show-toplevel)"

echo "=== before sync ==="
git status --short

echo "=== fetch ==="
git fetch origin main

echo "=== rebase local changes safely ==="
git pull --rebase --autostash origin main

echo "=== after sync ==="
git status --short
