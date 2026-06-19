#!/usr/bin/env bash
set -euo pipefail
cd "$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
mkdir -p reports/latest manifests/latest runs

PART_REPO_DIR="${PART_REPO_DIR:-external/particle_transformer}"
JETCLASS_OFFICIAL="${JETCLASS_OFFICIAL:-$HOME/Рабочий стол/JetClassOfficial}"
SPLIT_DIR="${SPLIT_DIR:-val_5M}"
DATADIR="$JETCLASS_OFFICIAL/$SPLIT_DIR"
MODE="${MODE:-kinpid}"
PART_CHECKPOINT="${PART_CHECKPOINT:-$PART_REPO_DIR/models/ParT_${MODE}.pt}"
BATCH_SIZE="${BATCH_SIZE:-64}"
NUM_WORKERS="${NUM_WORKERS:-1}"
GPUS="${GPUS:-0}"

pick_one() {
  local pat="$1"
  find "$DATADIR" -maxdepth 1 -type f -name "$pat" | sort | head -n 1
}

HToBB=$(pick_one 'HToBB_*.root')
HToCC=$(pick_one 'HToCC_*.root')
HToGG=$(pick_one 'HToGG_*.root')
HToWW2Q1L=$(pick_one 'HToWW2Q1L_*.root')
HToWW4Q=$(pick_one 'HToWW4Q_*.root')
TTBar=$(pick_one 'TTBar_[0-9]*.root')
TTBarLep=$(pick_one 'TTBarLep_*.root')
WToQQ=$(pick_one 'WToQQ_*.root')
ZToQQ=$(pick_one 'ZToQQ_*.root')
ZJetsToNuNu=$(pick_one 'ZJetsToNuNu_*.root')

for x in HToBB HToCC HToGG HToWW2Q1L HToWW4Q TTBar TTBarLep WToQQ ZToQQ ZJetsToNuNu; do
  if [ -z "${!x}" ]; then
    echo "ERROR: missing file for $x in $DATADIR"
    exit 1
  fi
done

DATA_ARGS=(
  "HToBB:${HToBB}"
  "HToCC:${HToCC}"
  "HToGG:${HToGG}"
  "HToWW2Q1L:${HToWW2Q1L}"
  "HToWW4Q:${HToWW4Q}"
  "TTBar:${TTBar}"
  "TTBarLep:${TTBarLep}"
  "WToQQ:${WToQQ}"
  "ZToQQ:${ZToQQ}"
  "ZJetsToNuNu:${ZJetsToNuNu}"
)

printf '%s\n' "${DATA_ARGS[@]}" > manifests/latest/part_weaver_predict_smoke_v3_args.txt

echo "SMOKE ParT predict: 1 file per class"
printf '  %s\n' "${DATA_ARGS[@]}"

weaver \
  --predict \
  --run-mode test \
  --data-test "${DATA_ARGS[@]}" \
  --data-config "$PART_REPO_DIR/data/JetClass/JetClass_${MODE}.yaml" \
  --network-config "$PART_REPO_DIR/networks/example_ParticleTransformer.py" \
  --model-prefix "$PART_CHECKPOINT" \
  --predict-output reports/latest/part_weaver_predict_smoke_v3.root \
  --batch-size "$BATCH_SIZE" \
  --batch-size-test "$BATCH_SIZE" \
  --num-workers "$NUM_WORKERS" \
  --fetch-step 1 \
  --gpus "$GPUS" \
  --log runs/part_weaver_predict_smoke_v3.log

cat > reports/latest/PART_WEAVER_PREDICT_SMOKE_V3.md <<EOF
# PART_WEAVER_PREDICT_SMOKE_V3

Fast official ParT/Weaver predict smoke test.

- split: ${DATADIR}
- files: 1 per class
- mode: ${MODE}
- checkpoint: ${PART_CHECKPOINT}
- output prefix: reports/latest/part_weaver_predict_smoke_v3.root
- log: runs/part_weaver_predict_smoke_v3.log

Use this for quick configuration checks before running full val/test.
EOF

git add scripts/RUN_PART_WEAVER_PREDICT_SMOKE_V3.sh reports/latest/PART_WEAVER_PREDICT_SMOKE_V3.md manifests/latest/part_weaver_predict_smoke_v3_args.txt reports/latest/part_weaver_predict_smoke_v3*.root runs/part_weaver_predict_smoke_v3.log || true
git commit -m "Add fast ParT Weaver smoke predict" || true
git push || true

echo "DONE smoke ParT predict. Report: reports/latest/PART_WEAVER_PREDICT_SMOKE_V3.md"
