# Known Observable Residual v2 — Hqql/Tbl lepton-isolation surrogate

This report tests whether explicit lepton/core isolation and hadronic-neighborhood features explain the Hqql/Tbl ambiguity found in Phases 1-3.

## Three numbers
| metric | value |
| --- | --- |
| surrogate_v2_acc_correct_test | 0.6299 |
| ParticleNet_acc_correct_test | 1.0000 |
| surrogate_v2_acc_confused_eval | 0.4548 |
| ParticleNet_acc_confused_eval | 0.0000 |
| surrogate_agreement_with_ParticleNet_on_confused | 0.5452 |

## Summary by split/group
| split | n | surrogate_acc | ParticleNet_acc | agreement | surrogate_tbl_rate | ParticleNet_tbl_rate |
| --- | --- | --- | --- | --- | --- | --- |
| correct_test | 2340 | 0.6299 | 1.0000 | 0.6299 | 0.6128 | 0.5009 |
| confused_eval | 299 | 0.4548 | 0.0000 | 0.5452 | 0.3880 | 0.5151 |
| all_hqql_tbl | 8098 | 0.6146 | 0.9631 | 0.6179 | 0.6111 | 0.5042 |
| train_correct | 5459 | 0.6168 | 1.0000 | 0.6168 | 0.6226 | 0.5050 |
| Hqql_correct | 3870 | 0.5010 | 1.0000 | 0.5010 | 0.4990 | 0.0000 |
| Hqql_to_Tbl | 154 | 0.5649 | 0.0000 | 0.4351 | 0.4351 | 1.0000 |
| Tbl_correct | 3929 | 0.7386 | 1.0000 | 0.7386 | 0.7386 | 1.0000 |
| Tbl_to_Hqql | 145 | 0.3379 | 0.0000 | 0.6621 | 0.3379 | 0.0000 |

## Hqql->Tbl rate by isolation bin
| bin | n_hqql | ParticleNet_rate | surrogate_rate | gap |
| --- | --- | --- | --- | --- |
| 0.00-0.10 | 492 | 0.0264 | 0.3476 | 0.3211 |
| 0.10-0.15 | 1442 | 0.0243 | 0.3717 | 0.3474 |
| 0.15-0.20 | 1384 | 0.0340 | 0.5629 | 0.5289 |
| 0.20-0.30 | 663 | 0.0724 | 0.7134 | 0.6410 |
| 0.30+ | 43 | 0.2558 | 0.9070 | 0.6512 |

## Top explicit features
| feature | abs_weight |
| --- | --- |
| best_lepton_iso_pt_ratio | 0.3725 |
| particle0_knn_muon_frac | 0.3603 |
| particle0_knn_electron_frac | 0.3465 |
| particle0_knn_charged_hadron_frac | 0.3073 |
| best_lepton_pt | 0.2575 |
| has_lepton | 0.2411 |
| deltaR_p0_lepton | 0.2397 |
| deltaR_lead_lepton | 0.2397 |
| missing_pt_proxy | 0.1722 |
| particle0_knn_pt_sum | 0.1673 |
| particle0_knn_photon_frac | 0.1504 |
| confidence | 0.1062 |
| particle0_is_lepton | 0.0908 |
| leading_is_lepton | 0.0908 |
| particle0_is_muon | 0.0720 |
| particle0_pt | 0.0687 |
| leading_pt | 0.0687 |
| particle0_knn_neutral_hadron_frac | 0.0282 |
| particle0_charge | 0.0271 |
| particle0_is_electron | 0.0073 |
| particle0_iso_pt_ratio | 0.0061 |
| leading_iso_pt_ratio | 0.0061 |
| particle0_pt_rank | 0.0000 |
| leading_pt_rank | 0.0000 |

## Interpretation

If the surrogate reproduces ParticleNet isolation-bin confusion rates and closes confused/correct behavior, the lepton-isolation mechanism is mostly decoded. If not, inspect the residual events for additional b-like, pairwise, or subjet geometry.
