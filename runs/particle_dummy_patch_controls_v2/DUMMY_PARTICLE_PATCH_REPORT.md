# Dummy Particle Patch Controls v2

Checks causal patch handles on dummy ParT: pair-bias zero, particle-block skip, cls-block zero, MLP top-neuron group zero.

| rank | patch | layer | group | delta_top_logit | KL | top1 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | cls_block_zero | 0 | cls_block | 1.7341 | 0.5371 | 0.1250 |
| 2 | particle_block_skip | 0 | block | 1.7140 | 1.3436 | 0.1250 |
| 3 | particle_block_skip | 1 | block | 1.3624 | 0.6742 | 0.3750 |
| 4 | mlp_top_group_zero | 0 | top16 | -0.2749 | 0.0342 | 1.0000 |
| 5 | mlp_top_group_zero | 1 | top16 | -0.0199 | 0.0265 | 0.7500 |
| 6 | pair_embed_zero |  | pair_bias | -0.0182 | 0.0015 | 1.0000 |
