# Full Head Question Catalog Spec v1

This fixes the earlier problem: `ALL_HEAD_QUESTIONS_AND_ANALYSIS.md` had one main question per pseudo-head, but it did not list every possible question/lens to ask for every head.

The full catalog must generate:

```text
reports/latest/FULL_HEAD_QUESTION_CATALOG.md
reports/latest/tables/full_head_question_catalog.csv
manifests/latest/full_head_question_catalog.json
```

## What it must contain

For every current ParticleNet pseudo-head group:

```text
L0_ch0:8
L0_ch8:16
...
L1_ch16:32
...
L2_ch224:256
```

it must list many questions, not just one:

1. `CORE_CURRENT_QUESTION`
2. `WEIGHT_SOURCE_TO_HEAD`
3. `PHYSICAL_FEATURE_TO_HEAD`
4. `ROUTE_WIDTH_TO_HEAD`
5. `LEADING_PARTICLE_TO_HEAD`
6. `HEAD_TO_CLASS_EFFECT`
7. `HEAD_TO_CLASS_CONTRAST`
8. `ACTIVATION_CLUSTER_HEAD`
9. `RANDOM_CHANNEL_CONTROL`
10. `WEIGHT_PATCH_CONSISTENCY`
11. `HELDOUT_STABILITY`
12. `ERROR_ROUTE_HEAD`
13. `KNN_NEIGHBOR_TO_HEAD`
14. `MULTI_HEAD_COMBINATION`

So if we have 24 heads, the catalog should have about 336 question rows.

## Row fields

Each row should include:

```text
head_id
layer
group
role
question_id
question
current_answer
status
priority
evidence_now
what_it_means_if_true
what_to_compute_next
next_script_or_lens
risk
```

## Status values

```text
ANSWERED_PARTIAL
TODO_P0
TODO_P1
TODO_P2
PAUSED
```

## Purpose

The full catalog should answer:

```text
How many heads are there?
What does every head currently seem to compute?
What questions can still be asked of every head?
Which questions are already partially answered?
Which ones are next?
```

This is the file to read when we want the huge list of all head questions and future analysis directions.
