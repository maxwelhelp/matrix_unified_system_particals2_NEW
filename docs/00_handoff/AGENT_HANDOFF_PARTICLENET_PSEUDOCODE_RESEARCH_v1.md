# Agent Handoff — ParticleNet Pseudocode / Mechanistic Research v1

This handoff tells the next agent what has already been done, where the evidence lives, what is currently believed, and what to implement next.

## Repository

```text
repo: maxwelhelp/matrix_unified_system_particals
branch: main
main local path used by user: ~/Рабочий стол/matrix_unified_system_particals
main data path: ~/Рабочий стол/jetclass_tiny_balanced
checkpoint: local_checkpoints/part/ParticleNet_kinpid.pt
mode: kinpid
```

## Core project idea

The project is not just saliency/feature importance. The goal is a **pseudocode interpretation layer** for ParticleNet:

```text
raw particles
  -> KNN / EdgeConv local graph operations
  -> pseudo-head channel groups
  -> per-particle output tensors
  -> class evidence / logits
  -> evidence-grounded pseudocode
```

The important differentiator is to extract readable semantic pseudocode for pseudo-head groups, then tie it to:

```text
1. real model code/layer path
2. real output tensors
3. controls/ablations
4. residual tests
5. class-specific behavior
6. KNN/EdgeConv inner traces
```

## Strongest evidence chain so far

Current evidence chain:

```text
stream suggested particle0/core dominance
-> particle0/top-k targeted controls confirmed local causality
-> order control reduced literal index/order artifact
-> confusion atlas showed structured class collapse
-> known-observable residual v1 found simple surrogate insufficient
-> pseudocode v2 linked semantic pseudocode + code alignment + output trace
-> question-driven analyzer ranked heads per research question
-> EdgeConv inner trace inspected selected heads inside EdgeConv outputs/KNN context
```

## Main current interpretation

Best working model:

```text
L0: early local feature builders over particles/neighbors, often not particle0
L1: middle context relays, also mostly not literal particle0
L2: late class-evidence readout, often core/particle0/leading-pT aligned
```

This means ParticleNet likely builds local/neighbor context first and then reads class evidence through core/top-k particles late in the network.

## Important: scope discipline

Do not overclaim.

Allowed:

```text
particle0/top-k is locally causal in the matched control run;
array-index artifact is reduced by order control;
simple known-observable surrogate v1 does not reproduce ParticleNet decisions;
pseudocode is semantic and evidence-grounded, not literal source code.
```

Not allowed:

```text
we discovered a new particle;
local control delta is a global stream trend;
known-observable proxy is fully rejected for all richer features;
pseudocode is exact source code.
```

## Key reports to read first

### 1. Question-driven stage analyzer

```text
reports/latest/QUESTION_DRIVEN_STAGE_ANALYZER_V1.md
reports/latest/tables/question_driven_stage_answers.csv
reports/latest/tables/question_driven_head_rankings.csv
```

This is the first dashboard to open. It answers:

```text
Q1: Where is late particle0/core readout?
Q2: What do L0/L1 compute before L2?
Q3: Is Hqql/Tbl residual axis explained by simple observables?
Q4: Which heads should be inspected inside EdgeConv next?
Q5: What is the full current evidence chain?
```

### 2. Pseudocode operation database v2

```text
reports/latest/PSEUDOCODE_OPERATION_DATABASE_V2.md
reports/latest/tables/pseudocode_operation_database_v2.csv
reports/latest/tables/pseudocode_operation_database_v2.jsonl
```

This merges:

```text
semantic pseudocode v1
+ corrected code alignment v2
+ actual head output trace v1
```

### 3. Correct layer code alignment

```text
reports/latest/LAYER_CODE_ALIGNMENT_V2.md
reports/latest/tables/layer_code_alignment_v2.csv
```

Correct mapping:

```text
L0_ch* -> edge_convs.0 output[:, ch0:ch1, :]
L1_ch* -> edge_convs.1 output[:, ch0:ch1, :]
L2_ch* -> edge_convs.2 output[:, ch0:ch1, :]
```

Do not use the old v1 alignment as final; v1 mapped some heads to internal sub-convs and was methodologically wrong.

### 4. Head output trace

```text
reports/latest/HEAD_OUTPUT_TRACE_V1.md
reports/latest/tables/head_output_trace.csv
reports/latest/tables/head_output_top_events.csv
```

Shows what each pseudo-head actually writes:

```text
activation strength
particle0_top_rate
leading_pt_match_rate
top activation class
logit correlation
top events
```

### 5. EdgeConv inner trace

```text
reports/latest/EDGE_CONV_INNER_TRACE_V1.md
reports/latest/tables/edgeconv_inner_trace_heads.csv
reports/latest/tables/edgeconv_inner_trace_events.csv
```

Current inner trace confirms:

```text
L2_ch224:256 has strong particle0/leading-pT alignment ~0.70
L2_ch0:32 has core-neighborhood readout ~0.42
L1/L0 selected heads are mostly context/feature builders or relays
inner conv outputs exist as [B, C, N, K] tensors with K=16
```

## Key current head rankings

From question-driven analyzer:

### Core / late readout heads

```text
L2_ch224:256 — strongest particle0/leading-pT core readout; Tbl top class
L2_ch128:160 — Tbl readout, class/logit correlation strong
L2_ch0:32 — Hqql/Tbl-related core readout
L2_ch32:64 — Tbl/QCD competition axis
```

### Local/context builder heads

```text
L1_ch16:32
L1_ch112:128
L0_ch40:48
L1_ch32:48
L0_ch48:56
L0_ch0:8
```

### Residual axis heads

```text
L2_ch128:160
L2_ch224:256
L1_ch32:48
L1_ch112:128
L2_ch64:96
L0_ch0:8
L2_ch0:32
```

## Current key numerical findings

### Particle0/top-k controls

```text
remove_particle0 acc_drop = 0.1941
random_remove1 acc_drop_mean = 0.0146
target/random ratio ~= 13.3x
keep_only_particle0 acc = 0.2027
```

Interpretation:

```text
particle0/core is locally causal, but particle0 alone is not enough globally.
```

### Order control

```text
random/reverse/move controls preserve predictions
max random shuffle flip = 0.0000
```

Interpretation:

```text
literal array-index artifact is strongly reduced.
```

### Known-observable residual v1

```text
status = RESIDUAL_SIGNAL_REMAINS
known_observable_agreement_with_model = 0.4102
known_observable_surrogate_acc = 0.3815
logit_r2_mean = 0.5676
residual_rel_mean = 0.3845
```

Interpretation:

```text
simple known-observable surrogate explains part of logits but does not reproduce model decisions.
Need richer residual v2 before strong claim.
```

## Existing tools/runners

Important runners:

```bash
bash scripts/RUN_PARTICLE0_TOPK_CONTROLS_V2.sh
bash scripts/RUN_PARTICLE_ORDER_CONTROL_V1.sh
bash scripts/RUN_CONTROL_CONFUSION_ATLAS_V1.sh
bash scripts/RUN_KNOWN_OBSERVABLE_RESIDUAL_V1.sh
bash scripts/RUN_CLASS_SPECIFIC_ALL_HEAD_GRADIENTS_V1.sh
bash scripts/RUN_OPERATION_LOGIC_ATLAS_V1.sh
bash scripts/RUN_PSEUDOCODE_OPERATION_DATABASE_V1.sh
bash scripts/RUN_LAYER_CODE_ALIGNMENT_V2.sh
bash scripts/RUN_HEAD_OUTPUT_TRACE_V1.sh
bash scripts/RUN_PSEUDOCODE_OPERATION_DATABASE_V2.sh
bash scripts/RUN_QUESTION_DRIVEN_STAGE_ANALYZER_V1.sh
bash scripts/RUN_EDGE_CONV_INNER_TRACE_V1.sh
bash scripts/RUN_AUTOMATIC_COMPARISON_ENGINE_V2.sh
bash scripts/RUN_STREAM_FEATURE_EMBEDDINGS_V1.sh
bash scripts/RUN_SCOPE_COMPARABILITY_GUARD_V1.sh
```

Recommended refresh order after new evidence:

```bash
bash scripts/RUN_QUESTION_DRIVEN_STAGE_ANALYZER_V1.sh
bash scripts/RUN_AUTOMATIC_COMPARISON_ENGINE_V2.sh
bash scripts/RUN_STREAM_FEATURE_EMBEDDINGS_V1.sh
bash scripts/RUN_SCOPE_COMPARABILITY_GUARD_V1.sh
```

## What the next agent should do next

### P0 — Update pseudocode using EdgeConv inner trace

Create:

```text
tools/build_pseudocode_operation_database_v3.py
scripts/RUN_PSEUDOCODE_OPERATION_DATABASE_V3.sh
```

It should merge:

```text
pseudocode_operation_database_v2.csv
edgeconv_inner_trace_heads.csv
edgeconv_inner_trace_events.csv
question_driven_head_rankings.csv
```

Add fields:

```text
knn_neighbor_pattern
inner_conv_shapes
inner_trace_interpretation
top_event_classes
top_event_particles
route_aware_pseudocode
```

Example refined pseudocode:

```python
# L2_ch224:256 route-aware readout
for event:
    core = particle0_or_leading_pt_particle
    neighbors = knn(core, k=16)
    context = read_L1_context(core, neighbors)
    evidence = aggregate_Tbl_like_core_context(context)
    logits += project_late_core_readout(evidence)
```

### P0 — EdgeConv inner trace v2

Current v1 captures block outputs and conv stack output shapes, but it does not yet expose graph-feature tensors or per-neighbor contribution scores.

Add:

```text
neighbor activation contribution
neighbor pt/rank/PID summaries
whether KNN list includes particle0 / leading particle
per-head top-neighbor class patterns
```

Possible file names:

```text
tools/edgeconv_inner_trace_v2.py
scripts/RUN_EDGE_CONV_INNER_TRACE_V2.sh
```

### P0 — residual v2 with richer known observables

Create richer known-observable residual test:

```text
pairwise deltaR moments
ECF-like 2-point/3-point approximations
subjet-like top-k pair features
tau-like proxies
per-file split if metadata available
```

Possible files:

```text
tools/known_observable_residual_v2.py
scripts/RUN_KNOWN_OBSERVABLE_RESIDUAL_V2.sh
```

### P1 — per-file / heldout stability

The current strong claims are still local/sampled. Need heldout stability:

```text
repeat controls + residual + output trace per ROOT file / file groups
check whether same heads and transitions survive
```

Possible files:

```text
tools/per_file_mechanism_stability_v1.py
scripts/RUN_PER_FILE_MECHANISM_STABILITY_V1.sh
```

## Current safest scientific statement

```text
ParticleNet_kinpid shows a staged mechanism candidate:
L0/L1 build local and neighborhood context; L2 performs late class-evidence readout often aligned with particle0/leading-pT core. Particle0/top-k removal is locally causal, array order is not the main explanation, and simple known-observable surrogate v1 does not reproduce ParticleNet decisions. The strongest residual/circuit axis involves Tbl/Hqql and related structured class competition. This is a mechanistic interpretation candidate, not a new-particle discovery claim yet.
```

## What not to do

Do not jump directly to big-stream scaling until these are done:

```text
route-aware pseudocode v3
EdgeConv inner trace v2
residual v2
heldout/per-file stability
```

Do not claim discovery until:

```text
known-observable residual v2 remains strong
heldout/per-file stability passes
cross-model agreement passes
physics sanity checks pass
```
