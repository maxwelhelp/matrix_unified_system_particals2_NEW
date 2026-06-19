# Head Output Interpretation v1

The pseudocode layer must be validated against real pseudo-head outputs.

Current layers:

```text
semantic pseudocode -> code alignment -> output trace
```

## Why output trace matters

A pseudo-head row should not only say what the head may compute. It should also describe what the head actually writes:

```text
activation strength
which classes activate it
which particles activate it
whether the top activated particle is particle0 / leading-pT / top-k
which logits it correlates with
what it passes to the next layer
```

## Correct ParticleNet pseudo-head outputs

```text
L0_ch*: slice of edge_convs.0 output [B, 64, N]
L1_ch*: slice of edge_convs.1 output [B, 128, N]
L2_ch*: slice of edge_convs.2 output [B, 256, N]
```

These are post-EdgeConv per-particle tensors, before final pooling/classifier.

## Required interpretation fields

```text
head_id
layer/channels
output_shape
activation_mean_abs
activation_max
sparsity_like
particle0_top_rate
top_activation_matches_leading_pt_rate
class_with_highest_activation
class_activation_contrast
logit_correlation_top_class
semantic_pseudocode
output_interpretation
```

## Meaning

This bridges from semantic pseudocode to actual computation:

```text
what the head says it computes
+
where in code it lives
+
what its output tensor actually does
```
