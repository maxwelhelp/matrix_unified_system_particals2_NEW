# Current status — ParticleNet Hqql/Tbl

## What is already established

### 1. Phase 1 statistics passed

```text
Hqql_to_Tbl = 154
Tbl_to_Hqql = 145
status = PASS
```

This is enough to stop reasoning from a few examples and start treating Hqql/Tbl confusion as a physical regime.

### 2. Observable finding: lepton/core isolation

Hqql->Tbl confusion rate by particle0 isolation:

```text
0.00-0.10 : 0.0264
0.10-0.15 : 0.0243
0.15-0.20 : 0.0340
0.20-0.30 : 0.0724
0.30+     : 0.2558
```

High-isolation Hqql events are much more likely to be predicted as Tbl.

### 3. Patch/control result

Hadronic-neighbor injection around the lepton/core often restores Hqql-like prediction, but random controls are also strong. Therefore causal patch evidence is suggestive, not final.

### 4. Residual V2/V2.1

Explicit isolation/KNN/missing-pT features confirm the direction, but do not fully reproduce ParticleNet behavior.

V2.1 behavior surrogate:

```text
AUC = 0.5908
accuracy = 0.9296, but class imbalance makes this less informative
```

Surrogate captures high-isolation risk but overpredicts the highest bin.

## Current claim level

Allowed claim:

```text
ParticleNet implicitly uses lepton/core isolation inside jet as a mechanistic discriminator for Hqql/Tbl ambiguity.
```

Not allowed yet:

```text
new particle / new interaction / final physics discovery
```

## Current residual

The network likely uses additional geometry beyond isolation:

```text
b-like candidate context
pairwise/subjet geometry
ECF-like 2/3-point features
tau-like proxies
angular separation between lepton and hadronic prongs
```
