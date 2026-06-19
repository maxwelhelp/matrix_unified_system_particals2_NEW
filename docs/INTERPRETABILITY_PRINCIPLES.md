# Interpretability principles for this project

This project must not be reduced to standard attention visualization.

The goal is a real computation decoder:

```text
valid model contract
→ real prediction accuracy
→ head/layer trace
→ role/path computation
→ matrix/pseudocode rule
→ control/ablation validation
→ physics-facing explanation
```

## Hard rules

1. Do not trust reports made before `PART_SANITY_CONTRACT.md` is `CONTRACT_OK`.
2. Do not use fake `SimpleNamespace` model contracts as evidence.
3. Do not call a plot or attention heatmap an explanation.
4. Every interpretation must carry provenance:
   - model/checkpoint
   - data config
   - class group
   - layer/module
   - head
   - query role
   - key role
   - score/margin
   - control status
5. A pseudocode rule is valid only if it is tied back to real traced events and real model predictions.
6. Standard methods can be used as tools, but the final object is not a standard method. The final object is a readable computation program.

## What counts as a decoded rule

A decoded rule should look like this:

```text
RULE R001
WHEN group = B_Hqql_to_Tbl
AND head = mod.blocks.7.attn#4
AND route = electron <- muon
AND route_strength_B_minus_A is high
THEN this head contributes to Hqql becoming Tbl-like
PROVENANCE: real-contract ParT_kinpid, JetClass_kinpid, 1024 traced events
CONTROL: pad-free / ablation / class-contrast status
```

## What does not count

These are not enough:

```text
attention heatmap
feature importance plot
pretty embedding picture
generic SHAP/LIME explanation
one class-accuracy table without head/layer provenance
```

## Current valid base

The current valid base is:

```text
model: ParT_kinpid.pt
config: JetClass_kinpid.yaml
prediction: official Weaver prediction ROOT symlinks
accuracy: non-collapsed analyzer output
supertrace: PART_ATTENTION_SUPERTRACE_REAL_CONTRACT_V1
physics interpreter: PART_SUPERTRACE_PHYSICS_INTERPRETER_V1
```

Older reports can be useful as ideas, but they must be re-run or re-validated against the current real contract before being treated as evidence.
