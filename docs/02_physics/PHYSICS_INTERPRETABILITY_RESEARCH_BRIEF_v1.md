# Physics Interpretability Research Brief v1

This brief records the physics-aware research direction after the medium/large stream runs.

## Why this matters

The project is not trying to merely explain a neural network visually. The goal is to turn model internals into testable physics-style hypotheses:

```text
model signal -> physical alternative explanations -> controls -> residual test -> heldout/cross-model validation
```

## Current empirical state

After the staged medium and large stream runs:

```text
latest large run: n_events = 5120
stream snapshots = 11
stream events = 4871
latest top all-head gate = L1_ch112:128
other stable heads = L1_ch16:32, L0_ch40:48, L2_ch224:256
strongest particle signal = particle0 / core_high_pt
strongest class concentration = Hqql / Tbl
```

Current status:

```text
strong method/debug signal, not a physics discovery claim
```

## Interpretation of the current signal

The current all-head stream suggests:

```text
core / leading-particle anchor
+
class-specific distributed head mixture
+
secondary context that is weaker than the core signal
```

The top stream particles are mostly:

```text
particle index 0
high-pT
near jet axis
charged
predicted Hqql/Tbl
```

This is useful, but ambiguous.

## Main alternative explanations

### A1 — Real leading-core physics

The network may be using genuine high-energy core information relevant to jet tagging.

### A2 — Sorting / ordering shortcut

Particle 0 may simply be the leading-pT particle because of preprocessing. In that case, the model may be using index/order as a shortcut.

### A3 — Known-observable proxy

The signal may be explained by known observables:

```text
jet pT
jet mass
nparticles
tau21 / tau32
energy correlation functions
energy flow polynomials
charge/PID proxies
```

### A4 — Class distribution artifact

Hqql/Tbl dominance may be caused by the current balanced subset or model confidence pattern, not a general mechanism.

## Physics concepts to compare against

### 1. Particle cloud / dynamic graph view

ParticleNet treats a jet as a particle cloud and uses dynamic graph convolution. Therefore, good interpretability should ask whether a head/group uses:

```text
local neighbor geometry
leading particle information
wide-angle radiation
PID/charge features
class-specific local particle neighborhoods
```

### 2. Pairwise particle interactions

Particle Transformer/JetClass emphasizes pairwise particle interactions. Our route-neighbor and class-specific-gradient tests should ask:

```text
which particle pairs or neighborhoods support the class logit?
```

### 3. Prong structure

Jet tagging often depends on one-prong, two-prong, three-prong, or four-prong substructure.

Questions:

```text
does a head respond to 1-prong core?
does it distinguish 2-prong W/Z/H-like structure?
does it capture top-like 3-prong or 4-prong structure?
```

### 4. Energy correlators / EFPs

Energy Flow Polynomials and energy correlators provide a systematic language for jet substructure. If our head signal is physics-like, it should be compared against:

```text
2-point correlators
3-point correlators
4-point correlators
EFP graph features
```

### 5. N-subjettiness ratios

Useful residual checks:

```text
tau21 = tau2 / tau1
tau32 = tau3 / tau2
```

These help distinguish prong-like structures.

## Required test ladder

A signal becomes stronger only if it passes this ladder:

```text
1. stream signal exists
2. survives particle0/top-k/order controls
3. class-specific gradients agree
4. route-neighbor trace agrees
5. not explained by known observables
6. stable across ROOT files / heldout tar parts
7. appears across models/checkpoints
```

## Current blocking questions

```text
Q1. If particle0 is removed, does Hqql/Tbl confidence collapse?
Q2. If only particle0 is kept, how much prediction remains?
Q3. If top-k particles are removed, which classes fail first?
Q4. If particle order is shuffled, does the same signal remain?
Q5. Are L1_ch112:128 and L1_ch16:32 class-specific or global?
Q6. Does the signal survive after mass/tau/nparticles/EFP residualization?
Q7. Does the same relation appear in ParticleNet_kin, ParticleNet_full, ParT_kinpid, ParT_full?
```

## Claim discipline

Do not claim:

```text
we discovered a particle or new interaction
```

Allowed current claim:

```text
we found a stable model-internal leading-core / particle0 signal that strongly supports Hqql/Tbl predictions and requires controls to separate physics from shortcut.
```

Strong future claim requires:

```text
causal control + residual after known observables + heldout + cross-model agreement
```
