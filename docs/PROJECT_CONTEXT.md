# Matrix Unified System Particles — project context

## Goal

This repository is for building an interpretable particle/jet neural-system around Particle Transformer / JetClass.

The target is not only classification accuracy. The target is to expose the internal computation path:

```text
JetClass ROOT events
→ official preprocessing contract: YAML + checkpoint + network wrapper
→ ParT model inputs: pf_points, pf_features, pf_vectors, pf_mask
→ attention heads / pair bias / CLS reads
→ role-level particle flows: charged_hadron, neutral_hadron, photon, electron, muon, CLS
→ grouped comparisons: correct vs confused classes
→ matrix/pseudocode interpretation of heads/layers
→ physics hypothesis about what interaction/topology the network uses
```

## Safety rule before interpretation

Never trust attention/supertrace/pseudocode reports until the inference contract is valid.

The contract is valid only when all of this matches:

- mode: `full` or `kinpid`
- YAML: `external/particle_transformer/data/JetClass/JetClass_<mode>.yaml`
- checkpoint: `external/particle_transformer/models/ParT_<mode>.pt`
- network wrapper: `external/particle_transformer/networks/example_ParticleTransformer.py`
- feature count from YAML matches model input dim
- checkpoint strict-load succeeds
- Weaver/direct prediction smoke accuracy is not collapsed

Old bad ROOT outputs must be treated as stale if the analyzer shows collapsed class accuracy.

## Modes

### full

Expected feature count: 17.

Includes displacement/trajectory features:

- `part_d0`
- `part_d0err`
- `part_dz`
- `part_dzerr`

Use with:

```text
external/particle_transformer/data/JetClass/JetClass_full.yaml
external/particle_transformer/models/ParT_full.pt
```

### kinpid

Expected feature count: 13.

No displacement/trajectory features.

Use with:

```text
external/particle_transformer/data/JetClass/JetClass_kinpid.yaml
external/particle_transformer/models/ParT_kinpid.pt
```

## Important subsystems

### 1. Contract / sanity

Checks that YAML, checkpoint, wrapper, feature count, and strict loading all agree.

Main command:

```bash
bash commands/part_01_sanity_contract.sh
```

Main outputs:

```text
reports/latest/PART_SANITY_CONTRACT.md
manifests/latest/part_sanity_contract.json
```

### 2. Weaver output analyzer

Reads prediction ROOT files, finds label branches and score branches, then computes per-file accuracy and confusion pairs.

Main tool:

```text
tools/part_weaver_output_analyzer_v1.py
```

Main command:

```bash
bash commands/part_02_analyze_weaver_outputs.sh
```

Main output:

```text
reports/latest/PART_WEAVER_OUTPUT_ANALYZER_V1.md
```

### 3. Attention supertrace

Hooks ParT attention modules and records top-k attention connections by layer/head.

Main tool:

```text
tools/part_attention_supertrace_v1.py
```

Interpretation target:

```text
head/layer → top attention pairs → particle roles → role flows → class-specific differences
```

Important warning: old versions of `part_attention_supertrace_v1.py` may contain a fake hardcoded data contract. Do not trust it as a direct-gate until it uses the same YAML/checkpoint contract as the official run.

### 4. Hqql/Tbl group analysis

Key groups:

```text
A_Hqql_correct
B_Hqql_to_Tbl
C_Tbl_correct
D_Tbl_to_Hqql
```

Purpose:

```text
Find which attention paths distinguish correct Hqql/Tbl classification from confusion.
```

### 5. Report index

Collects the lightweight report/map of the current run so a human/LLM can quickly understand the state.

Main command:

```bash
bash commands/part_03_report_index.sh
```

Main output:

```text
reports/latest/PART_INTERPRETABILITY_INDEX.md
```

## Recommended workflow

```bash
bash commands/part_00_sync_repo.sh
bash commands/run_part_interpretability_all.sh
```

The all-runner does this:

```text
1. sanity contract
2. analyze existing Weaver ROOT outputs if they exist
3. build report index
```

It does not run expensive training and does not download weights/datasets.

## What to inspect first

1. `reports/latest/PART_SANITY_CONTRACT.md`
2. `reports/latest/PART_WEAVER_OUTPUT_ANALYZER_V1.md`
3. `reports/latest/PART_INTERPRETABILITY_INDEX.md`
4. `tools/part_attention_supertrace_v1.py`
5. `tools/part_weaver_output_analyzer_v1.py`
6. `external/particle_transformer/data/JetClass/JetClass_full.yaml`
7. `external/particle_transformer/data/JetClass/JetClass_kinpid.yaml`
8. `external/particle_transformer/networks/example_ParticleTransformer.py`

## Current architectural risk

The biggest risk is not the model itself. The biggest risk is silent mismatch between:

```text
mode ↔ YAML ↔ checkpoint ↔ preprocessing ↔ generated ROOT scores ↔ supertrace input construction
```

If that mismatch exists, the interpretation is invalid even if the scripts run.

## Development principle

Every new interpretation report must state:

- which mode was used
- which YAML was used
- which checkpoint was used
- whether strict load passed
- whether smoke predictions were valid
- which ROOT outputs were analyzed
- whether the analyzed outputs are fresh or stale
