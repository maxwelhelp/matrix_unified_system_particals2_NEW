# Particle Transformer Matrix-Pseudocode Atlas Plan

This is the edited project plan for adapting the Qwen matrix-pseudocode atlas to particle-physics transformer models.

## 1. Goal

Build a causal interpretation and hypothesis-mining system for particle-physics transformer models.

The system should explain not only the predicted jet class, but also which particles, particle pairs, kinematic relations, attention heads, MLP channels, and residual/write paths causally move the class logits.

Pipeline:

```text
jet / event / particle cloud
  -> trained transformer model
  -> static matrix atlas
  -> runtime trace on real jets
  -> term/head/particle/pair/MLP patch controls
  -> class-logit attribution
  -> repeated mechanism mining
  -> physics hypothesis candidates
```

Important: this is not automatic discovery of new particles. It is a system for producing candidate mechanisms that require independent validation.

## 2. First target

Primary target: Particle Transformer / ParT for jet tagging on JetClass.

Why ParT first:

1. transformer architecture;
2. particles inside a jet can be treated as tokens;
3. public code / pretrained models / JetClass pipeline exist;
4. attention includes pairwise particle interactions;
5. JetClass is large enough for route and mechanism mining.

## 3. Mapping from LLM to particles

```text
LLM tokens        -> particles / jet constituents
text token type   -> particle type / charge / pT rank / detector feature
attention read    -> particle-to-particle interaction
VO payload        -> information transferred from source particle
lm_head logits    -> jet class logits
next-token trace  -> class-prediction trace
```

## 4. Dataset plan

Use JetClass in stages:

```text
Phase A: 10k jets  - smoke test and atlas debug
Phase B: 100k jets - stable route statistics
Phase C: 1M jets   - serious mechanism mining
Phase D: larger subset/full data only after pipeline is stable
```

Keep in trace:

```text
pT, eta, phi, mass/energy, charge, particle ID/type,
impact/displacement features if present,
particle index / pT rank,
pairwise deltaR,
pairwise invariant-mass proxy.
```

## 5. What to interpret

For each jet and class:

```text
class logit =
    attention head contributions
  + MLP channel/group contributions
  + particle-pair interaction contributions
  + global/event feature contributions
```

For each attention head:

```text
score_ij = const_delta
         + q_affine_i_delta
         + k_affine_j_delta
         + content_bilinear(i, j)
         + pairwise / geometry terms

A_ij = softmax(score_ij)
payload_j = VO_linear(x_j) + VO_bias
Y_i = sum_j A_ij payload_j
```

For MLP/SwiGLU/FFN:

```text
gate = W_gate x + b_gate
up   = W_up x + b_up
h    = activation(gate) * up
out  = W_down h + b_down
```

## 6. Required modes

### Static atlas

Only weights:

- Wq/Wk/Wv/Wo slices;
- QK affine/content split;
- VO linear/bias split;
- rank profiles;
- head type map;
- cross-layer transitions.

### Runtime atlas

On real jets:

- X/Q/K/V;
- scores;
- attention A;
- A@V;
- O/write output;
- MLP gate/up/down;
- class logits.

### Particle-aware routes

Candidate route labels:

- high_pT_core_read;
- local_deltaR_read;
- same_particle_type_read;
- charged_to_neutral_read;
- wide_angle_read;
- two_prong_candidate;
- three_prong_candidate;
- b_like_displaced_read;
- soft_radiation_read;
- pileup_like_read.

### Patch controls

Patch modes:

- remove content_bilinear;
- remove q_affine / k_affine / constant;
- remove VO_bias / VO_linear;
- ablate head;
- ablate route;
- ablate particle group;
- ablate pairwise edge group;
- ablate MLP group.

Metrics:

- class logit delta;
- probability delta;
- cross-entropy delta;
- top1 class match;
- A_rel;
- Y_delta_rel;
- class-specific effect.

### Causal paths

Search paths:

```text
head A -> residual direction -> head B
head -> MLP group -> class logit
particle pair route -> class logit
```

## 7. Hypothesis mining

A candidate mechanism should look like:

```text
For jets predicted as class C, mechanism M repeatedly activates
particle group / pair / route / head / MLP channel,
and causal patching changes class-C logit.
```

A strong hypothesis requires:

1. repeats on heldout jets;
2. class-specific enrichment;
3. causal patch effect;
4. counterfactual robustness;
5. control for pT, eta, particle count;
6. physics-readable description.

## 8. Counterfactual tests

- remove top-read particles;
- remove low-pT radiation;
- remove charged/neutral particles only;
- remove suspected pair;
- shuffle particle IDs while keeping kinematics;
- shuffle pT ranks while keeping particle types;
- preserve pT spectrum but destroy angular structure;
- preserve deltaR but destroy particle type;
- compare target class vs unrelated classes;
- compare trained vs randomized/fine-tuned checkpoints.

## 9. Implementation phases

Phase 0: setup

- clone ParT repo;
- load pretrained ParT;
- load JetClass small subset;
- confirm baseline accuracy on subset.

Phase 1: adapter

- implement `adapters/part_adapter.py`;
- expose layers/attention/qkv/o/mlp/classifier/pair-bias hooks.

Phase 2: static atlas

- QK/VO split;
- head rank/type map;
- pairwise term inventory.

Phase 3: runtime atlas

- reconstruct scores/A/Y/logits on 10k jets;
- route summaries.

Phase 4: patch/control

- head/term/particle/pair/MLP ablations;
- class-logit effects.

Phase 5: causal paths

- head -> head;
- head -> MLP;
- MLP -> class logit;
- pair route -> class logit.

Phase 6: hypothesis mining

- run 100k-1M jets;
- rank repeated mechanisms;
- produce candidate table.

Phase 7: validation

- heldout jets;
- counterfactual jets;
- scrambling controls;
- cross-model checks.

## 10. Deliverables

- `particle_static_atlas_v1.py`;
- `particle_runtime_trace_v1.py`;
- `particle_patch_controls_v1.py`;
- `particle_hypothesis_mining_v1.py`;
- `WHY_CLASS_REPORT.md`;
- `PARTICLE_PAIR_MECHANISM_REPORT.md`;
- `HYPOTHESIS_CANDIDATES.md`;
- CSV/JSON summaries.
