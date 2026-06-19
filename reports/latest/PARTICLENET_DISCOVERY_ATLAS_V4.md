# ParticleNet Discovery Atlas v4

Purpose: convert causal patches and dynamic graph routes into candidate physics/mechanistic hypotheses. These are not discovery claims yet; they are candidates requiring heldout validation and physics review.

checkpoint=local_checkpoints/part/ParticleNet_kinpid.pt
mode=kinpid
n=2560
missing=[] unexpected=[]

## Baseline

```json
{
  "n": 2560,
  "acc": 0.7574219107627869,
  "pred_counts": [
    241,
    243,
    220,
    280,
    274,
    255,
    251,
    270,
    273,
    253
  ],
  "true_counts": [
    256,
    256,
    256,
    256,
    256,
    256,
    256,
    256,
    256,
    256
  ]
}
```

## Candidate discovery hypotheses

- Global: strongest causal components are edge_conv_zero[1:edge_conv], edge_conv_zero[0:edge_conv], features_zero[input:all_features], feature_group_zero[input:coords_last2], edge_conv_zero[2:edge_conv].
- Feature hypothesis: most influential explicit channels/groups are coords_last2, kin_logs_0_4, pid_charge_5_10, part_deta, part_logptrel.
- Particle-subset hypothesis: removing top_pt particles produces strongest top-8 particle control effect; compare against random_control before claiming physics.
- Route layer 0: neighbor ΔR differs by class; lowest mean label_Wqq=0.1317, highest mean label_Tbqq=0.2550.
- Route layer 1: neighbor ΔR differs by class; lowest mean label_Wqq=0.1572, highest mean label_Tbqq=0.2793.
- Route layer 2: neighbor ΔR differs by class; lowest mean label_Wqq=0.1599, highest mean label_Tbqq=0.2873.

## Corrected particle-subset controls
| group | delta_logit | KL | top1 | acc->patch_acc | jaccard_top_pt |
| --- | --- | --- | --- | --- | --- |
| top_pt | 5.6238 | 2.1800 | 0.5180 | 0.7574->0.4488 | 1.0000 |
| top_energy | 5.6075 | 2.1731 | 0.5191 | 0.7574->0.4484 | 0.9435 |
| wide_angle_high_dr | 0.6982 | 0.2929 | 0.8523 | 0.7574->0.6953 | 0.0061 |
| core_low_dr | 1.2163 | 0.5133 | 0.8578 | 0.7574->0.6949 | 0.0749 |
| random_control | 0.3971 | 0.1870 | 0.8934 | 0.7574->0.7250 | 0.0328 |

## Dynamic KNN / EdgeConv route stats by class
| layer | class | k | neighbor_dr_mean | neighbor_dr_p90 | neighbor_pt_mean | neighbor_energy_mean |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | label_QCD | 16 | 0.1576 | 0.4009 | 20.4406 | 30.2653 |
| 0 | label_Hbb | 16 | 0.1849 | 0.3703 | 16.7192 | 23.4433 |
| 0 | label_Hcc | 16 | 0.1921 | 0.3753 | 17.7219 | 25.9114 |
| 0 | label_Hgg | 16 | 0.1752 | 0.3281 | 13.2720 | 19.2832 |
| 0 | label_H4q | 16 | 0.1736 | 0.3279 | 14.7385 | 21.9574 |
| 0 | label_Hqql | 16 | 0.1674 | 0.3352 | 22.5983 | 32.2673 |
| 0 | label_Zqq | 16 | 0.1539 | 0.3162 | 20.0533 | 29.2829 |
| 0 | label_Wqq | 16 | 0.1317 | 0.2509 | 21.4085 | 34.4694 |
| 0 | label_Tbqq | 16 | 0.2550 | 0.4785 | 13.7468 | 19.1786 |
| 0 | label_Tbl | 16 | 0.2032 | 0.4250 | 19.7456 | 26.5119 |
| 1 | label_QCD | 16 | 0.1897 | 0.4483 | 14.2108 | 20.9522 |
| 1 | label_Hbb | 16 | 0.2050 | 0.4041 | 13.3334 | 18.5863 |
| 1 | label_Hcc | 16 | 0.2141 | 0.4076 | 13.8665 | 20.3897 |
| 1 | label_Hgg | 16 | 0.1937 | 0.3664 | 9.7154 | 14.0313 |
| 1 | label_H4q | 16 | 0.2000 | 0.3736 | 10.8771 | 16.0678 |
| 1 | label_Hqql | 16 | 0.1938 | 0.3841 | 14.4106 | 20.4363 |
| 1 | label_Zqq | 16 | 0.1838 | 0.3685 | 14.6799 | 21.2039 |
| 1 | label_Wqq | 16 | 0.1572 | 0.2949 | 15.8574 | 25.1457 |
| 1 | label_Tbqq | 16 | 0.2793 | 0.5054 | 11.1274 | 15.4656 |
| 1 | label_Tbl | 16 | 0.2253 | 0.4701 | 15.4452 | 20.5148 |
| 2 | label_QCD | 16 | 0.1961 | 0.4728 | 13.9450 | 20.5952 |
| 2 | label_Hbb | 16 | 0.2097 | 0.4136 | 13.4028 | 18.7101 |
| 2 | label_Hcc | 16 | 0.2205 | 0.4196 | 13.9727 | 20.5077 |
| 2 | label_Hgg | 16 | 0.1983 | 0.3741 | 9.7827 | 14.1544 |
| 2 | label_H4q | 16 | 0.2077 | 0.3876 | 10.8817 | 16.0877 |
| 2 | label_Hqql | 16 | 0.2017 | 0.4093 | 14.1890 | 20.1471 |
| 2 | label_Zqq | 16 | 0.1871 | 0.3809 | 15.0174 | 21.6500 |
| 2 | label_Wqq | 16 | 0.1599 | 0.3006 | 16.3702 | 25.9881 |
| 2 | label_Tbqq | 16 | 0.2873 | 0.5200 | 10.9189 | 15.2457 |
| 2 | label_Tbl | 16 | 0.2305 | 0.4870 | 14.8915 | 19.8326 |

## Existing v3 causal tables used as context

- `reports/latest/tables/hypothesis_global_patches.csv`
- `reports/latest/tables/hypothesis_per_class.csv`
- `reports/latest/tables/hypothesis_examples.csv`

## New v4 tables

- `reports/latest/tables/discovery_route_knn_stats.csv`
- `reports/latest/tables/discovery_particle_controls.csv`
