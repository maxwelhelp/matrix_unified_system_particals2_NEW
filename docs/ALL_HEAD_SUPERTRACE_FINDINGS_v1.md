# All-Head Supertrace Findings v1

Target run:

```text
ParticleNet_kinpid.pt
SAMPLES_PER_FILE=256
n_events=2560
micro_batch=32
baseline_acc=0.7574
```

This report records the first successful differentiable all-head supertrace.

## What changed compared to single-head tracing

Single-head tracing studied one pseudo-head:

```text
L1 ch16:32
```

All-head supertrace adds differentiable gates over all EdgeConv pseudo-head groups and backpropagates the predicted-class logit through them.

This answers a different question:

```text
Which heads jointly support the current model answer?
```

## Top differentiable gates

Current top gates by absolute gradient:

```text
1. L1_ch112:128  grad +0.8006
2. L0_ch40:48   grad +0.6735
3. L2_ch224:256 grad +0.6716
4. L1_ch16:32   grad +0.6645
5. L0_ch48:56   grad +0.3620
6. L2_ch128:160 grad +0.3511
7. L0_ch8:16    grad +0.3350
8. L2_ch64:96   grad +0.2970
9. L2_ch0:32    grad +0.2642
10. L0_ch0:8    grad -0.2327
```

Important point:

```text
L1_ch16:32 was the strongest single-head patch candidate,
but in all-head differentiable support it is rank 4.
```

Interpretation:

```text
The full prediction is distributed across several heads. Single-head causal patch and all-head differentiable support are complementary, not identical.
```

## Class-level pattern

All-head super-score is highest for:

```text
Hqql: mean 3.6635, p90 4.3667, acc_within_pred 0.9608
Tbl:  mean 3.5990, p90 4.2220, acc_within_pred 0.9802
```

Lower mean groups include:

```text
Tbqq: mean 2.9502
Hgg:  mean 2.9959
Hbb/Hcc/H4q around 3.0
```

Interpretation:

```text
The current all-head supertrace is strongest on high-confidence semileptonic / mixed final-state classes, especially Hqql and Tbl.
```

This may mean:

1. these classes have cleaner head-system evidence;
2. the selected objective favors confident predictions;
3. the model uses a strong common head mixture for these classes.

## Particle-level pattern

Top events are dominated by:

```text
Hqql and Tbl
```

Top particle lists almost always include particle `0` as rank 1.

Example Hqql event 774:

```text
particle 0:
  super_score 4.4253
  pt ≈ 445
  energy ≈ 853
  deltaR ≈ 0.035
```

Then the same event includes a mixture of:

```text
core/high-pT particles:
  pt ≈ 47.7, 32.7, 31.3, 20.9

low-pT / wider or PID-specific particles:
  photon-like / neutral / charged particles
  deltaR up to ≈ 0.52
```

Example event 784:

```text
particle 0:
  pt ≈ 526
  deltaR ≈ 0.022

then wide/low-pT particles:
  deltaR ≈ 0.50–0.71
  pt often below 3
```

## Updated interpretation

Single-head L1_ch16:32 looked like:

```text
wide/boundary charged fragment + core context head
```

All-head supertrace looks more like:

```text
core-leading-particle anchor + distributed secondary particle context
```

So the model may use two-level evidence:

```text
1. strong core / leading particle anchor, often particle 0;
2. secondary particle pattern from wide/low-pT/PID fragments;
3. several heads combine these into class evidence.
```

## Important risk

Because particle 0 dominates many all-head top events, we must test if this is:

```text
real leading-particle physics signal
```

or an artifact of:

```text
particle ordering / sorting by pt
```

This is not a bug. It is a necessary hypothesis/control.

## New hypotheses

### AH1 — Distributed core-anchor + secondary-context mechanism

The all-head system appears to anchor strongly on the leading particle, then uses secondary particles for class separation.

Status:

```text
OBSERVED / NEEDS CONTROL
```

Next tests:

- remove particle 0;
- top-k particle sweep;
- compare with random same-count removal;
- per-class top-k effects.

### AH2 — Hqql/Tbl high-confidence head-system signature

The all-head supertrace is strongest for Hqql and Tbl predictions.

Status:

```text
OBSERVED
```

Next tests:

- class-specific head-gate gradients;
- Hqql vs H4q contrast;
- Tbl vs Tbqq contrast;
- correct vs wrong predictions.

### AH3 — Single-head and all-head evidence differ

L1_ch16:32 is not the top all-head gate, even though it is strong as a single patched head.

Status:

```text
IMPORTANT METHOD FINDING
```

Meaning:

```text
Patch importance and differentiable support should both be tracked.
```

Next tests:

- compare patch rank vs gate-gradient rank;
- identify heads that are suppressive/negative gates;
- run multi-head patch combinations.

## Next required code/reports

### P0 — leading particle controls

Implement:

```text
particle0 removal
particle0-only kept
top-k removal / keep
same-count random controls
```

### P0 — class-specific all-head gradients

Current gradients are averaged over all predicted classes. Need separate gradients for:

```text
Hqql
Tbl
Tbqq
Wqq
Zqq
Hbb/Hcc/Hgg
```

### P0 — route-neighbor all-head trace

For top particles from all-head supertrace:

```text
show KNN neighbors
neighbor pt/energy/deltaR
head group contribution
```

### P1 — evidence graph dataset

Store every run as structured evidence for a future neural/agent analyst:

```text
run -> class -> head -> particle -> feature -> route -> patch -> hypothesis
```

This is the right format if we later put a model/agent on top of our analysis data.
