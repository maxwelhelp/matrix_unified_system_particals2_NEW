# VETO_SEARCH_V2 — full KNN geometry

## Why V2 is needed

VETO_SEARCH_V1 found a real contrast inside high-isolation Hqql events:

```text
protected_highiso = Hqql_correct, iso>=0.30, n=32
actual_confused_highiso = Hqql_to_Tbl, iso>=0.30, n=11
```

V1 hints:

```text
protected-higher:
  muon-like core/lepton
  positive/less-negative charge
  higher KNN muon fraction
  higher KNN pT sum

confused-higher:
  higher isolation
  electron/photon-like core/lepton
  larger deltaR p0-lepton
  higher electron/neutral-hadron KNN fractions
```

But V1 uses Phase 1 CSV features only. It cannot see full KNN geometry.

## V2 question

```text
What exactly vetoes false Tbl-readout for high-isolation Hqql events?
```

## Groups

```text
protected_highiso:
  true=Hqql, pred=Hqql, particle0_iso>=0.30

actual_confused_highiso:
  true=Hqql, pred=Tbl, particle0_iso>=0.30
```

## New features to recompute

```text
knn_max_neighbor_pt
knn_sum_neighbor_pt
knn_mean_neighbor_pt
knn_hard_neighbor_count
knn_hard_charged_count
knn_hard_hadron_count
knn_pairwise_deltaR_mean
knn_pairwise_deltaR_std
knn_pairwise_deltaR_min
knn_deltaR_to_p0_mean
knn_deltaR_to_p0_min
lepton_hardest_hadron_deltaR
lepton_nearest_hadron_deltaR
second_lepton_present
second_lepton_pt
```

## Interpretation

Protected-higher features are veto candidates.
Confused-higher features are false Tbl trigger candidates.

If protected high-isolation events have harder/closer charged or hadronic KNN structure, then the veto mechanism is:

```text
high isolation creates Tbl-risk,
but compact/hard hadronic KNN geometry protects Hqql.
```
