# MATRIX_PROGRAM_FULL_TRACE_V1

Postprocessor over INTERNAL_ACTIVATION_CONTRAST_V2/V2_1. It builds particle_role -> head -> class paths from top-particle activation and zero-slice class contribution.

## Top path mechanisms
| diag | role | head | class | A | B | C | B-A | B-C | trigger | loss | anomaly |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| anomalous_third_topology_candidate | hardest_hadron | L1_ch0:16 | label_Hqql | 25.5523 | 182.2283 | -72.3716 | 156.6761 | 254.6000 | 0.0000 | 0.0000 | 39889.7166 |
| source_evidence_loss_candidate | particle0_best_lepton | L1_ch16:32 | label_Hqql | 131.7304 | 0.0000 | 269.5061 | -131.7304 | -269.5061 | 0.0000 | 131.7304 | 35502.1513 |
| anomalous_third_topology_candidate | hardest_hadron | L1_ch0:16 | label_Tbl | 32.1747 | 190.3982 | -22.8611 | 158.2235 | 213.2593 | 0.7385 | 0.0000 | 33742.6381 |
| anomalous_third_topology_candidate | particle0 | L1_ch0:16 | label_Hqql | 0.0000 | 147.7804 | -49.8586 | 147.7804 | 197.6391 | 0.0000 | 0.0000 | 29207.1823 |
| anomalous_third_topology_candidate | particle0 | L1_ch0:16 | label_Tbl | 0.0000 | 154.4059 | -5.9665 | 154.4059 | 160.3724 | 0.9568 | 0.0000 | 24762.4394 |
| anomalous_third_topology_candidate | hard_hadron | L1_ch0:16 | label_Hqql | -13.4281 | 89.1781 | -47.4833 | 102.6062 | 136.6614 | 0.0000 | 0.0000 | 14022.2988 |
| target_like_trigger_candidate | hard_hadron | L1_ch0:16 | label_Tbl | -17.1712 | 96.6986 | -6.8120 | 113.8698 | 103.5105 | 1.0896 | 0.0000 | 11786.7212 |
| anomalous_third_topology_candidate | nearest_hadron_to_best_lepton | L1_ch80:96 | label_Tbl | 74.0160 | 0.0000 | 109.9731 | -74.0160 | -109.9731 | 0.6670 | 0.0000 | 8139.7744 |
| anomalous_third_topology_candidate | other_lepton | L1_ch80:96 | label_Tbl | 80.8757 | 0.0000 | 97.7791 | -80.8757 | -97.7791 | 0.8188 | 0.0000 | 7907.9486 |
| source_evidence_loss_candidate | hardest_hadron | L1_ch112:128 | label_Hqql | 84.7534 | 0.0000 | 86.6403 | -84.7534 | -86.6403 | 0.0000 | 84.7534 | 7343.0567 |
| anomalous_third_topology_candidate | photon_neighbor | L1_ch80:96 | label_Hqql | 68.1021 | 119.2678 | -19.5422 | 51.1656 | 138.8100 | 0.0000 | 0.0000 | 7102.3003 |
| anomalous_third_topology_candidate | hardest_hadron | L1_ch96:112 | label_Hqql | 0.0000 | 90.7792 | 25.6056 | 90.7792 | 65.1737 | 0.0000 | 0.0000 | 5916.4131 |
| source_evidence_loss_candidate | hard_hadron | L1_ch16:32 | label_Hqql | 198.5034 | 154.8636 | 288.9772 | -43.6398 | -134.1137 | 0.0000 | 43.6398 | 5852.6969 |
| source_evidence_loss_candidate | particle0 | L1_ch64:80 | label_Hqql | 0.0000 | -76.0072 | 0.0000 | -76.0072 | -76.0072 | 0.0000 | 76.0072 | 5777.1010 |
| source_evidence_loss_candidate | nearest_hadron_to_best_lepton | L0_ch40:48 | label_Hqql | 68.6077 | 0.0000 | 82.8916 | -68.6077 | -82.8916 | 0.0000 | 68.6077 | 5686.9988 |
| anomalous_third_topology_candidate | second_lepton | L1_ch80:96 | label_Tbl | 73.1873 | 0.0000 | 75.3624 | -73.1873 | -75.3624 | 0.9584 | 0.0000 | 5515.5750 |
| anomalous_third_topology_candidate | second_lepton | L0_ch16:24 | label_Hqql | 0.0000 | 50.2260 | -57.3266 | 50.2260 | 107.5527 | 0.0000 | 0.0000 | 5401.9448 |
| anomalous_third_topology_candidate | hardest_hadron | L0_ch16:24 | label_Hqql | 0.0000 | 51.7053 | -50.4853 | 51.7053 | 102.1906 | 0.0000 | 0.0000 | 5283.7938 |
| target_like_trigger_candidate | particle0_best_lepton | L1_ch16:32 | label_Tbl | 84.8881 | 0.0000 | 55.2449 | -84.8881 | -55.2449 | 1.5093 | 0.0000 | 4689.6367 |
| source_evidence_loss_candidate | other_lepton | L0_ch8:16 | label_Hqql | 134.5210 | -51.6270 | -27.0365 | -186.1480 | -24.5905 | 0.0000 | 186.1480 | 4577.4678 |
| anomalous_third_topology_candidate | particle0 | L0_ch32:40 | label_Tbl | -3.9581 | -63.6592 | -0.8822 | -59.7011 | -62.7770 | 0.9361 | 0.0000 | 3747.8523 |
| target_like_trigger_candidate | photon_neighbor | L1_ch80:96 | label_Tbl | 68.0336 | 136.9842 | 85.8536 | 68.9506 | 51.1306 | 1.3227 | 0.0000 | 3525.4863 |
| anomalous_third_topology_candidate | particle0 | L1_ch64:80 | label_Tbl | 0.0000 | -59.1317 | 0.0000 | -59.1317 | -59.1317 | 0.9834 | 0.0000 | 3496.5628 |
| source_evidence_loss_candidate | best_lepton | L0_ch40:48 | label_Hqql | 62.3269 | 0.0000 | 55.0243 | -62.3269 | -55.0243 | 0.0000 | 62.3269 | 3429.4931 |
| source_evidence_loss_candidate | particle0 | L1_ch96:112 | label_Hqql | 83.3636 | 0.0000 | 40.3315 | -83.3636 | -40.3315 | 0.0000 | 83.3636 | 3362.1744 |
| target_like_trigger_candidate | nearest_hadron_to_best_lepton | L0_ch40:48 | label_Tbl | 57.9453 | 0.0000 | 57.1719 | -57.9453 | -57.1719 | 0.9961 | 0.0000 | 3312.8423 |
| anomalous_third_topology_candidate | second_lepton | L0_ch16:24 | label_Tbl | 0.0000 | 54.5097 | -1.3968 | 54.5097 | 55.9065 | 0.9579 | 0.0000 | 3047.4468 |
| anomalous_third_topology_candidate | hardest_hadron | L1_ch112:128 | label_Tbl | 52.1138 | 0.0000 | 54.7880 | -52.1138 | -54.7880 | 0.9341 | 0.0000 | 2855.2102 |
| source_evidence_loss_candidate | second_lepton | L0_ch8:16 | label_Hqql | 85.9127 | 21.8971 | -21.8083 | -64.0156 | 43.7054 | 0.0000 | 64.0156 | 2797.8276 |
| target_like_trigger_candidate | particle0 | L1_ch96:112 | label_Tbl | 60.0417 | 0.0000 | 36.4840 | -60.0417 | -36.4840 | 1.6018 | 0.0000 | 2190.5647 |
| target_like_trigger_candidate | hardest_hadron | L1_ch48:64 | label_Tbl | 20.8890 | -30.4454 | 5.1247 | -51.3345 | -35.5701 | 1.4037 | 0.0000 | 1825.9723 |
| target_like_trigger_candidate | other_lepton | L0_ch8:16 | label_Tbl | 63.0576 | 5.3498 | 36.9239 | -57.7078 | -31.5741 | 1.7716 | 0.0000 | 1822.0740 |
| anomalous_third_topology_candidate | hadron_neighbor | L0_ch16:24 | label_Tbl | 30.7689 | 65.2558 | 15.1320 | 34.4868 | 50.1238 | 0.6746 | 0.0000 | 1728.6106 |
| anomalous_third_topology_candidate | particle0 | L1_ch32:48 | label_Hqql | 0.0000 | 38.4981 | -4.8849 | 38.4981 | 43.3831 | 0.0000 | 0.0000 | 1670.1671 |
| source_evidence_loss_candidate | other_lepton | L1_ch80:96 | label_Hqql | 93.7284 | 0.0000 | -17.5912 | -93.7284 | 17.5912 | 0.0000 | 93.7284 | 1648.7966 |
| source_evidence_loss_candidate | photon_neighbor | L0_ch8:16 | label_Hqql | 45.5067 | 5.3658 | -34.2309 | -40.1409 | 39.5967 | 0.0000 | 40.1409 | 1589.4454 |
| source_evidence_loss_candidate | particle0_best_lepton | L1_ch48:64 | label_Hqql | 26.1883 | 0.0000 | -59.5098 | -26.1883 | 59.5098 | 0.0000 | 26.1883 | 1558.4615 |
| source_evidence_loss_candidate | particle0_best_lepton | L1_ch96:112 | label_Hqql | 76.6421 | 0.0000 | 19.0195 | -76.6421 | -19.0195 | 0.0000 | 76.6421 | 1457.6960 |
| target_like_trigger_candidate | particle0 | L1_ch48:64 | label_Tbl | 0.0000 | -37.8366 | -0.5890 | -37.8366 | -37.2476 | 0.9893 | 0.0000 | 1409.3228 |
| anomalous_third_topology_candidate | best_lepton | L0_ch8:16 | label_Tbl | 36.6274 | 0.0000 | 38.1118 | -36.6274 | -38.1118 | 0.9365 | 0.0000 | 1395.9347 |
| source_evidence_loss_candidate | nearest_hadron_to_best_lepton | L0_ch48:56 | label_Hqql | 62.5000 | 0.0000 | 22.1710 | -62.5000 | -22.1710 | 0.0000 | 62.5000 | 1385.6868 |
| source_evidence_loss_candidate | nearest_hadron_to_best_lepton | L1_ch80:96 | label_Hqql | 85.2932 | 0.0000 | -16.0326 | -85.2932 | 16.0326 | 0.0000 | 85.2932 | 1367.4715 |
| target_like_trigger_candidate | hardest_hadron | L0_ch16:24 | label_Tbl | 0.0000 | 56.1151 | 31.8812 | 56.1151 | 24.2339 | 2.2238 | 0.0000 | 1359.8865 |
| target_like_trigger_candidate | best_lepton | L0_ch40:48 | label_Tbl | 40.6387 | 0.0000 | 33.4319 | -40.6387 | -33.4319 | 1.1803 | 0.0000 | 1358.6294 |
| anomalous_third_topology_candidate | particle0_best_lepton | L1_ch80:96 | label_Hqql | 31.1394 | 52.2317 | -12.0220 | 21.0923 | 64.2536 | 0.0000 | 0.0000 | 1355.2559 |
| anomalous_third_topology_candidate | second_lepton | L0_ch40:48 | label_Tbl | 0.0000 | -19.6722 | 48.2812 | -19.6722 | -67.9534 | 0.2853 | 0.0000 | 1336.7942 |
| target_like_trigger_candidate | hadron_neighbor | L1_ch80:96 | label_Tbl | 82.4797 | 131.8961 | 105.2786 | 49.4164 | 26.6174 | 1.7893 | 0.0000 | 1315.3372 |
| source_evidence_loss_candidate | nearest_hadron_to_best_lepton | L0_ch0:8 | label_Hqql | 57.2191 | 37.2707 | -25.8293 | -19.9483 | 63.1001 | 0.0000 | 19.9483 | 1258.7414 |
| anomalous_third_topology_candidate | second_lepton | L1_ch96:112 | label_Hqql | 73.4564 | 91.4574 | 21.6931 | 18.0010 | 69.7643 | 0.0000 | 0.0000 | 1255.8286 |
| source_evidence_loss_candidate | hadron_neighbor | L0_ch8:16 | label_Hqql | 30.4134 | -6.5642 | -38.3345 | -36.9776 | 31.7703 | 0.0000 | 36.9776 | 1174.7896 |

## Top head programs
| head | diag | B_close_C | B-A source | B-A target | roles |
| --- | --- | --- | --- | --- | --- |
| L1_ch64:80 | mixed_or_unclear | -512.9345 | -0.2563 | 0.5563 | photon_neighbor:270;hadron_neighbor:171;hard_hadron:27;nearest_hadron_to_best_lepton:24;particle0_best_lepton:9 |
| L0_ch40:48 | lost_hqql_evidence_candidate | -250.2544 | -1.1540 | -0.4085 | hadron_neighbor:206;photon_neighbor:125;particle0_best_lepton:57;hard_hadron:56;hardest_hadron:26 |
| L1_ch0:16 | active_tbl_like_readout_candidate | 142.8701 | -0.6993 | 0.9044 | photon_neighbor:355;hadron_neighbor:98;nearest_hadron_to_best_lepton:16;hard_hadron:15;particle0_best_lepton:13 |
| L0_ch16:24 | active_tbl_like_readout_candidate | 128.3890 | -0.9464 | 0.6641 | hadron_neighbor:319;photon_neighbor:97;hard_hadron:34;nearest_hadron_to_best_lepton:27;particle0_best_lepton:13 |
| L1_ch80:96 | active_tbl_like_readout_candidate | 107.7441 | -0.1101 | 1.1220 | hadron_neighbor:216;photon_neighbor:212;hard_hadron:36;particle0_best_lepton:23;nearest_hadron_to_best_lepton:12 |
| L1_ch96:112 | mixed_or_unclear | -68.5056 | 0.0511 | 0.6187 | hadron_neighbor:173;photon_neighbor:165;hard_hadron:68;nearest_hadron_to_best_lepton:32;particle0_best_lepton:32 |
| L1_ch16:32 | mixed_or_unclear | 59.3826 | -0.2824 | -0.2786 | photon_neighbor:323;hadron_neighbor:106;hard_hadron:48;particle0_best_lepton:11;nearest_hadron_to_best_lepton:10 |
| L0_ch32:40 | lost_hqql_evidence_candidate | -53.1247 | -0.0299 | -0.2610 | hadron_neighbor:171;photon_neighbor:131;hard_hadron:125;hardest_hadron:52;particle0:19 |
| L1_ch112:128 | mixed_or_unclear | -46.6943 | -0.3454 | 0.3501 | hadron_neighbor:158;hard_hadron:108;particle0_best_lepton:91;photon_neighbor:70;nearest_hadron_to_best_lepton:40 |
| L0_ch56:64 | lost_hqql_evidence_candidate | -28.1347 | -0.5519 | 0.7307 | photon_neighbor:284;hadron_neighbor:121;hard_hadron:59;nearest_hadron_to_best_lepton:31;hardest_hadron:5 |
| L2_ch224:256 | lost_hqql_evidence_candidate | -27.9287 | 0.2378 | -0.4670 | particle0_best_lepton:148;hardest_hadron:101;hard_hadron:86;photon_neighbor:70;hadron_neighbor:31 |
| L0_ch0:8 | mixed_or_unclear | -24.8408 | -1.0447 | 1.2137 | photon_neighbor:380;hadron_neighbor:114;nearest_hadron_to_best_lepton:12;hard_hadron:5;other_lepton:1 |
| L2_ch32:64 | mixed_or_unclear | -19.2769 | -0.4246 | 0.3246 | particle0_best_lepton:148;hard_hadron:96;hardest_hadron:61;hadron_neighbor:59;photon_neighbor:57 |
| L0_ch24:32 | lost_hqql_evidence_candidate | 16.2202 | 0.3537 | 1.1543 | photon_neighbor:269;hard_hadron:98;hadron_neighbor:87;nearest_hadron_to_best_lepton:29;hardest_hadron:15 |
| L0_ch8:16 | mixed_or_unclear | -11.2570 | -2.3435 | 0.1079 | photon_neighbor:215;hadron_neighbor:174;particle0_best_lepton:75;second_lepton:24;other_lepton:10 |
| L2_ch160:192 | mixed_or_unclear | -8.3213 | -1.0202 | -0.0235 | particle0_best_lepton:148;photon_neighbor:102;hadron_neighbor:94;hard_hadron:50;nearest_hadron_to_best_lepton:41 |
| L1_ch32:48 | active_tbl_like_readout_candidate | 7.8095 | -0.2127 | 0.3607 | hadron_neighbor:231;photon_neighbor:74;particle0_best_lepton:65;nearest_hadron_to_best_lepton:64;hard_hadron:55 |
| L2_ch128:160 | lost_hqql_evidence_candidate | -6.6534 | -0.2256 | -0.0576 | particle0_best_lepton:146;hard_hadron:82;photon_neighbor:67;hadron_neighbor:67;hardest_hadron:59 |
| L2_ch0:32 | lost_hqql_evidence_candidate | -2.3092 | 0.0875 | 0.0778 | particle0_best_lepton:147;hard_hadron:98;hardest_hadron:72;photon_neighbor:54;hadron_neighbor:51 |
| L2_ch96:128 | mixed_or_unclear | -2.0797 | 0.0626 | -0.1330 | photon_neighbor:118;hadron_neighbor:100;particle0_best_lepton:96;hard_hadron:59;second_lepton:49 |
| L1_ch48:64 | active_tbl_like_readout_candidate | 1.1887 | -0.3795 | 0.0326 | photon_neighbor:180;hadron_neighbor:180;hard_hadron:68;nearest_hadron_to_best_lepton:32;hardest_hadron:20 |
| L0_ch48:56 | mixed_or_unclear | -0.4934 | -0.1276 | 0.8918 | photon_neighbor:251;hadron_neighbor:199;hard_hadron:18;particle0_best_lepton:13;nearest_hadron_to_best_lepton:12 |
| L2_ch192:224 | lost_hqql_evidence_candidate | -0.3476 | 0.2617 | 0.5661 | particle0_best_lepton:138;hard_hadron:112;hardest_hadron:88;photon_neighbor:52;second_lepton:45 |
| L2_ch64:96 | lost_hqql_evidence_candidate | -0.3136 | -0.4580 | -0.3468 | particle0_best_lepton:146;hadron_neighbor:137;photon_neighbor:79;hard_hadron:51;second_lepton:30 |

## Note

This V1 uses existing V2/V2.1 tables. To make it truly all-head, run V2 with a full HEADS list, then rerun this postprocessor. Exact EdgeConv source-block weight decomposition is reserved for V2 after module parsing is validated.
