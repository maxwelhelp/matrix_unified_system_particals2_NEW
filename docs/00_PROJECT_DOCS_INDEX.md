# Project Docs Index

This file organizes the project documentation into categories. Existing historical docs may still live directly in `docs/`; this index defines how to read them and how new docs should be grouped.

## 01 — Method and architecture

Core method docs:

```text
docs/MATRIX_PSEUDOCODE_DECOMPILER_METHOD_v1.md
docs/AUTOMATION_AND_FULL_NEURON_TRACE_PLAN.md
docs/TOKEN_VS_PARTICLE_ANALYSIS_PLAN_v1.md
docs/DIFFERENTIABLE_ALL_HEAD_SUPERTRACE_PLAN_v1.md
```

Read when asking:

```text
What exactly are we doing?
How does text-token tracing map to particle tracing?
What does all-head supertrace mean?
```

## 02 — Physics research and hypotheses

Research direction docs:

```text
docs/PARTICLE_TRANSFORMER_ATLAS_PLAN.md
docs/PARTICLE_DISCOVERY_PROGRAM_v1.md
docs/SINGLE_HEAD_PARTICLE_TRACE_FINDINGS_v1.md
docs/ALL_HEAD_SUPERTRACE_FINDINGS_v1.md
docs/UPDATED_RESEARCH_STATE_AFTER_ALL_HEAD_SUPERTRACE_v1.md
docs/02_physics/PHYSICS_INTERPRETABILITY_RESEARCH_BRIEF_v1.md
docs/02_physics/PHYSICS_QUESTION_BANK_v1.md
```

Read when asking:

```text
What physics questions should we test?
Is the signal meaningful or shortcut?
How does this connect to jet substructure research?
```

## 03 — Stream, evidence graph, and automation

Evidence/data pipeline docs:

```text
docs/EVIDENCE_GRAPH_AND_DYNAMIC_TRACE_DATASET_v1.md
docs/DYNAMIC_EVIDENCE_ANALYTICS_v1.md
docs/STREAMING_EVIDENCE_PIPELINE_v1.md
docs/STREAM_CYCLE_WORKFLOW_v1.md
docs/STREAM_TASK_WATCHER_v1.md
docs/RELATION_SIGNAL_GRAPH_v1.md
docs/AUTOMATIC_COMPARISON_ENGINE_v1.md
docs/AUTOMATIC_COMPARISON_ENGINE_v2.md
docs/03_stream/STREAM_AUTOMATION_README_v1.md
```

Read when asking:

```text
How do we convert runs into structured evidence?
What should the automatic watcher compare?
How do we query the stream?
```

## 04 — Controls, validation, and next experiments

Control/validation docs:

```text
docs/LARGE_STREAM_RUN_PLAN_v1.md
docs/04_controls/NEXT_CONTROL_MATRIX_v1.md
docs/04_controls/LARGE_STREAM_VALIDATION_PROTOCOL_v1.md
```

Read when asking:

```text
What do we run next?
What controls are blocking a stronger claim?
What is the safest way to scale data?
```

## 05 — Product and services

Product/value docs:

```text
docs/PRODUCT_SERVICES_AND_VALUE.md
```

Read when asking:

```text
What can be sold?
How do we explain the value without exposing the decoder?
```

## Current research state, short version

As of the large stream run:

```text
latest large stream: 5120 events
stable top heads: L1_ch112:128, L1_ch16:32, L0_ch40:48, L2_ch224:256
strongest stream signal: particle0/core_high_pt -> Hqql/Tbl
status: strong candidate signal, not physics proof
main risk: particle ordering / leading-pT shortcut / known-observable proxy
main blockers: particle0/top-k controls, order control, class-specific gradients, known-observable residual, heldout/per-file stability
```

## Rule for future docs

New docs should go into category folders when possible:

```text
docs/01_method/
docs/02_physics/
docs/03_stream/
docs/04_controls/
docs/05_product/
```

Old docs can stay where they are; use this index to find them.
