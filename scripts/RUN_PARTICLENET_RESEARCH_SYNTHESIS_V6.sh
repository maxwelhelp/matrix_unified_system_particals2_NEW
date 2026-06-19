#!/usr/bin/env bash
set -euo pipefail
cd "$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
mkdir -p runs reports/latest/tables manifests/latest
PYTHONUNBUFFERED=1 python tools/particlenet_research_synthesis_v6.py \
  --out-dir runs/particlenet_research_synthesis_v6 \
  2>&1 | tee runs/particlenet_research_synthesis_v6.log
cp -f runs/particlenet_research_synthesis_v6/PARTICLENET_RESEARCH_SYNTHESIS_V6.md reports/latest/PARTICLENET_RESEARCH_SYNTHESIS_V6.md
cp -f runs/particlenet_research_synthesis_v6/particlenet_research_synthesis_v6_summary.json manifests/latest/particlenet_research_synthesis_v6_summary.json
cp -f runs/particlenet_research_synthesis_v6/tables/research_hypothesis_board.csv reports/latest/tables/research_hypothesis_board.csv
git add docs/PARTICLE_HYPOTHESIS_REGISTRY_v1.md docs/PARTICLE_RESEARCH_WORKFLOW_v1.md tools/particlenet_research_synthesis_v6.py scripts/RUN_PARTICLENET_RESEARCH_SYNTHESIS_V6.sh reports/latest manifests/latest
git commit -m "Update ParticleNet research synthesis v6" || true
git push

echo "DONE research synthesis. Report: reports/latest/PARTICLENET_RESEARCH_SYNTHESIS_V6.md"
