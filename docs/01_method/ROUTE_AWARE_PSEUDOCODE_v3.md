# Route-Aware Pseudocode v3

This layer upgrades pseudocode from:

```text
read neighbors / write evidence
```

to:

```text
which particle is activated,
which KNN neighbors feed it,
whether the route contains particle0 / leading-pT,
what class/event pattern activates the head,
and how this becomes class evidence.
```

## Inputs

```text
pseudocode_operation_database_v2.csv
edgeconv_inner_trace_heads.csv
edgeconv_inner_trace_events.csv
question_driven_head_rankings.csv
known_observable_residual_v1.json
```

## Outputs

```text
reports/latest/PSEUDOCODE_OPERATION_DATABASE_V3.md
reports/latest/tables/pseudocode_operation_database_v3.csv
reports/latest/tables/pseudocode_operation_database_v3.jsonl
manifests/latest/pseudocode_operation_database_v3.json
```

## Meaning

V3 is the current highest-level interpretation file. It should be used as the human-readable program map of ParticleNet pseudo-heads.

A typical row should say:

```text
L0/L1 build context away from direct particle0 readout.
L2 heads read this context through core/leading-pT particles.
KNN neighbor lists show which neighbor route feeds the top activated particle.
```
