# ParticleNet Real Patch Controls v1

checkpoint=local_checkpoints/part/ParticleNet_kinpid.pt
mode=kinpid
n=2560
missing=[] unexpected=[]

## Baseline
{
  "patch": "baseline",
  "layer": "",
  "group": "",
  "n": 2560,
  "acc": 0.7574219107627869,
  "pred_counts": "[241, 243, 220, 280, 274, 255, 251, 270, 273, 253]",
  "true_counts": "[256, 256, 256, 256, 256, 256, 256, 256, 256, 256]"
}

## Adapter
{
  "has_edge_convs": true,
  "n_edge_convs": 3,
  "has_fc": true,
  "n_fc": 2,
  "has_bn_fts": true,
  "use_counts": true,
  "use_fusion": false
}

## Top causal patches
| rank | patch | layer | group | delta_logit | KL | top1 | acc->patch_acc |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | edge_conv_zero | 1 | edge_conv | 246.9066 | 91.9271 | 0.0988 | 0.7574->0.1000 |
| 2 | edge_conv_zero | 0 | edge_conv | 237.1047 | 19.0814 | 0.0996 | 0.7574->0.1000 |
| 3 | features_zero | input | features_zero | 108.2718 | 48.0418 | 0.0953 | 0.7574->0.0961 |
| 4 | feature_group_zero | input | coords_last2 | 34.7161 | 7.0771 | 0.1406 | 0.7574->0.1402 |
| 5 | edge_conv_zero | 2 | edge_conv | 21.8302 | 4.6334 | 0.0941 | 0.7574->0.1000 |
| 6 | feature_group_zero | input | kin_logs_0_4 | 13.7563 | 4.4309 | 0.1641 | 0.7574->0.1441 |
| 7 | mask_all_true | input | mask_all_true | 8.3195 | 2.3567 | 0.2430 | 0.7574->0.2355 |
| 8 | feature_group_zero | input | pid_charge_5_10 | 6.5074 | 3.5734 | 0.1035 | 0.7574->0.1047 |
| 9 | points_zero | input | points_zero | 1.2280 | 0.3049 | 0.7719 | 0.7574->0.6734 |
| 10 | fc_zero | 0 | fc | 0.8952 | 1.7606 | 0.1066 | 0.7574->0.1000 |
| 11 | fc_zero | 1 | fc | 0.8754 | 1.6416 | 0.0941 | 0.7574->0.1000 |
