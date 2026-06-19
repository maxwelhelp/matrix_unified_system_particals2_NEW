# Stream Feature Embeddings v1

This document defines structured embedding fields for stream analysis.

## Why not raw text embeddings first

The stream already contains structured scientific evidence:

```text
head ids
class labels
particle flags
control drops
relation signals
missing controls
risk labels
```

Before using LLM/text embeddings, we should build deterministic numerical embeddings from these fields.

These are better for first MLP/attention analyst because they are:

- reproducible;
- easy to debug;
- directly tied to evidence;
- small enough for CSV/JSONL;
- trainable later.

## Embedding targets

### 1. Stream event embeddings

For events from:

```text
reports/latest/tables/research_stream_events.jsonl
```

Each event gets numeric fields:

```text
event_type one-hot / code
score_norm
run_index_norm
class one-hot
head layer/channel features
particle0/core/wide/charged flags
pt/energy/deltaR normalized
negative gate flag
```

### 2. Relation edge embeddings

For edges from:

```text
reports/latest/tables/relation_signal_edges.csv
```

Each relation gets:

```text
relation_signal
support_norm
mean_strength_norm
lift_norm
confidence code
missing-control flag
particle0/core/wide/class/head/hypothesis flags
```

### 3. Control embeddings

For controls from:

```text
reports/latest/tables/particle0_topk_control_summary_v2.csv
```

Each control gets:

```text
acc
acc_drop
flip_rate
delta_logit
valid_particles_mean_after
control type flags
k value
```

### 4. Comparison embeddings

For rows from:

```text
reports/latest/tables/automatic_comparison_rows_v2.csv
```

Each comparison gets:

```text
priority code
status code
missing-control flag
risk flag
training label code
```

## What this enables

```text
clustering heads/events/relations
finding similar mechanisms
training task watcher MLP
training event-sequence attention analyst
detecting anomaly-like relation changes
fast dashboard scoring
```

## Important rule

These are **evidence embeddings**, not final scientific proof.

They help automate comparison and ranking, but controls still decide the claim status.
