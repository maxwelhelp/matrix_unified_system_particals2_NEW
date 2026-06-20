# PART_BUNDLE_CAUSAL_SWEEP_V1

Stability sweep for bundle/head causal patches over direct-replay Hqql/Tbl groups.

| bundle | kind | runs | helpful_runs | flip_runs | mean_B_delta_margin | mean_B_delta_tbl_pred | mean_A_delta_margin | mean_C_delta_margin |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| head_output_zero_mod.blocks.7.attn_h3 | head_output_zero | 6 | 6 | 6 | -4.570347e-02 | -2.734375e-02 | -4.859441e-02 | 3.079955e-03 |
| head_output_zero_mod.blocks.5.attn_h6 | head_output_zero | 6 | 6 | 6 | -1.277761e-02 | -2.343750e-02 | 6.509820e-02 | -1.339797e-01 |
| head_output_zero_mod.blocks.6.attn_h4 | head_output_zero | 6 | 6 | 6 | -1.032604e-02 | -1.171875e-02 | 6.490181e-02 | -1.193208e-01 |
| route_bundle_A_top8_gate_weighted | route_bundle | 6 | 0 | 6 | 1.959944e-02 | -1.171875e-02 | 4.779070e-02 | 8.300314e-03 |
| head_output_zero_mod.blocks.6.attn_h0 | head_output_zero | 6 | 0 | 6 | 2.158107e-02 | -1.171875e-02 | 8.224877e-02 | -5.954499e-02 |
| head_output_zero_mod.blocks.7.attn_h4 | head_output_zero | 6 | 6 | 0 | -2.576185e-02 | 0.000000e+00 | 1.620349e-01 | -6.856082e-02 |
| route_bundle_blocks7_head4_B | route_bundle | 6 | 3 | 0 | -7.172860e-04 | 0.000000e+00 | 4.539099e-04 | -6.035418e-03 |
| route_bundle_blocks6_head4_mixed | route_bundle | 6 | 0 | 0 | 1.894517e-02 | 0.000000e+00 | 4.693611e-02 | -1.681553e-03 |
| route_bundle_B_top8_gate_weighted | route_bundle | 6 | 3 | 0 | 3.249450e-03 | 0.000000e+00 | 2.142006e-03 | -1.597280e-02 |
| route_bundle_anomaly_top8_gate_weighted | route_bundle | 6 | 0 | 0 | 2.075598e-03 | 0.000000e+00 | 5.415867e-03 | -2.908145e-03 |
| route_bundle_blocks6_head0_B | route_bundle | 6 | 0 | 0 | 2.305983e-03 | 0.000000e+00 | 1.053698e-03 | -2.962905e-03 |

## Reading

- `helpful_runs`: runs where B Tbl-like margin decreased.
- `flip_runs`: runs where at least some B mistakes flipped away from Tbl.
- Strong candidate = high helpful_runs/flip_runs with moderate A/C damage.
