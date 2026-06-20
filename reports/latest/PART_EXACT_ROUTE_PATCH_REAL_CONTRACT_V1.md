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
| R010_A_protect | mod.blocks.6.attn | 4 | photon<-charged_hadron | PHOTON_HADRON_ROUTE | 0.037521462407312356 | 8.93657e-03 | 0.00000e+00 | 3.14278e-02 |
| R016_B_to_Tbl | mod.blocks.5.attn | 6 | muon<-neutral_hadron | LEPTON_READS_HADRON_ROUTE | 0.047433355925022624 | -6.10513e-03 | 0.00000e+00 | -1.75923e-04 |
| R007_B_to_Tbl | mod.blocks.6.attn | 4 | electron<-electron | LEPTON_LEPTON_ROUTE | 0.037521462407312356 | 2.64497e-03 | 0.00000e+00 | -1.59532e-04 |
| R007_A_protect | mod.blocks.6.attn | 4 | neutral_hadron<-charged_hadron | HADRON_HADRON_TOPOLOGY_ROUTE | 0.037521462407312356 | 2.58088e-03 | 0.00000e+00 | 2.87877e-03 |
| R003_B_to_Tbl | mod.blocks.7.attn | 4 | muon<-electron | LEPTON_LEPTON_ROUTE | 0.05027113783580717 | -1.35691e-03 | 0.00000e+00 | 3.25441e-05 |
| R008_A_protect | mod.blocks.6.attn | 4 | photon<-neutral_hadron | PHOTON_HADRON_ROUTE | 0.037521462407312356 | 9.72331e-04 | 0.00000e+00 | 4.70392e-03 |
| R001_B_to_Tbl | mod.blocks.7.attn | 4 | muon<-muon | LEPTON_LEPTON_ROUTE | 0.05027113783580717 | 2.91795e-04 | 0.00000e+00 | 1.49012e-07 |
| R011_B_to_Tbl | mod.blocks.6.attn | 4 | muon<-muon | LEPTON_LEPTON_ROUTE | 0.037521462407312356 | -1.74880e-04 | 0.00000e+00 | -4.23789e-05 |

## Validity notes

This is stronger than route visibility and gate gradient: it changes the actual attention mask for the chosen route and measures model-output change. It is still a v1 exact-route patch; if an attention mask shape is incompatible, that micro-call skips corruption rather than forcing an invalid mask.
