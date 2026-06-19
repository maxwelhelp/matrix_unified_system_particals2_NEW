# Real Particle Patch Controls v1

checkpoint=local_checkpoints/part/ParT_full.pt
mode=full
n=128
missing=[] unexpected=[]

## Baseline
{
  "patch": "baseline",
  "layer": "",
  "group": "",
  "pred_counts": "[53, 0, 10, 0, 0, 4, 56, 0, 0, 5]",
  "acc": 0.0
}

## Top patches
| rank | patch | layer | group | delta_logit | KL | top1 | acc->patch_acc |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | cls_block_zero | 1 | cls_block | 4.2553 | 1.2167 | 0.4141 | 0.0000->0.0000 |
| 2 | cls_block_zero | 0 | cls_block | 1.6956 | 4.1235 | 0.4141 | 0.0000->0.0000 |
| 3 | pair_embed_zero |  | pair_bias | 0.7856 | 0.8361 | 0.5938 | 0.0000->0.0000 |
| 4 | particle_block_skip | 0 | block | 0.7510 | 0.7726 | 0.6328 | 0.0000->0.0000 |
| 5 | particle_block_skip | 3 | block | 0.3986 | 0.2415 | 0.7500 | 0.0000->0.0078 |
| 6 | particle_block_skip | 2 | block | 0.3725 | 0.3523 | 0.7500 | 0.0000->0.0000 |
| 7 | particle_block_skip | 7 | block | 0.3362 | 0.5162 | 0.7266 | 0.0000->0.0000 |
| 8 | particle_block_skip | 4 | block | 0.2860 | 0.2909 | 0.7266 | 0.0000->0.0000 |
| 9 | particle_block_skip | 1 | block | 0.2178 | 0.4030 | 0.7188 | 0.0000->0.0000 |
| 10 | particle_block_skip | 5 | block | 0.1369 | 0.5209 | 0.6719 | 0.0000->0.0000 |
| 11 | particle_block_skip | 6 | block | 0.1356 | 0.5998 | 0.6484 | 0.0000->0.0000 |
| 12 | mlp_top_group_zero | 3 | top32 | 0.1022 | 0.0108 | 0.9219 | 0.0000->0.0000 |
| 13 | mlp_top_group_zero | 1 | top32 | 0.0560 | 0.0619 | 0.8984 | 0.0000->0.0000 |
| 14 | mlp_top_group_zero | 6 | top32 | -0.0345 | 0.0368 | 0.9062 | 0.0000->0.0000 |
| 15 | mlp_top_group_zero | 5 | top32 | -0.0280 | 0.0146 | 0.9375 | 0.0000->0.0000 |
| 16 | mlp_top_group_zero | 2 | top32 | 0.0271 | 0.0192 | 0.9219 | 0.0000->0.0000 |
| 17 | mlp_top_group_zero | 7 | top32 | 0.0249 | 0.0574 | 0.8984 | 0.0000->0.0000 |
| 18 | mlp_top_group_zero | 4 | top32 | 0.0173 | 0.0186 | 0.9453 | 0.0000->0.0000 |
| 19 | mlp_top_group_zero | 0 | top32 | -0.0115 | 0.0684 | 0.8828 | 0.0000->0.0000 |
