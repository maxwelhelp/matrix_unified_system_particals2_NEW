# Задание агенту: продолжить ParticleNet pseudocode / mechanistic research

Работай в репозитории:

```text
maxwelhelp/matrix_unified_system_particals
branch: main
локально у пользователя: ~/Рабочий стол/matrix_unified_system_particals
data: ~/Рабочий стол/jetclass_tiny_balanced
checkpoint: local_checkpoints/part/ParticleNet_kinpid.pt
mode: kinpid
```

## Главная цель

Продолжить не saliency/gradient анализ, а именно **декомпиляцию ParticleNet в псевдокод операций**.

Нужно связать:

```text
raw particles
-> KNN / EdgeConv
-> pseudo-head channel groups
-> реальные output tensors
-> class evidence
-> controls / residual / heldout
-> readable pseudocode
```

Главный смысл проекта: получить не просто “какая голова важна”, а:

```text
что эта pseudo-head-группа читает,
на каком уже преобразованном входе,
какую операцию выполняет,
что пишет дальше,
какие частицы/классы она поддерживает,
и какой физический смысл это может иметь.
```

## Где уже всё зафиксировано

Прочитай сначала:

```text
docs/00_handoff/AGENT_HANDOFF_PARTICLENET_PSEUDOCODE_RESEARCH_v1.md
reports/latest/QUESTION_DRIVEN_STAGE_ANALYZER_V1.md
reports/latest/PSEUDOCODE_OPERATION_DATABASE_V2.md
reports/latest/LAYER_CODE_ALIGNMENT_V2.md
reports/latest/HEAD_OUTPUT_TRACE_V1.md
reports/latest/EDGE_CONV_INNER_TRACE_V1.md
reports/latest/KNOWN_OBSERVABLE_RESIDUAL_V1.md
reports/latest/AUTOMATIC_COMPARISON_ENGINE_V2.md
reports/latest/SCOPE_COMPARABILITY_GUARD_V1.md
```

Таблицы:

```text
reports/latest/tables/question_driven_head_rankings.csv
reports/latest/tables/pseudocode_operation_database_v2.csv
reports/latest/tables/layer_code_alignment_v2.csv
reports/latest/tables/head_output_trace.csv
reports/latest/tables/edgeconv_inner_trace_heads.csv
reports/latest/tables/edgeconv_inner_trace_events.csv
reports/latest/tables/known_observable_residual_by_class.csv
```

## Что уже установлено

Текущая рабочая схема:

```text
L0: early local particle/edge/PID/radial feature builders
L1: middle neighborhood/context relays
L2: late class-evidence readout, часто через particle0 / leading-pT core
```

Особенно важные головы:

```text
L2_ch224:256 — strongest particle0/leading-pT core readout, Tbl-heavy
L2_ch128:160 — Tbl readout / residual axis
L2_ch0:32 — Hqql/Tbl-related core readout
L2_ch32:64 — Tbl/QCD competition
L1_ch16:32 — context relay / QCD axis
L1_ch112:128 — context relay / Tbl/Wqq relation
L0_ch40:48 — early local builder
L0_ch0:8 — early local builder linked to Hqql/Tbqq residual signals
```

Контрольная цепочка:

```text
particle0/top-k controls:
  remove_particle0 acc_drop = 0.1941
  random_remove1 acc_drop_mean = 0.0146
  ratio ~= 13.3x
  keep_only_particle0 acc = 0.2027

order control:
  random/reverse/move controls preserve predictions
  index/order artifact strongly reduced

known-observable residual v1:
  RESIDUAL_SIGNAL_REMAINS
  agreement with model = 0.4102
  simple known-observable surrogate does not reproduce ParticleNet decisions
```

Нельзя утверждать “открыли новую частицу”. Можно утверждать:

```text
ParticleNet_kinpid имеет сильный mechanism candidate:
L0/L1 строят контекст,
L2 читает class evidence через core/leading particle,
particle0/top-k causal локально подтверждён,
order artifact снижен,
simple known-observable surrogate v1 не объясняет решения полностью.
```

## Что сделать следующим

### P0. Построить PSEUDOCODE_OPERATION_DATABASE_V3

Создай:

```text
tools/build_pseudocode_operation_database_v3.py
scripts/RUN_PSEUDOCODE_OPERATION_DATABASE_V3.sh
```

Входы:

```text
pseudocode_operation_database_v2.csv
edgeconv_inner_trace_heads.csv
edgeconv_inner_trace_events.csv
question_driven_head_rankings.csv
known_observable_residual_v1.json
```

Добавить поля:

```text
knn_neighbor_pattern
top_event_particle_pattern
inner_conv_shapes
inner_trace_interpretation
route_aware_pseudocode
core_vs_context_role
event_examples
next_validation
```

Пример нужного псевдокода:

```python
# L2_ch224:256 route-aware readout
for event:
    core = particle0_or_leading_pt_particle
    neighbors = knn(core, k=16)
    context = read_L1_context(core, neighbors)
    evidence = aggregate_Tbl_like_core_context(context)
    logits += project_late_core_readout(evidence)
```

Для L1/L0:

```python
# L1/L0 context builder
for particle i:
    neighbors = knn(i)
    local_edges = read_edge_features(i, neighbors)
    context = build_neighbor_context(local_edges)
    write_context_for_L2_readout(context)
```

### P0. Сделать EDGE_CONV_INNER_TRACE_V2

Текущий `EDGE_CONV_INNER_TRACE_V1` уже показывает block output, conv shapes, top particles и KNN neighbors. Но нужно глубже:

Создать:

```text
tools/edgeconv_inner_trace_v2.py
scripts/RUN_EDGE_CONV_INNER_TRACE_V2.sh
```

Добавить:

```text
neighbor contribution estimate
neighbor pt/rank/PID summaries
whether KNN list includes particle0 / leading particle
per-head neighbor-type statistics
top-neighbor class patterns
event-level route explanation
```

Цель: понять не только “top particle = 0”, а **какие соседи кормят этот core-readout**.

### P0. Сделать richer residual v2

Создать:

```text
tools/known_observable_residual_v2.py
scripts/RUN_KNOWN_OBSERVABLE_RESIDUAL_V2.sh
```

Добавить признаки:

```text
pairwise deltaR moments
ECF-like 2-point approximations
ECF-like 3-point approximations
top-k pair/subjet features
tau21/tau32-like proxies
per-file split if possible
```

Цель: проверить, остаётся ли residual после более честных physics observables.

### P1. Сделать per-file / heldout stability

Создать:

```text
tools/per_file_mechanism_stability_v1.py
scripts/RUN_PER_FILE_MECHANISM_STABILITY_V1.sh
```

Проверить:

```text
те же heads?
те же class transitions?
те же particle0/top-k effects?
тот же residual axis?
```

по разным ROOT-файлам / группам файлов.

## После каждого нового шага

Пересобирать:

```bash
bash scripts/RUN_QUESTION_DRIVEN_STAGE_ANALYZER_V1.sh
bash scripts/RUN_AUTOMATIC_COMPARISON_ENGINE_V2.sh
bash scripts/RUN_STREAM_FEATURE_EMBEDDINGS_V1.sh
bash scripts/RUN_SCOPE_COMPARABILITY_GUARD_V1.sh
```

Если добавлен новый псевдокодный слой, обновить:

```bash
bash scripts/RUN_PSEUDOCODE_OPERATION_DATABASE_V2.sh
# потом новый V3 runner
```

## Главное правило

Не превращать это в обычную таблицу важности.

Каждый результат должен двигать нас к формату:

```text
question
-> evidence stages
-> ranked heads
-> code location
-> real output tensor
-> KNN / EdgeConv route
-> route-aware pseudocode
-> physics meaning
-> risks
-> next validation
```

Итоговая цель: **нейросеть как читаемая программа по частицам**, а не просто attribution.

