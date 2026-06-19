# Stream Task Watcher v1

This document defines the first automatic analyst over the research stream.

## Core idea

Do **not** let an MLP/attention model watch the stream randomly.

Instead, define trained/trackable tasks:

```text
stream evidence -> fixed task bank -> score/risk/next experiment
```

The watcher should answer only predefined research questions.

## Why this is needed

The stream index is fast because it only builds an index from existing evidence graphs. The heavy work is still model runs / controls.

The watcher sits above the stream:

```text
model run -> evidence graph -> stream events -> task watcher -> next experiment
```

## Initial task bank

### T1 — PARTICLE0_SHORTCUT_OR_CORE_ANCHOR

Question:

```text
Is the all-head system over-dominated by particle0 / leading-core evidence?
```

Evidence:

- fraction of top particle events that are particle0;
- particle0 scores;
- class concentration Hqql/Tbl;
- top-k controls when available.

Next experiment:

```text
particle0 removal / keep-only particle0 / top-k removal / random same-count controls
```

### T2 — HEAD_RANK_STABILITY

Question:

```text
Do the same heads stay important across snapshots?
```

Evidence:

- latest top head list;
- rank deltas;
- gate gradient deltas.

### T3 — NEGATIVE_SUPPRESSIVE_GATES

Question:

```text
Are there heads that suppress the current class logit?
```

Evidence:

- negative gate gradients;
- class-specific negative gates later.

### T4 — HQQL_TBL_SIGNATURE

Question:

```text
Is the current stream mostly dominated by Hqql/Tbl high-confidence events?
```

Evidence:

- top particles/classes;
- class particle pattern summary;
- all-head super-score by class.

### T5 — PATCH_VS_GRADIENT_DIVERGENCE

Question:

```text
Which heads are patch-important but not gradient-important, or gradient-important but not patch-important?
```

Evidence:

- head gate gradients;
- patch acc/logit drops;
- rank comparison.

### T6 — WIDE_SECONDARY_CONTEXT

Question:

```text
Besides particle0/core, is there a stable wide/secondary particle context?
```

Evidence:

- wide-tagged particle stream events;
- single-head traces;
- later route-neighbor traces.

## Watcher output

Files:

```text
reports/latest/STREAM_TASK_WATCHER_V1.md
manifests/latest/stream_task_watcher_v1.json
reports/latest/tables/stream_task_watcher_scores.csv
reports/latest/tables/stream_task_training_dataset.jsonl
```

## MLP/attention model plan

Current v1 uses deterministic task feature extraction and weak labels.

Later, when we have enough snapshots/controls, train a small model:

```text
input: task feature vector over stream history
output: task state / risk / next experiment
```

Possible model:

```text
MLP for fixed summary vectors
small attention model for event sequences
```

But only after the task bank is stable. The model should not invent tasks; it should score known tasks.

## Rule

The watcher is not a discovery oracle.

It is an automation layer for:

- detecting stable patterns;
- detecting missing controls;
- prioritizing next experiments;
- building a dataset for later neural analyst.
