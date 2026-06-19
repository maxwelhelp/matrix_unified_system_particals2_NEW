# Particle0 / Top-k Controls v2

KNN-safe version: ParticleNet is loaded with `trim=False`, so aggressive controls like `keep_only_particle0` do not crash EdgeConv KNN. Removed particles have zero features/points and mask=False.

n_events=2560 baseline_acc=0.7574 mode=kinpid

## Control summary
| control | valid_mean | acc | acc_drop | flip_rate | delta_base_pred_logit |
| --- | --- | --- | --- | --- | --- |
| baseline | 39.3988 | 0.7574 | 0.0000 | 0.0000 | 0.0000 |
| remove_particle0 | 38.3988 | 0.5633 | 0.1941 | 0.3160 | -3.5645 |
| keep_only_particle0 | 1.0000 | 0.2027 | 0.5547 | 0.7941 | -26.5106 |
| remove_top1 | 38.3988 | 0.5633 | 0.1941 | 0.3160 | -3.5645 |
| keep_top1 | 1.0000 | 0.2027 | 0.5547 | 0.7941 | -26.5106 |
| random_remove1_r0 | 38.3988 | 0.7449 | 0.0125 | 0.0609 | -0.2199 |
| random_remove1_r1 | 38.3988 | 0.7387 | 0.0187 | 0.0637 | -0.2120 |
| random_remove1_r2 | 38.3988 | 0.7449 | 0.0125 | 0.0625 | -0.1865 |
| remove_top2 | 37.3988 | 0.4566 | 0.3008 | 0.4664 | -5.5531 |
| keep_top2 | 2.0000 | 0.2430 | 0.5145 | 0.7477 | -16.7977 |
| random_remove2_r0 | 37.3988 | 0.7195 | 0.0379 | 0.0934 | -0.3821 |
| random_remove2_r1 | 37.3988 | 0.7207 | 0.0367 | 0.1012 | -0.4423 |
| random_remove2_r2 | 37.3988 | 0.7301 | 0.0273 | 0.0949 | -0.3323 |
| remove_top4 | 35.3992 | 0.3492 | 0.4082 | 0.5922 | -8.2648 |
| keep_top4 | 3.9996 | 0.2922 | 0.4652 | 0.7004 | -12.2420 |
| random_remove4_r0 | 35.3992 | 0.6871 | 0.0703 | 0.1727 | -0.9011 |
| random_remove4_r1 | 35.3992 | 0.6883 | 0.0691 | 0.1820 | -0.9729 |
| random_remove4_r2 | 35.3992 | 0.6773 | 0.0801 | 0.1809 | -0.8665 |
| remove_top8 | 31.4035 | 0.2691 | 0.4883 | 0.6844 | -11.2240 |
| keep_top8 | 7.9953 | 0.3773 | 0.3801 | 0.6055 | -6.4296 |
| random_remove8_r0 | 31.4035 | 0.5855 | 0.1719 | 0.3090 | -2.5122 |
| random_remove8_r1 | 31.4035 | 0.5883 | 0.1691 | 0.3148 | -2.3222 |
| random_remove8_r2 | 31.4035 | 0.5813 | 0.1762 | 0.3137 | -2.3756 |
| remove_top16 | 23.5000 | 0.1980 | 0.5594 | 0.7871 | -14.7724 |
| keep_top16 | 15.8988 | 0.5391 | 0.2184 | 0.4051 | -1.7016 |
| random_remove16_r0 | 23.5000 | 0.3793 | 0.3781 | 0.5664 | -6.9018 |
| random_remove16_r1 | 23.5000 | 0.3801 | 0.3773 | 0.5703 | -6.8569 |
| random_remove16_r2 | 23.5000 | 0.3891 | 0.3684 | 0.5562 | -6.8688 |

## Random baselines
| family | repeats | acc_mean | acc_drop_mean | flip_mean | delta_logit_mean |
| --- | --- | --- | --- | --- | --- |
| random_remove1 | 3 | 0.7428 | 0.0146 | 0.0624 | -0.2061 |
| random_remove2 | 3 | 0.7234 | 0.0340 | 0.0965 | -0.3856 |
| random_remove4 | 3 | 0.6842 | 0.0732 | 0.1785 | -0.9135 |
| random_remove8 | 3 | 0.5850 | 0.1724 | 0.3125 | -2.4033 |
| random_remove16 | 3 | 0.3828 | 0.3746 | 0.5643 | -6.8758 |

## Interpretation hooks
| finding | acc | acc_drop | flip_rate | meaning |
| --- | --- | --- | --- | --- |
| remove_particle0 | 0.5633 | 0.1941 | 0.3160 | Large drop => particle0/leading-core is causally important. |
| keep_only_particle0 | 0.2027 | 0.5547 | 0.7941 | High acc => shortcut/proxy risk. |
| remove_top1 | 0.5633 | 0.1941 | 0.3160 | Targeted top1 removal vs random_remove1 tests if leading particle matters beyond random deletion. |
| keep_top16 | 0.5391 | 0.2184 | 0.4051 | High acc means top-16 particles carry much of class evidence. |

## Decision logic

- `remove_particle0` >> `random_remove1` drop: leading particle is specifically causal.
- `keep_only_particle0` high accuracy: shortcut/proxy risk is high.
- `remove_topK` curve stronger than random baselines: core/top-k dependence is real.
- Class-wise table tells which classes depend on core/top-k most.
