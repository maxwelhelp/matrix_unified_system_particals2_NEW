# PART_MIGRATION_PLAN_V1

## Decision

Next particle-physics architecture:

```text
Particle Transformer / ParT
repository: jet-universe/particle_transformer
```

Why ParT first:

```text
ParticleNet -> ParT is the lowest-risk migration.
JetClass stays the same.
A/B/C confusion pipeline stays the same.
Pseudo-head channel slices become real attention heads.
Pairwise particle-interaction bias makes physical interpretation cleaner.
```

## Claim boundary

ParT on JetClass is still a supervised tagger.

Correct claim:

```text
interpretable tagger mechanism
implicit observable / topology degeneracy
failure mode / robustness improvement
```

Incorrect claim:

```text
new particle
new interaction
physics beyond simulated distribution
```

For real discovery-style work later, use ParT as a backbone with weak supervision / anomaly detection / self-supervised objective, or move to OmniJet / masked-particle modeling.

## Why ParT helps our interpreter

ParticleNet required reverse engineering:

```text
KNN aggregation
EdgeConv Conv/BN/ReLU
pseudo-head channel slices
```

ParT exposes a cleaner path:

```text
particle_i, particle_j
-> pairwise feature / pairwise bias
-> attention score
-> attention probability
-> value flow
-> class direction
```

So the matrix program becomes:

```text
PAIR_FEATURE(i,j)
-> PAIRWISE_BIAS_HEAD(i,j)
-> QK_SCORE_HEAD(i,j)
-> ATTENTION_WEIGHT_HEAD(i,j)
-> VALUE_FLOW(j -> i)
-> CLASS_DIRECTION
```

## Phase 0 — bootstrap only

Do not train first.

First tasks:

```text
1. clone ParT repo into external/particle_transformer
2. check Python imports
3. locate model definition files
4. locate config/checkpoint files if present
5. create local report
```

Output:

```text
reports/latest/PART_BOOTSTRAP_PROBE_V1.md
manifests/latest/part_bootstrap_probe_v1.json
```

## Phase 1 — inference only

Goal:

```text
load pretrained ParT checkpoint
run logits on jetclass_tiny_balanced
rebuild Hqql/Tbl confusion groups A/B/C
```

No training yet.

## Phase 2 — attention trace

For A/B/C events export:

```text
attention_scores
pairwise_bias
attention_probs
value_norm
class contribution
top particle pairs
```

Output:

```text
reports/latest/PART_INTERPRETER_V1.md
reports/latest/tables/part_attention_heads.csv
reports/latest/tables/part_particle_pair_flows.csv
reports/latest/tables/part_top_confusion_paths.csv
```

## Phase 3 — compare with ParticleNet

Check whether ParT reproduces the ParticleNet mechanism:

```text
ParticleNet finding:
  lower/mid hadron/photon-neighborhood target-risk flow
  weakened Hqql evidence in later heads
  B is anomalous third-topology, not normal Tbl

ParT test:
  do attention heads directly attend to the same pairwise geometry?
  lepton-hard_hadron?
  photon-neighbor?
  core/hadron neighborhood?
```

If both architectures find the same physical regime, the claim becomes stronger:

```text
architecture-independent tagger-confusion topology / candidate explicit observable
```

## Later path to discovery-style work

After ParT works:

```text
ParT backbone + CWoLa / weak supervision
ParT/OmniJet self-supervised masked-particle modeling
real-data anomaly detection with SM background comparison
```

But the immediate target is ParT interpretability on JetClass, not new physics claims.
