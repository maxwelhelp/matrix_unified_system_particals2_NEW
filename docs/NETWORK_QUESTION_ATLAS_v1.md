# Network Question Atlas v1

This document defines the next research layer: treat every model component as a question-asking device.

The goal is not only to say:

> this layer is important

but to infer:

> what question does this component ask about the input, what answer does it produce, and how does that answer affect the final class/logit?

## Core idea

A trained network can be viewed as a set of learned questions.

Examples:

- EdgeConv route question: "Which particles should interact with this particle?"
- EdgeConv channel-head question: "Is there a local high-pt / wide-angle / class-specific structure here?"
- Feature lens question: "Does this class depend on particle energy fraction, relative pt, charge/PID, or geometry?"
- Particle subset lens question: "Is the prediction supported by leading particles, core particles, wide-angle particles, or random/background particles?"
- Observable lens question: "Is the learned signal aligned with known physics observables such as mass, tau variables, or particle multiplicity?"

## Terminology

### Component

A part of the model that can be traced or patched.

For ParticleNet:

- input feature groups;
- particle subsets;
- EdgeConv blocks;
- EdgeConv channel-head groups;
- FC classifier layers;
- KNN route statistics.

For Transformer / ParT later:

- attention heads;
- pair bias;
- MLP neurons/groups;
- residual stream directions;
- class/logit directions.

### Question

A human-readable interpretation of what the component seems to test.

Example:

```text
Component: EdgeConv L1 ch16:32
Question: Is there a learned local particle-neighborhood pattern that supports class separation?
Evidence: zeroing this pseudo-head drops accuracy strongly.
```

### Answer

The component's output or effect on logits.

Example:

```text
Answer: this pseudo-head supports the original predicted class; patching it drops confidence and accuracy.
```

### Lens

A probe or counterfactual view that asks one explicit question of the model.

Examples:

- top-pt particle lens;
- top-energy particle lens;
- wide-angle particle lens;
- feature-channel lens;
- route-width lens;
- known-observable lens;
- error-route lens;
- pseudo-head lens.

## Current ParticleNet question map

The current validated model is:

```text
ParticleNet_kinpid.pt
JetClass tiny balanced subset
baseline accuracy around 0.757
```

Current strongest component questions:

### Q1 — EdgeConv learned-neighborhood separator

**Question:** Does the model separate classes using dynamic particle-neighbor message passing?

**Current answer:** yes, strongly. EdgeConv blocks and pseudo-head groups have large causal effects.

**Evidence:** EdgeConv pseudo-head `L1:ch16:32` and full EdgeConv patches strongly reduce accuracy.

**Status:** causal-patched, needs activation-cluster refinement.

### Q2 — EdgeConv pseudo-head specialization

**Question:** Are there internal channel groups behaving like heads?

**Current answer:** yes, likely. Equal channel slices already reveal strong groups.

**Current candidate heads:**

- `L1:ch16:32`
- `L2:ch224:256`
- `L0:ch40:48`
- `L1:ch112:128`
- `L0:ch24:32`

**Status:** causal-patched, but fixed slices should be replaced by activation clusters.

### Q3 — Leading-particle core

**Question:** Does the model rely on leading high-pt/high-energy particles more than random particles?

**Current answer:** yes.

**Evidence:** top-pt ablation is much more damaging than random particle ablation.

**Status:** causal-patched, needs top-k sweep and per-class breakdown.

### Q4 — Route width / jet structure

**Question:** Does the learned KNN route width differ by class?

**Current answer:** yes descriptively.

**Current pattern:** `Wqq` has compact routes, `Tbqq` has wide routes.

**Status:** observed, needs causal route-group patch and heldout stability.

### Q5 — Explicit feature-channel class codes

**Question:** Which explicit particle feature does each class rely on?

**Current answer:** different classes depend on different features.

Examples:

- `Wqq/Zqq` depend strongly on `part_logptrel`;
- `Tbqq` depends strongly on `part_deltaR`;
- `Hbb/Hcc` depend strongly on `part_logerel`;
- `Hqql` depends strongly on `part_pt_log`.

**Status:** causal-patched but needs permutation/noise controls.

### Q6 — Known-observable alignment

**Question:** Are learned route patterns aligned with known observables?

**Current answer:** partly yes.

Example:

- `Tbqq` has wider routes, higher mass, and more particles than `Tbl/Wqq`.

**Status:** observed, needs residual analysis.

### Q7 — Error-route question

**Question:** Do wrong predictions happen because the jet asks/answers questions like another class?

**Current answer:** not tested yet.

**Next:** build error atlas true->pred pairs.

### Q8 — Transformer attention question map

**Question:** Do real attention heads in a valid Transformer particle model ask similar route/interaction questions?

**Current answer:** paused.

**Reason:** current ParT checkpoint invocation is not valid for claims.

## Research rule

A question is accepted into the atlas only if it has:

1. a component or lens;
2. a measured answer/effect;
3. causal/control evidence;
4. a risk note;
5. a next validation step.

## Next implementation

`PARTICLENET_QUESTION_ATLAS_V1.md` should be auto-generated from latest CSV/JSON outputs and include:

- component id;
- question;
- answer/effect;
- evidence source;
- confidence;
- risk;
- next lens/test.
