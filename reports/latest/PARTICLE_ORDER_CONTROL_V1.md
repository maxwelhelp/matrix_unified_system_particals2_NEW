# Particle Order Control v1

Tests whether the model depends on particle array index/order, or whether particle0 effect is tied to physical leading/core content.

n_events=2560 baseline_acc=0.7574 verdict=ORDER_INVARIANT_OR_NEAR_INVARIANT

## Summary
| control | acc | flip | mean_abs_logit_diff | max_abs_logit_diff | delta_base_pred_logit |
| --- | --- | --- | --- | --- | --- |
| identity | 0.7574 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| reverse | 0.7574 | 0.0000 | 1.230e-04 | 1.6824 | 4.572e-05 |
| particle0_to_end | 0.7574 | 0.0000 | 2.190e-07 | 7.629e-06 | 0.0000 |
| particle0_to_middle | 0.7574 | 0.0000 | 1.973e-07 | 7.629e-06 | 0.0000 |
| sort_pt_desc | 0.7574 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| sort_pt_asc | 0.7574 | 0.0000 | 1.232e-04 | 1.6824 | 4.572e-05 |
| random_shuffle_r0 | 0.7574 | 0.0000 | 8.973e-07 | 0.0054 | 2.980e-07 |
| random_shuffle_r1 | 0.7574 | 0.0000 | 2.271e-07 | 7.629e-06 | 0.0000 |
| random_shuffle_r2 | 0.7574 | 0.0000 | 2.235e-07 | 7.629e-06 | 0.0000 |

## Interpretation

- If random/reverse/particle0_to_end barely change logits/predictions, ParticleNet is effectively permutation invariant here. Then particle0/top-k causality is about the physical leading/core particle, not literal index position.
- If order shuffles change predictions, order/sorting is a serious artifact and must be fixed before physics claims.
- `sort_pt_asc` is intentionally extreme: if it changes outputs, inspect whether padding/trim/implementation creates order sensitivity.
