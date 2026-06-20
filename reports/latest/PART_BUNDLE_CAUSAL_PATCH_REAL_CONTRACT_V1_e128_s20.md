# PART_BUNDLE_CAUSAL_PATCH_REAL_CONTRACT_V1

Bundle/head causal patch over direct-replay ParT Hqql/Tbl groups. This tests algorithmic nodes, not only one attention route.

- events: **512**
- events_per_group: **128**
- bundles tested: **11**
- patch_strength: **20.0**
- groups_csv: `reports/latest/tables/part_hqql_tbl_groups_direct_replay_v1.csv`
- rules_csv: `reports/latest/tables/part_rule_gate_join_real_contract_v1.csv`

## Top bundle effects
| bundle | kind | n_rules | B_delta_margin | B_delta_tbl_pred | A_delta_margin | C_delta_margin | D_delta_margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| head_output_zero_mod.blocks.7.attn_h3 | head_output_zero | 2 | -4.41701e-02 | -2.34375e-02 | -5.00894e-02 | 1.95036e-03 | -3.58504e-02 |
| head_output_zero_mod.blocks.7.attn_h4 | head_output_zero | 4 | -2.66249e-02 | 0.00000e+00 | 1.62924e-01 | -6.94022e-02 | 5.22310e-02 |
| route_bundle_A_top8_gate_weighted | route_bundle | 8 | 2.11273e-02 | -7.81250e-03 | 4.42630e-02 | 7.10722e-03 | 2.61307e-02 |
| route_bundle_blocks6_head4_mixed | route_bundle | 6 | 2.05379e-02 | 0.00000e+00 | 4.48582e-02 | -2.77080e-03 | 2.76228e-02 |
| head_output_zero_mod.blocks.6.attn_h0 | head_output_zero | 4 | 1.66404e-02 | -7.81250e-03 | 7.79758e-02 | -5.48406e-02 | 6.48841e-02 |
| head_output_zero_mod.blocks.6.attn_h4 | head_output_zero | 6 | -1.18348e-02 | -7.81250e-03 | 6.12896e-02 | -1.15365e-01 | 2.17211e-02 |
| head_output_zero_mod.blocks.5.attn_h6 | head_output_zero | 1 | -1.01072e-02 | -1.56250e-02 | 6.17652e-02 | -1.35305e-01 | 2.55534e-02 |
| route_bundle_B_top8_gate_weighted | route_bundle | 8 | 9.31228e-03 | 0.00000e+00 | 2.36383e-03 | -1.51969e-02 | -9.30279e-05 |
| route_bundle_anomaly_top8_gate_weighted | route_bundle | 8 | 2.95723e-03 | 0.00000e+00 | 3.86260e-03 | -4.24515e-03 | 4.15509e-03 |
| route_bundle_blocks7_head4_B | route_bundle | 2 | 1.21856e-03 | 0.00000e+00 | 4.18406e-04 | -7.12710e-03 | 1.25989e-03 |
| route_bundle_blocks6_head0_B | route_bundle | 4 | 1.01702e-03 | 0.00000e+00 | 8.05527e-04 | -2.78051e-03 | -2.31547e-03 |

## Reading rule

- Negative `B_delta_margin`: patch reduces Tbl-like margin in Hqql→Tbl mistakes; bundle supports confusion.
- Positive `B_delta_margin`: patch increases Tbl-like margin; bundle may be protective/suppressive.
- Nonzero `B_delta_tbl_pred` means the bundle can flip some class decisions, not just margins.
- Compare with `A_delta_margin/C_delta_margin` to see damage to correct regimes.
