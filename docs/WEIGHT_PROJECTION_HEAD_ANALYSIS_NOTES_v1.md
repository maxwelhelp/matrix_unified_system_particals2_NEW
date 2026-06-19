# Weight Projection Head Analysis Notes v1

This document records the interpretation step the user asked for: do not just list projection scores, but reason like we did for Qwen heads — combine projection elements until the question becomes logical.

## Core correction

We are not only asking activation/patch questions.

We are asking **weight-projection questions**:

```text
What question is written into this head/layer's weights?
```

A good head question usually has multiple elements:

```text
source feature / hidden source
    -> pseudo-head / output channel group
        -> route/activation behavior
            -> class or contrast direction
```

So the question is not just:

```text
Does this head matter?
```

It is:

```text
Which evidence does this head read, what internal answer does it compute, and which class/contrast does that answer support?
```

## Current evidence available

Current validated model:

```text
ParticleNet_kinpid.pt
baseline accuracy ~= 0.757
```

Current reports:

- `PARTICLENET_RESEARCH_COMPASS_V5.md`
- `PARTICLENET_RESEARCH_SYNTHESIS_V6.md`
- `PARTICLENET_WEIGHT_PROJECTION_QUESTIONS_V1.md`
- `research_edge_channel_heads.csv`
- `weight_projection_questions.csv`

The weight projection scan found:

1. many two-element projection questions: source/input slices feeding output pseudo-head groups;
2. physical feature projections in early modules;
3. classifier contrast directions such as Wqq-vs-Zqq and Tbqq-vs-Tbl.

## Manual example: EdgeConv L1 ch16:32

### Raw causal evidence

Component:

```text
EdgeConv layer 1, output channels 16:32
```

Patch result:

```text
baseline accuracy: 0.7574
patched accuracy:  0.4934
delta_pred_logit:  9.1146
KL:                1.2543
top1_match:        0.5328
```

This is the strongest current pseudo-head group.

### What question might this head ask?

Layer 1 is not the first feature-reading layer and not the final classifier. It is the middle learned-neighborhood stage.

So the likely question is not simply:

```text
Is there PID?
```

or:

```text
Is there high pT?
```

A better hypothesis is:

```text
Does this jet contain a learned particle-neighborhood pattern, built from earlier feature evidence, that supports class separation?
```

Because v4/v5 already showed:

- EdgeConv routes differ by class;
- Wqq tends to compact routes;
- Tbqq tends to wide routes;
- leading particles matter;
- explicit features matter, but EdgeConv is the main causal mechanism.

### Candidate composite lenses for L1 ch16:32

The logical projections to test are:

#### Lens A — hidden-source to pseudo-head

```text
EdgeConv0 hidden source groups -> EdgeConv1 ch16:32
```

Question:

```text
Which previous learned features feed this strong middle pseudo-head?
```

Why:

Layer 1 reads learned features, not raw particle channels directly.

#### Lens B — route-width to pseudo-head

```text
compact/wide KNN route evidence -> EdgeConv1 ch16:32
```

Question:

```text
Is L1 ch16:32 the pseudo-head that converts route width into class evidence?
```

Why:

Route stats show Wqq compact vs Tbqq wide, and L1 is the strongest pseudo-head.

#### Lens C — leading-particle to pseudo-head

```text
top-pT/top-energy particle subset -> EdgeConv1 ch16:32
```

Question:

```text
Does L1 ch16:32 specialize in leading-particle core evidence?
```

Why:

Top-pT ablation is much stronger than random ablation.

#### Lens D — pseudo-head to class contrast

```text
EdgeConv1 ch16:32 -> classifier contrast direction
```

Important contrasts:

```text
Wqq vs Zqq
Tbqq vs Tbl
QCD vs Wqq
QCD vs Tbqq
```

Question:

```text
Which class decision does this pseudo-head support?
```

### Current best interpretation

Current best wording:

> EdgeConv L1 ch16:32 appears to be a high-level learned-neighborhood pseudo-head. It likely combines earlier feature evidence and dynamic particle-neighbor structure into a class-separating signal. The next projection should test whether it is specifically a route-width / leading-particle / W-vs-top contrast head.

Confidence:

```text
causal importance: high
specific semantic interpretation: medium/low until head-aligned projection and activation-cluster tests
```

## What to do for all heads

For every EdgeConv pseudo-head group:

1. attach causal patch evidence;
2. attach weight-projection rows that overlap the same layer/channel group;
3. infer likely source question:
   - early raw feature/PID/geometry;
   - hidden source group;
   - route width;
   - leading particle;
   - classifier contrast;
4. write a human question;
5. write next lens to validate.

This is automated by:

```text
tools/particlenet_head_projection_composer_v2.py
scripts/RUN_PARTICLENET_HEAD_PROJECTION_COMPOSER_V2.sh
```

## Important limitation

The current v1 weight scan is useful but still coarse:

- equal channel groups are not learned clusters;
- flat input slices may not correspond to semantic features in deeper layers;
- weight projection alone is not causal.

A strong claim requires triangulation:

```text
weight projection + activation/route stats + causal patch + control
```
