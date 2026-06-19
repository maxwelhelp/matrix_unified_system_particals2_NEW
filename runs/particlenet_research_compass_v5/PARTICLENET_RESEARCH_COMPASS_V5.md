# ParticleNet Research Compass v5

Purpose: richer research layer for particle-interaction hypotheses. It adds EdgeConv channel-head groups, per-class feature channels, known observables, and class contrasts.

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

## Priority hypotheses / research notes

- EdgeConv pseudo-head hypothesis: strongest channel-head groups are L1:ch16:32, L2:ch224:256, L0:ch40:48, L1:ch112:128, L0:ch24:32. These groups should be traced as internal model heads.
- Route-width hypothesis L0: label_Wqq has compact neighbor routing (0.1317), label_Tbqq has wide routing (0.2550).
- Route-width hypothesis L1: label_Wqq has compact neighbor routing (0.1572), label_Tbqq has wide routing (0.2793).
- Route-width hypothesis L2: label_Wqq has compact neighbor routing (0.1599), label_Tbqq has wide routing (0.2873).
- Route-width hypothesis L0: label_Wqq has compact neighbor routing (0.1317), label_Tbqq has wide routing (0.2550).
- Route-width hypothesis L1: label_Wqq has compact neighbor routing (0.1572), label_Tbqq has wide routing (0.2793).
- Route-width hypothesis L2: label_Wqq has compact neighbor routing (0.1599), label_Tbqq has wide routing (0.2873).
- label_Hbb: strongest explicit feature-channel candidate is part_logerel with logit_drop=6.05.
- label_Hcc: strongest explicit feature-channel candidate is part_logerel with logit_drop=6.91.
- label_Hgg: strongest explicit feature-channel candidate is part_deta with logit_drop=5.85.
- label_Hqql: strongest explicit feature-channel candidate is part_pt_log with logit_drop=10.19.
- label_QCD: strongest explicit feature-channel candidate is part_deta with logit_drop=7.80.
- label_Tbl: strongest explicit feature-channel candidate is part_deta with logit_drop=9.48.
- label_Tbqq: strongest explicit feature-channel candidate is part_deltaR with logit_drop=6.46.
- label_Wqq: strongest explicit feature-channel candidate is part_logptrel with logit_drop=10.23.
- label_Zqq: strongest explicit feature-channel candidate is part_logptrel with logit_drop=9.10.
- Leading-particle control: top_pt ablation accuracy=0.449 vs random=0.725; leading particles are not interchangeable with random particles.

## EdgeConv pseudo-head groups: strongest causal channel groups
| rank | layer | channel_head | channels | delta_logit | KL | top1 | acc->patch_acc |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 1 | 1 | 16:32 | 9.1146 | 1.2543 | 0.5328 | 0.7574->0.4934 |
| 2 | 2 | 7 | 224:256 | 4.7637 | 0.3071 | 0.7770 | 0.7574->0.6945 |
| 3 | 0 | 5 | 40:48 | 3.8152 | 0.4933 | 0.6949 | 0.7574->0.6203 |
| 4 | 1 | 7 | 112:128 | 3.2633 | 0.3863 | 0.7215 | 0.7574->0.6418 |
| 5 | 0 | 3 | 24:32 | 2.3407 | 0.7448 | 0.6207 | 0.7574->0.5578 |
| 6 | 0 | 1 | 8:16 | 1.6804 | 0.3652 | 0.7145 | 0.7574->0.6227 |
| 7 | 2 | 2 | 64:96 | 1.5940 | 0.0298 | 0.9270 | 0.7574->0.7418 |
| 8 | 0 | 6 | 48:56 | 1.3935 | 0.4176 | 0.6895 | 0.7574->0.6215 |
| 9 | 0 | 2 | 16:24 | 1.0691 | 0.3690 | 0.7262 | 0.7574->0.6297 |
| 10 | 2 | 0 | 0:32 | 0.8878 | 0.1968 | 0.8141 | 0.7574->0.6777 |
| 11 | 0 | 0 | 0:8 | 0.8533 | 0.4884 | 0.6445 | 0.7574->0.5973 |
| 12 | 1 | 6 | 96:112 | 0.8114 | 0.1861 | 0.7789 | 0.7574->0.6840 |
| 13 | 2 | 4 | 128:160 | 0.7800 | 0.0461 | 0.9039 | 0.7574->0.7453 |
| 14 | 0 | 7 | 56:64 | 0.6102 | 0.2228 | 0.7598 | 0.7574->0.6723 |
| 15 | 0 | 4 | 32:40 | 0.4912 | 0.1227 | 0.8672 | 0.7574->0.7152 |
| 16 | 1 | 2 | 32:48 | 0.4806 | 0.1153 | 0.8367 | 0.7574->0.7090 |
| 17 | 2 | 5 | 160:192 | 0.4214 | 0.0372 | 0.9430 | 0.7574->0.7508 |
| 18 | 1 | 3 | 48:64 | 0.4032 | 0.0586 | 0.8922 | 0.7574->0.7359 |
| 19 | 1 | 5 | 80:96 | 0.3713 | 0.0877 | 0.8988 | 0.7574->0.7418 |
| 20 | 2 | 6 | 192:224 | 0.3158 | 0.0336 | 0.9402 | 0.7574->0.7488 |
| 21 | 1 | 0 | 0:16 | 0.2483 | 0.1032 | 0.8609 | 0.7574->0.7340 |
| 22 | 2 | 1 | 32:64 | 0.1883 | 0.0512 | 0.9016 | 0.7574->0.7414 |
| 23 | 2 | 3 | 96:128 | 0.1720 | 0.0215 | 0.9359 | 0.7574->0.7586 |
| 24 | 1 | 4 | 64:80 | 0.1514 | 0.0616 | 0.8949 | 0.7574->0.7379 |

## Per-class strongest explicit feature channel
| class | feature | logit_drop | acc_drop | base->patch_acc |
| --- | --- | --- | --- | --- |
| label_H4q | part_deta | 4.6871 | 0.2305 | 0.7812->0.5508 |
| label_Hbb | part_logerel | 6.0519 | 0.1680 | 0.6484->0.4805 |
| label_Hcc | part_logerel | 6.9139 | 0.5078 | 0.5820->0.0742 |
| label_Hgg | part_deta | 5.8504 | 0.6328 | 0.6914->0.0586 |
| label_Hqql | part_pt_log | 10.1857 | 0.8906 | 0.9570->0.0664 |
| label_QCD | part_deta | 7.7969 | 0.0820 | 0.6992->0.6172 |
| label_Tbl | part_deta | 9.4816 | 0.1992 | 0.9688->0.7695 |
| label_Tbqq | part_deltaR | 6.4561 | 0.7930 | 0.9062->0.1133 |
| label_Wqq | part_logptrel | 10.2271 | 0.7188 | 0.7305->0.0117 |
| label_Zqq | part_logptrel | 9.1045 | 0.6094 | 0.6094->0.0000 |

## Known observables by class
| class | n | jet_nparticles_mean | jet_sdmass_mean | jet_tau1_mean | jet_tau2_mean | jet_tau3_mean | jet_tau4_mean |
| --- | --- | --- | --- | --- | --- | --- | --- |
| label_Hbb | 256 | 41.5977 | 104.9351 | 0.1713 | 0.0572 | 0.0397 | 0.0328 |
| label_Hcc | 256 | 38.6680 | 113.0451 | 0.1807 | 0.0576 | 0.0389 | 0.0316 |
| label_Hgg | 256 | 55.8945 | 103.6110 | 0.1833 | 0.0817 | 0.0601 | 0.0493 |
| label_Hqql | 256 | 28.7344 | 80.2343 | 0.1416 | 0.0647 | 0.0333 | 0.0236 |
| label_H4q | 256 | 48.6953 | 104.9481 | 0.1939 | 0.1040 | 0.0656 | 0.0484 |
| label_Tbl | 256 | 27.8047 | 109.0637 | 0.1780 | 0.0453 | 0.0273 | 0.0209 |
| label_Tbqq | 256 | 49.9648 | 163.6966 | 0.2718 | 0.1273 | 0.0617 | 0.0471 |
| label_Wqq | 256 | 31.6680 | 72.4410 | 0.1230 | 0.0437 | 0.0300 | 0.0241 |
| label_QCD | 256 | 36.8125 | 62.0474 | 0.1064 | 0.0517 | 0.0367 | 0.0293 |
| label_Zqq | 256 | 34.1484 | 80.7730 | 0.1292 | 0.0478 | 0.0328 | 0.0265 |

## Class contrast table
| contrast | L0_dr_delta | L1_dr_delta | L2_dr_delta | sdmass_delta | nparticles_delta |
| --- | --- | --- | --- | --- | --- |
| label_Wqq_vs_label_Zqq | -0.0222 | -0.0265 | -0.0272 | -8.3320 | -2.4805 |
| label_Tbqq_vs_label_Tbl | 0.0517 | 0.0539 | 0.0568 | 54.6329 | 22.1602 |
| label_Hbb_vs_label_Hcc | -0.0072 | -0.0091 | -0.0108 | -8.1100 | 2.9297 |
| label_Hbb_vs_label_Hgg | 0.0097 | 0.0113 | 0.0114 | 1.3241 | -14.2969 |
| label_H4q_vs_label_Hqql | 0.0063 | 0.0062 | 0.0061 | 24.7138 | 19.9609 |
| label_QCD_vs_label_Wqq | 0.0259 | 0.0324 | 0.0363 | -10.3936 | 5.1445 |
| label_QCD_vs_label_Tbqq | -0.0973 | -0.0896 | -0.0911 | -101.6492 | -13.1523 |

## Tables written

- `reports/latest/tables/research_edge_channel_heads.csv`
- `reports/latest/tables/research_edge_channel_heads_per_class.csv`
- `reports/latest/tables/research_feature_channels_per_class.csv`
- `reports/latest/tables/research_known_observables_by_class.csv`
- `reports/latest/tables/research_class_contrasts.csv`
