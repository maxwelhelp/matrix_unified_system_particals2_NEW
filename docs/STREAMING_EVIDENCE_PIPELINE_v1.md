# Streaming Evidence Pipeline v1

This document defines the stream-processing layer for the particle interpretability project.

## Core idea

Treat research outputs like a stream of evidence events, similar to how text analysis treats many tokens/documents:

```text
text domain:
  article -> tokens -> heads -> token evidence -> summary -> drilldown

particle domain:
  run -> events -> particles -> heads -> graph evidence -> stream summary -> drilldown
```

The goal is not to read every report manually. The goal is:

1. see the main state quickly;
2. identify alerts and changes;
3. drill down by query when needed;
4. keep a dataset for future neural/agent analysis.

## Stream event types

The stream should include events like:

```text
RUN_SUMMARY
HEAD_GATE
HEAD_PATCH
HEAD_QUESTION
PARTICLE_TOP
CLASS_PATTERN
HYPOTHESIS_UPDATE
ALERT
NEXT_ACTION
```

Each event should be compact JSONL.

Example:

```json
{
  "event_type": "HEAD_GATE",
  "run_index": 1,
  "head_id": "L1_ch112:128",
  "score": 0.8006,
  "tags": ["head", "gate", "top_head", "L1"]
}
```

## Main files

The stream layer produces:

```text
manifests/latest/research_stream_index_v1.json
reports/latest/RESEARCH_STREAM_INDEX_V1.md
reports/latest/tables/research_stream_events.jsonl
reports/latest/tables/research_stream_cards.csv
reports/latest/tables/research_stream_alerts.csv
```

And query tool:

```text
tools/query_research_stream_v1.py
```

## How ChatGPT/agent should use it

### Step 1 — read the stream dashboard

Open:

```text
manifests/latest/research_stream_index_v1.json
```

Look at:

```text
main_cards
alerts
top_heads
top_classes
top_hypotheses
next_actions
available_drilldowns
```

### Step 2 — drill down only when needed

Examples:

```bash
python tools/query_research_stream_v1.py --query particle0 --top 20
python tools/query_research_stream_v1.py --head L1_ch112:128
python tools/query_research_stream_v1.py --class label_Hqql
python tools/query_research_stream_v1.py --hypothesis AH1
python tools/query_research_stream_v1.py --event-type HEAD_GATE
```

### Step 3 — decide next experiment

The agent should output:

```text
current strongest evidence
weakest control
next experiment
expected falsification signal
```

## Difference from dynamics

`RESEARCH_DYNAMICS_V1` compares snapshots.

`RESEARCH_STREAM_INDEX_V1` transforms all snapshots into a queryable evidence stream.

Dynamics answers:

```text
what changed between runs?
```

Stream answers:

```text
what evidence exists, what is important, and where should I drill down?
```

## Redis / DB plan

### Now

Use Git-tracked JSON/CSV/JSONL.

### Later

Use SQLite/DuckDB for many rows.

### Redis

Use Redis for live cache/replay only:

```text
latest stream cards
latest alerts
interactive query cache
```

Redis should not be the only permanent store.

## Why this matters

This gives us a dataset suitable for:

- fast human analysis;
- ChatGPT/agent analysis;
- future neural hypothesis generator;
- replaying evidence over time;
- tracking whether a physics-like hypothesis is stable or just a one-run artifact.
