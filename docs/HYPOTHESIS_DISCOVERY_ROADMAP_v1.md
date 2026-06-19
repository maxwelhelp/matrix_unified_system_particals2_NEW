# Hypothesis Discovery Roadmap v1

Goal: turn the particle atlas into a hypothesis engine, not just a debug report.

## Current validated model

`ParticleNet_kinpid.pt` is currently the validated model:

- official Weaver prediction is good (~0.766 accuracy on the balanced tiny subset);
- direct local loader is good (~0.757 accuracy);
- labels and ROOT data are validated;
- causal patches work.

`ParT_*` is currently not valid for explanation because direct official prediction is ~0.10 accuracy. Do not use ParT attention claims as scientific evidence until a valid ParT checkpoint/invocation is found.

## What “all layers” means for ParticleNet

ParticleNet has no Transformer attention. Its attention-like mechanism is dynamic graph message passing:

1. `pf_points`: geometry coordinates, usually `(part_deta, part_dphi)`.
2. `edge_convs[0]`: first dynamic KNN graph + local message transform.
3. `edge_convs[1]`: second dynamic graph over learned features.
4. `edge_convs[2]`: third dynamic graph over learned features.
5. `fc[0]`: classifier hidden layer.
6. `fc[1]`: classifier output logits.

So for ParticleNet we should trace:

- input groups: kinematics, PID/charge, coordinates;
- particle groups: top-pt, top-energy, high-deltaR particles;
- every EdgeConv block;
- classifier FC layers;
- per-class effects, not just global average.

## What “attention” means here

For ParticleNet, the analogue of attention is not softmax attention; it is KNN edge selection and EdgeConv message passing. We should call it:

- dynamic graph routing;
- particle-neighbor message passing;
- KNN edge causal map.

For real attention analysis, use ParT or another valid Transformer model only after baseline accuracy is validated. Required before claims:

1. valid checkpoint accuracy;
2. attention score / pair bias extraction;
3. pair_embed and attention-head patch;
4. per-class and per-example logit attribution;
5. controls: feature-only, geometry-only, random particles, top-particle ablation.

## Hypothesis criteria

A hypothesis is accepted only if it passes:

1. baseline accuracy is valid;
2. causal patch effect is large and stable;
3. per-class effect is interpretable;
4. example-level signed logit drops agree with global effect;
5. control patches do not explain the same effect trivially.

Example hypotheses we can test:

- Hbb/Hcc rely more on PID/charge features than W/Z.
- W/Z/H4q rely more on geometry/kinematic graph structure.
- Top classes rely on high-energy/top-pt particle subsets.
- EdgeConv layer 1 is the main class-separating stage.
- Coordinates `(deta,dphi)` are more important than raw point-zero suggests because EdgeConv uses them for KNN routing.

## Next outputs

`PARTICLENET_HYPOTHESIS_ATLAS_V3.md` should include:

- baseline;
- global causal ranking;
- per-class patch table;
- per-feature channel table;
- particle-group ablation table;
- example-level signed logit drops;
- a short auto-generated list of candidate hypotheses.
