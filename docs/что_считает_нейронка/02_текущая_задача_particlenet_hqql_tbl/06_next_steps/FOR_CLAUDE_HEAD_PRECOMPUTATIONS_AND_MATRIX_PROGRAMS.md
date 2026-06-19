# For Claude — head precomputations, projections, and matrix-program reading

## What we already have

We are not only doing external bins/patches/surrogates. We already have a large internal interpretation layer over ParticleNet pseudo-heads.

Existing internal reports/tables include:

```text
reports/latest/PARTICLENET_ALL_HEAD_SUPERTRACE_V1.md
reports/latest/HEAD_OUTPUT_TRACE_V1.md
reports/latest/CLASS_SPECIFIC_ALL_HEAD_GRADIENTS_V1.md
reports/latest/FULL_HEAD_QUESTION_CATALOG.md
reports/latest/PARTICLENET_HEAD_PROJECTION_COMPOSER_V2.md

reports/latest/tables/all_head_supertrace_events.csv
reports/latest/tables/all_head_supertrace_particles.csv
reports/latest/tables/all_head_gate_gradients.csv
reports/latest/tables/head_output_trace.csv
reports/latest/tables/class_specific_head_gradients.csv
reports/latest/tables/head_projection_question_map.csv
reports/latest/tables/full_head_question_catalog.csv
```

These are not just raw metrics. They are different lenses over the same pseudo-head computations.

## What is a pseudo-head here

ParticleNet does not have transformer attention heads. We split channel groups inside EdgeConv blocks into pseudo-heads:

```text
L0_ch0:8
L1_ch16:32
L2_ch128:160
L2_ch224:256
...
```

Each pseudo-head is a channel slice that can be read as a local matrix program:

```text
input particle features
+ KNN neighbor features
+ edge differences
+ learned channel projection
+ nonlinearity / aggregation
+ next layer routing
+ classifier class direction
```

So when we say “head”, we mean:

```text
a learned channel-subspace that reads particle-neighborhood evidence and writes a class-relevant intermediate representation.
```

## What projections/lenses we already compute

For each pseudo-head we can look through several lenses.

### 1. Patch lens

We zero/patch the channel group and measure:

```text
acc_drop
class-specific drop
logit delta
KL
```

This answers:

```text
Does this pseudo-head causally matter?
```

### 2. Weight lens

We inspect which source/input channel blocks and output groups carry module weight energy.

Example phrases from the current tables:

```text
WL2 input/source projection: Input slice 128:160 carries 0.3615 of module weight energy
WL3 output pseudo-head projection: Output group 128:160 carries 0.3887 of module weight energy
```

This answers:

```text
What previous channel programs feed this pseudo-head?
Where does this pseudo-head write its output?
```

### 3. Route lens

For middle heads, we read the route/neighborhood role:

```text
compact/wide KNN route stats -> this pseudo-head
leading-particle route
particle0/core route
```

This answers:

```text
What local particle-neighborhood pattern is this head reading?
```

### 4. Class direction lens

For late heads, we project the channel group into classifier class/contrast directions.

This answers:

```text
Which class logits does this pseudo-head support or suppress?
```

### 5. Particle supertrace lens

We rank particles by super_score and keep particle features:

```text
PID
pT
charge
deltaR
isElectron/isMuon/isPhoton/isChargedHadron
```

This answers:

```text
Which particles are actually used by the network for this event/readout?
```

## Concrete example: L2_ch128:160

`L2_ch128:160` is the clean example for the Hqql/Tbl question.

From class-specific head gradients:

```text
For label_Hqql:
  L2_ch128:160 is rank 1
  abs_grad ~= 1.8701

For label_Tbl:
  top summary also points to L2_ch128:160
  abs_grad ~= 1.5447
```

So this pseudo-head is important for both Hqql and Tbl class evidence.

From the projection/question map:

```text
head_id: L2_ch128:160
role: late aggregation / class-evidence head
question: Does this pseudo-head aggregate higher-level particle-neighborhood evidence before the classifier?
semantic_hint: kinematic/energy, class-specific: label_Hqql, label_Tbl, label_Tbqq
lenses:
  Patch lens: zero EdgeConv L2 ch128:160
  Weight lens: source/input blocks -> output ch128:160
  Class direction lens: this pseudo-head -> classifier class/contrast direction
class effects:
  label_Hqql drop ~= 2.2104
  label_Tbl  drop ~= 2.1597
```

This means:

```text
L2_ch128:160 is not a raw feature reader.
It is a late class-evidence accumulator that receives earlier particle-neighborhood programs and writes into Hqql/Tbl/Tbqq class directions.
```

## Example matrix-program pseudocode

A late head like `L2_ch128:160` can be read as:

```python
# Pseudo-head: L2_ch128:160
# Role: late aggregation / class-evidence head
# Axis: Hqql/Tbl/Tbqq class evidence

for event in batch:
    H = previous_layer_particle_states          # [particles, channels]
    P = particle_features                       # pT, PID, charge, geometry
    G = knn_graph(P)                            # local particle-neighborhood graph

    for particle i:
        nb = G.neighbors(i)

        # read higher-level evidence built by previous heads
        local_context = concat(
            H[i, source_blocks],
            mean(H[nb, source_blocks]),
            max(H[nb, source_blocks]),
            edge_features(i, nb),
        )

        # learned matrix program / projection
        z_i = W_in_to_128_160 @ local_context + b
        z_i = nonlinearity(z_i)

        # write class-evidence slice
        H2[i, 128:160] = z_i

    # aggregation before classifier
    event_vector = aggregate_particles(H2[:, 128:160])

    # class-direction readout
    hqql_score = dot(event_vector, classifier_direction['label_Hqql'])
    tbl_score  = dot(event_vector, classifier_direction['label_Tbl'])

    return hqql_score, tbl_score
```

This is why we can ask directly:

```text
Do confused high-isolation Hqql events activate L2_ch128:160 like Tbl_correct or like protected Hqql?
```

## Earlier/lower-level pseudo-head example

An early head like `L0_ch0:8` is different. It reads raw local geometry/PID evidence:

```python
# Pseudo-head: L0_ch0:8
# Role: early feature / geometry / PID reader

for particle i:
    nb = knn(i)
    local = read(
        pt_energy(i),
        pid_charge(i),
        deltaR(i, nb),
        edge(i, nb),
        pid_charge(nb),
    )

    z_i = W_raw_to_0_8 @ local + b
    z_i = nonlinearity(z_i)

    write_local(z_i, axis='Hqql/Tbl core-confusion or class-relevant local evidence')
```

So the whole network can be read as a stack:

```text
L0 heads:
  raw PID/charge/pT/geometry readers

L1 heads:
  route-composition / learned-neighborhood programs

L2 heads:
  late aggregation / class-evidence programs
```

## What we need to do now

The external analysis has already generated a physical hypothesis:

```text
high isolation creates Tbl-risk
spread lepton-centered KNN geometry is suspicious
second-lepton ambiguity is suspicious
```

Now we should check it inside the model.

Use groups:

```text
A = protected_highiso
    true=Hqql, pred=Hqql, isolation>0.30

B = confused_highiso
    true=Hqql, pred=Tbl, isolation>0.30

C = Tbl_correct
    true=Tbl, pred=Tbl
```

Direct internal question:

```text
For heads like L2_ch128:160, L2_ch160:192, L2_ch224:256:
  Is B closer to C than to A in activation space?
```

If yes:

```text
ParticleNet internally maps confused high-isolation Hqql toward Tbl-like class-evidence space.
```

If no:

```text
ParticleNet may simply lose Hqql evidence without forming true Tbl evidence.
```

## Specific tables we still need

Current supertrace tables already provide:

```text
head priority
class-specific gradients
projection/question maps
particle supertrace
semantic pseudocode
```

But for the direct A/B/C proof we still need one additional table:

```text
event_idx, group, head_id, layer, channels, activation_mean, activation_max, activation_norm, top_particle_idx, top_particle_activation
```

Preferably also:

```text
event_idx, group, head_id, particle_idx, particle_activation, PID, pT, charge, deltaR
```

This should be extracted only for A/B/C events, not for the whole dataset.

## The exact next experiment

```text
INTERNAL_ACTIVATION_CONTRAST_V2
```

Compute per-event/per-head activation summaries for:

```text
A protected_highiso
B confused_highiso
C Tbl_correct
```

Rank heads by:

```text
B_minus_A_effect
B_minus_C_effect
B_closer_to_C_score = distance(B,A) - distance(B,C)
```

Then inspect particle attribution for the top heads.

## What Claude should judge

The important question is no longer whether bins/patches suggest a feature.

The question is:

```text
Which pseudo-head/channel program internally carries the transition from protected Hqql to Tbl-like readout?
```

And for Hqql/Tbl, the first suspects are:

```text
L2_ch128:160  # Hqql/Tbl class-evidence accumulator
L2_ch160:192  # Hqql-relevant late head
L2_ch224:256  # strong global gradient late class-evidence head
L1_ch32:48    # middle route-composition Hqql/Tbl/Tbqq head
L1_ch80:96    # middle route-composition Tbl/Hqql/H4q head
```
