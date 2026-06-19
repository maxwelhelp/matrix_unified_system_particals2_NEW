# Updated Research State After All-Head Supertrace v1

This document updates the current hypotheses after the first successful all-head differentiable supertrace.

## Validated run

```text
Model: ParticleNet_kinpid.pt
Dataset: JetClass tiny balanced subset
SAMPLES_PER_FILE=256
n_events=2560
micro_batch=32
baseline_acc=0.7574
objective_pred_logit_mean=0.8754
```

## Main method update

Previous analyses mostly used:

```text
single-head patch / single-head particle trace
```

The new run uses:

```text
all EdgeConv pseudo-head gates simultaneously
```

This means we can now separate two questions:

```text
1. Which single head is individually important if patched?
2. Which heads jointly support the current predicted-class logit?
```

These are not identical.

## Important result

Single-head tracing emphasized:

```text
L1_ch16:32
```

All-head differentiable support ranks:

```text
1. L1_ch112:128
2. L0_ch40:48
3. L2_ch224:256
4. L1_ch16:32
5. L0_ch48:56
```

Interpretation:

```text
The network answer is distributed across early, middle, and late pseudo-head groups.
```

## Updated hypotheses

### AH1 — Distributed core-anchor + secondary-context mechanism

**Claim:** The all-head system appears to anchor strongly on the leading/core particle, often particle 0, and then uses secondary particles for class separation.

**Evidence:**

- Top all-head events often rank particle 0 first.
- Particle 0 is usually very high-pT and near the jet axis.
- Secondary particles include lower-pT, sometimes wider-angle or PID-specific fragments.

**Status:** `OBSERVED / NEEDS CONTROL`

**Risk:** particle 0 dominance may be a sorting/ordering artifact or a normal leading-particle shortcut.

**Next controls:**

- remove particle 0;
- keep only particle 0;
- remove top-k particles;
- same-count random controls;
- per-class top-k effects.

---

### AH2 — Hqql/Tbl high-confidence head-system signature

**Claim:** The all-head supertrace is strongest for `Hqql` and `Tbl` predictions.

**Evidence:**

```text
Hqql: super_mean ~= 3.6635, acc_within_pred ~= 0.9608
Tbl:  super_mean ~= 3.5990, acc_within_pred ~= 0.9802
```

**Status:** `OBSERVED`

**Next tests:**

- class-specific all-head gradients;
- Hqql vs H4q contrast;
- Tbl vs Tbqq contrast;
- correct-vs-wrong examples.

---

### AH3 — Single-head and all-head evidence differ

**Claim:** Single-head patch rank and all-head gradient rank measure different aspects of computation.

**Evidence:**

- `L1_ch16:32` is strong in single-head analysis but only rank 4 in all-head gate gradient.
- Top all-head gates include `L1_ch112:128`, `L0_ch40:48`, `L2_ch224:256`.

**Status:** `IMPORTANT METHOD FINDING`

**Next tests:**

- compare patch rank vs gate-gradient rank for all heads;
- identify suppressive negative heads;
- run multi-head patch combinations.

---

### AH4 — Head-system mixture hypothesis

**Claim:** The model uses a multi-stage mixture:

```text
L0 heads: early raw feature / geometry / PID readers
L1 heads: route/context composition
L2 heads: late class evidence aggregation
```

**Evidence:**

Top all-head gates span all three layers:

```text
L0_ch40:48
L1_ch112:128
L1_ch16:32
L2_ch224:256
```

**Status:** `OBSERVED`

**Next tests:**

- per-layer ablation;
- head-combination patch;
- head-to-class-contrast projection.

## Discovery relevance

Current result does not discover a new particle.

But it improves the method path toward discovery:

```text
event -> particles -> head gates -> class logits -> hypotheses -> controls
```

To become discovery-relevant, the next missing pieces are:

1. evidence graph / dynamic trace dataset;
2. leading-particle controls;
3. class-specific head gradients;
4. route-neighbor trace;
5. residual analysis after known observables;
6. anomaly/signal-injection mode.

## New data direction

All future runs should be stored not only as markdown reports but as structured evidence:

```text
run_id
class_id
head_id
particle_id
feature vector
route vector
patch vector
hypothesis links
next-control links
```

This enables:

- fast lookup;
- graph analytics;
- vector search;
- neural/agent hypothesis generation;
- replaying dynamics over runs.
