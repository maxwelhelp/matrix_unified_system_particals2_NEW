#!/usr/bin/env bash
set -euo pipefail
cd "$(git rev-parse --show-toplevel 2>/dev/null || pwd)"

EXT="${EXTERNAL_PARTICLE_TRANSFORMER:-$HOME/Рабочий стол/external_particle_transformer}"
DATA="${JETCLASS_TINY:-$HOME/Рабочий стол/jetclass_tiny_balanced}"
FEATURE="${FEATURE:-kinpid}"
WEIGHTS="${WEIGHTS:-$PWD/local_checkpoints/part/ParT_kinpid.pt}"
OUTDIR="$PWD/runs/official_part_load_weights_v8_${FEATURE}"
mkdir -p "$OUTDIR" reports/latest manifests/latest

if ! command -v weaver >/dev/null 2>&1; then
  echo "ERROR: weaver command not found. Run: pip install 'weaver-core>=0.4'" >&2
  exit 1
fi

cd "$EXT"

# Important difference from v5:
#   --model-prefix is a temporary output prefix
#   --load-model-weights is the pretrained ParT .pt file
# This matches the official fine-tune usage in train_TopLandscape.sh.
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
  --network-config networks/example_ParticleTransformer.py --use-amp \
  --model-prefix "$OUTDIR/tmp_net" \
  --load-model-weights "$WEIGHTS" \
  --gpus "${GPUS:-0}" \
  --batch-size "${BATCH_SIZE:-256}" \
  --num-workers "${NUM_WORKERS:-1}" \
  --in-memory --fetch-step 1 \
  --predict-output "$OUTDIR/pred.root" \
  2>&1 | tee "$OUTDIR/weaver_predict.log"

cd - >/dev/null

PRED_DIR="$OUTDIR" PYTHONUNBUFFERED=1 python tools/official_weaver_pred_probe_v7_label_branch.py \
  --pred-dir "$OUTDIR" \
  --out-dir runs/official_part_load_weights_v8_probe \
  2>&1 | tee runs/official_part_load_weights_v8_probe.log

cp -f runs/official_part_load_weights_v8_probe/OFFICIAL_WEAVER_PRED_PROBE_V7_LABEL_BRANCH.md reports/latest/OFFICIAL_PART_LOAD_WEIGHTS_V8_REPORT.md
cp -f runs/official_part_load_weights_v8_probe/official_weaver_pred_probe_v7_label_branch.json manifests/latest/official_part_load_weights_v8_summary.json

git add scripts/RUN_OFFICIAL_PART_LOAD_WEIGHTS_V8.sh reports/latest/OFFICIAL_PART_LOAD_WEIGHTS_V8_REPORT.md manifests/latest/official_part_load_weights_v8_summary.json
git commit -m "Update official ParT load-model-weights v8 diagnostic" || true
git push

echo "DONE ParT load-model-weights v8. Report: reports/latest/OFFICIAL_PART_LOAD_WEIGHTS_V8_REPORT.md"
