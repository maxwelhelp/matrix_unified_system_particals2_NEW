# Single Head Particle Trace Findings v1

Target head:

```text
ParticleNet EdgeConv L1 ch16:32
```

This document records the first particle-level trace interpretation. It is the ParticleNet analogue of the earlier text-token analysis.

## Run summary

The first trace used:

```text
n_events = 640
baseline_acc = 0.7719
captured output shape = [640, 128, 128]
```

The trace ranks concrete particles inside concrete jets by the activation energy of the selected pseudo-head.

## Main observation

The head does **not** look like a pure top-pT head.

In several top events, the strongest particles for this head are often:

- high-index real particles near the end of the particle list;
- low-pT but high-|deta/dphi| or high-deltaR particles;
- charged particles in several strongest ranks;
- followed by core / higher-pT particles in the same event.

This suggests a better current hypothesis:

> EdgeConv L1 ch16:32 may be a middle learned-neighborhood head that detects a combination of wide-angle / boundary particle evidence plus core high-pT context, then turns that into class-separating evidence.

This is more specific than the older label:

```text
kinematic/energy head
```

## Examples from the trace

### Event 337 — predicted Tbl

Strongest particle:

```text
particle 19
head_energy = 71.7
pt ≈ 0.25
energy ≈ 1.25
deltaR ≈ 2.22
charge = +1
```

Then the same event also includes core-ish particles with larger pT and lower deltaR.

Interpretation:

```text
wide/outer charged particle + core context
```

### Event 397 — predicted Tbqq

Top particles:

```text
particle 49: deltaR ≈ 1.85, low pt, charge +1
particle 48: deltaR ≈ 3.06, low pt, charge +1
then particles with pt ≈ 24.5, 9.4, 7.2, 6.1 in the core
```

Interpretation:

```text
wide/boundary particles plus strong core/top-like structure
```

### Event 517 — predicted QCD

Top particles include:

```text
particle 44: deltaR ≈ 2.49, pt ≈ 1.67, charge +1
particle 43: deltaR ≈ 2.13, pt ≈ 1.86, charge +1
then core particles with pt ≈ 12.36 and 7.72
```

Interpretation:

```text
QCD-like wide charged fragments plus core activity
```

## Updated hypothesis for L1 ch16:32

Old hypothesis:

```text
middle learned-neighborhood / route-composition head
```

Better hypothesis after particle trace:

```text
L1 ch16:32 asks whether the jet contains a wide-angle / boundary particle pattern, often involving charged low-pT particles, combined with a core high-pT context that helps separate top/QCD/Higgs/vector classes.
```

Confidence:

```text
causal importance: high
particle-level pattern: medium
physics interpretation: low/medium until route-neighbor and heldout tests
```

## What to compute next

### P0 — route-neighbor trace

For the top particles selected by this head:

```text
show their KNN neighbors
neighbor deltaR
neighbor pt/energy
whether neighbors are core or wide-angle
```

Goal:

```text
Does the head activate on wide particles because of their neighbors, or because of the particle itself?
```

### P0 — top-head particle traces

Run the same particle trace for the top heads from the catalog:

```text
L1_ch16:32
L0_ch24:32
L0_ch0:8
L0_ch40:48
L0_ch48:56
L0_ch8:16
L0_ch16:24
L1_ch112:128
```

Goal:

```text
Do different heads look at different particle patterns, or do they all just select high-index/wide particles?
```

### P0 — long trace

Repeat with:

```text
SAMPLES_PER_FILE=256
SAMPLES_PER_FILE=512
```

Goal:

```text
Check stability of the particle-level pattern.
```

### P1 — class-contrast trace

For this head, project/measure support for:

```text
Tbqq vs Tbl
Wqq vs Zqq
Hbb vs Hcc
QCD vs Tbqq
```

### P1 — control for ordering / high-index bias

Because many top particles have high indices, test:

```text
is the head truly selecting physical wide particles,
or is it accidentally sensitive to ordering / low-pT tail position?
```

Controls:

- shuffle particle order;
- compare by deltaR rather than index;
- compare same deltaR/random particles;
- inspect masks and real particle counts.

## Discovery relevance

This does not discover a new particle yet.

But it is a concrete step toward a discovery tool:

```text
head -> concrete particles -> neighbor route -> class/contrast effect -> residual after known observables
```

If a head consistently selects a particle-interaction pattern not explained by known observables, and this survives heldout data and anomaly tests, then it can become a physics candidate hypothesis.
