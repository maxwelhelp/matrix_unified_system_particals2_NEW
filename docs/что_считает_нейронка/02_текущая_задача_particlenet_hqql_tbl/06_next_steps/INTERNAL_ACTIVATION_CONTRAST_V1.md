# INTERNAL_ACTIVATION_CONTRAST_V1 — next step for Hqql/Tbl

## Why this replaces more blind patching

External analysis has already produced a concrete physical hypothesis:

```text
high isolation creates Tbl-risk
spread lepton-centered KNN geometry is suspicious
second-lepton ambiguity is suspicious
```

Now we should inspect the network directly.

## Groups

```text
A protected_highiso:
  true=Hqql, pred=Hqql, isolation>0.30

B confused_highiso:
  true=Hqql, pred=Tbl, isolation>0.30

C Tbl_correct:
  true=Tbl, pred=Tbl
```

## Main question

```text
Does B look internally like C or just unlike A?
```

Interpretation:

```text
B ~= C:
  real Tbl-like internal readout

B != A but B not ~= C:
  loss of Hqql evidence, not necessarily Tbl evidence
```

## Channel groups to check first

```text
L2_ch224:256
L2_ch128:160
L2_ch160:192
all L2 groups if available
```

## Tables to produce

```text
internal_activation_group_contrasts.csv
internal_activation_channel_contrasts.csv
internal_activation_particle_attribution.csv
```

## Required metrics

```text
mean activation by group A/B/C
B-A effect
B-C effect
B closer to C score
channel rank
event examples
particle attribution if available
```

## Direct second-lepton test

For confused_highiso with second_lepton_present=True:

```text
compare activation on:
  best lepton
  second lepton
  random non-lepton
  Tbl_correct lepton-like objects
```

Question:

```text
Does second lepton activate Tbl/top-cascade-like internal channels?
```

## First local search command

```bash
cd "$HOME/Рабочий стол/matrix_unified_system_particals"

find reports manifests runs -iname '*supertrace*' -o -iname '*activation*' -o -iname '*head*' | sort | head -200
find reports/latest/tables -type f | grep -Ei 'head|activation|supertrace|trace|channel|pseudo'
```

If activation outputs exist, analyze them directly. If not, add a new extractor hook to ParticleNet and dump only A/B/C events, not the whole dataset.
