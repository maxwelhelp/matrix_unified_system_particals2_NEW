#!/usr/bin/env bash
set -euo pipefail

cd "$(git rev-parse --show-toplevel 2>/dev/null || pwd)"

EXT="${EXTERNAL_PARTICLE_TRANSFORMER:-$HOME/Рабочий стол/external_particle_transformer}"
DATA="${JETCLASS_TINY:-$HOME/Рабочий стол/jetclass_tiny_balanced}"
FEATURE="${FEATURE:-kinpid}"
WEIGHTS="${WEIGHTS:-$PWD/local_checkpoints/part/ParT_kinpid.pt}"
OUTDIR="$PWD/runs/official_part_wrapped_ckpt_v9_${FEATURE}"
WRAPPED="$OUTDIR/ParT_${FEATURE}_wrapped_mod.pt"

mkdir -p "$OUTDIR" reports/latest manifests/latest

python tools/wrap_part_checkpoint_v9.py \
  --input "$WEIGHTS" \
  --output "$WRAPPED" \
  2>&1 | tee "$OUTDIR/wrap_checkpoint.log"

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
  --network-config networks/example_ParticleTransformer.py --use-amp \
  --model-prefix "$WRAPPED" \
  --gpus "${GPUS:-0}" \
  --batch-size "${BATCH_SIZE:-256}" \
  --num-workers "${NUM_WORKERS:-1}" \
  --in-memory --fetch-step 1 \
  --predict-output "$OUTDIR/pred.root" \
  2>&1 | tee "$OUTDIR/weaver_predict.log"

cd - >/dev/null

PYTHONUNBUFFERED=1 python tools/official_weaver_pred_probe_v7_label_branch.py \
  --pred-dir "$OUTDIR" \
  --out-dir runs/official_part_wrapped_ckpt_v9_probe \
  2>&1 | tee runs/official_part_wrapped_ckpt_v9_probe.log

cp -f runs/official_part_wrapped_ckpt_v9_probe/OFFICIAL_WEAVER_PRED_PROBE_V7_LABEL_BRANCH.md \
  reports/latest/OFFICIAL_PART_WRAPPED_CKPT_V9_REPORT.md

cp -f runs/official_part_wrapped_ckpt_v9_probe/official_weaver_pred_probe_v7_label_branch.json \
  manifests/latest/official_part_wrapped_ckpt_v9_summary.json

git add \
  tools/wrap_part_checkpoint_v9.py \
  scripts/RUN_OFFICIAL_PART_WRAPPED_CKPT_V9.sh \
  reports/latest/OFFICIAL_PART_WRAPPED_CKPT_V9_REPORT.md \
  manifests/latest/official_part_wrapped_ckpt_v9_summary.json

git commit -m "Update official ParT wrapped checkpoint v9 diagnostic" || true
git push

echo "DONE v9. Report: reports/latest/OFFICIAL_PART_WRAPPED_CKPT_V9_REPORT.md"
