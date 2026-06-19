# Project Status and Roadmap

## Current status

The particles repo is now a fork target for adapting the Qwen matrix-pseudocode system to Particle Transformer / ParT.

Done:

- copied lightweight Qwen core tools/scripts;
- added particle atlas plan;
- added agent task document;
- added base adapter interface;
- added ParT adapter skeleton;
- added particle probe skeleton;
- added real dummy ParT probe script;
- added runner that publishes lightweight dummy-probe summaries;
- added particle-specific requirements.

## Important model components to cover

For ParT, we must not analyze only attention. Required components:

1. input feature embedding: `embed`, `pf_embed`, `sv_embed`;
2. pairwise physics embedding: `pair_embed`;
3. particle self-attention blocks: `blocks`;
4. class-token attention blocks: `cls_blocks`;
5. learned `cls_token`;
6. attention projections packed inside `MultiheadAttention`;
7. attention output projection;
8. head scaling `c_attn`;
9. MLP `fc1`, activation, `fc2`;
10. residual scaling `w_resid`;
11. norms: `pre_attn_norm`, `post_attn_norm`, `pre_fc_norm`, `post_fc_norm`, final `norm`;
12. classifier head `fc`;
13. masks and padded particles;
14. optional extra pair features `uu` / `uu_idx`.

## Immediate next milestone

Run dummy ParT probe:

```bash
bash scripts/RUN_PARTICLE_DUMMY_PROBE_V1.sh
```

Success means:

- `weaver-core` imports;
- dummy `ParticleTransformer` is created;
- forward pass returns logits `[batch, classes]`;
- adapter finds blocks, cls_blocks, pair_embed, classifier;
- report is pushed to GitHub.

Expected outputs:

```text
reports/latest/DUMMY_PARTICLE_PROBE_REPORT.md
manifests/latest/dummy_particle_probe.json
```

## Next coding phases

### Phase 1: real ParT loader

Create:

```text
tools/particle_load_part_model_v1.py
```

Goal:

- load official ParT config/checkpoint;
- wrap with `ParticleTransformerAdapter`;
- produce model map.

### Phase 2: JetClass tiny loader

Create:

```text
data/jetclass_loader.py
```

Goal:

- 100 jets smoke;
- 1000 jets debug;
- keep particle features, Lorentz vectors, masks, labels.

### Phase 3: runtime trace

Create:

```text
tools/particle_runtime_trace_v1.py
```

Goal:

- class logits;
- input embed output;
- pair_embed attention bias;
- particle block attention;
- cls_block attention;
- MLP fc1/fc2 hidden;
- classifier contributions.

### Phase 4: patch controls

Create:

```text
tools/particle_patch_controls_v1.py
```

Patch modes:

- ablate head;
- ablate pair bias;
- ablate particle group;
- ablate pair group;
- ablate MLP group;
- ablate cls token path.

Metrics:

- class logit delta;
- probability delta;
- CE delta;
- top1 match;
- class-specific enrichment.

### Phase 5: WHY_CLASS report

Create:

```text
tools/particle_why_class_report_v1.py
```

Report:

- why predicted class;
- top particles read;
- top pairs;
- top heads;
- top MLP groups;
- class-logit contributors;
- counterfactual checks.

### Phase 6: hypothesis mining

Create:

```text
tools/particle_hypothesis_mining_v1.py
```

Goal:

- repeated class-specific mechanisms;
- heldout stability;
- counterfactual pass/fail;
- physics-readable hypothesis candidates.

## Definition of success

Smoke success:

- dummy ParT works;
- adapter sees all critical modules.

First real success:

- pretrained ParT loads;
- 100-1000 JetClass jets run;
- one head patch changes class logit;
- one MLP group patch changes class logit;
- one pair-bias patch changes class logit;
- `WHY_CLASS_REPORT.md` is produced.

Strong success:

- 10k jets;
- repeated class-specific routes;
- causal patch effects repeat on heldout jets;
- at least 5 hypothesis candidates;
- counterfactual validation for top candidates.
