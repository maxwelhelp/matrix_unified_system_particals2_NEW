# VETO_SEARCH_V1 — what protects high-isolation Hqql?

## Why this is the next question

Residual V2.1 showed:

```text
high-isolation bin 0.30+:
ParticleNet Hqql->Tbl rate = 0.2558
surrogate calibrated rate  = 0.8140
```

The surrogate says most high-isolation Hqql should become Tbl-like. ParticleNet says only about 26% do.

Therefore the next question is inverted:

```text
Not: why do confused Hqql go to Tbl?
But: what saves the other high-isolation Hqql from Tbl-readout?
```

## Groups

```text
protected_highiso:
  true=Hqql, pred=Hqql, particle0_iso >= 0.30

actual_confused_highiso:
  true=Hqql, pred=Tbl, particle0_iso >= 0.30
```

## Features to compare

Fast V1 from Phase 1 CSV:

```text
particle0_knn_charged_hadron_frac
particle0_knn_neutral_hadron_frac
particle0_knn_photon_frac
particle0_knn_electron_frac
particle0_knn_muon_frac
particle0_knn_pt_sum
missing_pt_proxy
best_lepton_iso_pt_ratio
deltaR_p0_lepton
deltaR_lead_lepton
leading_iso_pt_ratio
```

Future V2 full recomputation:

```text
knn_max_neighbor_pT
pairwise deltaR among neighbors
n_hard_charged_neighbors
second_lepton_present
lepton + hardest hadron deltaR
subjet/prong geometry
```

## Interpretation

If protected_highiso has a feature that actual_confused_highiso lacks, that feature is a candidate **veto mechanism** against false Tbl-readout.
