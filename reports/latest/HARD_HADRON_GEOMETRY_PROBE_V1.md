# HARD_HADRON_GEOMETRY_PROBE_V1

Checks whether hard-hadron top activators of L1_ch80:96 enter best-lepton KNN, how close they are to the lepton, and whether the same particles also reach L2_ch128:160 top3.

## Summary
| group | role | n | deltaR_lep | in_lep_KNN | knn_rank | pt | L2_same_top3 | L1_act | L2_act_if_top3 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A_protected_highiso | hadron_neighbor | 44 | 0.4070 | 0.0682 | 93.2273 | 3.7869 | 0.0000 | 35.6500 | 0.0000 |
| A_protected_highiso | hard_hadron | 5 | 0.1981 | 0.2000 | 82.2000 | 18.0586 | 0.0000 | 27.4060 | 0.0000 |
| A_protected_highiso | nearest_hadron_to_best_lepton | 1 | 0.0784 | 1.0000 | 3.0000 | 4.0823 | 0.0000 | 33.7750 | 0.0000 |
| B_confused_highiso | hadron_neighbor | 14 | 0.6909 | 0.1429 | 86.1429 | 4.6003 | 0.0000 | 41.9766 | 0.0000 |
| B_confused_highiso | hard_hadron | 7 | 0.2316 | 0.1429 | 86.7143 | 10.5800 | 0.0000 | 32.2979 | 0.0000 |
| C_Tbl_correct | hadron_neighbor | 158 | 0.6453 | 0.0190 | 97.3481 | 5.0499 | 0.0190 | 40.8149 | 0.0237 |
| C_Tbl_correct | hard_hadron | 24 | 0.3598 | 0.0000 | 99.0000 | 25.2012 | 0.0417 | 28.6904 | 0.1097 |
| C_Tbl_correct | hardest_hadron | 4 | 0.2579 | 0.0000 | 99.0000 | 54.8969 | 0.0000 | 31.8526 | 0.0000 |
| C_Tbl_correct | nearest_hadron_to_best_lepton | 11 | 0.1959 | 0.8182 | 24.0909 | 9.5697 | 0.0000 | 34.4880 | 0.0000 |

## Interpretation

If B_confused hard hadrons have lower deltaR to best_lepton and higher in_lep_KNN rate than A, then L1_ch80:96 is driven by lepton-neighborhood hadronic contamination. If the same particles do not appear in L2_ch128:160 top activations, L2 does not recover Hqql evidence from that context.
