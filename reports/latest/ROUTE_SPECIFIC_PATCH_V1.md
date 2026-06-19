# Route Specific Patch v1

Causal patch test for event-level active L2/core routes.

## Summary by head/mode
| head | mode | n | flip_rate | mean_delta_base_logit | mean_patched_conf |
| --- | --- | --- | --- | --- | --- |
| L2_ch224:256 | remove_top_particle | 3 | 1.0000 | -25.7413 | 0.0001 |
| L2_ch224:256 | remove_knn_neighbors | 3 | 1.0000 | -26.8548 | 0.0001 |
| L2_ch224:256 | remove_top_plus_knn | 3 | 1.0000 | -26.8548 | 0.0001 |
| L2_ch224:256 | random_same_count | 3 | 0.3333 | -0.1738 | 0.7754 |
| L2_ch128:160 | remove_top_particle | 3 | 1.0000 | -25.7413 | 0.0001 |
| L2_ch128:160 | remove_knn_neighbors | 3 | 1.0000 | -26.8548 | 0.0001 |
| L2_ch128:160 | remove_top_plus_knn | 3 | 1.0000 | -26.8548 | 0.0001 |
| L2_ch128:160 | random_same_count | 3 | 0.3333 | -0.4494 | 0.6209 |
| L2_ch32:64 | remove_top_particle | 3 | 1.0000 | -25.7413 | 0.0001 |
| L2_ch32:64 | remove_knn_neighbors | 3 | 1.0000 | -26.8548 | 0.0001 |
| L2_ch32:64 | remove_top_plus_knn | 3 | 1.0000 | -26.8548 | 0.0001 |
| L2_ch32:64 | random_same_count | 3 | 0.0000 | -0.3199 | 0.8261 |
| L2_ch0:32 | remove_top_particle | 3 | 1.0000 | -25.7413 | 0.0001 |
| L2_ch0:32 | remove_knn_neighbors | 3 | 1.0000 | -26.8548 | 0.0001 |
| L2_ch0:32 | remove_top_plus_knn | 3 | 1.0000 | -26.8548 | 0.0001 |
| L2_ch0:32 | random_same_count | 3 | 0.3333 | -1.1473 | 0.6974 |

## Rows
| event | true | base | patched | head | mode | flip | d_base_logit | indices |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 197 | label_Hqql | label_Tbl | label_QCD | L2_ch224:256 | remove_top_particle | 1 | -25.8225 | [0] |
| 197 | label_Hqql | label_Tbl | label_QCD | L2_ch224:256 | remove_knn_neighbors | 1 | -26.6623 | [0, 10, 18, 23, 25, 35, 43, 60, 68, 75, 85, 93, 100, 110, 118, 125] |
| 197 | label_Hqql | label_Tbl | label_QCD | L2_ch224:256 | remove_top_plus_knn | 1 | -26.6623 | [0, 10, 18, 23, 25, 35, 43, 60, 68, 75, 85, 93, 100, 110, 118, 125] |
| 197 | label_Hqql | label_Tbl | label_Hqql | L2_ch224:256 | random_same_count | 1 | 0.3532 | [1, 2, 3, 4, 6, 7, 9, 11, 12, 13, 14, 15, 16, 19, 20, 22] |
| 197 | label_Hqql | label_Tbl | label_QCD | L2_ch128:160 | remove_top_particle | 1 | -25.8225 | [0] |
| 197 | label_Hqql | label_Tbl | label_QCD | L2_ch128:160 | remove_knn_neighbors | 1 | -26.6623 | [0, 10, 18, 23, 25, 35, 43, 60, 68, 75, 85, 93, 100, 110, 118, 125] |
| 197 | label_Hqql | label_Tbl | label_QCD | L2_ch128:160 | remove_top_plus_knn | 1 | -26.6623 | [0, 10, 18, 23, 25, 35, 43, 60, 68, 75, 85, 93, 100, 110, 118, 125] |
| 197 | label_Hqql | label_Tbl | label_Hqql | L2_ch128:160 | random_same_count | 1 | 0.3182 | [1, 2, 3, 5, 6, 7, 8, 11, 12, 13, 14, 15, 16, 20, 21, 24] |
| 197 | label_Hqql | label_Tbl | label_QCD | L2_ch32:64 | remove_top_particle | 1 | -25.8225 | [0] |
| 197 | label_Hqql | label_Tbl | label_QCD | L2_ch32:64 | remove_knn_neighbors | 1 | -26.6623 | [0, 10, 18, 23, 25, 35, 43, 60, 68, 75, 85, 93, 100, 110, 118, 125] |
| 197 | label_Hqql | label_Tbl | label_QCD | L2_ch32:64 | remove_top_plus_knn | 1 | -26.6623 | [0, 10, 18, 23, 25, 35, 43, 60, 68, 75, 85, 93, 100, 110, 118, 125] |
| 197 | label_Hqql | label_Tbl | label_Tbl | L2_ch32:64 | random_same_count | 0 | 0.8904 | [1, 2, 3, 4, 5, 7, 8, 11, 12, 13, 14, 15, 16, 17, 19, 24] |
| 197 | label_Hqql | label_Tbl | label_QCD | L2_ch0:32 | remove_top_particle | 1 | -25.8225 | [0] |
| 197 | label_Hqql | label_Tbl | label_QCD | L2_ch0:32 | remove_knn_neighbors | 1 | -26.6623 | [0, 10, 18, 23, 25, 35, 43, 60, 68, 75, 85, 93, 100, 110, 118, 125] |
| 197 | label_Hqql | label_Tbl | label_QCD | L2_ch0:32 | remove_top_plus_knn | 1 | -26.6623 | [0, 10, 18, 23, 25, 35, 43, 60, 68, 75, 85, 93, 100, 110, 118, 125] |
| 197 | label_Hqql | label_Tbl | label_Hqql | L2_ch0:32 | random_same_count | 1 | -0.2757 | [1, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 17, 19, 20, 21, 22] |
| 369 | label_Tbl | label_Tbl | label_Hcc | L2_ch224:256 | remove_top_particle | 1 | -15.3691 | [0] |
| 369 | label_Tbl | label_Tbl | label_Hcc | L2_ch224:256 | remove_knn_neighbors | 1 | -15.9132 | [0, 8, 14, 24, 31, 44, 50, 60, 67, 72, 80, 86, 96, 103, 108, 116] |
| 369 | label_Tbl | label_Tbl | label_Hcc | L2_ch224:256 | remove_top_plus_knn | 1 | -15.9132 | [0, 8, 14, 24, 31, 44, 50, 60, 67, 72, 80, 86, 96, 103, 108, 116] |
| 369 | label_Tbl | label_Tbl | label_Tbl | L2_ch224:256 | random_same_count | 0 | 1.1683 | [2, 3, 6, 10, 12, 13, 15, 16, 18, 19, 21, 23, 26, 27, 28, 30] |
| 369 | label_Tbl | label_Tbl | label_Hcc | L2_ch128:160 | remove_top_particle | 1 | -15.3691 | [0] |
| 369 | label_Tbl | label_Tbl | label_Hcc | L2_ch128:160 | remove_knn_neighbors | 1 | -15.9132 | [0, 8, 14, 24, 31, 44, 50, 60, 67, 72, 80, 86, 96, 103, 108, 116] |
| 369 | label_Tbl | label_Tbl | label_Hcc | L2_ch128:160 | remove_top_plus_knn | 1 | -15.9132 | [0, 8, 14, 24, 31, 44, 50, 60, 67, 72, 80, 86, 96, 103, 108, 116] |
| 369 | label_Tbl | label_Tbl | label_Tbl | L2_ch128:160 | random_same_count | 0 | 0.3766 | [1, 3, 7, 9, 12, 13, 15, 17, 21, 22, 23, 27, 28, 30, 32, 33] |
| 369 | label_Tbl | label_Tbl | label_Hcc | L2_ch32:64 | remove_top_particle | 1 | -15.3691 | [0] |
| 369 | label_Tbl | label_Tbl | label_Hcc | L2_ch32:64 | remove_knn_neighbors | 1 | -15.9132 | [0, 8, 14, 24, 31, 44, 50, 60, 67, 72, 80, 86, 96, 103, 108, 116] |
| 369 | label_Tbl | label_Tbl | label_Hcc | L2_ch32:64 | remove_top_plus_knn | 1 | -15.9132 | [0, 8, 14, 24, 31, 44, 50, 60, 67, 72, 80, 86, 96, 103, 108, 116] |
| 369 | label_Tbl | label_Tbl | label_Tbl | L2_ch32:64 | random_same_count | 0 | 0.1927 | [2, 5, 6, 9, 11, 15, 17, 18, 19, 20, 23, 27, 29, 30, 33, 35] |
| 369 | label_Tbl | label_Tbl | label_Hcc | L2_ch0:32 | remove_top_particle | 1 | -15.3691 | [0] |
| 369 | label_Tbl | label_Tbl | label_Hcc | L2_ch0:32 | remove_knn_neighbors | 1 | -15.9132 | [0, 8, 14, 24, 31, 44, 50, 60, 67, 72, 80, 86, 96, 103, 108, 116] |
| 369 | label_Tbl | label_Tbl | label_Hcc | L2_ch0:32 | remove_top_plus_knn | 1 | -15.9132 | [0, 8, 14, 24, 31, 44, 50, 60, 67, 72, 80, 86, 96, 103, 108, 116] |
| 369 | label_Tbl | label_Tbl | label_Tbl | L2_ch0:32 | random_same_count | 0 | -1.1231 | [1, 2, 3, 4, 5, 7, 10, 13, 16, 17, 22, 26, 27, 28, 32, 34] |
| 355 | label_Tbl | label_Tbl | label_Tbqq | L2_ch224:256 | remove_top_particle | 1 | -36.0323 | [0] |
| 355 | label_Tbl | label_Tbl | label_Tbqq | L2_ch224:256 | remove_knn_neighbors | 1 | -37.9889 | [0, 15, 17, 18, 33, 35, 36, 53, 71, 72, 89, 90, 107, 108, 125, 126] |
| 355 | label_Tbl | label_Tbl | label_Tbqq | L2_ch224:256 | remove_top_plus_knn | 1 | -37.9889 | [0, 15, 17, 18, 33, 35, 36, 53, 71, 72, 89, 90, 107, 108, 125, 126] |
| 355 | label_Tbl | label_Tbl | label_Tbl | L2_ch224:256 | random_same_count | 0 | -2.0430 | [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16] |
| 355 | label_Tbl | label_Tbl | label_Tbqq | L2_ch128:160 | remove_top_particle | 1 | -36.0323 | [0] |
| 355 | label_Tbl | label_Tbl | label_Tbqq | L2_ch128:160 | remove_knn_neighbors | 1 | -37.9889 | [0, 15, 17, 18, 33, 35, 36, 53, 71, 72, 89, 90, 107, 108, 125, 126] |
| 355 | label_Tbl | label_Tbl | label_Tbqq | L2_ch128:160 | remove_top_plus_knn | 1 | -37.9889 | [0, 15, 17, 18, 33, 35, 36, 53, 71, 72, 89, 90, 107, 108, 125, 126] |
| 355 | label_Tbl | label_Tbl | label_Tbl | L2_ch128:160 | random_same_count | 0 | -2.0430 | [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16] |
| 355 | label_Tbl | label_Tbl | label_Tbqq | L2_ch32:64 | remove_top_particle | 1 | -36.0323 | [0] |
| 355 | label_Tbl | label_Tbl | label_Tbqq | L2_ch32:64 | remove_knn_neighbors | 1 | -37.9889 | [0, 15, 17, 18, 33, 35, 36, 53, 71, 72, 89, 90, 107, 108, 125, 126] |
| 355 | label_Tbl | label_Tbl | label_Tbqq | L2_ch32:64 | remove_top_plus_knn | 1 | -37.9889 | [0, 15, 17, 18, 33, 35, 36, 53, 71, 72, 89, 90, 107, 108, 125, 126] |
| 355 | label_Tbl | label_Tbl | label_Tbl | L2_ch32:64 | random_same_count | 0 | -2.0430 | [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16] |
| 355 | label_Tbl | label_Tbl | label_Tbqq | L2_ch0:32 | remove_top_particle | 1 | -36.0323 | [0] |
| 355 | label_Tbl | label_Tbl | label_Tbqq | L2_ch0:32 | remove_knn_neighbors | 1 | -37.9889 | [0, 15, 17, 18, 33, 35, 36, 53, 71, 72, 89, 90, 107, 108, 125, 126] |
| 355 | label_Tbl | label_Tbl | label_Tbqq | L2_ch0:32 | remove_top_plus_knn | 1 | -37.9889 | [0, 15, 17, 18, 33, 35, 36, 53, 71, 72, 89, 90, 107, 108, 125, 126] |
| 355 | label_Tbl | label_Tbl | label_Tbl | L2_ch0:32 | random_same_count | 0 | -2.0430 | [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16] |

## Interpretation

Compare targeted remove_top/knn/top_plus_knn against random_same_count. Strong support means targeted route patch flips or reduces baseline logit more than random.
