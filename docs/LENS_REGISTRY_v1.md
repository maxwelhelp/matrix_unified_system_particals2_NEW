# Lens Registry v1

This registry defines lenses: explicit questions we ask a trained model.

A lens should be implemented as either:

- a causal patch;
- an attribution/probe;
- a contrast analysis;
- a route statistic;
- a known-observable comparison.

## Lens format

```text
Lens ID:
Question:
Applies to:
Signal measured:
Control:
Current status:
Next implementation:
```

---

## L1 — EdgeConv full-block lens

**Question:** Does this EdgeConv block carry class-separating information?

**Applies to:** ParticleNet `edge_convs[0..2]`.

**Signal:** accuracy/logit/KL drop after zeroing full block output.

**Control:** compare against FC patch and random-like weak patches.

**Status:** implemented.

---

## L2 — EdgeConv pseudo-head lens

**Question:** Does a specific channel group inside EdgeConv behave like an internal head?

**Applies to:** ParticleNet EdgeConv outputs.

**Signal:** accuracy/logit/KL drop after zeroing channel group.

**Control:** random channel groups of same size.

**Status:** implemented as equal channel slices; needs activation-cluster version.

---

## L3 — Activation-cluster pseudo-head lens

**Question:** Are there learned functional channel clusters that are more meaningful than equal slices?

**Applies to:** EdgeConv activations.

**Signal:** cluster patch effect and class specificity.

**Control:** random cluster/channel sets.

**Status:** TODO P0.

---

## L4 — Leading-particle lens

**Question:** Does the model rely on leading particles more than random particles?

**Applies to:** particle subsets.

**Signal:** top-pT / top-energy ablation vs random ablation.

**Control:** random particles, top-k sweep.

**Status:** implemented basic; needs k sweep and per-class table.

---

## L5 — Particle route-width lens

**Question:** Does the learned KNN route use compact or wide neighbor structures by class?

**Applies to:** EdgeConv KNN route.

**Signal:** neighbor ΔR / pT / energy stats by class and layer.

**Control:** route-group causal patch.

**Status:** descriptive implemented; causal route patch TODO.

---

## L6 — Compact/wide route causal lens

**Question:** Are compact or wide neighbor edges causally necessary for class logits?

**Applies to:** EdgeConv routes.

**Signal:** patch/remove compact, wide, top-pT-neighbor, random neighbor routes.

**Control:** random route removal with same count.

**Status:** TODO P0/P1.

---

## L7 — Feature-channel lens

**Question:** Which explicit particle features support each class?

**Applies to:** input feature channels.

**Signal:** per-class logit/accuracy drop after feature-channel zeroing.

**Control:** permutation/noise controls.

**Status:** implemented zeroing; needs permutation/noise.

---

## L8 — Known-observable lens

**Question:** Does the model's learned pattern align with known observables?

**Applies to:** jet-level observables.

**Signal:** class-wise mass, multiplicity, tau variables; contrast with learned route stats.

**Control:** residual analysis after controlling for observables.

**Status:** implemented descriptive; residual TODO.

---

## L9 — Class-contrast lens

**Question:** What differentiates class A from class B?

**Applies to:** selected class pairs.

Current important contrasts:

- `Wqq` vs `Zqq`;
- `Tbqq` vs `Tbl`;
- `Hbb` vs `Hcc`;
- `Hbb` vs `Hgg`;
- `H4q` vs `Hqql`;
- `QCD` vs `Wqq`;
- `QCD` vs `Tbqq`.

**Signal:** route, feature, observable, pseudo-head differences.

**Control:** same lens on heldout samples.

**Status:** partially implemented.

---

## L10 — Error-route lens

**Question:** Why did the model choose the wrong class?

**Applies to:** wrong predictions grouped by true->pred pair.

**Signal:** competing logits, route stats, feature drops.

**Control:** compare to correct examples of true and predicted class.

**Status:** TODO P2.

---

## L11 — Transformer attention lens

**Question:** What question does each attention head ask about particles/tokens?

**Applies to:** ParT or another valid Transformer model.

**Signal:** attention weights, pair bias, head ablation, logit attribution.

**Control:** attention-head patch, random head, feature controls.

**Status:** paused until valid Transformer checkpoint.

---

## L12 — Residual / classifier direction lens

**Question:** Which internal component directly supports class logit directions?

**Applies to:** EdgeConv outputs, FC hidden state, Transformer residual streams later.

**Signal:** component output projected onto class weight/logit direction.

**Control:** signed logit drop after patch.

**Status:** TODO.

---

## L13 — Dataset/heldout stability lens

**Question:** Does the hypothesis remain true on more files or heldout splits?

**Applies to:** all hypotheses.

**Signal:** effect size distribution over different ROOT files.

**Control:** no single-file shortcut.

**Status:** TODO P0.
