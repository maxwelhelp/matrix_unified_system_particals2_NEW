# Real Particle Patch Controls v3 official preprocess

checkpoint=local_checkpoints/part/ParT_full.pt
mode=full
preprocess=official_wrap_v3
n=2560 samples_per_file=256
missing=[] unexpected=[]

## Baseline
{
  "patch": "baseline",
  "layer": "",
  "group": "",
  "n": 2560,
  "pred_counts": "[909, 0, 206, 0, 21, 344, 954, 0, 0, 126]",
  "true_counts": "[256, 256, 256, 256, 256, 256, 256, 256, 256, 256]",
  "acc": 0.11640625447034836
}

## Top patches
| rank | patch | layer | group | delta_logit | KL | top1 | acc->patch_acc |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | cls_block_zero | 1 | cls_block | 4.6446 | 1.4241 | 0.3551 | 0.1164->0.1000 |
| 2 | cls_block_zero | 0 | cls_block | 2.1336 | 3.8343 | 0.3539 | 0.1164->0.1008 |
| 3 | pair_embed_zero |  | pair_bias | 1.3839 | 0.9653 | 0.6195 | 0.1164->0.1109 |
| 4 | particle_block_skip | 0 | block | 0.7420 | 0.7912 | 0.6547 | 0.1164->0.1074 |
| 5 | particle_block_skip | 1 | block | 0.4515 | 0.3872 | 0.7258 | 0.1164->0.1129 |
| 6 | particle_block_skip | 7 | block | 0.3689 | 0.8128 | 0.6402 | 0.1164->0.1121 |
| 7 | particle_block_skip | 6 | block | 0.1675 | 0.4169 | 0.7051 | 0.1164->0.1219 |
| 8 | particle_block_skip | 2 | block | 0.1606 | 0.2716 | 0.7836 | 0.1164->0.1172 |
| 9 | particle_block_skip | 3 | block | 0.1272 | 0.2015 | 0.8227 | 0.1164->0.1152 |
| 10 | particle_block_skip | 5 | block | -0.0810 | 0.3793 | 0.7176 | 0.1164->0.1324 |
| 11 | mlp_top_group_zero | 7 | top32 | -0.0549 | 0.1166 | 0.8742 | 0.1164->0.1176 |
| 12 | mlp_top_group_zero | 6 | top32 | -0.0320 | 0.0306 | 0.9266 | 0.1164->0.1133 |
| 13 | mlp_top_group_zero | 1 | top32 | 0.0292 | 0.0238 | 0.9469 | 0.1164->0.1184 |
| 14 | particle_block_skip | 4 | block | -0.0229 | 0.2441 | 0.7820 | 0.1164->0.1258 |
| 15 | mlp_top_group_zero | 2 | top32 | 0.0190 | 0.0125 | 0.9500 | 0.1164->0.1148 |
| 16 | mlp_top_group_zero | 0 | top32 | -0.0138 | 0.0308 | 0.9313 | 0.1164->0.1168 |
| 17 | mlp_top_group_zero | 4 | top32 | 0.0130 | 0.0138 | 0.9469 | 0.1164->0.1184 |
| 18 | mlp_top_group_zero | 3 | top32 | 0.0078 | 0.0071 | 0.9684 | 0.1164->0.1160 |
| 19 | mlp_top_group_zero | 5 | top32 | 7.644e-04 | 0.0191 | 0.9406 | 0.1164->0.1187 |
