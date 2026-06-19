# Finding — Lepton/core isolation inside jet

## Short statement

ParticleNet uses lepton/core isolation inside the jet as an implicit discriminator for Hqql/Tbl ambiguity.

## Evidence

### Isolation bins

```text
Hqql->Tbl confusion rate:
0.00-0.10 : 0.0264
0.10-0.15 : 0.0243
0.15-0.20 : 0.0340
0.20-0.30 : 0.0724
0.30+     : 0.2558
```

The highest isolation bin has about 9.7x higher confusion rate than the lowest bin.

### Phase 3B threshold effect

```text
fraction=0.0 -> success=0.0000
fraction=0.2 -> success=0.6533
fraction=0.4 -> success=0.6467
fraction=0.6 -> success=0.6067
fraction=0.8 -> success=0.6267
fraction=1.0 -> success=0.6200
```

A small hadronic-neighborhood replacement already breaks the Tbl-like route.

### Matched control

```text
Hqql_correct hadrons: success=0.6200, delta_margin=+1.9644
QCD matched hadrons:  success=0.5333, delta_margin=+2.0360
```

This says the current effect is mostly about hadronic density / isolation, not uniquely Hqql-specific topology.

## Physical interpretation

The network implicitly computes something like:

```text
proximity(lepton, hadronic_activity_inside_jet)
```

When lepton/core is too isolated from hadronic activity, Hqql becomes Tbl-like to ParticleNet.

## Residual

Explicit features do not fully reproduce the model. V2.1 behavior surrogate has AUC 0.5908 and overpredicts the high-isolation bin. Therefore the next needed features are pairwise/subjet/b-like geometry.
