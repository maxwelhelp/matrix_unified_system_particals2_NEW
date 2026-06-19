# Relation Signal Graph v1

This document defines automatic relationship mining over the stream/evidence graph.

## Goal

Build relationships automatically across:

```text
head <-> class
head <-> hypothesis
particle pattern <-> class
particle pattern <-> hypothesis
task <-> next action
negative gate <-> suppressive hypothesis
wide/core/particle0 <-> class signatures
```

The goal is not to connect everything with everything. That creates noise.

The goal is to compute **signals**:

```text
relationship strength
support
risk
next control
```

## Signal types

### R1 — Head-Class signal

Example:

```text
L1_ch112:128 -> Hqql/Tbl evidence stream
```

Current v1 is approximate because we do not yet have class-specific head gradients.

Next control:

```text
class-specific all-head gradients
```

### R2 — ParticlePattern-Class signal

Examples:

```text
particle0/core_high_pt -> Hqql
particle0/core_high_pt -> Tbl
wide/charged secondary -> QCD/Tbqq maybe
```

Current signal can be measured from particle stream events.

### R3 — Head-Hypothesis signal

Examples:

```text
L1_ch112:128 -> AH4 head-system mixture
L1_ch16:32 -> AH3 patch-vs-gradient divergence
```

### R4 — Task-Hypothesis signal

Examples:

```text
T1 particle0 watcher -> AH1
T5 patch/gradient divergence -> AH3
```

### R5 — Alert-NextAction signal

Examples:

```text
particle0/core dominance alert -> particle0 removal/top-k controls
negative gates alert -> suppressive head analysis
```

## Scoring

Each relation gets:

```text
support: how many events/rows support it
strength: normalized score or mean evidence score
lift_like: relation frequency vs global frequency
confidence: low/medium/high based on support + strength + missing controls
risk: why it may be false
next_control: what test should falsify/confirm it
```

## Important limitation

Relation signals are **not causal proof**.

They are automatic prioritization for deeper experiments.

A relation becomes strong only after:

```text
stream signal + causal patch/control + heldout stability
```

## Outputs

```text
reports/latest/RELATION_SIGNAL_GRAPH_V1.md
manifests/latest/relation_signal_graph_v1.json
reports/latest/tables/relation_signal_edges.csv
reports/latest/tables/relation_signal_nodes.csv
reports/latest/tables/relation_signal_alerts.csv
```

## Next step after v1

After particle0/top-k controls and class-specific gradients, the relation graph should be upgraded to include:

```text
causal_edge_score
control_passed
heldout_stability
relation_status: candidate / supported / rejected / needs_control
```
