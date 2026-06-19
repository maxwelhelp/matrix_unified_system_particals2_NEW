# GEOMETRY_VETO_PATCH_V1

Patch tests for high-isolation Hqql_to_Tbl events.

## Summary
| test | n | success_to_Hqql | flip | delta_margin |
| --- | --- | --- | --- | --- |
| G1_compact_knn_injection | 11 | 0.0909 | 0.1818 | 0.3546 |
| G1_control_same_pid_pt | 11 | 0.1818 | 0.1818 | -0.6001 |
| G2_control_random_removal | 6 | 0.0000 | 0.0000 | -0.0577 |
| G2_second_lepton_removal | 6 | 0.1667 | 0.1667 | 0.5771 |
| G3_compact_knn_plus_second_lepton_removal | 6 | 0.1667 | 0.1667 | 0.5943 |

## Example rows
| test | target | donor | base | patched | success | delta_margin | idx |
| --- | --- | --- | --- | --- | --- | --- | --- |
| G1_compact_knn_injection | 12649 | 14742 | label_Tbl | label_Tbl | 0 | 0.1696 | [79, 64, 101, 22, 43, 122, 92, 13, 112, 33, 38, 117, 53, 70, 54] |
| G1_control_same_pid_pt | 12649 | 14742 | label_Tbl | label_Tbl | 0 | -0.0198 | [79, 64, 101, 22, 43, 122, 92, 13, 112, 33, 38, 117, 53, 70, 54] |
| G2_second_lepton_removal | 12649 | 14742 | label_Tbl | label_Tbl | 0 | -0.5893 | [47] |
| G2_control_random_removal | 12649 | 14742 | label_Tbl | label_Tbl | 0 | -0.0550 | [44] |
| G3_compact_knn_plus_second_lepton_removal | 12649 | 14742 | label_Tbl | label_Tbl | 0 | 0.6233 | [79, 64, 101, 22, 43, 122, 92, 13, 112, 33, 38, 117, 53, 70, 54, 47] |
| G1_compact_knn_injection | 12982 | 13089 | label_Tbl | label_Hqql | 1 | 2.7537 | [104, 82, 30, 119, 15, 67, 43, 95, 77, 25, 37, 89, 79, 27, 44] |
| G1_control_same_pid_pt | 12982 | 13089 | label_Tbl | label_Hqql | 1 | 1.7781 | [104, 82, 30, 119, 15, 67, 43, 95, 77, 25, 37, 89, 79, 27, 44] |
| G1_compact_knn_injection | 13045 | 13529 | label_Tbl | label_Tbqq | 0 | -0.6550 | [108, 122, 14, 68, 44, 98, 123, 15, 69, 41, 95, 23, 77, 103, 49] |
| G1_control_same_pid_pt | 13045 | 13529 | label_Tbl | label_Tbl | 0 | -0.6494 | [108, 122, 14, 68, 44, 98, 123, 15, 69, 41, 95, 23, 77, 103, 49] |
| G2_second_lepton_removal | 13045 | 13529 | label_Tbl | label_Hqql | 1 | 2.3321 | [2] |
| G2_control_random_removal | 13045 | 13529 | label_Tbl | label_Tbl | 0 | -0.2269 | [14] |
| G3_compact_knn_plus_second_lepton_removal | 13045 | 13529 | label_Tbl | label_Tbl | 0 | -0.0521 | [108, 122, 14, 68, 44, 98, 123, 15, 69, 41, 95, 23, 77, 103, 49, 2] |
| G1_compact_knn_injection | 13583 | 13897 | label_Tbl | label_Tbl | 0 | 1.0803 | [100, 104, 4, 54, 75, 125, 25, 61, 111, 11, 67, 117, 17, 57, 7] |
| G1_control_same_pid_pt | 13583 | 13897 | label_Tbl | label_Tbl | 0 | 0.5944 | [100, 104, 4, 54, 75, 125, 25, 61, 111, 11, 67, 117, 17, 57, 7] |
| G2_second_lepton_removal | 13583 | 13897 | label_Tbl | label_Tbl | 0 | 1.9882 | [14] |
| G2_control_random_removal | 13583 | 13897 | label_Tbl | label_Tbl | 0 | -0.0173 | [24] |
| G3_compact_knn_plus_second_lepton_removal | 13583 | 13897 | label_Tbl | label_Hqql | 1 | 2.8840 | [100, 104, 4, 54, 75, 125, 25, 61, 111, 11, 67, 117, 17, 57, 7, 14] |
| G1_compact_knn_injection | 13787 | 12358 | label_Tbl | label_Tbl | 0 | -3.2390 | [86, 121, 35, 78, 124, 81, 38, 65, 108, 22, 83, 126, 40, 62, 19] |
| G1_control_same_pid_pt | 13787 | 12358 | label_Tbl | label_Tbl | 0 | -2.1227 | [86, 121, 35, 78, 124, 81, 38, 65, 108, 22, 83, 126, 40, 62, 19] |
| G1_compact_knn_injection | 13997 | 15233 | label_Tbl | label_Tbl | 0 | 1.7203 | [86, 104, 18, 61, 70, 113, 27, 126, 40, 83, 85, 42, 119, 76, 33] |
| G1_control_same_pid_pt | 13997 | 15233 | label_Tbl | label_Tbl | 0 | -0.7327 | [86, 104, 18, 61, 70, 113, 27, 126, 40, 83, 85, 42, 119, 76, 33] |
| G1_compact_knn_injection | 14711 | 14991 | label_Tbl | label_Tbl | 0 | -0.4468 | [74, 119, 45, 34, 108, 93, 19, 32, 106, 99, 25, 63, 38, 112, 103] |
| G1_control_same_pid_pt | 14711 | 14991 | label_Tbl | label_Tbl | 0 | -1.4309 | [74, 119, 45, 34, 108, 93, 19, 32, 106, 99, 25, 63, 38, 112, 103] |
| G2_second_lepton_removal | 14711 | 14991 | label_Tbl | label_Tbl | 0 | 0.1565 | [66] |
| G2_control_random_removal | 14711 | 14991 | label_Tbl | label_Tbl | 0 | 0.0006 | [59] |
| G3_compact_knn_plus_second_lepton_removal | 14711 | 14991 | label_Tbl | label_Tbl | 0 | -0.5702 | [74, 119, 45, 34, 108, 93, 19, 32, 106, 99, 25, 63, 38, 112, 103, 66] |
| G1_compact_knn_injection | 15288 | 13897 | label_Tbl | label_Tbl | 0 | 0.8567 | [94, 125, 31, 78, 103, 56, 9, 57, 104, 10, 86, 39, 102, 55, 8] |
| G1_control_same_pid_pt | 15288 | 13897 | label_Tbl | label_Hqql | 1 | 1.0903 | [94, 125, 31, 78, 103, 56, 9, 57, 104, 10, 86, 39, 102, 55, 8] |
| G1_compact_knn_injection | 15528 | 14625 | label_Tbl | label_Tbl | 0 | -0.2659 | [109, 86, 33, 18, 71, 124, 92, 39, 52, 105, 87, 34, 110, 57, 4] |
| G1_control_same_pid_pt | 15528 | 14625 | label_Tbl | label_Tbl | 0 | -1.3636 | [109, 86, 33, 18, 71, 124, 92, 39, 52, 105, 87, 34, 110, 57, 4] |
| G2_second_lepton_removal | 15528 | 14625 | label_Tbl | label_Tbl | 0 | 0.1407 | [15] |
| G2_control_random_removal | 15528 | 14625 | label_Tbl | label_Tbl | 0 | -0.1599 | [22] |
| G3_compact_knn_plus_second_lepton_removal | 15528 | 14625 | label_Tbl | label_Tbl | 0 | 0.1457 | [109, 86, 33, 18, 71, 124, 92, 39, 52, 105, 87, 34, 110, 57, 4, 15] |
| G1_compact_knn_injection | 15658 | 14625 | label_Tbl | label_Tbl | 0 | 0.9513 | [73, 116, 43, 49, 122, 107, 34, 41, 114, 75, 2, 5, 78, 97, 24, 65] |
| G1_control_same_pid_pt | 15658 | 14625 | label_Tbl | label_Tbl | 0 | -1.1548 | [73, 116, 43, 49, 122, 107, 34, 41, 114, 75, 2, 5, 78, 97, 24, 65] |
| G2_second_lepton_removal | 15658 | 14625 | label_Tbl | label_Tbl | 0 | -0.5654 | [5] |
| G2_control_random_removal | 15658 | 14625 | label_Tbl | label_Tbl | 0 | 0.1125 | [69] |
| G3_compact_knn_plus_second_lepton_removal | 15658 | 14625 | label_Tbl | label_Tbl | 0 | 0.5353 | [73, 116, 43, 49, 122, 107, 34, 41, 114, 75, 2, 5, 78, 97, 24, 65, 5] |
| G1_compact_knn_injection | 15893 | 14381 | label_Tbl | label_Tbl | 0 | 0.9758 | [90, 88, 43, 24, 69, 114, 86, 41, 40, 85, 72, 117, 27, 76, 31] |
| G1_control_same_pid_pt | 15893 | 14381 | label_Tbl | label_Tbl | 0 | -2.5894 | [90, 88, 43, 24, 69, 114, 86, 41, 40, 85, 72, 117, 27, 76, 31] |

## Interpretation

G1 tests compact lepton-centered KNN geometry. G2 tests second-lepton ambiguity. G3 tests whether the two mechanisms are additive. Compare each targeted test with its control before raising claim level.
