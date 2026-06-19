# Real Particle Patch Controls v2 balanced

checkpoint=local_checkpoints/part/ParT_kinpid.pt
mode=kinpid
n=2560 samples_per_file=256
missing=[] unexpected=[]

## Baseline
{
  "patch": "baseline",
  "layer": "",
  "group": "",
  "n": 2560,
  "pred_counts": "[1534, 45, 106, 3, 41, 7, 771, 34, 1, 18]",
  "true_counts": "[256, 256, 256, 256, 256, 256, 256, 256, 256, 256]",
  "acc": 0.10507812350988388
}

## Top patches
| rank | patch | layer | group | delta_logit | KL | top1 | acc->patch_acc |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | cls_block_zero | 0 | cls_block | 3.6605 | 2.0935 | 0.2883 | 0.1051->0.1012 |
| 2 | cls_block_zero | 1 | cls_block | 3.4113 | 1.1589 | 0.5992 | 0.1051->0.1000 |
| 3 | particle_block_skip | 4 | block | 0.3249 | 0.1752 | 0.8063 | 0.1051->0.1184 |
| 4 | particle_block_skip | 5 | block | 0.2715 | 0.1475 | 0.8266 | 0.1051->0.1156 |
| 5 | particle_block_skip | 6 | block | -0.1272 | 0.3157 | 0.7871 | 0.1051->0.0855 |
| 6 | mlp_top_group_zero | 4 | top32 | -0.1155 | 0.0134 | 0.9547 | 0.1051->0.1066 |
| 7 | mlp_top_group_zero | 3 | top32 | -0.1134 | 0.0249 | 0.9387 | 0.1051->0.1086 |
| 8 | pair_embed_zero |  | pair_bias | -0.1049 | 0.9267 | 0.6910 | 0.1051->0.0797 |
| 9 | particle_block_skip | 0 | block | -0.0994 | 0.9152 | 0.6574 | 0.1051->0.0898 |
| 10 | mlp_top_group_zero | 0 | top32 | -0.0931 | 0.0262 | 0.9359 | 0.1051->0.1023 |
| 11 | particle_block_skip | 2 | block | 0.0851 | 0.1619 | 0.8348 | 0.1051->0.0918 |
| 12 | particle_block_skip | 7 | block | 0.0796 | 0.3712 | 0.7461 | 0.1051->0.0852 |
| 13 | mlp_top_group_zero | 7 | top32 | 0.0749 | 0.0239 | 0.9328 | 0.1051->0.1031 |
| 14 | mlp_top_group_zero | 2 | top32 | -0.0422 | 0.0190 | 0.9457 | 0.1051->0.1055 |
| 15 | mlp_top_group_zero | 1 | top32 | 0.0324 | 0.0378 | 0.9176 | 0.1051->0.1066 |
| 16 | mlp_top_group_zero | 5 | top32 | 0.0117 | 0.0115 | 0.9574 | 0.1051->0.1055 |
| 17 | particle_block_skip | 1 | block | -0.0025 | 0.3443 | 0.7730 | 0.1051->0.1125 |
| 18 | mlp_top_group_zero | 6 | top32 | -0.0014 | 0.0100 | 0.9586 | 0.1051->0.1004 |
| 19 | particle_block_skip | 3 | block | 0.0012 | 0.2513 | 0.7988 | 0.1051->0.0938 |
