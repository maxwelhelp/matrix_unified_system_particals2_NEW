# Known Observable Residual v2.1 — Hqql behavior surrogate

This report predicts ParticleNet behavior on true Hqql events: whether ParticleNet outputs Tbl. It is better calibrated for the isolation-regime question than V2 true-label surrogate.

## Summary
| metric | value |
| --- | --- |
| n_hqql | 4024.0000 |
| train_n | 2816.0000 |
| test_n | 1208.0000 |
| train_particlenet_hqql_to_tbl_rate | 0.0391 |
| test_particlenet_hqql_to_tbl_rate | 0.0364 |
| behavior_surrogate_acc_test | 0.9296 |
| behavior_surrogate_auc_test | 0.5908 |
| calibrated_threshold | 0.4838 |

## Hqql->Tbl behavior by isolation bin
| bin | n | ParticleNet_rate | surrogate_prob_mean | surrogate_calibrated_rate | gap_rate |
| --- | --- | --- | --- | --- | --- |
| 0.00-0.10 | 492 | 0.0264 | 0.0970 | 0.0000 | -0.0264 |
| 0.10-0.15 | 1442 | 0.0243 | 0.1566 | 0.0000 | -0.0243 |
| 0.15-0.20 | 1384 | 0.0340 | 0.2442 | 0.0029 | -0.0311 |
| 0.20-0.30 | 663 | 0.0724 | 0.3848 | 0.1780 | 0.1056 |
| 0.30+ | 43 | 0.2558 | 0.6130 | 0.8140 | 0.5581 |

## Top features
| feature | abs_weight |
| --- | --- |
| best_lepton_iso_pt_ratio | 0.3052 |
| missing_pt_proxy | 0.2582 |
| particle0_iso_pt_ratio | 0.1625 |
| leading_iso_pt_ratio | 0.1625 |
| deltaR_p0_lepton | 0.1449 |
| deltaR_lead_lepton | 0.1449 |
| particle0_knn_pt_sum | 0.1386 |
| particle0_is_lepton | 0.1353 |
| leading_is_lepton | 0.1353 |
| particle0_knn_charged_hadron_frac | 0.1316 |
| particle0_is_muon | 0.1161 |
| particle0_knn_photon_frac | 0.0700 |
| particle0_knn_neutral_hadron_frac | 0.0686 |
| particle0_knn_electron_frac | 0.0453 |
| particle0_charge | 0.0395 |
| particle0_pt | 0.0195 |
| particle0_is_electron | 0.0149 |
| particle0_knn_muon_frac | 0.0048 |

## Interpretation

If calibrated surrogate rates follow ParticleNet rates across bins, explicit isolation/core/KNN observables explain model behavior. If not, remaining residual likely needs b-like, pairwise, or subjet geometry.
