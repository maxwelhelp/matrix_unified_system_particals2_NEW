# VETO_SEARCH_V2_FULL_KNN_GEOMETRY

Full KNN geometry contrast for high-isolation Hqql protected vs actual-confused events. This version tests the core-lepton alignment hypothesis.

## Groups
| group | n | p0_pid_modes | p0_is_lepton_aligned_rate |
| --- | --- | --- | --- |
| protected_highiso | 32 | muon:16, electron:15, charged_hadron:1 | 0.9688 |
| actual_confused_highiso | 11 | electron:7, muon:3, photon:1 | 0.9091 |

## Protected-higher candidates / possible veto
| feature | protected_mean | confused_mean | diff | ratio | std_effect |
| --- | --- | --- | --- | --- | --- |
| lep_knn_size | 15.7500 | 15.2727 | 0.4773 | 1.0312 | 1.0519 |
| lep_knn_lepton_count | 1.7188 | 1.1818 | 0.5369 | 1.4543 | 0.9564 |
| lep_knn_sum_pt | 534.2228 | 341.6322 | 192.5906 | 1.5637 | 0.9335 |
| p0_knn_lepton_count | 1.6875 | 1.0909 | 0.5966 | 1.5469 | 0.9232 |
| lep_knn_mean_pt | 33.7454 | 22.3098 | 11.4356 | 1.5126 | 0.8873 |
| lep_knn_lepton_frac | 0.1087 | 0.0773 | 0.0315 | 1.4070 | 0.8758 |
| p0_knn_lepton_frac | 0.1068 | 0.0712 | 0.0356 | 1.4993 | 0.8583 |
| p0_knn_size | 15.7500 | 15.3636 | 0.3864 | 1.0251 | 0.8163 |
| lepton_hardest_hadron_pt | 60.9932 | 41.8379 | 19.1553 | 1.4578 | 0.5616 |
| lep_knn_muon_frac | 0.0549 | 0.0295 | 0.0254 | 1.8598 | 0.4838 |
| p0_knn_sum_pt | 527.0839 | 417.7545 | 109.3295 | 1.2617 | 0.4624 |
| p0_knn_muon_frac | 0.0530 | 0.0295 | 0.0234 | 1.7937 | 0.4429 |
| p0_knn_mean_pt | 33.2993 | 27.0184 | 6.2808 | 1.2325 | 0.4289 |
| p0_is_lepton_aligned | 0.9688 | 0.9091 | 0.0597 | 1.0656 | 0.2414 |
| p0_idx_equals_best_lepton | 0.9688 | 0.9091 | 0.0597 | 1.0656 | 0.2414 |

## Confused-higher candidates / possible false-Tbl trigger
| feature | protected_mean | confused_mean | diff | ratio | std_effect |
| --- | --- | --- | --- | --- | --- |
| lep_knn_hard_hadron_count | 2.7188 | 4.1818 | -1.4631 | 0.6501 | -1.0209 |
| lep_knn_pairwise_deltaR_max | 0.1931 | 0.2917 | -0.0987 | 0.6618 | -1.0118 |
| lep_knn_pairwise_deltaR_mean | 0.0915 | 0.1362 | -0.0447 | 0.6719 | -0.9919 |
| lepton_hardest_hadron_deltaR | 0.2503 | 0.3751 | -0.1248 | 0.6673 | -0.9877 |
| lepton_nearest_hadron_deltaR | 0.0799 | 0.1346 | -0.0547 | 0.5937 | -0.9563 |
| p0_knn_deltaR_to_center_mean | 0.0855 | 0.1636 | -0.0781 | 0.5225 | -0.9555 |
| lep_knn_deltaR_to_center_mean | 0.0875 | 0.1596 | -0.0721 | 0.5482 | -0.9525 |
| p0_knn_pairwise_deltaR_max | 0.1895 | 0.3457 | -0.1562 | 0.5482 | -0.8640 |
| second_lepton_present | 0.1562 | 0.5455 | -0.3892 | 0.2865 | -0.8609 |
| p0_knn_pairwise_deltaR_mean | 0.0903 | 0.1652 | -0.0749 | 0.5467 | -0.8428 |
| p0_knn_hard_hadron_count | 2.6875 | 3.8182 | -1.1307 | 0.7039 | -0.7939 |
| second_lepton_pt | 1.2084 | 5.2144 | -4.0060 | 0.2317 | -0.6868 |
| p0_iso | 0.3132 | 0.3343 | -0.0211 | 0.9370 | -0.6109 |
| lep_knn_hard_charged_count | 2.3438 | 3.1818 | -0.8381 | 0.7366 | -0.5844 |
| p0_knn_hard_charged_count | 2.3125 | 3.0909 | -0.7784 | 0.7482 | -0.5395 |

## Interpretation

Primary hypothesis: high isolation creates Tbl-risk; p0-lepton alignment and lepton-centric hard/charged/hadronic KNN geometry may veto false Tbl-readout. If confused-higher `computed_deltaR_p0_lepton` or lower `p0_is_lepton_aligned` dominates, the next mechanism is core/lepton mismatch rather than muon/electron PID alone.
