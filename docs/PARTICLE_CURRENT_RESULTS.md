# Particle Atlas Current Results

## Latest completed step

Dummy Particle Patch Controls v2 completed and pushed.

## What was tested

On a dummy randomly initialized ParticleTransformer:

- pair_embed_zero;
- particle_block_skip;
- cls_block_zero;
- mlp_top_group_zero.

Metrics:

- delta_top_logit;
- KL;
- top1_match.

## Result summary

Strongest dummy effects:

```text
cls_block_zero       delta_top_logit=1.9470  KL=0.4491  top1_match=0.125
particle_block_skip0 delta_top_logit=1.5605  KL=0.9389  top1_match=0.125
particle_block_skip1 delta_top_logit=0.8209  KL=0.6107  top1_match=0.125
```

MLP group patch produced smaller but measurable effects:

```text
mlp_top_group_zero layer1 delta_top_logit=-0.1021 KL=0.0210 top1_match=1.0
mlp_top_group_zero layer0 delta_top_logit=0.0223  KL=0.0536 top1_match=0.75
```

Pair bias zero had near-zero dummy effect:

```text
pair_embed_zero delta_top_logit=-0.0064 KL=1.574e-04 top1_match=1.0
```

This is expected on a random dummy model. PairEmbed importance must be judged on trained ParT / real jets, not dummy random weights.

## Interpretation

The adapter and patch hooks are now real, not just a plan:

- class-token block control works;
- particle block control works;
- MLP group control works;
- pair-bias hook is wired, but dummy effect is small;
- class-logit metrics are computed.

## Current status

Done:

- dummy ParT forward;
- adapter coverage for Embed / PairEmbed / blocks / cls_blocks / classifier;
- dummy patch controls;
- lightweight GitHub reporting.

Next:

1. implement real ParT loader;
2. load official or local pretrained checkpoint;
3. run same patch controls on real jets or realistic batches;
4. add JetClass tiny loader;
5. build WHY_CLASS_REPORT;
6. mine repeated class-specific mechanisms.

## Next success criterion

On a trained model or real checkpoint:

- pair_embed_zero should show meaningful effect for at least some jets/classes;
- particle block patch should alter class logits;
- cls_block patch should alter class logits;
- MLP group patch should alter class logits;
- WHY_CLASS_REPORT should explain one predicted class.
