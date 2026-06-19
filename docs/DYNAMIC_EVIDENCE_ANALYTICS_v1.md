# Dynamic Evidence Analytics v1

This document defines the next layer after the evidence graph:

```text
single run evidence graph -> dynamics over many runs
```

## Why dynamics matter

A single run can show an interesting pattern, but discovery-level work needs stability:

```text
Does the same head stay important?
Does particle0/core dominance persist?
Does a class-specific pattern stay stable across samples/files?
Does a hypothesis get stronger or weaker after controls?
```

So we need to save snapshots and compare them.

## Snapshot rule

After each meaningful run, build the evidence graph with history copy:

```bash
HISTORY_COPY=1 bash scripts/RUN_RESEARCH_EVIDENCE_GRAPH_V1.sh
```

This writes:

```text
manifests/history/research_evidence_graph_YYYYMMDD_HHMMSS.json
```

Then run dynamics:

```bash
bash scripts/RUN_RESEARCH_DYNAMICS_V1.sh
```

## Dynamic questions

### D1 — Head rank stability

```text
Do the same heads remain top-ranked by all-head gate gradient?
```

Important heads now:

```text
L1_ch112:128
L0_ch40:48
L2_ch224:256
L1_ch16:32
L0_ch48:56
```

### D2 — Patch-vs-gradient divergence over time

```text
Which heads are strong by single-head patch but weaker in all-head gradient?
Which heads are strong by all-head gradient but not by patch?
```

This tells us whether a component is:

- individually causal;
- jointly supportive;
- suppressive/competitive;
- redundant.

### D3 — Particle0 / leading-core dominance

```text
Does the all-head system always select particle0?
```

If yes, it may be:

- real leading-particle physics signal;
- ordering/sorting artifact;
- model shortcut.

### D4 — Class-specific dynamics

```text
Do Hqql/Tbl always have high all-head super-score?
Does Wqq/Zqq behavior change with sample size?
```

### D5 — Hypothesis state changes

```text
AH1, AH2, AH3, AH4: stronger or weaker after controls?
```

## Storage plan

### First stage: Git JSON/CSV

Small and versioned:

```text
manifests/history/*.json
reports/latest/tables/dynamics_*.csv
reports/latest/RESEARCH_DYNAMICS_V1.md
```

### Second stage: SQLite/DuckDB

Use when history grows beyond Git-friendly size.

### Redis later

Use Redis only for live dashboard/replay cache:

```text
latest graph
latest top heads
latest events
interactive queries
```

Do not use Redis as the only archive.

## What dynamics gives us

Dynamics lets us separate:

```text
interesting one-run artifact
```

from:

```text
stable mechanism candidate
```

This is critical before claiming anything physics-relevant.
