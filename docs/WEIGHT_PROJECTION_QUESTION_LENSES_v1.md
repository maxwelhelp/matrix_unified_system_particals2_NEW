# Weight Projection Question Lenses v1

This document fixes the idea that the network can be inspected by projecting weights onto explicit question lenses.

The previous question atlas mostly used activations and causal patches. This document adds the missing layer:

> weights are also answers to learned questions, and we can ask those questions by projecting weight matrices/tensors onto lens bases, masks, feature groups, pseudo-head groups, class directions, and combinations of them.

## Core idea

For a weight tensor `W`, a lens `P` is a structured direction or mask that represents a question.

A projection score answers:

```text
How much of W lies in the question direction P?
```

Conceptually:

```text
score(W, P) = <W, P> / (||W|| ||P||)
```

For masks/groups:

```text
energy(W, mask) = ||W * mask|| / ||W||
```

The question is not only a single projection. It can be a combination:

```text
feature group -> pseudo-head group
pseudo-head group -> class logit
route group -> feature group
feature A + feature B -> output group
head A + head B -> same class direction
```

So a real question can be made of two or more elements.

## Examples of projection questions

### Single-element question

```text
Does this layer strongly use particle geometry channels?
```

Projection/mask:

```text
input channels = part_deta, part_dphi
```

### Two-element question

```text
Does EdgeConv pseudo-head L1:ch16:32 read geometry channels?
```

Projection/mask:

```text
output channels = ch16:32
input channels = part_deta, part_dphi
```

### Three-element question

```text
Does a pseudo-head that reads geometry also support Wqq-vs-Tbqq class separation?
```

Projection/mask chain:

```text
input geometry -> EdgeConv pseudo-head -> classifier Wqq/Tbqq direction
```

### Multi-head combination question

```text
Do two pseudo-heads jointly ask the same route-width question?
```

Projection combination:

```text
P = P_head_A + P_head_B
or
P = block(head_A, feature_group_X) + block(head_B, feature_group_Y)
```

## Projection lens types

### WL1 — Weight norm / energy lens

Question:

```text
Which layers/components carry the largest raw weight energy?
```

Use:

- sanity check;
- identify important modules;
- compare with causal patch effects.

Risk:

- high weight norm does not guarantee causal effect.

### WL2 — Input feature projection lens

Question:

```text
Which explicit input features does this component read?
```

Examples:

- `part_pt_log`
- `part_e_log`
- `part_logptrel`
- `part_logerel`
- `part_deltaR`
- `PID/charge`
- `deta/dphi`

### WL3 — Output pseudo-head projection lens

Question:

```text
Which output channel groups behave like internal heads?
```

For ParticleNet:

- EdgeConv output channel groups.

For Transformers:

- attention heads / MLP groups.

### WL4 — Block interaction projection lens

Question:

```text
Which input group feeds which output pseudo-head?
```

This is the first real combined question:

```text
input group X -> output group Y
```

### WL5 — Class direction lens

Question:

```text
Which hidden groups project into which class logit directions?
```

For classifier weights:

```text
hidden channel group -> class logit
```

### WL6 — Pair / contrast class lens

Question:

```text
Which hidden groups support class A over class B?
```

Projection direction:

```text
W_class_A - W_class_B
```

Important contrasts:

- `Wqq` vs `Zqq`
- `Tbqq` vs `Tbl`
- `Hbb` vs `Hcc`
- `Hbb` vs `Hgg`
- `QCD` vs `Wqq`
- `QCD` vs `Tbqq`

### WL7 — Multi-lens composition

Question:

```text
Does the same component answer multiple questions at once?
```

Examples:

```text
geometry + top-pT
PID + energy fraction
route-width + class contrast
pseudo-head A + pseudo-head B
```

### WL8 — Weight-vs-activation consistency lens

Question:

```text
Does a weight projection question match activation/patch evidence?
```

Example:

```text
weight projection says L1:ch16:32 reads geometry;
patch says L1:ch16:32 is causal;
route stats show class-specific neighbor width.
```

This is stronger than weight-only or activation-only evidence.

## Evidence rule

A weight projection question is not accepted as a strong hypothesis alone.

Evidence levels:

1. `WEIGHT_ONLY`: projection is strong but no causal evidence.
2. `WEIGHT_PLUS_PATCH`: projection aligns with causal patch.
3. `WEIGHT_PLUS_ACTIVATION`: projection aligns with activation/route stats.
4. `TRIANGULATED`: weight projection + activation/route + causal patch + control.

## Current implementation target

`particlenet_weight_projection_question_lenses_v1.py` should produce:

- per-module weight energy;
- output pseudo-head energy;
- input/source group energy;
- block interaction energy `input group -> output group`;
- classifier class and contrast projection;
- a natural-language question for every high-scoring projection.

## Why this matters

This turns the analysis from:

```text
Layer X is important.
```

into:

```text
Layer X / pseudo-head Y seems to ask:
'Is this particle-neighborhood pattern using geometry + relative pT evidence for W/Z/top class separation?'
```

That is the map of network questions we want to maintain.
