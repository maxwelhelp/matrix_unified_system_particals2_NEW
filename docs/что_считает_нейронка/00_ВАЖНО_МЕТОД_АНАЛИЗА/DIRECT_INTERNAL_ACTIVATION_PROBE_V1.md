# DIRECT_INTERNAL_ACTIVATION_PROBE_V1

## Critical correction

We were underusing the strongest advantage of this project.

We have partial/full access to internal model computations, but recently we mostly used external methods:

```text
bins
patches
surrogates
feature rankers
```

These methods are useful when the model is a black box. But our goal is interpretability. Once an external analysis gives a concrete physical hypothesis, the next step should be direct internal verification.

Short version:

```text
External methods find the physical question.
Internal activations answer what the network actually represents.
```

## What was wrong

The external path was not useless. It gave the Hqql/Tbl physical hypothesis:

```text
high lepton/core isolation -> Tbl-risk
spread lepton-centered KNN geometry -> false Tbl trigger candidate
second-lepton ambiguity -> false Tbl trigger candidate
```

But after this point, continuing only with patch/surrogate tests is inefficient.

We should not try to guess internal mechanisms from stdout-style outputs if we can inspect internal activations directly.

## New rule

After a hypothesis becomes physically concrete, run direct activation contrast before more patch variations.

```text
confusion/bins/patch/surrogate -> hypothesis
hypothesis -> direct internal activation contrast
activation contrast -> channel/head mechanism
then patch only the discovered internal mechanism
```

## Current direct test for Hqql/Tbl

Use three event groups:

```text
A = protected_highiso
    true=Hqql, pred=Hqql, isolation>0.30

B = confused_highiso
    true=Hqql, pred=Tbl, isolation>0.30

C = Tbl_correct
    true=Tbl, pred=Tbl
```

Questions:

```text
1. Which L2 activation channels separate B from A?
2. Is B closer to C than to A in activation space?
3. Which channels satisfy B != A and B ~= C?
4. Which input particles contribute to those channels?
```

The important interpretation:

```text
B ~= C in L2 space:
  the network really represents confused Hqql as Tbl-like.

B != A but B not ~= C:
  the network may simply lose Hqql evidence, not actively build Tbl evidence.
```

## Known channel groups to prioritize

Earlier traces suggested pseudo-head/channel groups such as:

```text
L2_ch224:256
L2_ch128:160
L2_ch160:192
```

Do not assume these are final. Start with all L2 channel groups if available, then rank.

## Metrics to compute

For every layer/channel group:

```text
mean_activation_A
mean_activation_B
mean_activation_C
std_effect_B_minus_A
std_effect_B_minus_C
cosine_distance(B,A)
cosine_distance(B,C)
tbl_like_score = distance(B,A) - distance(B,C)
```

High `tbl_like_score` means B is closer to Tbl_correct than to protected Hqql.

## Second-lepton direct test

For confused events where second_lepton_present=True:

```text
look at L1/L2 activations for the second lepton particle
compare against:
  best lepton particle
  random non-lepton particle
  Tbl_correct second-lepton-like objects
```

Question:

```text
Does the network encode the second lepton as a Tbl/top-cascade-like signal?
```

If yes, this is direct evidence for the second-lepton trigger mechanism.

## Output expected from direct probe

The direct probe should write:

```text
reports/latest/INTERNAL_ACTIVATION_CONTRAST_V1.md
reports/latest/tables/internal_activation_group_contrasts.csv
reports/latest/tables/internal_activation_channel_contrasts.csv
reports/latest/tables/internal_activation_particle_attribution.csv
manifests/latest/internal_activation_contrast_v1.json
```

Each row should contain:

```text
layer
group_or_channel
A_mean
B_mean
C_mean
B_minus_A_effect
B_minus_C_effect
B_closer_to_C_score
interpretation
next_action
```

## Claim upgrade condition

If we find channels where:

```text
B differs from A
B is close to C
those channels localize to second-lepton or spread KNN geometry
```

then the Hqql/Tbl hypothesis becomes much stronger than patch-only evidence.

Possible claim:

```text
ParticleNet internally maps high-isolation confused Hqql events toward the Tbl activation manifold, driven by second-lepton / lepton-centered geometry channels.
```

## Practical next command

Before writing a new extractor, locate existing activation/supertrace outputs locally:

```bash
find reports manifests runs -iname '*supertrace*' -o -iname '*activation*' -o -iname '*head*' | sort | head -200
find reports/latest/tables -type f | grep -Ei 'head|activation|supertrace|trace|channel|pseudo'
```

If those files exist, build `internal_activation_contrast_v1.py` as a reader/aggregator.
If not, add hooks to ParticleNet forward pass to export L1/L2 activations for groups A/B/C.
