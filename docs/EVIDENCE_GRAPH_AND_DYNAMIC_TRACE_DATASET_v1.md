# Evidence Graph and Dynamic Trace Dataset v1

This document defines the next data layer for the project.

## Why we need it

Markdown reports are good for reading, but weak for systematic analysis.

We need structured data that can represent:

```text
run -> class -> event -> head -> particle -> feature -> route -> patch -> hypothesis
```

This lets us:

- compare runs over time;
- build vectors for heads/events/particles;
- search similar events or heads;
- train a small neural/agent analyst;
- replay model dynamics;
- build dashboards without reading all logs.

## Storage levels

### Level 1 — JSON/JSONL files

Default and safest.

Files:

```text
manifests/latest/research_evidence_graph_v1.json
reports/latest/tables/evidence_head_vectors.csv
reports/latest/tables/evidence_particle_vectors.csv
reports/latest/tables/evidence_edges.csv
```

Use this first. It is Git-friendly if kept compact.

### Level 2 — SQLite / DuckDB later

Good when rows become large.

Use for:

- millions of particle rows;
- many runs;
- fast filtering;
- local analytics.

### Level 3 — Redis later

Useful for live/replay/dashboard state, not as the only source of truth.

Use Redis for:

- latest run cache;
- fast agent lookup;
- interactive replay;
- temporary vector/session cache.

Do not make Redis the permanent archive. Keep JSONL/SQLite as the durable store.

### Level 4 — Vector index later

Use after we have enough examples.

Vectors:

- head vectors;
- particle-event vectors;
- class-contrast vectors;
- hypothesis vectors.

Can be stored in FAISS/Qdrant/SQLite-vss later.

## Evidence graph nodes

### Run node

```json
{
  "type": "run",
  "id": "run:all_head_supertrace:v1:latest",
  "metrics": {
    "n_events": 2560,
    "baseline_acc": 0.7574
  }
}
```

### Head node

```json
{
  "type": "head",
  "id": "head:L1_ch112:128",
  "vector": {
    "gate_grad": 0.8006,
    "patch_acc_drop": null,
    "layer": 1
  }
}
```

### Event node

```json
{
  "type": "event",
  "id": "event:978",
  "true_label": "label_Hqql",
  "pred_label": "label_Hqql",
  "confidence": 0.9999
}
```

### Particle node

```json
{
  "type": "particle",
  "id": "event:978:particle:0",
  "vector": {
    "pt": 445.1,
    "energy": 853.0,
    "deltaR": 0.035,
    "charge": 1,
    "super_score": 4.42
  }
}
```

### Hypothesis node

```json
{
  "type": "hypothesis",
  "id": "hypothesis:AH1",
  "title": "Distributed core-anchor + secondary-context mechanism",
  "status": "OBSERVED_NEEDS_CONTROL"
}
```

## Evidence graph edges

Examples:

```text
run -> head
run -> event
event -> particle
head -> particle
head -> hypothesis
event -> class
particle -> feature_group
hypothesis -> next_control
```

## What this gives us

### 1. Fast analysis

Instead of reading many markdown files, an agent can inspect:

```text
research_evidence_graph_v1.json
```

### 2. Dynamics over runs

If we save a timestamped copy per run:

```text
manifests/history/research_evidence_graph_YYYYMMDD_HHMM.json
```

we can see:

```text
head rank changes
particle pattern stability
class-specific changes
hypothesis confidence changes
```

### 3. Dataset for neural analyst

Training rows can look like:

```json
{
  "input": {
    "head_vector": {...},
    "particle_vectors": [...],
    "route_stats": {...},
    "patch_effects": {...}
  },
  "target": {
    "hypothesis_type": "core_anchor_secondary_context",
    "missing_control": "particle0_removal",
    "next_best_experiment": "top_k_sweep"
  }
}
```

## First implementation

`build_research_evidence_graph_v1.py` builds a compact evidence graph from current latest reports.

It is not final, but it gives the correct schema and first working dataset.
