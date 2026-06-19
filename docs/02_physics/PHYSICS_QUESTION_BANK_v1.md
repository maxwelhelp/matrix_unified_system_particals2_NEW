# Physics Question Bank v1

This is the question bank for physics-aware stream analysis. These questions should become automatic comparisons and eventually training rows for a neural/agent analyst.

## Category A — Particle/core controls

### A1. Leading particle dependence

Question:

```text
Does the model depend on particle0 / leading-pT particle?
```

Signals:

```text
particle0 top-rank fraction
particle0 super-score
class-specific particle0 dominance
```

Controls:

```text
remove particle0
keep only particle0
remove top-k particles
same-count random removal
```

### A2. Ordering vs coordinate signal

Question:

```text
Is the model using particle index/order or physical coordinates?
```

Controls:

```text
shuffle particle order
sort by different rule
compare particle index vs pt/deltaR signals
```

## Category B — Class-specific questions

### B1. Hqql/Tbl signature

Question:

```text
Why does Hqql/Tbl dominate top all-head evidence?
```

Tests:

```text
class-specific all-head gradients
correct-vs-wrong split
balanced vs natural class distribution
per-file stability
```

### B2. Wqq/Zqq/Hbb/Hcc contrasts

Question:

```text
Which heads/particles separate nearby physics classes?
```

Contrasts:

```text
Wqq vs Zqq
Hbb vs Hcc
Hqql vs H4q
Tbl vs Tbqq
QCD vs signal-like jets
```

## Category C — Prongness and jet substructure

### C1. One-prong core

Question:

```text
Is the head mostly reading a one-prong leading-core structure?
```

Compare against:

```text
leading-pT particle
jet mass
nparticles
tau1
```

### C2. Two-prong structure

Question:

```text
Does the head distinguish two-prong W/Z/H-like structure?
```

Compare against:

```text
tau21
2-point energy correlators
pairwise particle geometry
```

### C3. Three/four-prong structure

Question:

```text
Does the head encode top-like or multi-prong structure?
```

Compare against:

```text
tau32
3-point / 4-point energy correlators
multi-neighbor route patterns
```

## Category D — Route/neighborhood questions

### D1. Local neighbor evidence

Question:

```text
Does a top particle activate because of itself or because of its KNN neighbors?
```

Required trace:

```text
top particle -> KNN neighbors -> neighbor pt/energy/deltaR/PID -> head contribution
```

### D2. Wide secondary context

Question:

```text
Are wide/low-pT particles useful secondary evidence or noise?
```

Tests:

```text
wide particle removal
route-neighbor trace
heldout stability
class-specific relation
```

## Category E — Head/circuit questions

### E1. Source-relay-readout pattern

Question:

```text
Do L0/L1/L2 heads form a source-relay-readout circuit?
```

Expected mapping:

```text
L0: source/raw feature and geometry reader
L1: relay/context/neighborhood composition
L2: readout/class evidence aggregation
```

Tests:

```text
layer-wise ablation
head-pair synergy
path patching
class-specific gradients
```

### E2. Patch vs gradient divergence

Question:

```text
Which heads are jointly supportive but individually redundant?
```

Compare:

```text
single-head patch effect
all-head gate gradient
multi-head patch effect
```

## Category F — Residual/discovery questions

### F1. Known-observable residual

Question:

```text
Does the head/particle signal remain after known observables explain the prediction?
```

Known observables:

```text
jet pT
jet mass
nparticles
tau21/tau32
energy correlators / EFPs
charge/PID summaries
```

### F2. Cross-model agreement

Question:

```text
Does the same signal appear in ParticleNet and ParT variants?
```

Models/checkpoints:

```text
ParticleNet_kin
ParticleNet_kinpid
ParticleNet_full
ParT_kin
ParT_kinpid
ParT_full
```

### F3. Discovery readiness

Question:

```text
Is this still method debugging, known-physics interpretation, residual candidate, anomaly candidate, or discovery candidate?
```

Decision:

```text
method_debug: missing controls
known_physics: explained by known observables
residual_candidate: survives known observables
anomaly_candidate: appears in anomaly/background-only setup
discovery_candidate: survives controls + heldout + cross-model + domain review
```
