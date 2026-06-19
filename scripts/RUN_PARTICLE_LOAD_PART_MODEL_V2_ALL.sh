#!/usr/bin/env bash
set -euo pipefail
cd "$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
mkdir -p runs reports/latest manifests/latest
for CKPT in local_checkpoints/part/ParT_*.pt; do
  [ -f "$CKPT" ] || continue
  NAME="$(basename "$CKPT" .pt)"
  OUT="runs/load_${NAME}_v2"
  echo "=== loading $CKPT ==="
  PYTHONUNBUFFERED=1 python tools/particle_load_part_model_v2.py --checkpoint "$CKPT" --device "${DEVICE:-cuda}" --out-dir "$OUT" 2>&1 | tee "${OUT}.log"
  cp -f "$OUT/PART_MODEL_LOAD_REPORT_V2.md" "reports/latest/PART_MODEL_LOAD_REPORT_${NAME}_V2.md"
  cp -f "$OUT/part_model_load_report_v2.json" "manifests/latest/part_model_load_report_${NAME}_v2.json"
done
python - <<'PY'
import json
from pathlib import Path
rows=[]
for p in sorted(Path('manifests/latest').glob('part_model_load_report_ParT_*_v2.json')):
    o=json.loads(p.read_text())
    rows.append({'file':str(p),'checkpoint':o['load']['checkpoint'],'loaded_good':o.get('loaded_good'), 'missing': len(o['load'].get('missing') or []), 'unexpected': len(o['load'].get('unexpected') or []), 'error': o['load'].get('error')})
Path('manifests/latest/part_model_load_v2_all_summary.json').write_text(json.dumps(rows,indent=2,ensure_ascii=False))
md=['# ParT checkpoint load v2 summary\n\n','| checkpoint | loaded_good | missing | unexpected | error |\n| --- | --- | ---: | ---: | --- |\n']
for r in rows: md.append(f"| `{r['checkpoint']}` | {r['loaded_good']} | {r['missing']} | {r['unexpected']} | {r['error']} |\n")
Path('reports/latest/PART_MODEL_LOAD_V2_ALL_SUMMARY.md').write_text(''.join(md))
PY
git add tools/particle_load_part_model_v2.py scripts/RUN_PARTICLE_LOAD_PART_MODEL_V2_ALL.sh reports/latest manifests/latest
git commit -m "Add official ParT checkpoint loader v2 summaries" || true
git push
