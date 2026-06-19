# Matrix Unified System — Particle Atlas

Private project for adapting the matrix-pseudocode / causal-tracing system from LLM transformer analysis to particle-physics transformer models.

## One-paragraph goal

This repo builds a particle-transformer mechanism atlas: it collects traces, gradients, attention/head/particle evidence, relation graphs, automatic comparison tasks, and lightweight reports so that candidate physics mechanisms can be proposed and then validated with counterfactual controls.

This is not automatic scientific proof. It is a candidate-generator for mechanisms that must be validated with heldout jets, controlled removals, class-specific gradients, simulation checks, and physics expert review.

## Primary target

```text
Particle Transformer / ParT for jet tagging
JetClass small subset first
later: JetFormer / MIParT / other particle-cloud transformers
```

## Core mapping

```text
LLM token          -> jet constituent / particle
attention read     -> particle-to-particle read
QK score term      -> pair/geometry-aware interaction score
VO payload         -> information written from source particle
MLP group          -> class-logit writer/suppressor
lm_head logit      -> jet class logit / classifier head logit
why-token report   -> why-class report
```

## Pipeline map

```text
jet/event/particle cloud
  -> trained particle transformer
  -> model probe / runtime trace
  -> head/particle/relation evidence
  -> evidence graph history
  -> stream task watcher
  -> relation signal graph
  -> automatic comparison engine
  -> P0/P1 validation tasks
  -> physics hypothesis candidates
```

## Current active cycle

The current cycle output shown by the runner includes:

```text
research_evidence_graph_v1
stream_task_watcher
automatic_comparison_engine_v1/v2
relation_signal_graph_v1
```

Typical cycle command:

```bash
RUN_MODEL=0 SAMPLES_PER_FILE=64 MICRO_BATCH=32 bash scripts/<cycle_script>.sh
```

`RUN_MODEL=0` means skip expensive model execution and rebuild analysis/manifests from existing outputs.

## Important directories

```text
manifests/latest/       latest lightweight machine-readable outputs
manifests/history/      timestamped history snapshots
reports/diagnostics/   human-readable diagnostics/review notes
scripts/               runnable cycles / builders / watchers
commands/              stable user-facing commands, if present
runs/                  local heavy outputs; should not be committed
```

## Important current files

Latest outputs commonly used for review:

```text
manifests/latest/research_evidence_graph_v1.json
manifests/latest/stream_task_watcher.json
manifests/latest/relation_signal_graph_v1.json
manifests/latest/automatic_comparison_engine_v2.json
```

History snapshots can be large but useful:

```text
manifests/history/research_evidence_graph_*.json
```

## Current high-priority tasks seen in watcher

The task watcher currently highlights P0 issues such as:

```text
T1_PARTICLE0_SHORTCUT_OR_CORE_ANCHOR
  Question: is the all-head system over-dominated by particle0 / leading-core evidence?
  Next: particle0 removal, keep-only particle0, top-k removal, same-count random controls.

T4_HQQL_TBL_SIGNATURE
  Question: is the stream dominated by Hqql/Tbl high-confidence events?
  Next: class-specific all-head gradients for Hqql, Tbl, Tbqq, Wqq, Zqq.

T2_HEAD_RANK_STABILITY
  Question: do the same heads stay important across snapshots?
  Next: keep tracking; if unstable, split by class/sample size and run heldout stability.
```

## What another agent should review first

Read in this order:

```text
README.md
manifests/latest/automatic_comparison_engine_v2.json
manifests/latest/stream_task_watcher.json
manifests/latest/research_evidence_graph_v1.json
manifests/latest/relation_signal_graph_v1.json
reports/diagnostics/*.md
```

Then answer:

1. Which P0 tasks are real and which are artifacts?
2. Is particle0 a shortcut/core anchor or a legitimate physics carrier?
3. Are Hqql/Tbl signatures class-specific or stream bias?
4. Are head ranks stable across snapshots and sample sizes?
5. Which controls are missing before claiming a mechanism?
6. Which findings should be promoted into a formal validation experiment?

## Validation controls required before claims

Do not treat an evidence graph as proof. Minimum controls:

```text
heldout jets
class-specific gradients
particle0 removal control
keep-only particle0 control
top-k particle removal
same-count random removal
head ablation / patch control
relation / pair-feature counterfactual
seed and snapshot stability
```

## Git and sync rules

Heavy raw outputs and checkpoints should stay local. Lightweight JSON manifests and diagnostics can be committed if they are needed for review.

If `git push` says `fetch first`, use:

```bash
git status -sb
git pull --rebase origin main
git push origin main
```

If rebase conflicts, do not force-push. Resolve conflicts, then:

```bash
git add <resolved-files>
GIT_EDITOR=true git rebase --continue
git push origin main
```

If the working tree is clean, this helper pattern is safe:

```bash
git pull --rebase origin main && git push origin main
```

## Do not delete local data

Avoid:

```bash
git clean -fdx
```

It can delete ignored local runs/datasets.

## Development direction

Short-term:

```text
1. Fix push/rebase workflow so cycle commits do not pile up unpushed.
2. Keep manifest outputs lightweight and reviewable.
3. Add/maintain diagnostics reports for P0 tasks.
4. Run particle0 shortcut/core-anchor controls.
5. Run Hqql/Tbl class-specific gradient controls.
6. Track head-rank stability across snapshots.
```

Medium-term:

```text
1. Convert recurring P0 controls into stable commands.
2. Add report publisher similar to architecture_builder.
3. Add automatic archive of best/interesting evidence patterns.
4. Connect accepted mechanisms to formal physics validation notebooks.
```
