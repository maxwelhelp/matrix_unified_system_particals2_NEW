# Automatic Comparison Engine v1

This document translates the human reasoning process into explicit comparisons.

The goal is not another generic graph. The goal is to automate the specific comparisons that currently produce useful hypotheses.

## What the human analyst is comparing

### C1 — Stream relation vs missing control

Human reasoning:

```text
particle0/core_high_pt has strong relation to AH1 and Hqql/Tbl.
But it can be a shortcut.
Therefore the next experiment is particle0/top-k controls.
```

Automatic comparison:

```text
relation_signal(pattern:particle0/core -> AH1/class)
vs
control_status(particle0 removal/top-k/random)
```

Useful output:

```text
Strong candidate, not confirmed, missing P0 control.
```

---

### C2 — Pattern relation vs physical alternative

Human reasoning:

```text
particle0/core signal could mean real leading-core physics or sorting shortcut.
wide secondary signal could mean real neighborhood context or class imbalance.
```

Automatic comparison:

```text
pattern relation
vs
known risk alternatives
vs
available falsification tests
```

Useful output:

```text
Interpretation split: physics candidate / shortcut candidate / needs control.
```

---

### C3 — Single-head patch vs all-head gradient

Human reasoning:

```text
L1_ch16:32 was strong in single-head patch but rank 4 in all-head gradient.
Therefore patch importance and joint support differ.
```

Automatic comparison:

```text
patch_acc_drop / patch_delta_logit
vs
gate_abs_grad / gate_rank
```

Useful output:

```text
head role = individually causal / jointly supportive / divergent / suppressive / redundant
```

---

### C4 — Head rank stability vs sample/run changes

Human reasoning:

```text
L1_ch112:128 and L0_ch40:48 stay top across snapshots.
Stable heads are more meaningful than one-run spikes.
```

Automatic comparison:

```text
head_rank_history
vs
run conditions: sample size, controls, dataset subset
```

Useful output:

```text
stable mechanism candidate / unstable artifact / class-specific head
```

---

### C5 — Class signature vs class-specific gradient need

Human reasoning:

```text
Hqql/Tbl dominate the all-head stream.
But global all-head gradients are averaged across classes.
Need class-specific gradients.
```

Automatic comparison:

```text
class frequency/score in stream
vs
availability of class-specific gradients
```

Useful output:

```text
strong class signature but missing class-specific attribution
```

---

### C6 — Wide/secondary context vs route-neighbor evidence

Human reasoning:

```text
wide particles have a strong signal to Tbl and secondary context.
But without KNN neighbors we do not know if it is route logic or just loose fragments.
```

Automatic comparison:

```text
wide particle relations
vs
route-neighbor trace availability
vs
causal route controls
```

Useful output:

```text
candidate secondary context, needs route-neighbor trace
```

---

### C7 — Negative gate vs suppressive role

Human reasoning:

```text
Negative gate gradients may indicate suppressive heads.
But local gradients can be misleading.
Need class-specific suppressive analysis.
```

Automatic comparison:

```text
negative_gate_count / heads
vs
class-specific negative gradients
vs
patch effects
```

Useful output:

```text
possible suppressive head, needs class-specific check
```

## Output schema

Each comparison row should include:

```text
comparison_id
claim
support_signal
contradiction_signal
missing_control
risk
recommended_next_experiment
status
priority
training_label
```

## Status values

```text
CANDIDATE_STRONG_MISSING_CONTROL
SUPPORTED_BY_MULTIPLE_SIGNALS
CONTRADICTED
NEEDS_CLASS_SPECIFIC_TEST
NEEDS_ROUTE_TRACE
NEEDS_HELDOUT
LOW_PRIORITY
```

## Why this is the right training data

A future MLP/attention analyst should not learn from raw markdown.

It should learn from examples like:

```json
{
  "input": {
    "relation_signal": 0.94,
    "support": 115,
    "missing_control": "particle0_topk",
    "risk": "sorting shortcut"
  },
  "target": {
    "status": "CANDIDATE_STRONG_MISSING_CONTROL",
    "next_experiment": "particle0_topk_controls"
  }
}
```

That is the correct level for automation.
