# Operation Logic Atlas Plan v1

Goal: convert pseudo-head evidence into an interpretable computation map.

The question is not only:

```text
which pseudo-head is important?
```

The better question is:

```text
what does this pseudo-head compute, after previous transformations, and what does that mean for particles/classes?
```

## Model path to describe

For ParticleNet, each event goes through a particle-cloud graph path:

```text
raw particle features
  -> KNN neighborhood from particle coordinates
  -> EdgeConv layer 0: local pair/edge feature extraction
  -> EdgeConv layer 1: higher-level neighborhood composition
  -> EdgeConv layer 2: class evidence aggregation
  -> pooling / classifier
```

Our pseudo-heads are channel groups inside these EdgeConv outputs:

```text
L0_ch*: early local geometry / PID / energy-edge readers
L1_ch*: middle neighborhood composition / class-route relays
L2_ch*: late class-evidence aggregation / readout heads
```

## What each pseudo-head row should contain

```text
head_id
layer
channels
stage_role
input_state
likely_operation
particle_question
class_question
evidence_sources
pseudocode
physics_meaning
risks
next_test
```

## Evidence sources to combine

```text
all-head supertrace
class-specific gradients
particle0/top-k controls
order control
confusion atlas
known-observable residual
relation graph
stream embeddings
```

## Pseudocode template

Example:

```python
# L1_ch112:128, middle relay
for particle i:
    local_core = read_high_pt_core_and_neighbors(i)
    shape = mix(radial_spread, pt_concentration, PID_context)
    if class_context in {Hqql, Tbl}:
        write_core_anchor_evidence(shape)
```

This is not literal source code. It is an evidence-grounded semantic pseudocode of what the pseudo-head appears to compute.

## Interpretation discipline

Allowed wording:

```text
candidate operation
likely reads
supported by controls
needs residual v2 / heldout / class gradients
```

Not allowed wording:

```text
definitely discovered a new particle
```

## Why this matters

Operation-level summaries are the bridge between:

```text
raw gradients / controls
```

and:

```text
human research hypotheses about particles and interactions
```
