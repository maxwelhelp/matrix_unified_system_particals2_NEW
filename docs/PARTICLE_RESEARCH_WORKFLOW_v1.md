# Particle Research Workflow v1

This document explains how to run and maintain the particle research track.

## Principle

Do not chase pretty interpretations. Every claim must be attached to:

1. a validated model accuracy;
2. a causal patch/control;
3. a class-specific result;
4. a failure mode or risk;
5. a next validation step.

## Current validated stack

Use this stack for real claims:

```bash
ParticleNet_kinpid.pt
JetClass tiny balanced ROOT subset
reports/latest/PARTICLENET_RESEARCH_COMPASS_V5.md
reports/latest/PARTICLENET_DISCOVERY_ATLAS_V4.md
```

Do not use current `ParT_*` for claims until accuracy is fixed.

## Standard run sequence

After pulling the repo:

```bash
cd "$HOME/Рабочий стол/matrix_unified_system_particals"
git pull --rebase origin main
```

Run the research stack:

```bash
SAMPLES_PER_FILE=128 \
CHECKPOINT="local_checkpoints/part/ParticleNet_kinpid.pt" \
MODE=kinpid \
JETCLASS_TINY="$HOME/Рабочий стол/jetclass_tiny_balanced" \
bash scripts/RUN_PARTICLENET_RESEARCH_STACK.sh
```

For a larger run:

```bash
SAMPLES_PER_FILE=256 \
CHECKPOINT="local_checkpoints/part/ParticleNet_kinpid.pt" \
MODE=kinpid \
JETCLASS_TINY="$HOME/Рабочий стол/jetclass_tiny_balanced" \
bash scripts/RUN_PARTICLENET_RESEARCH_STACK.sh
```

## What reports to read

1. `reports/latest/PARTICLENET_RESEARCH_SYNTHESIS_V6.md`
   - one-page research board and priorities.

2. `reports/latest/PARTICLENET_RESEARCH_COMPASS_V5.md`
   - pseudo-heads, feature channels, known observables, class contrasts.

3. `reports/latest/PARTICLENET_DISCOVERY_ATLAS_V4.md`
   - route stats and particle-subset controls.

4. `docs/PARTICLE_HYPOTHESIS_REGISTRY_v1.md`
   - persistent hypothesis list and evidence levels.

## Files safe to push

Safe:

```text
reports/latest/*.md
reports/latest/tables/*.csv
manifests/latest/*.json
docs/*.md
scripts/*.sh
tools/*.py
adapters/*.py
```

Do not push:

```text
runs/**/*.root
runs/**/*.pt
local_checkpoints/**
*.tar
*.root
large datasets
```

## How to decide if a hypothesis is worth keeping

Keep if:

- effect is causal and not just correlation;
- effect survives at least one control;
- effect has a class-specific pattern;
- it suggests a concrete next test.

Drop or downgrade if:

- effect disappears on heldout files;
- random control explains it;
- it is fully explained by a known observable shortcut;
- the model accuracy is not valid.

## Immediate roadmap

### R1 — Stabilize ParticleNet hypotheses

- Run v6 synthesis on 128 and 256 samples per file.
- Add heldout files from more tar parts.
- Compare whether top hypotheses persist.

### R2 — Route-group causal patch

Implement route-level controls:

- compact-neighbor edges;
- wide-angle edges;
- high-pt neighbor edges;
- random neighbor edges.

### R3 — Learned pseudo-head clusters

Replace equal channel slices with activation clusters:

- channel covariance clustering;
- class-conditioned activation clustering;
- random channel-group controls.

### R4 — Error atlas

Study wrong predictions:

- true -> predicted confusion pairs;
- route stats of errors;
- feature-channel drops for competing class logits.

### R5 — Recover valid attention model

Find or train valid ParT checkpoint:

- validate accuracy;
- extract attention heads / pair bias;
- compare attention heads to ParticleNet route pseudo-heads.
