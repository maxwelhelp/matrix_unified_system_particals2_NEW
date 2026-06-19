# Stream Automation README v1

This document explains the automated stream-analysis stack.

## Pipeline

```text
model run
  -> all-head supertrace
  -> evidence graph
  -> dynamics
  -> stream index
  -> task watcher
  -> relation signal graph
  -> automatic comparison engine v2
```

## Main command groups

### Rebuild indices only

Use when model output already exists:

```bash
RUN_MODEL=0 bash scripts/RUN_STREAM_CYCLE_V1.sh
bash scripts/RUN_STREAM_TASK_WATCHER_V1.sh
bash scripts/RUN_RELATION_SIGNAL_GRAPH_V1.sh
bash scripts/RUN_AUTOMATIC_COMPARISON_ENGINE_V2.sh
```

### Run staged model stream

```bash
STAGE=smoke bash scripts/RUN_LARGE_STREAM_STAGE_V1.sh
STAGE=medium bash scripts/RUN_LARGE_STREAM_STAGE_V1.sh
STAGE=large bash scripts/RUN_LARGE_STREAM_STAGE_V1.sh
```

Do not run the entire downloaded dataset before controls.

## First files to read

```text
reports/latest/RESEARCH_STREAM_INDEX_V1.md
reports/latest/STREAM_TASK_WATCHER_V1.md
reports/latest/RELATION_SIGNAL_GRAPH_V1.md
reports/latest/AUTOMATIC_COMPARISON_ENGINE_V2.md
```

## Query commands

### Stream query

```bash
python tools/query_research_stream_v1.py --event-type HEAD_GATE --top 20
python tools/query_research_stream_v1.py --query particle0 --top 30
python tools/query_research_stream_v1.py --class-label label_Hqql --top 30
python tools/query_research_stream_v1.py --tag wide --top 30
python tools/query_research_stream_v1.py --hypothesis AH1 --top 30
```

### Relation query

```bash
python tools/query_relation_signal_graph_v1.py --query particle0 --top 20
python tools/query_relation_signal_graph_v1.py --src pattern:particle0 --top 20
python tools/query_relation_signal_graph_v1.py --dst hypothesis:AH1 --top 20
python tools/query_relation_signal_graph_v1.py --confidence HIGH --top 20
```

## Current stream state

Latest large stream shows:

```text
stable top heads: L1_ch112:128, L1_ch16:32, L0_ch40:48, L2_ch224:256
strong signal: particle0/core_high_pt -> Hqql/Tbl
main risk: sorting/leading-pT shortcut or known-observable proxy
```

## Automation rule

The stream should not make discovery claims by itself.

It should output:

```text
strong signal
alternative explanations
missing controls
next experiment
training row for future analyst
```

## Future DB plan

When Git files become too large:

```text
SQLite/DuckDB = durable local archive and analytics
Redis = live cache/replay only
Vector index = later, after enough controls and snapshots
```
