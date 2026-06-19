# Mechanistic Finding v1 — Lepton isolation for Hqql/Tbl disambiguation

## Finding

ParticleNet appears to use **lepton isolation within the jet core** as an implicit discriminant for the Hqql/Tbl ambiguity.

This is a mechanistic physics finding, not a new-particle claim.

## Evidence

### Phase 1 / 3C observable evidence

Hqql->Tbl confusion rate as a function of particle0 isolation:

```text
0.00-0.10 : 0.0264
0.10-0.15 : 0.0243
0.15-0.20 : 0.0340
0.20-0.30 : 0.0724
0.30+     : 0.2558
```

The high-isolation bin has roughly a 9.7x higher Hqql->Tbl confusion rate than the low-isolation bin.

### Phase 2 / 3B causal-style evidence

Hadronic-neighbor injection around the lepton/core route often restores Hqql-like prediction. The effect appears threshold-like:

```text
fraction=0.0 -> success=0.0000
fraction=0.2 -> success=0.6533
fraction=0.4 -> success=0.6467
fraction=0.6 -> success=0.6067
fraction=0.8 -> success=0.6267
fraction=1.0 -> success=0.6200
```

A small hadronic-neighborhood perturbation is enough to break the Tbl-like route.

### Phase 3A matched control

Hqql-specific hadrons are not uniquely responsible:

```text
Hqql_correct hadrons: success=0.6200, delta_margin=+1.9644
QCD matched hadrons:  success=0.5333, delta_margin=+2.0360
```

Thus the current claim is not "special Hqql topology". The stronger claim is:

```text
ParticleNet uses lepton/core isolation and nearby hadronic activity as a physical discriminator.
```

## Physical interpretation

The network implicitly computes something like:

```text
proximity(lepton, hadronic_activity_inside_jet)
```

When the lepton/core is too isolated from hadronic activity, Hqql events become Tbl-like to the model.

This matches the physical intuition that Hqql has W->lnu plus hadronic qq activity. If the lepton is isolated from this activity, the event enters a topology where Hqql and Tbl become ambiguous.

## Next validation

Run Known Observable Residual v2 with explicit features:

```text
p0 isolation
p0 lepton flag
p0 pT rank
KNN hadron fraction
KNN charged/neutral/photon/electron/muon fractions
missing-pT proxy
lepton-core geometry
```

If the surrogate closes most of the Hqql/Tbl residual, the mechanism is largely decoded. If residual remains, inspect remaining events for additional geometry, b-like context, or pairwise/subjet features.
