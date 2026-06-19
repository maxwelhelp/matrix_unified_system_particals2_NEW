# PART_EXACT_ROUTE_PATCH_REAL_CONTRACT_V1

Exact route patch over real-contract ParT attention. This suppresses one role-route inside one attention head/module and measures Hqql/Tbl margin changes.

- events: **128**
- events_per_group: **32**
- rules tested: **8**
- patch_strength: **40.0**
- checkpoint: `external/particle_transformer/models/ParT_kinpid.pt`
- data_config: `external/particle_transformer/data/JetClass/JetClass_kinpid.yaml`

## Interpretation rule

- Negative `B_delta_tbl_minus_hqql`: patch reduced Tbl-like margin in Hqql→Tbl mistakes, so this route supports confusion.
- Positive `B_delta_tbl_minus_hqql`: patch increased Tbl-like margin, so this route was protective or suppressive.
- Large absolute delta means stronger causal effect candidate.

## Top exact route effects
| rule | module | head | route | type | gate_grad | B_delta_margin | B_delta_tbl_pred | A_delta_margin |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R006_B_to_Tbl | mod.blocks.5.attn | 4 | muon<-electron | LEPTON_LEPTON_ROUTE | 0.03289270959794521 | -4.42023e-03 | 0.00000e+00 | -1.76765e-05 |
| R005_B_to_Tbl | mod.blocks.7.attn | 5 | electron<-electron | LEPTON_LEPTON_ROUTE | 0.032470749341882765 | 1.96942e-03 | 0.00000e+00 | 2.14070e-04 |
| R013_B_to_Tbl | mod.blocks.3.attn | 5 | neutral_hadron<-muon | HADRON_READS_LEPTON_ROUTE | 0.039971290389075875 | 6.86126e-04 | 0.00000e+00 | 4.34667e-05 |
| R004_B_to_Tbl | mod.blocks.4.attn | 4 | muon<-electron | LEPTON_LEPTON_ROUTE | 0.03624523666803725 | -3.09896e-04 | 0.00000e+00 | 1.33406e-03 |
| R007_A_protect | mod.blocks.7.attn | 5 | electron<-muon | LEPTON_LEPTON_ROUTE | 0.032470749341882765 | -2.69748e-05 | 0.00000e+00 | -1.85259e-05 |
| R010_B_to_Tbl | mod.blocks.4.attn | 4 | muon<-muon | LEPTON_LEPTON_ROUTE | 0.03624523666803725 | -1.14292e-05 | 0.00000e+00 | 1.65638e-04 |
| R002_A_protect | mod.blocks.7.attn | 1 | muon<-muon | LEPTON_LEPTON_ROUTE | -0.026622435136232525 | 8.75443e-08 | 0.00000e+00 | -2.71946e-07 |
| R003_A_protect | mod.blocks.7.attn | 5 | muon<-electron | LEPTON_LEPTON_ROUTE | 0.032470749341882765 | 5.58794e-08 | 0.00000e+00 | -2.80887e-06 |

## Validity notes

This is stronger than route visibility and gate gradient: it changes the actual attention mask for the chosen route and measures model-output change. It is still a v1 exact-route patch; if an attention mask shape is incompatible, that micro-call skips corruption rather than forcing an invalid mask.
