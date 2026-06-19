# Research Dashboard JSON Spec v1

This document defines the compact JSON dashboard used by ChatGPT / agents to quickly understand the current research state without reading every report and log.

## Goal

After each meaningful run, generate:

```text
manifests/latest/research_dashboard_latest.json
reports/latest/RESEARCH_DASHBOARD_LATEST.md
```

The JSON should be small enough to inspect quickly, but rich enough to support hypothesis generation.

## Dashboard sections

### metadata

```json
{
  "model": "ParticleNet_kinpid.pt",
  "mode": "kinpid",
  "baseline_acc": 0.7574,
  "n": 2560,
  "valid_model": true
}
```

### executive_summary

Short bullets:

- what is validated;
- strongest result;
- most important risk;
- next best action.

### top_hypotheses

Top P0/P1 hypotheses from `research_hypothesis_board.csv`.

Fields:

```json
{
  "id": "H2",
  "priority": "P0",
  "status": "CAUSAL_PATCHED",
  "score": 78,
  "title": "EdgeConv pseudo-head specialization",
  "evidence": "...",
  "risk": "...",
  "next_test": "..."
}
```

### top_heads

Most important pseudo-heads from `head_projection_question_map.csv`.

Fields:

```json
{
  "head_id": "L1_ch16:32",
  "acc_drop": 0.2641,
  "role": "middle learned-neighborhood / route-composition head",
  "question": "...",
  "semantic_hint": "...",
  "composite_lens": "...",
  "next_test": "..."
}
```

### weight_projection_questions

Top projection questions from `weight_projection_questions.csv`.

Include:

- strongest physical feature projections;
- strongest block interactions;
- strongest class/contrast directions.

### route_and_particle_findings

From v4:

- top-pT vs random ablation;
- compact/wide route patterns;
- route stats by layer/class.

### class_feature_map

From v5:

- strongest feature-channel per class.

### risks

Things that currently weaken claims:

- equal channel slices, not learned clusters;
- route stats descriptive, not route-causal yet;
- need heldout stability;
- ParT attention paused.

### next_actions

Ranked action list:

1. Activation-cluster pseudo-heads.
2. Random channel controls.
3. Top-k particle sweep.
4. Route-group causal patch.
5. Error atlas.
6. Valid ParT/attention model.

## Rule

The dashboard is not a replacement for full CSV/MD logs. It is the first thing to read. If a result is interesting, then open the linked report/table.
