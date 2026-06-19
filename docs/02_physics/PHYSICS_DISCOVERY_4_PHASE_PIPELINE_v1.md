# Physics Discovery 4-Phase Pipeline v1

This is the current main roadmap for turning ParticleNet introspection into a physics hypothesis candidate.

## Core shift

Claude's correction is accepted.

Old question:

```text
How does the network compute?
```

Correct question:

```text
What physical regime does the network compute, and when does confusion happen systematically?
```

Old pipeline:

```text
route -> causal patch -> residual -> hypothesis
```

Correct pipeline:

```text
confusion regime -> physical observable -> ambiguity reason -> route -> patch -> residual -> stability -> physics hypothesis
```

## Main physics question

```text
In what kinematic/topological regime are Hqql and Tbl physically ambiguous, and what does ParticleNet see to disambiguate them?
```

If residual remains after richer physics observables, the residual route becomes a candidate for a new useful observable / mechanism, not automatically a new particle.

## Phase 1 — Statistics / confusion regime

Goal: collect enough events so we are not reasoning from 4 examples.

Target counts:

```text
Hqql_to_Tbl >= 100 events if possible
Tbl_to_Hqql >= 100 events if possible
```

For each event record:

```text
particle0 PID / pT / charge / pT rank
leading particle PID / pT / charge
KNN neighbor PID composition
lepton isolation proxy
missing-pT proxy
lepton + core deltaR
lepton + leading deltaR
```

Output:

```text
A table of physical conditions where confusion happens systematically.
```

Key file/tool:

```text
tools/hqql_tbl_confusion_physics_regime_v1.py
scripts/RUN_HQQL_TBL_CONFUSION_PHYSICS_REGIME_V1.sh
scripts/RUN_PHASE1_HQQL_TBL_FULL_STATISTICS_V1.sh
```

## Phase 2 — Physical swap / route causality

Goal: prove whether lepton/core or secondary KNN context causally drives Hqql/Tbl disambiguation.

Tests:

```text
A. lepton/core swap: swap particle0/lepton from Tbl_correct into Hqql_correct
B. neighbor swap: keep lepton, swap only KNN neighbors from Tbl_correct
C. b/hadronic-context patch: mask/replace hadronic or b-like neighbors separately
```

Output:

```text
Answer whether lepton itself or its secondary context holds Tbl-like readout.
```

Existing precursor:

```text
ROUTE_SPECIFIC_PATCH_V1 already shows targeted L2 route removal is much stronger than random same-count on selected events.
```

## Phase 3 — Known Observable Residual v2

Goal: test if standard/richer physics observables explain the network decision.

Add features:

```text
lepton isolation proxy
missing-pT proxy
lepton + b/core deltaR
lepton-neighborhood PID composition
ECF-like 2-point / 3-point features
mT proxy for W candidate
top-k pair geometry
PID/charge neighborhood summary
```

Compare:

```text
ParticleNet decision/accuracy vs surrogate v2 on Hqql/Tbl and all classes
```

If residual remains:

```text
The network may be using a feature not captured by this observable set.
That becomes a candidate for a new useful observable/mechanism.
```

## Phase 4 — Stability / cross-model

Goal: prove the mechanism is not one-file or one-model artifact.

Tests:

```text
per-file stability over multiple ROOT files
same heads/routes/confusion regime?
ParticleNet vs ParT or another independent architecture
same physical ambiguity regime?
```

If Phase 1-4 pass:

```text
mechanism candidate with physics meaning
```

not necessarily:

```text
new particle / new interaction
```

## What can be claimed at each phase

| Phase | Allowed claim |
| --- | --- |
| After 1 | Confusion systematically happens under physical conditions X. |
| After 2 | Secondary KNN/core context causally holds disambiguation. |
| After 3 | Residual remains or vanishes after richer observables. |
| After 4 | Mechanism is stable / architecture-independent enough for physics hypothesis candidate. |

## Current known results before Phase 1 scaling

Small diagnostic run:

```text
Hqql_to_Tbl n=4 only, too small for final pattern.
particle0/leading often lepton-like in Hqql/Tbl groups.
L2 route-specific patch on selected events is strongly causal compared to random same-count.
```

Therefore the next action is Phase 1 full statistics.

## Immediate next action

Run:

```bash
bash scripts/RUN_PHASE1_HQQL_TBL_FULL_STATISTICS_V1.sh
```

Use staged configs first:

```text
PHASE1_STAGE=medium
PHASE1_STAGE=large
PHASE1_STAGE=full
```
