#!/usr/bin/env bash
set -uo pipefail
cd "$(git rev-parse --show-toplevel)"
mkdir -p reports/latest/tables manifests/latest reports/latest/auto_pair_atlas_resume_logs

START="${PAIR_ATLAS_START:-1}"
if [[ -n "${PAIR_ATLAS_END:-}" ]]; then
  END="$PAIR_ATLAS_END"
elif [[ -n "${PAIR_ATLAS_TOPK:-}" ]]; then
  END=$((START + PAIR_ATLAS_TOPK - 1))
else
  END="72"
fi

SKIP_EXISTING="${PAIR_ATLAS_SKIP_EXISTING:-1}"
FORCE="${PAIR_ATLAS_FORCE:-0}"
CONTINUE_ON_ERROR="${PAIR_ATLAS_CONTINUE_ON_ERROR:-1}"
RUN_HEAD_ROLE_SUMMARY="${PAIR_ATLAS_RUN_HEAD_ROLE_SUMMARY:-1}"
STATUS_CSV="reports/latest/tables/part_full_pair_atlas_resume_status_v1.csv"
STATUS_MD="reports/latest/PART_FULL_PAIR_ATLAS_RESUME_STATUS_V1.md"
STATUS_JSON="manifests/latest/part_full_pair_atlas_resume_status_v1.json"
LOGDIR="reports/latest/auto_pair_atlas_resume_logs"

printf 'rank,tag,src_label,tgt_label,status,groups_status,graph_status,log_path\n' > "$STATUS_CSV"

echo "===== AUTO FULL PAIR ATLAS RESUME ====="
echo "start=$START end=$END skip_existing=$SKIP_EXISTING force=$FORCE continue_on_error=$CONTINUE_ON_ERROR"
echo "status_csv=$STATUS_CSV"

pair_meta() {
  local rank="$1"
  PAIR_ATLAS_RANK="$rank" python - <<'PY'
import csv, os, re, sys
rank=int(os.environ.get('PAIR_ATLAS_RANK','1'))
rows=list(csv.DictReader(open('reports/latest/tables/part_all_class_atlas_pairs_v1.csv', newline='', encoding='utf-8')))
if rank < 1 or rank > len(rows):
    print(f'__BAD_RANK__\t\t\t0')
    sys.exit(0)
r=rows[rank-1]
def safe(x): return re.sub(r'[^A-Za-z0-9]+','_',x.replace('label_','')).strip('_')
tag=f"rank{rank:03d}_{safe(r['src_label'])}_to_{safe(r['tgt_label'])}"
ready=str(r.get('ready_for_direct_pair_builder','1'))
print(f"{tag}\t{r['src_label']}\t{r['tgt_label']}\t{ready}")
PY
}

append_status() {
  local rank="$1" tag="$2" src="$3" tgt="$4" status="$5" groups_status="$6" graph_status="$7" log_path="$8"
  printf '%s,%s,%s,%s,%s,%s,%s,%s\n' "$rank" "$tag" "$src" "$tgt" "$status" "$groups_status" "$graph_status" "$log_path" >> "$STATUS_CSV"
}

run_and_log() {
  local log_path="$1"; shift
  echo "command: $*" > "$log_path"
  "$@" >> "$log_path" 2>&1
}

fail_count=0
skip_count=0
ok_count=0
run_count=0

for R in $(seq "$START" "$END"); do
  META="$(pair_meta "$R")"
  IFS=$'\t' read -r TAG SRC TGT READY <<< "$META"
  if [[ "$TAG" == "__BAD_RANK__" || -z "$TAG" ]]; then
    echo "===== RANK $R: BAD RANK / no atlas row ====="
    append_status "$R" "$TAG" "$SRC" "$TGT" "BAD_RANK" "NA" "NA" ""
    fail_count=$((fail_count+1))
    [[ "$CONTINUE_ON_ERROR" == "1" ]] || exit 2
    continue
  fi

  GROUPS_CSV="reports/latest/tables/part_pair_groups_${TAG}_v1.csv"
  GRAPH_JSON="manifests/latest/part_pair_program_graph_${TAG}_v1.json"
  LOG_PATH="$LOGDIR/rank${R}_${TAG}.log"
  echo
  echo "===== RANK $R: $SRC -> $TGT ($TAG) ====="

  if [[ "$READY" != "1" ]]; then
    echo "SKIP_NOT_READY: atlas planner says pair is not ready"
    append_status "$R" "$TAG" "$SRC" "$TGT" "SKIP_NOT_READY" "NA" "NA" "$LOG_PATH"
    skip_count=$((skip_count+1))
    continue
  fi

  if [[ "$FORCE" != "1" && "$SKIP_EXISTING" == "1" && -s "$GRAPH_JSON" ]]; then
    echo "SKIP_EXISTING: $GRAPH_JSON"
    append_status "$R" "$TAG" "$SRC" "$TGT" "SKIP_EXISTING" "OK_OR_EXISTING" "OK_EXISTING" "$LOG_PATH"
    skip_count=$((skip_count+1))
    continue
  fi

  groups_status="OK_EXISTING"
  if [[ "$FORCE" == "1" || ! -s "$GROUPS_CSV" ]]; then
    echo "build groups..."
    run_and_log "$LOG_PATH" env \
      PAIR_ATLAS_RANK="$R" \
      PAIR_DIRECT_SCAN_LIMIT="${PAIR_DIRECT_SCAN_LIMIT:-20000}" \
      PAIR_DIRECT_BATCH_SIZE="${PAIR_DIRECT_BATCH_SIZE:-64}" \
      PAIR_DIRECT_MAX_PER_GROUP="${PAIR_DIRECT_MAX_PER_GROUP:-256}" \
      bash commands/part_31_build_pair_direct_replay_groups.sh
    rc=$?
    if [[ $rc -ne 0 ]]; then
      echo "GROUPS_FAIL rc=$rc log=$LOG_PATH"
      append_status "$R" "$TAG" "$SRC" "$TGT" "GROUPS_FAIL" "FAIL" "NOT_RUN" "$LOG_PATH"
      fail_count=$((fail_count+1))
      [[ "$CONTINUE_ON_ERROR" == "1" ]] || exit $rc
      continue
    fi
    groups_status="OK_BUILT"
  else
    echo "groups exist: $GROUPS_CSV"
    echo "groups exist: $GROUPS_CSV" > "$LOG_PATH"
  fi

  echo "run program graph..."
  run_and_log "$LOG_PATH" env \
    PAIR_ATLAS_RANK="$R" \
    PAIR_PIPE_EVENTS_PER_GROUP="${PAIR_PIPE_EVENTS_PER_GROUP:-16}" \
    PAIR_PIPE_MICRO_BATCH="${PAIR_PIPE_MICRO_BATCH:-4}" \
    PAIR_PIPE_VALUE_MICRO_BATCH="${PAIR_PIPE_VALUE_MICRO_BATCH:-4}" \
    PAIR_PIPE_VAL_EVENTS_PER_GROUP="${PAIR_PIPE_VAL_EVENTS_PER_GROUP:-16}" \
    PAIR_PIPE_VAL_MICRO_BATCH="${PAIR_PIPE_VAL_MICRO_BATCH:-8}" \
    PAIR_PIPE_MAX_CANDIDATES="${PAIR_PIPE_MAX_CANDIDATES:-8}" \
    PAIR_PIPE_STRENGTHS="${PAIR_PIPE_STRENGTHS:-40}" \
    bash commands/part_32_run_pair_rank_program_graph_adapter.sh
  rc=$?
  if [[ $rc -ne 0 || ! -s "$GRAPH_JSON" ]]; then
    echo "GRAPH_FAIL rc=$rc graph=$GRAPH_JSON log=$LOG_PATH"
    append_status "$R" "$TAG" "$SRC" "$TGT" "GRAPH_FAIL" "$groups_status" "FAIL" "$LOG_PATH"
    fail_count=$((fail_count+1))
    [[ "$CONTINUE_ON_ERROR" == "1" ]] || exit ${rc:-2}
    continue
  fi

  echo "OK: $GRAPH_JSON"
  append_status "$R" "$TAG" "$SRC" "$TGT" "OK" "$groups_status" "OK" "$LOG_PATH"
  ok_count=$((ok_count+1))
  run_count=$((run_count+1))
done

# Rebuild pair atlas summary from all existing pair graph jsons, using a filtered best edge if possible.
python - <<'PY'
import csv, json, re
from pathlib import Path

def load_json(path):
    p=Path(path)
    if not p.exists(): return {}
    try: return json.loads(p.read_text(encoding='utf-8'))
    except Exception: return {}

def read_csv(path):
    p=Path(path)
    if not p.exists(): return []
    with p.open(newline='', encoding='utf-8') as f: return list(csv.DictReader(f))

def tag_to_pair(tag):
    m=re.match(r'rank(\d+)_([^_]+)_to_(.+)', tag)
    if not m: return ('', '', '')
    return (int(m.group(1)), 'label_'+m.group(2), 'label_'+m.group(3))

def fw(x):
    try: return float(x)
    except Exception: return 0.0

rows=[]
for p in sorted(Path('manifests/latest').glob('part_pair_program_graph_rank*_v1.json')):
    tag=p.name.replace('part_pair_program_graph_','').replace('_v1.json','')
    rank,src,tgt=tag_to_pair(tag)
    pg=load_json(p)
    disc=load_json(f'manifests/latest/part_pair_discovery_{tag}_v1.json')
    val_rows=read_csv(f'reports/latest/tables/part_pair_validation_{tag}_summary_v1.csv')
    strong=[r for r in val_rows if abs(fw(r.get('best_B_delta_margin'))) >= 1e-3]
    strong.sort(key=lambda r: abs(fw(r.get('best_B_delta_margin'))) + 2*abs(fw(r.get('best_B_delta_tbl_pred'))), reverse=True)
    best=strong[0] if strong else {}
    rows.append({
        'rank':rank,'tag':tag,'src_label':src,'tgt_label':tgt,
        'nodes':pg.get('nodes',''),'edges':pg.get('edges',''),
        'discovery_candidates':disc.get('candidates',''),
        'validation_rows':len(val_rows),
        'strong_validation_rows':len(strong),
        'best_head':best.get('head_id',''),
        'best_pair':best.get('pair_role',''),
        'best_diag':best.get('diagnosis',''),
        'best_B_delta':best.get('best_B_delta_margin',''),
        'best_B_flip':best.get('best_B_delta_tbl_pred',''),
        'best_score':best.get('score',''),
    })
rows.sort(key=lambda r: int(r['rank'] or 9999))
Path('reports/latest/tables').mkdir(parents=True, exist_ok=True)
with open('reports/latest/tables/part_pair_atlas_summary_v1.csv','w',newline='',encoding='utf-8') as f:
    fields=list(rows[0].keys()) if rows else ['rank']
    w=csv.DictWriter(f,fieldnames=fields); w.writeheader(); w.writerows(rows)
Path('manifests/latest/part_pair_atlas_summary_v1.json').write_text(json.dumps({'ok':True,'pairs':len(rows),'rows':rows},indent=2,ensure_ascii=False),encoding='utf-8')
lines=['# PART_PAIR_ATLAS_SUMMARY_V1\n\nAll-class pair atlas summary over generated pair program graphs. Best mechanism is filtered with abs(B_delta)>=1e-3.\n\n',f'- pairs: **{len(rows)}**\n\n','| rank | src | tgt | nodes | edges | discovery | validation | strong | best_head | best_pair | B_delta | B_flip | score |\n','| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | --- | --- | ---: | ---: | ---: |\n']
for r in rows:
    lines.append(f"| {r['rank']} | {r['src_label']} | {r['tgt_label']} | {r['nodes']} | {r['edges']} | {r['discovery_candidates']} | {r['validation_rows']} | {r['strong_validation_rows']} | `{r['best_head']}` | `{r['best_pair']}` | {r['best_B_delta']} | {r['best_B_flip']} | {r['best_score']} |\n")
lines.append('\n## Decision\n\n')
lines.append('`PAIR_ATLAS_SUMMARY_OK`: all generated pair graphs were summarized with nonzero best-mechanism filter.\n' if rows else '`PAIR_ATLAS_EMPTY`: no pair graphs found.\n')
Path('reports/latest/PART_PAIR_ATLAS_SUMMARY_V1.md').write_text(''.join(lines),encoding='utf-8')
print(json.dumps({'ok':True,'pairs':len(rows),'out_md':'reports/latest/PART_PAIR_ATLAS_SUMMARY_V1.md'},indent=2))
PY

if [[ "$RUN_HEAD_ROLE_SUMMARY" == "1" ]]; then
  bash commands/part_34_pair_atlas_head_role_summary.sh
fi

python - <<'PY'
import csv, json
from pathlib import Path
rows=list(csv.DictReader(open('reports/latest/tables/part_full_pair_atlas_resume_status_v1.csv', newline='', encoding='utf-8')))
counts={}
for r in rows: counts[r['status']]=counts.get(r['status'],0)+1
obj={'ok': counts.get('GROUPS_FAIL',0)==0 and counts.get('GRAPH_FAIL',0)==0 and counts.get('BAD_RANK',0)==0, 'counts':counts, 'rows':rows}
Path('manifests/latest/part_full_pair_atlas_resume_status_v1.json').write_text(json.dumps(obj,indent=2,ensure_ascii=False),encoding='utf-8')
lines=['# PART_FULL_PAIR_ATLAS_RESUME_STATUS_V1\n\nResume-safe full pair atlas runner status.\n\n',f'- ok: **{obj["ok"]}**\n',f'- counts: `{counts}`\n\n','| rank | tag | src | tgt | status | groups | graph | log |\n','| ---: | --- | --- | --- | --- | --- | --- | --- |\n']
for r in rows:
    lines.append(f"| {r['rank']} | `{r['tag']}` | {r['src_label']} | {r['tgt_label']} | **{r['status']}** | {r['groups_status']} | {r['graph_status']} | `{r['log_path']}` |\n")
Path('reports/latest/PART_FULL_PAIR_ATLAS_RESUME_STATUS_V1.md').write_text(''.join(lines),encoding='utf-8')
print(json.dumps({'ok':obj['ok'],'counts':counts,'out_md':'reports/latest/PART_FULL_PAIR_ATLAS_RESUME_STATUS_V1.md'},indent=2))
PY

echo
sed -n '1,260p' "$STATUS_MD"
echo
echo "===== PAIR ATLAS SUMMARY ====="
sed -n '1,220p' reports/latest/PART_PAIR_ATLAS_SUMMARY_V1.md
