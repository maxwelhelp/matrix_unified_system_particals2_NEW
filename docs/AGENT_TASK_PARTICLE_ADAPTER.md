# Agent Task: Port Matrix Unified System to Particle Transformer

## Mission

Copy the lightweight core from `maxwelhelp/matrix_unified_system` into this repo and adapt it to Particle Transformer / ParT for JetClass.

Do not commit heavy datasets, checkpoints, or runs.

## Step 1: Copy core project

Copy from base repo:

- `tools/`
- `scripts/`
- `run_scripts/`
- `requirements.txt`
- useful docs only

Do not copy:

- `runs/`
- `results_zips/`
- `*.zip`
- model weights
- datasets

## Step 2: Add adapter interface

Create:

```text
adapters/base_adapter.py
adapters/part_adapter.py
```

Base interface:

```python
class ModelAdapter:
    def load_model(self): ...
    def load_data(self): ...
    def get_layers(self): ...
    def get_attention(self, layer): ...
    def get_qkv(self, layer): ...
    def get_o_proj(self, layer): ...
    def get_pairwise_bias(self, layer): ...
    def get_mlp(self, layer): ...
    def get_mlp_down(self, layer): ...
    def get_classifier_head(self): ...
    def forward_with_cache(self, batch): ...
    def patch_head(self, layer, head, mode): ...
    def patch_mlp_group(self, layer, neurons): ...
    def patch_particle_group(self, particle_indices): ...
    def patch_pair_group(self, pair_indices): ...
```

## Step 3: Implement ParT adapter

`adapters/part_adapter.py` must find:

- transformer blocks;
- attention module;
- q/k/v projections;
- output projection;
- pairwise particle interaction / pair embedding term;
- FFN / MLP up/gate/down if present;
- classifier head.

If names differ, write a probe script and map names explicitly.

## Step 4: Data loader

Create:

```text
data/jetclass_loader.py
```

Small mode first:

- 100 jets smoke test;
- 10k jets debug atlas;
- no full dataset until pipeline works.

Each batch must preserve:

- particle features;
- mask;
- class labels;
- pT rank;
- particle type/charge if available;
- pairwise deltaR and invariant-mass proxy if computable.

## Step 5: Tools to implement

```text
tools/particle_model_probe_v1.py
tools/particle_static_atlas_v1.py
tools/particle_runtime_trace_v1.py
tools/particle_patch_controls_v1.py
tools/particle_hypothesis_mining_v1.py
```

## Step 6: Reports

Write lightweight reports:

```text
reports/latest/WHY_CLASS_REPORT.md
reports/latest/PARTICLE_PAIR_MECHANISM_REPORT.md
reports/latest/PARTICLE_MLP_GROUP_REPORT.md
reports/latest/HYPOTHESIS_CANDIDATES.md
```

Tables:

```text
reports/latest/tables/particle_head_summary.csv
reports/latest/tables/particle_pair_routes.csv
reports/latest/tables/particle_patch_controls.csv
reports/latest/tables/particle_mlp_groups.csv
reports/latest/tables/hypothesis_candidates.csv
```

## Step 7: First success criterion

On 100-1000 jets:

- model loads;
- forward works;
- class logits reproduced;
- at least one head ablation changes class logit;
- at least one MLP group patch changes class logit;
- `WHY_CLASS_REPORT.md` is produced.

## Step 8: Strong success criterion

On 10k jets:

- route clusters are stable;
- patch effects repeat on heldout jets;
- class-specific mechanisms appear;
- at least 5 hypothesis candidates are produced;
- counterfactual tests are implemented for top candidates.

## Important

The decoder internals remain private. Commit only code, configs, docs, and lightweight summaries. Heavy datasets/checkpoints/runs stay local.
