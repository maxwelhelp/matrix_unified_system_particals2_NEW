#!/usr/bin/env bash
set -euo pipefail
cd "$(git rev-parse --show-toplevel 2>/dev/null || pwd)"

EXT="${EXTERNAL_PARTICLE_TRANSFORMER:-$HOME/Рабочий стол/external_particle_transformer}"
DATA="${JETCLASS_TINY:-$HOME/Рабочий стол/jetclass_tiny_balanced}"
FEATURE="${FEATURE:-kinpid}"
CKPT="${CHECKPOINT:-$PWD/local_checkpoints/part/ParT_kinpid.pt}"
OUTDIR="$PWD/runs/official_weaver_predict_v5_${FEATURE}"
mkdir -p "$OUTDIR" reports/latest manifests/latest

if ! command -v weaver >/dev/null 2>&1; then
  echo "ERROR: weaver command not found. Run: pip install 'weaver-core>=0.4'" >&2
  exit 1
fi

cd "$EXT"

weaver --predict \
  --data-test \
  "HToBB:${DATA}/HToBB_*.root" \
  "HToCC:${DATA}/HToCC_*.root" \
  "HToGG:${DATA}/HToGG_*.root" \
  "HToWW2Q1L:${DATA}/HToWW2Q1L_*.root" \
  "HToWW4Q:${DATA}/HToWW4Q_*.root" \
  "TTBar:${DATA}/TTBar_*.root" \
  "TTBarLep:${DATA}/TTBarLep_*.root" \
  "WToQQ:${DATA}/WToQQ_*.root" \
  "ZToQQ:${DATA}/ZToQQ_*.root" \
  "ZJetsToNuNu:${DATA}/ZJetsToNuNu_*.root" \
  --data-config "data/JetClass/JetClass_${FEATURE}.yaml" \
  --network-config networks/example_ParticleTransformer.py \
  --model-prefix "$CKPT" \
  --gpus "${GPUS:-0}" \
  --batch-size "${BATCH_SIZE:-256}" \
  --num-workers "${NUM_WORKERS:-1}" \
  --in-memory --fetch-step 1 \
  --predict-output "$OUTDIR/pred.root" \
  2>&1 | tee "$OUTDIR/weaver_predict.log"

cd - >/dev/null

python - <<'PY'
import json, glob
from pathlib import Path
out = Path('runs')
paths = sorted(Path('.').glob('runs/official_weaver_predict_v5_*/pred.root'))
rec = {'ok': bool(paths), 'pred_files': [str(p) for p in paths]}
Path('manifests/latest/official_weaver_predict_v5_summary.json').write_text(json.dumps(rec, indent=2, ensure_ascii=False))
md = ['# Official Weaver Predict v5\n\n', 'This run uses the official `weaver --predict` path, external ParticleTransformer network config, official JetClass YAML, and local ParT checkpoint.\n\n', '```json\n', json.dumps(rec, indent=2, ensure_ascii=False), '\n```\n']
Path('reports/latest/OFFICIAL_WEAVER_PREDICT_V5.md').write_text(''.join(md))
PY

git add scripts/RUN_OFFICIAL_WEAVER_PREDICT_V5.sh reports/latest/OFFICIAL_WEAVER_PREDICT_V5.md manifests/latest/official_weaver_predict_v5_summary.json
git commit -m "Update official weaver predict v5 summary" || true
git push

echo "DONE official weaver predict: $OUTDIR/pred.root"
