# PART_BUNDLE_CAUSAL_PATCH_REAL_CONTRACT_V1

Bundle/head causal patch over direct-replay ParT Hqql/Tbl groups. This tests algorithmic nodes, not only one attention route.

- events: **256**
- events_per_group: **64**
- bundles tested: **11**
- patch_strength: **40.0**
- groups_csv: `reports/latest/tables/part_hqql_tbl_groups_direct_replay_v1.csv`
- rules_csv: `reports/latest/tables/part_rule_gate_join_real_contract_v1.csv`

## Top bundle effects
| bundle | kind | n_rules | B_delta_margin | B_delta_tbl_pred | A_delta_margin | C_delta_margin | D_delta_margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| head_output_zero_mod.blocks.7.attn_h3 | head_output_zero | 2 | -4.72368e-02 | -3.12500e-02 | -4.70994e-02 | 4.20955e-03 | -3.30458e-02 |
| head_output_zero_mod.blocks.6.attn_h0 | head_output_zero | 4 | 2.65217e-02 | -1.56250e-02 | 8.65218e-02 | -6.42494e-02 | 7.09670e-02 |
| head_output_zero_mod.blocks.7.attn_h4 | head_output_zero | 4 | -2.48988e-02 | 0.00000e+00 | 1.61146e-01 | -6.77194e-02 | 5.06492e-02 |
| route_bundle_A_top8_gate_weighted | route_bundle | 8 | 1.80716e-02 | -1.56250e-02 | 5.13184e-02 | 9.49343e-03 | 2.60267e-02 |
| route_bundle_blocks6_head4_mixed | route_bundle | 6 | 1.73524e-02 | 0.00000e+00 | 4.90140e-02 | -5.92329e-04 | 2.69363e-02 |
| head_output_zero_mod.blocks.5.attn_h6 | head_output_zero | 1 | -1.54480e-02 | -3.12500e-02 | 6.84312e-02 | -1.32655e-01 | 4.43534e-02 |
| head_output_zero_mod.blocks.6.attn_h4 | head_output_zero | 6 | -8.81726e-03 | -1.56250e-02 | 6.85140e-02 | -1.23276e-01 | 1.64037e-02 |
| route_bundle_blocks6_head0_B | route_bundle | 4 | 3.59496e-03 | 0.00000e+00 | 1.30187e-03 | -3.14528e-03 | -9.55217e-04 |
| route_bundle_B_top8_gate_weighted | route_bundle | 8 | -2.81335e-03 | 0.00000e+00 | 1.92019e-03 | -1.67484e-02 | 1.09408e-03 |
| route_bundle_blocks7_head4_B | route_bundle | 2 | -2.65314e-03 | 0.00000e+00 | 4.89414e-04 | -4.94326e-03 | 1.99892e-03 |
| route_bundle_anomaly_top8_gate_weighted | route_bundle | 8 | 1.19396e-03 | 0.00000e+00 | 6.96912e-03 | -1.57068e-03 | 2.64824e-03 |

## Reading rule

- Negative `B_delta_margin`: patch reduces Tbl-like margin in Hqql→Tbl mistakes; bundle supports confusion.
- Positive `B_delta_margin`: patch increases Tbl-like margin; bundle may be protective/suppressive.
- Nonzero `B_delta_tbl_pred` means the bundle can flip some class decisions, not just margins.
- Compare with `A_delta_margin/C_delta_margin` to see damage to correct regimes.
