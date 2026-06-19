# ParticleNet Hypothesis Atlas v3

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

## Global causal map: all inputs, particles, EdgeConv and FC layers
| rank | patch | layer | group | delta_logit | KL | top1 | acc->patch_acc |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | edge_conv_zero | 1 | edge_conv | 246.9066 | 91.9271 | 0.0988 | 0.7574->0.1000 |
| 2 | edge_conv_zero | 0 | edge_conv | 237.1047 | 19.0814 | 0.0996 | 0.7574->0.1000 |
| 3 | features_zero | input | all_features | 108.2718 | 48.0418 | 0.0953 | 0.7574->0.0961 |
| 4 | feature_group_zero | input | coords_last2 | 34.7161 | 7.0771 | 0.1406 | 0.7574->0.1402 |
| 5 | edge_conv_zero | 2 | edge_conv | 21.8302 | 4.6334 | 0.0941 | 0.7574->0.1000 |
| 6 | feature_group_zero | input | kin_logs_0_4 | 13.7563 | 4.4309 | 0.1641 | 0.7574->0.1441 |
| 7 | mask_all_true | input | mask | 8.3195 | 2.3567 | 0.2430 | 0.7574->0.2355 |
| 8 | feature_group_zero | input | pid_charge_5_10 | 6.5074 | 3.5734 | 0.1035 | 0.7574->0.1047 |
| 9 | feature_channel_zero | input | part_deta | 6.2161 | 1.2076 | 0.5805 | 0.7574->0.5305 |
| 10 | feature_channel_zero | input | part_logptrel | 6.0046 | 1.6883 | 0.4211 | 0.7574->0.3824 |
| 11 | particle_topk_mask_zero | particles | top_pt | 5.6237 | 2.1800 | 0.5180 | 0.7574->0.4488 |
| 12 | particle_topk_mask_zero | particles | top_energy | 5.6237 | 2.1800 | 0.5180 | 0.7574->0.4488 |
| 13 | particle_topk_mask_zero | particles | high_deltaR | 5.6237 | 2.1800 | 0.5180 | 0.7574->0.4488 |
| 14 | feature_channel_zero | input | part_pt_log | 4.7710 | 2.2510 | 0.1707 | 0.7574->0.1664 |
| 15 | feature_channel_zero | input | part_logerel | 4.5538 | 1.0433 | 0.5984 | 0.7574->0.5336 |
| 16 | feature_channel_zero | input | part_dphi | 4.0908 | 0.7598 | 0.6039 | 0.7574->0.5457 |
| 17 | feature_channel_zero | input | part_deltaR | 3.8997 | 0.9278 | 0.5855 | 0.7574->0.5262 |
| 18 | points_zero | input | all_points | 1.2280 | 0.3049 | 0.7719 | 0.7574->0.6734 |
| 19 | feature_channel_zero | input | part_isChargedHadron | 1.1772 | 0.4939 | 0.6547 | 0.7574->0.5859 |
| 20 | feature_channel_zero | input | part_isPhoton | 1.0152 | 0.4623 | 0.6762 | 0.7574->0.6059 |
| 21 | fc_zero | 0 | fc | 0.8952 | 1.7606 | 0.1066 | 0.7574->0.1000 |
| 22 | fc_zero | 1 | fc | 0.8754 | 1.6416 | 0.0941 | 0.7574->0.1000 |
| 23 | feature_channel_zero | input | part_isMuon | 0.8640 | 0.5698 | 0.8848 | 0.7574->0.6562 |
| 24 | feature_channel_zero | input | part_charge | 0.8485 | 0.4715 | 0.6711 | 0.7574->0.6066 |
| 25 | feature_channel_zero | input | part_isElectron | 0.8315 | 0.5666 | 0.8781 | 0.7574->0.6652 |
| 26 | feature_channel_zero | input | part_isNeutralHadron | 0.6090 | 0.2730 | 0.7820 | 0.7574->0.6734 |
| 27 | feature_channel_zero | input | part_e_log | 0.3349 | 0.0532 | 0.8926 | 0.7574->0.7316 |

## Per-class strongest causal patch
| class | patch | layer | group | acc_drop | logit_drop | base->patch_acc |
| --- | --- | --- | --- | --- | --- | --- |
| label_QCD | edge_conv_zero | 1 | edge_conv | 0.6992 | 253.5277 | 0.6992->0.0000 |
| label_Hbb | edge_conv_zero | 1 | edge_conv | 0.6484 | 281.1666 | 0.6484->0.0000 |
| label_Hcc | edge_conv_zero | 1 | edge_conv | 0.5820 | 277.2205 | 0.5820->0.0000 |
| label_Hgg | edge_conv_zero | 1 | edge_conv | 0.6914 | 318.1755 | 0.6914->0.0000 |
| label_H4q | edge_conv_zero | 1 | edge_conv | 0.7812 | 295.5944 | 0.7812->0.0000 |
| label_Hqql | edge_conv_zero | 1 | edge_conv | 0.9570 | 168.9806 | 0.9570->0.0000 |
| label_Zqq | edge_conv_zero | 1 | edge_conv | 0.6094 | 259.6505 | 0.6094->0.0000 |
| label_Wqq | edge_conv_zero | 0 | edge_conv | 0.7305 | 239.6121 | 0.7305->0.0000 |
| label_Tbqq | edge_conv_zero | 1 | edge_conv | 0.9062 | 243.2261 | 0.9062->0.0000 |
| label_Tbl | edge_conv_zero | 0 | edge_conv | 0.9688 | 253.6387 | 0.9688->0.0000 |

## Candidate hypotheses

- label_H4q: class decision is strongly dependent on `edge_conv_zero:1:edge_conv`; patch acc drop=0.781.
- label_Hbb: class decision is strongly dependent on `edge_conv_zero:1:edge_conv`; patch acc drop=0.648.
- label_Hcc: class decision is strongly dependent on `edge_conv_zero:1:edge_conv`; patch acc drop=0.582.
- label_Hgg: class decision is strongly dependent on `edge_conv_zero:1:edge_conv`; patch acc drop=0.691.
- label_Hqql: class decision is strongly dependent on `edge_conv_zero:1:edge_conv`; patch acc drop=0.957.
- label_QCD: class decision is strongly dependent on `edge_conv_zero:1:edge_conv`; patch acc drop=0.699.
- label_Tbl: class decision is strongly dependent on `edge_conv_zero:0:edge_conv`; patch acc drop=0.969.
- label_Tbqq: class decision is strongly dependent on `edge_conv_zero:1:edge_conv`; patch acc drop=0.906.
- label_Wqq: class decision is strongly dependent on `edge_conv_zero:0:edge_conv`; patch acc drop=0.730.
- label_Zqq: class decision is strongly dependent on `edge_conv_zero:1:edge_conv`; patch acc drop=0.609.
- Global mechanism: strongest causal components are edge_conv_zero[1:edge_conv], edge_conv_zero[0:edge_conv], features_zero[input:all_features].

## Example-level signed drops
| idx | pred | pred_label | true | true_label | conf | pred_logit | true_logit | drop_features_zero_input_all_features | drop_feature_group_zero_input_coords_last2 | drop_feature_group_zero_input_kin_logs_0_4 | drop_mask_all_true_input_mask | drop_feature_group_zero_input_pid_charge_5_10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2117 | 0 | label_QCD | 0 | label_QCD | 0.9999281167984009 | -16.417905807495117 | -16.417905807495117 | 5.238534927368164 | 8.732532501220703 | -1.190047264099121 | 20.129968643188477 | 0.7359466552734375 |
| 2113 | 0 | label_QCD | 0 | label_QCD | 0.9993353486061096 | -1.7375850677490234 | -1.7375850677490234 | 10.493647575378418 | 30.535337448120117 | 16.479225158691406 | 15.930545806884766 | 0.42104363441467285 |
| 246 | 1 | label_Hbb | 1 | label_Hbb | 0.9978238344192505 | -0.041639357805252075 | -0.041639357805252075 | 86.67711639404297 | 15.878432273864746 | 14.470736503601074 | 10.526312828063965 | 9.179255485534668 |
| 206 | 1 | label_Hbb | 1 | label_Hbb | 0.9972424507141113 | 0.595314085483551 | 0.595314085483551 | 87.31407165527344 | 17.41710662841797 | 16.16995620727539 | 12.448153495788574 | 10.331439018249512 |
| 425 | 2 | label_Hcc | 2 | label_Hcc | 0.9970899820327759 | 2.4434261322021484 | 2.4434261322021484 | 111.65914916992188 | 16.857925415039062 | 22.483232498168945 | 33.23802947998047 | 10.662986755371094 |
| 333 | 2 | label_Hcc | 2 | label_Hcc | 0.9881271719932556 | 2.373568058013916 | 2.373568058013916 | 111.58928680419922 | 76.23107147216797 | 17.15643310546875 | 17.258224487304688 | 6.23907470703125 |
| 754 | 3 | label_Hgg | 3 | label_Hgg | 0.9879035353660583 | 0.6643581986427307 | 0.6643581986427307 | 114.1934814453125 | 20.471294403076172 | 11.876548767089844 | 9.625391006469727 | 8.971356391906738 |
| 555 | 3 | label_Hgg | 3 | label_Hgg | 0.9755978584289551 | 0.7866596579551697 | 0.7866596579551697 | 114.31578063964844 | 16.46820068359375 | 6.202691555023193 | 4.548703670501709 | 5.148252010345459 |
| 1166 | 4 | label_H4q | 4 | label_H4q | 0.9989914298057556 | 3.247354030609131 | 3.247354030609131 | 165.08956909179688 | 52.25920867919922 | 12.125288009643555 | 21.774852752685547 | 10.154624938964844 |
| 1034 | 4 | label_H4q | 4 | label_H4q | 0.9965152740478516 | 3.253621816635132 | 3.253621816635132 | 165.09584045410156 | 39.3082275390625 | 9.566410064697266 | 20.66577911376953 | 9.976166725158691 |
| 795 | 5 | label_Hqql | 5 | label_Hqql | 0.9999996423721313 | 4.907090663909912 | 4.907090663909912 | 65.86481475830078 | 18.91716957092285 | 34.25741195678711 | 18.98136329650879 | 6.477044582366943 |
| 855 | 5 | label_Hqql | 5 | label_Hqql | 0.9999951124191284 | 3.175077199935913 | 3.175077199935913 | 112.98324584960938 | 39.022647857666016 | 27.083248138427734 | 12.060062408447266 | 5.919833183288574 |
| 2527 | 6 | label_Zqq | 6 | label_Zqq | 0.9607760906219482 | -2.082850456237793 | -2.082850456237793 | 114.49052429199219 | 14.710551261901855 | 11.615408897399902 | 10.64864730834961 | 2.863165855407715 |
| 2414 | 6 | label_Zqq | 6 | label_Zqq | 0.9536870121955872 | 1.5763447284698486 | 1.5763447284698486 | 118.14971923828125 | 50.90066146850586 | 18.10921859741211 | 7.155026435852051 | 6.36085319519043 |
| 1968 | 7 | label_Wqq | 7 | label_Wqq | 0.9745469689369202 | 1.0333333015441895 | 1.0333333015441895 | 106.20655059814453 | 98.07418060302734 | 12.929685592651367 | 11.321527481079102 | 8.551897048950195 |
| 1812 | 7 | label_Wqq | 7 | label_Wqq | 0.9740322232246399 | 0.7448228597640991 | 0.7448228597640991 | 105.91805267333984 | 43.71139144897461 | 13.980262756347656 | 6.621339321136475 | 6.198444366455078 |
| 1702 | 8 | label_Tbqq | 8 | label_Tbqq | 0.999966025352478 | 2.7572081089019775 | 2.7572081089019775 | 136.2233123779297 | 57.95811080932617 | 21.366382598876953 | 11.723438262939453 | 9.784173011779785 |
| 1612 | 8 | label_Tbqq | 8 | label_Tbqq | 0.9999363422393799 | 1.2317509651184082 | 1.2317509651184082 | 134.69786071777344 | 27.123443603515625 | 22.40577507019043 | 13.796672821044922 | 2.673454761505127 |
| 1309 | 9 | label_Tbl | 9 | label_Tbl | 1.0 | 0.5695033073425293 | 0.5695033073425293 | 47.32085037231445 | 31.75030517578125 | 24.240272521972656 | 7.061765193939209 | 11.600107192993164 |
| 1287 | 9 | label_Tbl | 9 | label_Tbl | 1.0 | 1.405466079711914 | 1.405466079711914 | 60.02690124511719 | 19.069049835205078 | 25.797693252563477 | 9.62353801727295 | 9.297764778137207 |

Full CSV tables:
- `reports/latest/tables/hypothesis_global_patches.csv`
- `reports/latest/tables/hypothesis_per_class.csv`
- `reports/latest/tables/hypothesis_examples.csv`
