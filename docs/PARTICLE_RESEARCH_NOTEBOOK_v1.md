# Particle Research Notebook v1

This document is the working research notebook for the particle-direction of the matrix pseudocode / causal atlas project.

## Core goal

Use trained particle classifiers as hypothesis generators:

1. validate that the model really predicts the physics task;
2. decompose the model into causal components;
3. identify what particle interactions / jet-substructure patterns the model relies on;
4. convert those patterns into explicit candidate hypotheses;
5. validate those hypotheses with controls, heldout data, and known observables.

We do **not** claim discovery from a neural-network attribution alone. We claim candidate mechanisms and candidate hypotheses that require validation.

## Current validated model

Validated now:

- `ParticleNet_kinpid.pt`
- JetClass tiny balanced ROOT subset
- direct local loader accuracy around `0.757`
- official Weaver ParticleNet accuracy around `0.767`

Paused / invalid for evidence now:

- `ParT_*` direct attention claims, because current ParT checkpoint invocation gives around random accuracy.

## Meaning of “heads” in this repo

For Transformer models:

- head = attention head.

For ParticleNet:

- there is no softmax attention head;
- the closest analogue is an EdgeConv dynamic graph route plus channel groups inside EdgeConv outputs.

So in ParticleNet reports:

- `edge_conv[0..2]` = dynamic graph message-passing stages;
- `edge_conv channel-head groups` = channel slices inside EdgeConv output, patched like pseudo-heads;
- `KNN route` = particle-to-neighbor routing analogue of token-to-token attention.

## Current strongest observations

From current v3/v4 reports:

1. `edge_conv[1]` and `edge_conv[0]` are dominant causal components.
2. Removing all particle features drops the model close to random.
3. `deta/dphi`, kinematic log features, and PID/charge are all important, but in different ways.
4. Removing top-pt / top-energy particles is much more damaging than random particle removal.
5. KNN route stats show class-specific neighbor width: `Wqq` routes are compact, `Tbqq` routes are wide.

## Candidate hypothesis families

### H1 — Learned-neighborhood separator

ParticleNet separates jet classes mainly through learned dynamic particle-neighbor message passing, especially `edge_conv[1]`, not through final classifier weights alone.

Evidence required:

- EdgeConv patch drops accuracy;
- EdgeConv channel-head group patch identifies compact subcomponents;
- class-specific route stats differ;
- heldout stability.

### H2 — Leading-particle core hypothesis

The classifier relies strongly on leading high-pt / high-energy particles. This is supported if top-pt/top-energy ablation is much stronger than random ablation.

Evidence required:

- top-pt and top-energy ablations outperform random controls;
- effect is stable across ROOT files;
- comparison with jet mass / tau variables.

### H3 — Compact Wqq vs wide top-like route hypothesis

`Wqq` appears to use more compact neighbor routes, while `Tbqq` appears to use wider particle-neighbor neighborhoods.

Evidence required:

- route ΔR stats stable across EdgeConv layers;
- heldout check on more files;
- contrast table Wqq vs Zqq vs top classes;
- route-group causal patch, not only descriptive stats.

### H4 — Explicit-feature vs route interaction hypothesis

The model likely combines explicit particle features and dynamic graph routes. If feature ablation and route statistics both affect the same class, the model may use an interaction rather than a single observable shortcut.

Evidence required:

- per-class feature-channel ablation;
- edge channel-head group ablation;
- example-level signed drops;
- known-observable comparison.

## What to write after every run

After each run, append notes with:

```text
Run ID:
Dataset / sample size:
Checkpoint:
Accuracy:
Strongest global component:
Strongest per-class effects:
New candidate hypothesis:
Control that supports it:
Control that weakens it:
Next validation step:
```

## Next required reports

1. `PARTICLENET_RESEARCH_COMPASS_V5.md`
   - EdgeConv channel-head groups.
   - Per-class nontrivial feature map.
   - Known observable comparison.
   - Class contrast table.
   - Hypothesis priority list.

2. Heldout stability report.

3. Route-group causal patch report.

4. Attention-style report after a valid ParT checkpoint is found.
