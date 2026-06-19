#!/usr/bin/env bash
set -euo pipefail
cd "$(git rev-parse --show-toplevel 2>/dev/null || pwd)"

echo "[stack] ParticleNet research stack"
echo "[stack] SAMPLES_PER_FILE=${SAMPLES_PER_FILE:-128} MODE=${MODE:-kinpid}"

# 1) Core causal why-class / hypothesis atlas
bash scripts/RUN_PARTICLENET_HYPOTHESIS_ATLAS_V3.sh

# 2) Discovery route / particle controls
bash scripts/RUN_PARTICLENET_DISCOVERY_ATLAS_V4.sh

# 3) Research compass: pseudo-heads, observables, contrasts
bash scripts/RUN_PARTICLENET_RESEARCH_COMPASS_V5.sh

# 4) Synthesis: board, priorities, next tests
bash scripts/RUN_PARTICLENET_RESEARCH_SYNTHESIS_V6.sh

echo "[stack] DONE. Main report: reports/latest/PARTICLENET_RESEARCH_SYNTHESIS_V6.md"
