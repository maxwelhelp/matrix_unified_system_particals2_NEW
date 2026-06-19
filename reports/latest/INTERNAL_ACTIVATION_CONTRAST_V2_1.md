# INTERNAL_ACTIVATION_CONTRAST_V2_1

Particle-role annotation for V2 top activations.

## Focus role contrasts
| head | role | A top1 | B top1 | C top1 | B-A top1 | A top3 | B top3 | C top3 | B-A top3 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| L1_ch80:96 | hard_hadron | 0.0312 | 0.1818 | 0.0391 | 0.1506 | 0.0521 | 0.2121 | 0.0625 | 0.1600 |
| L1_ch80:96 | hadron_neighbor | 0.6250 | 0.4545 | 0.5078 | -0.1705 | 0.4583 | 0.4242 | 0.4115 | -0.0341 |
| L1_ch32:48 | hadron_neighbor | 0.6250 | 0.5455 | 0.4453 | -0.0795 | 0.5208 | 0.4545 | 0.4323 | -0.0663 |
| L1_ch32:48 | hard_hadron | 0.0625 | 0.0909 | 0.1094 | 0.0284 | 0.0521 | 0.1515 | 0.1172 | 0.0994 |
| L1_ch32:48 | nearest_hadron_to_best_lepton | 0.0938 | 0.1818 | 0.1641 | 0.0881 | 0.1250 | 0.0909 | 0.1276 | -0.0341 |
| L2_ch128:160 | second_lepton | 0.0000 | 0.0000 | 0.0234 | 0.0000 | 0.0208 | 0.1212 | 0.0911 | 0.1004 |
| L2_ch128:160 | particle0_best_lepton | 0.9688 | 0.9091 | 0.8125 | -0.0597 | 0.3229 | 0.3030 | 0.2734 | -0.0199 |
| L2_ch128:160 | best_lepton | 0.0312 | 0.0909 | 0.1641 | 0.0597 | 0.0104 | 0.0303 | 0.0547 | 0.0199 |
| L2_ch128:160 | hard_hadron | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.2604 | 0.1818 | 0.1328 | -0.0786 |
| L1_ch32:48 | particle0_best_lepton | 0.0625 | 0.0000 | 0.1875 | -0.0625 | 0.0938 | 0.0909 | 0.1380 | -0.0028 |
| L2_ch128:160 | hardest_hadron | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.1562 | 0.0909 | 0.1068 | -0.0653 |
| L2_ch128:160 | nearest_hadron_to_best_lepton | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0606 | 0.0391 | 0.0606 |
| L1_ch32:48 | hardest_hadron | 0.0000 | 0.0000 | 0.0078 | 0.0000 | 0.0312 | 0.0000 | 0.0182 | -0.0312 |
| L1_ch80:96 | particle0_best_lepton | 0.0000 | 0.0000 | 0.0469 | 0.0000 | 0.0104 | 0.0303 | 0.0547 | 0.0199 |
| L1_ch80:96 | nearest_hadron_to_best_lepton | 0.0000 | 0.0000 | 0.0234 | 0.0000 | 0.0104 | 0.0000 | 0.0286 | -0.0104 |
| L1_ch80:96 | second_lepton | 0.0000 | 0.0000 | 0.0078 | 0.0000 | 0.0104 | 0.0000 | 0.0104 | -0.0104 |
| L2_ch128:160 | hadron_neighbor | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.1146 | 0.1212 | 0.1354 | 0.0066 |
| L1_ch80:96 | best_lepton | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| L1_ch80:96 | hardest_hadron | 0.0000 | 0.0000 | 0.0234 | 0.0000 | 0.0000 | 0.0000 | 0.0104 | 0.0000 |
| L1_ch32:48 | best_lepton | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0052 | 0.0000 |
| L1_ch32:48 | second_lepton | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0078 | 0.0000 |

## Interpretation

If `second_lepton` is high in B for L1_ch80:96, the second-lepton trigger directly drives the Tbl-like route. If hadron roles dominate, the L1 route is more geometry-driven. If particle0/best_lepton dominates in both A and B, the same core is read differently due to context.
