# INTERNAL_ACTIVATION_CONTRAST_V2_1

V2 showed a mixed mechanism:

```text
L1_ch80:96 and L1_ch32:48:
  active Tbl-like route contribution in confused Hqql

L2_ch128:160 and L2_ch224:256:
  loss of Hqql evidence, not clean Tbl activation
```

V2.1 answers the missing particle-level question:

```text
Which particles activate the L1 Tbl-like route in B_confused_highiso?
```

## Particle roles

For each top particle from `internal_activation_contrast_v2_top_particles.csv`, V2.1 annotates:

```text
particle0_best_lepton
particle0
best_lepton
second_lepton
nearest_hadron_to_best_lepton
hardest_hadron
hard_hadron
hadron_neighbor
photon_neighbor
other_lepton
other
```

## Main test

Focus heads:

```text
L1_ch80:96   # strongest active Tbl-like route candidate
L1_ch32:48   # secondary active Tbl-like route candidate
L2_ch128:160 # lost Hqql class-evidence head
```

Compare role rates in:

```text
A_protected_highiso
B_confused_highiso
C_Tbl_correct
```

## Interpretation

If `second_lepton` top-rate is high in B for L1_ch80:96 and low in A:

```text
second lepton directly triggers Tbl-like L1 route
```

If hadron roles / far or hard hadron roles dominate in B:

```text
spread lepton-centered KNN geometry triggers Tbl-like L1 route
```

If particle0/best_lepton dominates in both A and B but activation differs:

```text
the same core particle is read differently because its neighborhood context differs
```

This is the last missing step before a clean mechanistic claim.
