# VETO_SEARCH_V1

Question: what protects high-isolation true Hqql events from false Tbl-readout?

## Groups
| group | n | particle0_pid_modes | leading_pid_modes |
| --- | --- | --- | --- |
| protected_highiso = Hqql_correct iso>=thr | 32 | muon:16, electron:15, charged_hadron:1 | muon:16, electron:15, charged_hadron:1 |
| actual_confused_highiso = Hqql_to_Tbl iso>=thr | 11 | electron:7, muon:3, photon:1 | electron:7, muon:3, photon:1 |

## Top protected-higher candidates (possible veto features)
| feature | protected_mean | confused_mean | diff | ratio | std_effect |
| --- | --- | --- | --- | --- | --- |
| confidence | 0.8904 | 0.8127 | 0.0778 | 1.0957 | 0.6326 |
| best_lepton_charge | 0.0625 | -0.4545 | 0.5170 | -0.1375 | 0.5303 |
| best_lepton_is_muon | 0.5312 | 0.2727 | 0.2585 | 1.9479 | 0.5303 |
| leading_charge | 0.1250 | -0.3636 | 0.4886 | -0.3438 | 0.5052 |
| particle0_charge | 0.1250 | -0.3636 | 0.4886 | -0.3438 | 0.5052 |
| best_lepton_knn_muon_frac | 0.0605 | 0.0341 | 0.0265 | 1.7760 | 0.4722 |
| leading_is_muon | 0.5000 | 0.2727 | 0.2273 | 1.8333 | 0.4657 |
| particle0_is_muon | 0.5000 | 0.2727 | 0.2273 | 1.8333 | 0.4657 |
| particle0_knn_muon_frac | 0.0586 | 0.0341 | 0.0245 | 1.7187 | 0.4334 |
| leading_knn_muon_frac | 0.0586 | 0.0341 | 0.0245 | 1.7187 | 0.4334 |
| best_lepton_knn_pt_sum | 604.1571 | 525.4551 | 78.7020 | 1.1498 | 0.3104 |
| leading_is_charged_hadron | 0.0312 | 0.0000 | 0.0312 | 999.0000 | 0.2500 |
| particle0_is_charged_hadron | 0.0312 | 0.0000 | 0.0312 | 999.0000 | 0.2500 |
| leading_is_lepton | 0.9688 | 0.9091 | 0.0597 | 1.0656 | 0.2414 |
| particle0_is_lepton | 0.9688 | 0.9091 | 0.0597 | 1.0656 | 0.2414 |

## Top confused-higher candidates (possible Tbl trigger features)
| feature | protected_mean | confused_mean | diff | ratio | std_effect |
| --- | --- | --- | --- | --- | --- |
| leading_iso_pt_ratio | 0.3132 | 0.3343 | -0.0211 | 0.9370 | -0.6109 |
| particle0_iso_pt_ratio | 0.3132 | 0.3343 | -0.0211 | 0.9370 | -0.6109 |
| best_lepton_is_electron | 0.4688 | 0.7273 | -0.2585 | 0.6445 | -0.5303 |
| leading_is_photon | 0.0000 | 0.0909 | -0.0909 | 0.0000 | -0.4264 |
| particle0_is_photon | 0.0000 | 0.0909 | -0.0909 | 0.0000 | -0.4264 |
| deltaR_p0_lepton | 0.0031 | 0.0606 | -0.0575 | 0.0513 | -0.4032 |
| deltaR_lead_lepton | 0.0031 | 0.0606 | -0.0575 | 0.0513 | -0.4032 |
| best_lepton_pt_rank | 0.0312 | 0.2727 | -0.2415 | 0.1146 | -0.3705 |
| best_lepton_knn_electron_frac | 0.0625 | 0.0852 | -0.0227 | 0.7333 | -0.3363 |
| leading_is_electron | 0.4688 | 0.6364 | -0.1676 | 0.7366 | -0.3314 |
| particle0_is_electron | 0.4688 | 0.6364 | -0.1676 | 0.7366 | -0.3314 |
| best_lepton_knn_neutral_hadron_frac | 0.0723 | 0.0966 | -0.0243 | 0.7482 | -0.2387 |
| particle0_pt | 268.5531 | 292.2207 | -23.6677 | 0.9190 | -0.2172 |
| leading_pt | 268.5531 | 292.2207 | -23.6677 | 0.9190 | -0.2172 |
| particle0_knn_electron_frac | 0.0625 | 0.0739 | -0.0114 | 0.8462 | -0.1644 |

## Interpretation

Protected-higher features are candidate veto mechanisms: they may prevent a high-isolation Hqql event from becoming Tbl-like. Confused-higher features are candidate trigger mechanisms for false Tbl-readout. V1 uses Phase 1 CSV features only; if a candidate appears, V2 should recompute full KNN geometry such as max neighbor pT, pairwise deltaR spread, and hard charged neighbor counts.
