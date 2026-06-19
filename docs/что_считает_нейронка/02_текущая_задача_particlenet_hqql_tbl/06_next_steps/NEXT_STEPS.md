# Next steps — current ParticleNet Hqql/Tbl task

## Immediate next scientific step

Build **Known Observable Residual V3** with pairwise/subjet/b-like geometry.

Why:

```text
V2.1 confirms lepton/core isolation is important,
but AUC=0.5908 and high-isolation bin is overpredicted.
Therefore explicit isolation/KNN/missing-pT features do not fully explain ParticleNet.
```

## Residual V3 feature candidates

```text
lepton + b-like candidate angular separation
lepton + highest charged hadron deltaR
lepton + top-k hadronic prong deltaR
pairwise charged/neutral geometry
ECF-like 2-point / 3-point approximations
tau21/tau32-like proxies
top-k subjet axis geometry
hadronic activity asymmetry around lepton/core
```

## What would count as progress

```text
AUC V2.1 = 0.5908
V3 target: significantly higher AUC and better calibrated isolation-bin rates
```

## What would be a strong finding

If V3 closes most of the residual:

```text
ParticleNet's Hqql/Tbl behavior is largely explained by lepton/core isolation plus pairwise/subjet geometry.
```

If V3 does not close residual:

```text
There is a remaining model-specific residual route, likely worth deeper event-level inspection.
```

## What not to do next

Do not return to generic head tracing unless needed. The current bottleneck is physical feature explanation, not route discovery.
