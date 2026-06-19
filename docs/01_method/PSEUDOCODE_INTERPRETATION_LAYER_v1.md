# Pseudocode Interpretation Layer v1

This is the core differentiator of the project.

The goal is not only to say:

```text
this pseudo-head is important
```

The goal is to write an evidence-grounded pseudocode program for each pseudo-head:

```text
what transformed input it receives
what particle/class question it asks
what operation it likely performs
what evidence it writes to the next stage
what this means physically
what risks and controls remain
```

## Required output formats

The pseudocode layer should always produce three formats:

```text
1. Markdown report for human reading
2. CSV table for dashboards/spreadsheets
3. JSONL rows for training/search/retrieval
```

## Required fields per pseudo-head

```text
head_id
layer
channels
stage_role
pre_layer_state
reads
core_operation_steps
writes
class_competition
particle_interpretation
physics_interpretation
pseudocode
supporting_evidence
confidence_level
remaining_risks
next_tests
```

## Interpretation discipline

This is semantic pseudocode, not literal source code.

Allowed:

```text
candidate operation
likely reads/writes
supported by evidence
needs heldout/residual/class-specific tests
```

Not allowed:

```text
definitely discovered new particle/interactions
```

## Why this matters

Other approaches often stop at saliency, gradients, or feature importance.

This project aims to extract a readable program:

```text
raw particles -> graph neighborhoods -> pseudo-head operations -> class evidence -> controls/residual validation
```

The pseudocode database is the bridge from neural activity to mechanistic hypotheses.
