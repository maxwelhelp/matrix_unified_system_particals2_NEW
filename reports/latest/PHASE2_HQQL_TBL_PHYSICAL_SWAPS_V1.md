# Phase 2 Hqql/Tbl Physical Swaps v1

Physical causal tests for Hqql/Tbl ambiguity.

## Summary
| test | target_group | n | flip | success_to_Hqql | delta_margin | delta_base_logit |
| --- | --- | --- | --- | --- | --- | --- |
| 2A_isolation_hadronic_injection | Hqql_to_Tbl | 150 | 0.6667 | 0.6200 | 1.9644 | -3.0571 |
| 2C_neighbor_swap | Hqql_to_Tbl | 150 | 0.3800 | 0.3400 | 0.4108 | -3.1487 |
| random_same_count | Hqql_to_Tbl | 150 | 0.5800 | 0.5333 | 1.4397 | -1.2367 |
| 2B_lepton_core_swap | Tbl_correct | 150 | 0.3133 | 0.1600 | 4.7451 | -3.0754 |
| random_same_count | Tbl_correct | 150 | 0.1733 | 0.1600 | 4.5344 | -0.9294 |

## Example rows
| test | target | donor | group | base | patched | success_Hqql | d_margin | p0 | donor_p0 | idx |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2A_isolation_hadronic_injection | 12293 | 12929 | Hqql_to_Tbl | label_Tbl | label_Hqql | 1 | 7.3530 | electron | electron | [75, 25, 100, 125, 118, 93, 68, 18] |
| 2C_neighbor_swap | 12293 | 12929 | Hqql_to_Tbl | label_Tbl | label_Tbl | 0 | 3.2441 | electron | electron | [75, 25, 100, 125, 118, 93, 68, 18] |
| random_same_count | 12293 | 12929 | Hqql_to_Tbl | label_Tbl | label_Hqql | 1 | 8.5259 | electron | electron | [7, 35, 12, 99, 53, 14, 108, 116] |
| 2A_isolation_hadronic_injection | 12298 | 14605 | Hqql_to_Tbl | label_Tbl | label_Tbl | 0 | 1.5717 | electron | charged_hadron | [72, 48, 60, 12, 24, 36, 96, 120] |
| 2C_neighbor_swap | 12298 | 14605 | Hqql_to_Tbl | label_Tbl | label_Hqql | 1 | 3.2752 | electron | charged_hadron | [72, 48, 60, 12, 24, 36, 96, 120] |
| random_same_count | 12298 | 14605 | Hqql_to_Tbl | label_Tbl | label_Tbl | 0 | 1.8629 | electron | charged_hadron | [7, 21, 18, 44, 72, 43, 90, 32] |
| 2A_isolation_hadronic_injection | 12364 | 16293 | Hqql_to_Tbl | label_Tbl | label_Tbl | 0 | -0.1050 | neutral_hadron | photon | [32, 16, 80, 64, 96, 112, 116, 100] |
| 2C_neighbor_swap | 12364 | 16293 | Hqql_to_Tbl | label_Tbl | label_Tbl | 0 | -0.0796 | neutral_hadron | photon | [32, 16, 80, 64, 96, 112, 116, 100] |
| random_same_count | 12364 | 16293 | Hqql_to_Tbl | label_Tbl | label_Wqq | 0 | 4.4732 | neutral_hadron | photon | [49, 9, 1, 41, 94, 58, 14, 116] |
| 2A_isolation_hadronic_injection | 12434 | 15270 | Hqql_to_Tbl | label_Tbl | label_Tbl | 0 | 2.6732 | muon | electron | [84, 126, 22, 106, 64, 96, 54, 12] |
| 2C_neighbor_swap | 12434 | 15270 | Hqql_to_Tbl | label_Tbl | label_Tbl | 0 | -0.1945 | muon | electron | [84, 126, 22, 106, 64, 96, 54, 12] |
| random_same_count | 12434 | 15270 | Hqql_to_Tbl | label_Tbl | label_Tbl | 0 | 2.6478 | muon | electron | [38, 117, 56, 74, 62, 34, 61, 108] |
| 2A_isolation_hadronic_injection | 12551 | 13286 | Hqql_to_Tbl | label_Tbl | label_Tbl | 0 | 0.6746 | electron | muon | [106, 96, 43, 119, 13, 66, 62, 9] |
| 2C_neighbor_swap | 12551 | 13286 | Hqql_to_Tbl | label_Tbl | label_Tbl | 0 | -3.4038 | electron | muon | [106, 96, 43, 119, 13, 66, 62, 9] |
| random_same_count | 12551 | 13286 | Hqql_to_Tbl | label_Tbl | label_Hqql | 1 | 1.0903 | electron | muon | [106, 78, 82, 68, 73, 104, 123, 41] |
| 2A_isolation_hadronic_injection | 12563 | 13588 | Hqql_to_Tbl | label_Tbl | label_Hqql | 1 | 2.4411 | muon | muon | [98, 89, 40, 114, 16, 65, 39, 88] |
| 2C_neighbor_swap | 12563 | 13588 | Hqql_to_Tbl | label_Tbl | label_Tbl | 0 | -1.4814 | muon | muon | [98, 89, 40, 114, 16, 65, 39, 88] |
| random_same_count | 12563 | 13588 | Hqql_to_Tbl | label_Tbl | label_Hqql | 1 | 1.0948 | muon | muon | [69, 82, 102, 86, 77, 114, 107, 63] |
| 2A_isolation_hadronic_injection | 12577 | 15991 | Hqql_to_Tbl | label_Tbl | label_Tbl | 0 | -1.1519 | electron | muon | [74, 111, 119, 82, 8, 45, 50, 13] |
| 2C_neighbor_swap | 12577 | 15991 | Hqql_to_Tbl | label_Tbl | label_Hqql | 1 | 3.1750 | electron | muon | [74, 111, 119, 82, 8, 45, 50, 13] |
| random_same_count | 12577 | 15991 | Hqql_to_Tbl | label_Tbl | label_Hqql | 1 | 1.1331 | electron | muon | [83, 24, 93, 105, 11, 117, 63, 85] |
| 2A_isolation_hadronic_injection | 12598 | 14089 | Hqql_to_Tbl | label_Tbl | label_Hqql | 1 | 3.9396 | electron | muon | [28, 84, 112, 123, 67, 95, 39, 11] |
| 2C_neighbor_swap | 12598 | 14089 | Hqql_to_Tbl | label_Tbl | label_Tbl | 0 | 2.2055 | electron | muon | [28, 84, 112, 123, 67, 95, 39, 11] |
| random_same_count | 12598 | 14089 | Hqql_to_Tbl | label_Tbl | label_Tbl | 0 | 1.7603 | electron | muon | [93, 59, 50, 74, 100, 44, 3, 25] |
| 2A_isolation_hadronic_injection | 12619 | 13732 | Hqql_to_Tbl | label_Tbl | label_Tbl | 0 | -0.7997 | electron | electron | [72, 108, 20, 92, 56, 106, 70, 34] |
| 2C_neighbor_swap | 12619 | 13732 | Hqql_to_Tbl | label_Tbl | label_Hqql | 1 | 1.2730 | electron | electron | [72, 108, 20, 92, 56, 106, 70, 34] |
| random_same_count | 12619 | 13732 | Hqql_to_Tbl | label_Tbl | label_Tbl | 0 | 0.6713 | electron | electron | [30, 52, 69, 65, 93, 106, 117, 8] |
| 2A_isolation_hadronic_injection | 12649 | 13666 | Hqql_to_Tbl | label_Tbl | label_Tbl | 0 | 2.2568 | muon | neutral_hadron | [79, 64, 101, 22, 43, 122, 92, 13] |
| 2C_neighbor_swap | 12649 | 13666 | Hqql_to_Tbl | label_Tbl | label_Tbl | 0 | 1.8972 | muon | neutral_hadron | [79, 64, 101, 22, 43, 122, 92, 13] |
| random_same_count | 12649 | 13666 | Hqql_to_Tbl | label_Tbl | label_Tbl | 0 | 2.4738 | muon | neutral_hadron | [30, 70, 62, 126, 23, 20, 127, 69] |
| 2A_isolation_hadronic_injection | 12699 | 13574 | Hqql_to_Tbl | label_Tbl | label_Tbl | 0 | -0.8355 | muon | muon | [70, 105, 125, 90, 20, 55, 59, 24] |
| 2C_neighbor_swap | 12699 | 13574 | Hqql_to_Tbl | label_Tbl | label_Tbl | 0 | -1.8383 | muon | muon | [70, 105, 125, 90, 20, 55, 59, 24] |
| random_same_count | 12699 | 13574 | Hqql_to_Tbl | label_Tbl | label_Tbl | 0 | -1.7210 | muon | muon | [25, 3, 33, 103, 46, 88, 35, 123] |
| 2A_isolation_hadronic_injection | 12707 | 14989 | Hqql_to_Tbl | label_Tbl | label_Hqql | 1 | 2.2864 | muon | electron | [28, 84, 112, 127, 71, 99, 15, 43] |
| 2C_neighbor_swap | 12707 | 14989 | Hqql_to_Tbl | label_Tbl | label_Tbl | 0 | 1.5820 | muon | electron | [28, 84, 112, 127, 71, 99, 15, 43] |
| random_same_count | 12707 | 14989 | Hqql_to_Tbl | label_Tbl | label_Hqql | 1 | 2.4520 | muon | electron | [46, 91, 12, 11, 56, 115, 2, 102] |
| 2A_isolation_hadronic_injection | 12717 | 14284 | Hqql_to_Tbl | label_Tbl | label_Tbl | 0 | 0.4309 | electron | charged_hadron | [86, 94, 8, 51, 73, 116, 30, 54] |
| 2C_neighbor_swap | 12717 | 14284 | Hqql_to_Tbl | label_Tbl | label_Tbl | 0 | 0.2471 | electron | charged_hadron | [86, 94, 8, 51, 73, 116, 30, 54] |
| random_same_count | 12717 | 14284 | Hqql_to_Tbl | label_Tbl | label_Hqql | 1 | 0.7040 | electron | charged_hadron | [127, 42, 34, 123, 61, 5, 97, 72] |
| 2A_isolation_hadronic_injection | 12778 | 12949 | Hqql_to_Tbl | label_Tbl | label_Tbl | 0 | 5.0240 | electron | muon | [26, 78, 104, 107, 55, 81, 3, 29] |
| 2C_neighbor_swap | 12778 | 12949 | Hqql_to_Tbl | label_Tbl | label_Tbl | 0 | 0.6074 | electron | muon | [26, 78, 104, 107, 55, 81, 3, 29] |
| random_same_count | 12778 | 12949 | Hqql_to_Tbl | label_Tbl | label_Tbl | 0 | 0.6644 | electron | muon | [124, 54, 9, 92, 112, 87, 19, 48] |
| 2A_isolation_hadronic_injection | 12819 | 15977 | Hqql_to_Tbl | label_Tbl | label_Hqql | 1 | 2.3219 | electron | electron | [114, 80, 23, 27, 84, 82, 25, 101] |
| 2C_neighbor_swap | 12819 | 15977 | Hqql_to_Tbl | label_Tbl | label_Tbl | 0 | 1.2212 | electron | electron | [114, 80, 23, 27, 84, 82, 25, 101] |
| random_same_count | 12819 | 15977 | Hqql_to_Tbl | label_Tbl | label_Hqql | 1 | 1.4101 | electron | electron | [98, 67, 50, 69, 40, 19, 117, 84] |
| 2A_isolation_hadronic_injection | 12827 | 14994 | Hqql_to_Tbl | label_Tbl | label_Tbl | 0 | 2.1387 | electron | neutral_hadron | [31, 93, 124, 81, 50, 112, 19, 44] |
| 2C_neighbor_swap | 12827 | 14994 | Hqql_to_Tbl | label_Tbl | label_Tbl | 0 | 1.1942 | electron | neutral_hadron | [31, 93, 124, 81, 50, 112, 19, 44] |
| random_same_count | 12827 | 14994 | Hqql_to_Tbl | label_Tbl | label_Tbl | 0 | 0.7429 | electron | neutral_hadron | [69, 125, 44, 67, 16, 81, 22, 103] |
| 2A_isolation_hadronic_injection | 12874 | 13118 | Hqql_to_Tbl | label_Tbl | label_Hqql | 1 | 2.4251 | muon | muon | [72, 108, 24, 96, 60, 92, 20, 56] |
| 2C_neighbor_swap | 12874 | 13118 | Hqql_to_Tbl | label_Tbl | label_Tbl | 0 | 0.4457 | muon | muon | [72, 108, 24, 96, 60, 92, 20, 56] |
| random_same_count | 12874 | 13118 | Hqql_to_Tbl | label_Tbl | label_Tbl | 0 | 0.3392 | muon | muon | [3, 45, 58, 112, 95, 93, 126, 92] |
| 2A_isolation_hadronic_injection | 12882 | 14991 | Hqql_to_Tbl | label_Tbl | label_Hqql | 1 | 1.3514 | electron | muon | [96, 85, 37, 42, 90, 121, 25, 73] |
| 2C_neighbor_swap | 12882 | 14991 | Hqql_to_Tbl | label_Tbl | label_Tbl | 0 | -3.3331 | electron | muon | [96, 85, 37, 42, 90, 121, 25, 73] |
| random_same_count | 12882 | 14991 | Hqql_to_Tbl | label_Tbl | label_Hqql | 1 | 1.8363 | electron | muon | [67, 42, 112, 66, 72, 18, 44, 65] |
| 2A_isolation_hadronic_injection | 12914 | 14389 | Hqql_to_Tbl | label_Tbl | label_Hqql | 1 | 3.4398 | photon | neutral_hadron | [122, 126, 4, 65, 125, 64, 3, 67] |
| 2C_neighbor_swap | 12914 | 14389 | Hqql_to_Tbl | label_Tbl | label_Hqql | 1 | 3.3566 | photon | neutral_hadron | [122, 126, 4, 65, 125, 64, 3, 67] |
| random_same_count | 12914 | 14389 | Hqql_to_Tbl | label_Tbl | label_Tbl | 0 | 1.1461 | photon | neutral_hadron | [12, 35, 120, 65, 32, 27, 114, 42] |
| 2A_isolation_hadronic_injection | 12917 | 12368 | Hqql_to_Tbl | label_Tbl | label_Tbl | 0 | 0.2707 | electron | muon | [30, 90, 120, 38, 68, 98, 8, 80] |
| 2C_neighbor_swap | 12917 | 12368 | Hqql_to_Tbl | label_Tbl | label_Hqql | 1 | 2.0997 | electron | muon | [30, 90, 120, 38, 68, 98, 8, 80] |
| random_same_count | 12917 | 12368 | Hqql_to_Tbl | label_Tbl | label_Hqql | 1 | 2.3376 | electron | muon | [65, 26, 98, 115, 3, 25, 35, 73] |
| 2A_isolation_hadronic_injection | 12937 | 13578 | Hqql_to_Tbl | label_Tbl | label_Tbl | 0 | -0.7881 | electron | photon | [75, 25, 100, 125, 121, 96, 71, 21] |
| 2C_neighbor_swap | 12937 | 13578 | Hqql_to_Tbl | label_Tbl | label_Hqql | 1 | 3.0024 | electron | photon | [75, 25, 100, 125, 121, 96, 71, 21] |
| random_same_count | 12937 | 13578 | Hqql_to_Tbl | label_Tbl | label_Hqql | 1 | 1.9899 | electron | photon | [119, 114, 104, 120, 69, 18, 101, 116] |
| 2A_isolation_hadronic_injection | 12946 | 12420 | Hqql_to_Tbl | label_Tbl | label_Hqql | 1 | 3.3736 | muon | charged_hadron | [80, 120, 35, 115, 75, 108, 28, 68] |
| 2C_neighbor_swap | 12946 | 12420 | Hqql_to_Tbl | label_Tbl | label_Hqql | 1 | 2.4098 | muon | charged_hadron | [80, 120, 35, 115, 75, 108, 28, 68] |
| random_same_count | 12946 | 12420 | Hqql_to_Tbl | label_Tbl | label_Tbl | 0 | -0.9358 | muon | charged_hadron | [107, 74, 111, 63, 44, 51, 118, 29] |
| 2A_isolation_hadronic_injection | 12962 | 12721 | Hqql_to_Tbl | label_Tbl | label_Hqql | 1 | 3.9049 | muon | electron | [44, 22, 110, 88, 102, 124, 36, 14] |
| 2C_neighbor_swap | 12962 | 12721 | Hqql_to_Tbl | label_Tbl | label_Hqql | 1 | 3.0285 | muon | electron | [44, 22, 110, 88, 102, 124, 36, 14] |
| random_same_count | 12962 | 12721 | Hqql_to_Tbl | label_Tbl | label_Hqql | 1 | 1.8561 | muon | electron | [102, 77, 78, 125, 64, 44, 90, 75] |
| 2A_isolation_hadronic_injection | 12982 | 14952 | Hqql_to_Tbl | label_Tbl | label_Hqql | 1 | 2.1708 | electron | charged_hadron | [104, 82, 30, 119, 15, 67, 43, 95] |
| 2C_neighbor_swap | 12982 | 14952 | Hqql_to_Tbl | label_Tbl | label_Tbl | 0 | -0.7614 | electron | charged_hadron | [104, 82, 30, 119, 15, 67, 43, 95] |
| random_same_count | 12982 | 14952 | Hqql_to_Tbl | label_Tbl | label_Hqql | 1 | 2.1842 | electron | charged_hadron | [110, 54, 41, 46, 28, 99, 58, 44] |
| 2A_isolation_hadronic_injection | 12996 | 13181 | Hqql_to_Tbl | label_Tbl | label_Hqql | 1 | 3.8572 | muon | charged_hadron | [26, 78, 104, 120, 68, 94, 42, 16] |
| 2C_neighbor_swap | 12996 | 13181 | Hqql_to_Tbl | label_Tbl | label_Hqql | 1 | 2.6048 | muon | charged_hadron | [26, 78, 104, 120, 68, 94, 42, 16] |
| random_same_count | 12996 | 13181 | Hqql_to_Tbl | label_Tbl | label_Tbl | 0 | -0.8850 | muon | charged_hadron | [108, 54, 49, 65, 34, 107, 119, 23] |
| 2A_isolation_hadronic_injection | 13045 | 12923 | Hqql_to_Tbl | label_Tbl | label_Hqql | 1 | 0.7672 | electron | muon | [108, 122, 14, 68, 44, 98, 123, 15] |
| 2C_neighbor_swap | 13045 | 12923 | Hqql_to_Tbl | label_Tbl | label_Tbl | 0 | -0.9391 | electron | muon | [108, 122, 14, 68, 44, 98, 123, 15] |
| random_same_count | 13045 | 12923 | Hqql_to_Tbl | label_Tbl | label_Hqql | 1 | 1.7152 | electron | muon | [117, 34, 65, 105, 78, 42, 8, 121] |
| 2A_isolation_hadronic_injection | 13065 | 15575 | Hqql_to_Tbl | label_Tbl | label_Hqql | 1 | 2.0842 | charged_hadron | charged_hadron | [28, 84, 112, 122, 66, 94, 10, 38] |
| 2C_neighbor_swap | 13065 | 15575 | Hqql_to_Tbl | label_Tbl | label_Hqql | 1 | 1.4424 | charged_hadron | charged_hadron | [28, 84, 112, 122, 66, 94, 10, 38] |
| random_same_count | 13065 | 15575 | Hqql_to_Tbl | label_Tbl | label_Hqql | 1 | 1.2095 | charged_hadron | charged_hadron | [98, 124, 91, 42, 32, 83, 58, 35] |
| 2A_isolation_hadronic_injection | 13107 | 14763 | Hqql_to_Tbl | label_Tbl | label_Hqql | 1 | 4.5125 | photon | muon | [26, 78, 104, 111, 59, 85, 7, 33] |
| 2C_neighbor_swap | 13107 | 14763 | Hqql_to_Tbl | label_Tbl | label_Tbl | 0 | 0.3535 | photon | muon | [26, 78, 104, 111, 59, 85, 7, 33] |
| random_same_count | 13107 | 14763 | Hqql_to_Tbl | label_Tbl | label_Hqql | 1 | 1.4276 | photon | muon | [59, 65, 74, 116, 119, 36, 44, 123] |
| 2A_isolation_hadronic_injection | 13108 | 14511 | Hqql_to_Tbl | label_Tbl | label_Tbl | 0 | -0.8758 | electron | muon | [31, 93, 124, 45, 76, 107, 14, 82] |
| 2C_neighbor_swap | 13108 | 14511 | Hqql_to_Tbl | label_Tbl | label_Hqql | 1 | 2.4940 | electron | muon | [31, 93, 124, 45, 76, 107, 14, 82] |
| random_same_count | 13108 | 14511 | Hqql_to_Tbl | label_Tbl | label_Tbl | 0 | 0.8798 | electron | muon | [17, 62, 69, 6, 61, 70, 19, 42] |
| 2A_isolation_hadronic_injection | 13112 | 16106 | Hqql_to_Tbl | label_Tbl | label_Tbl | 0 | 3.2455 | electron | electron | [75, 25, 100, 125, 113, 88, 38, 13] |
| 2C_neighbor_swap | 13112 | 16106 | Hqql_to_Tbl | label_Tbl | label_Tbl | 0 | -1.5095 | electron | electron | [75, 25, 100, 125, 113, 88, 38, 13] |
| random_same_count | 13112 | 16106 | Hqql_to_Tbl | label_Tbl | label_Hqql | 1 | 5.9174 | electron | electron | [60, 65, 116, 117, 114, 77, 100, 122] |
| 2A_isolation_hadronic_injection | 13152 | 12772 | Hqql_to_Tbl | label_Tbl | label_Hqql | 1 | 2.3574 | electron | muon | [78, 117, 34, 112, 73, 93, 15, 54] |
| 2C_neighbor_swap | 13152 | 12772 | Hqql_to_Tbl | label_Tbl | label_Tbl | 0 | -2.4267 | electron | muon | [78, 117, 34, 112, 73, 93, 15, 54] |
| random_same_count | 13152 | 12772 | Hqql_to_Tbl | label_Tbl | label_H4q | 0 | 3.6974 | electron | muon | [50, 30, 89, 114, 9, 112, 33, 37] |
| 2A_isolation_hadronic_injection | 13236 | 14589 | Hqql_to_Tbl | label_Tbl | label_Hqql | 1 | 0.9929 | muon | electron | [26, 78, 104, 77, 51, 103, 25, 35] |
| 2C_neighbor_swap | 13236 | 14589 | Hqql_to_Tbl | label_Tbl | label_Tbl | 0 | -1.0842 | muon | electron | [26, 78, 104, 77, 51, 103, 25, 35] |
| random_same_count | 13236 | 14589 | Hqql_to_Tbl | label_Tbl | label_Hqql | 1 | 0.3103 | muon | electron | [87, 22, 26, 6, 35, 68, 98, 95] |
| 2A_isolation_hadronic_injection | 13239 | 13444 | Hqql_to_Tbl | label_Tbl | label_Hqql | 1 | 2.0571 | electron | neutral_hadron | [84, 126, 11, 95, 53, 100, 16, 58] |
| 2C_neighbor_swap | 13239 | 13444 | Hqql_to_Tbl | label_Tbl | label_Tbl | 0 | -1.6045 | electron | neutral_hadron | [84, 126, 11, 95, 53, 100, 16, 58] |
| random_same_count | 13239 | 13444 | Hqql_to_Tbl | label_Tbl | label_Tbl | 0 | -0.5053 | electron | neutral_hadron | [60, 29, 37, 68, 12, 14, 57, 79] |
| 2A_isolation_hadronic_injection | 13252 | 15294 | Hqql_to_Tbl | label_Tbl | label_Hqql | 1 | 5.8265 | electron | charged_hadron | [29, 87, 116, 82, 53, 111, 24, 51] |
| 2C_neighbor_swap | 13252 | 15294 | Hqql_to_Tbl | label_Tbl | label_Tbl | 0 | 1.8524 | electron | charged_hadron | [29, 87, 116, 82, 53, 111, 24, 51] |
| random_same_count | 13252 | 15294 | Hqql_to_Tbl | label_Tbl | label_Tbl | 0 | 2.8431 | electron | charged_hadron | [9, 82, 121, 51, 53, 103, 102, 58] |
| 2A_isolation_hadronic_injection | 13302 | 14068 | Hqql_to_Tbl | label_Tbl | label_Hqql | 1 | 2.0275 | electron | charged_hadron | [104, 114, 10, 62, 75, 127, 23, 125] |
| 2C_neighbor_swap | 13302 | 14068 | Hqql_to_Tbl | label_Tbl | label_Hqql | 1 | 1.4309 | electron | charged_hadron | [104, 114, 10, 62, 75, 127, 23, 125] |
| random_same_count | 13302 | 14068 | Hqql_to_Tbl | label_Tbl | label_Hqql | 1 | 1.3167 | electron | charged_hadron | [20, 64, 18, 25, 119, 28, 126, 31] |
| 2A_isolation_hadronic_injection | 13347 | 14921 | Hqql_to_Tbl | label_Tbl | label_Hqql | 1 | 0.2900 | electron | electron | [94, 117, 23, 70, 120, 73, 26, 68] |
| 2C_neighbor_swap | 13347 | 14921 | Hqql_to_Tbl | label_Tbl | label_Hqql | 1 | 0.5466 | electron | electron | [94, 117, 23, 70, 120, 73, 26, 68] |
| random_same_count | 13347 | 14921 | Hqql_to_Tbl | label_Tbl | label_Tbl | 0 | -0.8087 | electron | electron | [4, 2, 53, 84, 42, 71, 6, 119] |
| 2A_isolation_hadronic_injection | 13377 | 14669 | Hqql_to_Tbl | label_Tbl | label_Tbl | 0 | -0.2056 | electron | charged_hadron | [70, 105, 23, 93, 58, 94, 59, 24] |
| 2C_neighbor_swap | 13377 | 14669 | Hqql_to_Tbl | label_Tbl | label_Tbl | 0 | 0.2945 | electron | charged_hadron | [70, 105, 23, 93, 58, 94, 59, 24] |
| random_same_count | 13377 | 14669 | Hqql_to_Tbl | label_Tbl | label_Tbl | 0 | -2.0657 | electron | charged_hadron | [38, 119, 24, 39, 15, 37, 86, 83] |
| 2A_isolation_hadronic_injection | 13384 | 13432 | Hqql_to_Tbl | label_Tbl | label_Hqql | 1 | 3.3281 | electron | electron | [88, 103, 15, 59, 74, 118, 30, 62] |
| 2C_neighbor_swap | 13384 | 13432 | Hqql_to_Tbl | label_Tbl | label_Tbl | 0 | -0.3869 | electron | electron | [88, 103, 15, 59, 74, 118, 30, 62] |
| random_same_count | 13384 | 13432 | Hqql_to_Tbl | label_Tbl | label_Hqql | 1 | 2.1990 | electron | electron | [20, 60, 29, 54, 66, 85, 118, 56] |
| 2A_isolation_hadronic_injection | 13441 | 13758 | Hqql_to_Tbl | label_Tbl | label_Hqql | 1 | 2.2647 | muon | muon | [68, 102, 118, 84, 16, 50, 55, 21] |
| 2C_neighbor_swap | 13441 | 13758 | Hqql_to_Tbl | label_Tbl | label_Hqql | 1 | 2.1413 | muon | muon | [68, 102, 118, 84, 16, 50, 55, 21] |
| random_same_count | 13441 | 13758 | Hqql_to_Tbl | label_Tbl | label_Tbl | 0 | -0.0631 | muon | muon | [112, 6, 37, 18, 61, 94, 93, 117] |
| 2A_isolation_hadronic_injection | 13449 | 14756 | Hqql_to_Tbl | label_Tbl | label_QCD | 0 | -0.1081 | muon | charged_hadron | [34, 17, 85, 68, 102, 119, 32, 117] |
| 2C_neighbor_swap | 13449 | 14756 | Hqql_to_Tbl | label_Tbl | label_Tbl | 0 | -0.6365 | muon | charged_hadron | [34, 17, 85, 68, 102, 119, 32, 117] |
| random_same_count | 13449 | 14756 | Hqql_to_Tbl | label_Tbl | label_Tbl | 0 | 0.0011 | muon | charged_hadron | [79, 3, 57, 67, 46, 37, 47, 28] |

## Interpretation

2A asks whether adding hadronic Hqql-like neighbors around the same lepton restores Hqql. 2B asks whether the lepton itself is enough. 2C asks whether neighbor context alone restores Hqql. Compare targeted tests against random_same_count for each target group.
