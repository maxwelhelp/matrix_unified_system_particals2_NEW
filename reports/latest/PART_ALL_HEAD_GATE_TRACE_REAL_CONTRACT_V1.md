# PART_ALL_HEAD_GATE_TRACE_REAL_CONTRACT_V1

ParT real-contract all-head differentiable gate trace. This ports the ParticleNet all-head gate idea onto the current `ParT_kinpid` run.

- events: **256**
- groups: `{'A_Hqql_correct': 64, 'B_Hqql_to_Tbl': 64, 'C_Tbl_correct': 64, 'D_Tbl_to_Hqql': 64}`
- checkpoint: `external/particle_transformer/models/ParT_kinpid.pt`
- data_config: `external/particle_transformer/data/JetClass/JetClass_kinpid.yaml`
- gate rows: **80**
- joined pseudocode rules: **48**

## Important status

This is a real differentiable all-head trace, but v1 gates attention module output head/channel slices. It is stronger than static route scoring, but the next version should patch exact pre-output-projection attention head routes.

## Top positive gates
| module | head | channels | grad | abs |
| --- | --- | --- | --- | --- |
| mod.cls_blocks.0.attn | 7 | 112:128 | 6.90978e-01 | 6.90978e-01 |
| mod.cls_blocks.0.attn | 4 | 64:80 | 5.45896e-01 | 5.45896e-01 |
| mod.cls_blocks.1.attn | 6 | 96:112 | 2.67908e-01 | 2.67908e-01 |
| mod.cls_blocks.0.attn | 1 | 16:32 | 1.38373e-01 | 1.38373e-01 |
| mod.cls_blocks.0.attn | 6 | 96:112 | 1.32386e-01 | 1.32386e-01 |
| mod.cls_blocks.0.attn | 2 | 32:48 | 7.71346e-02 | 7.71346e-02 |
| mod.cls_blocks.0.attn | 5 | 80:96 | 7.65452e-02 | 7.65452e-02 |
| mod.cls_blocks.1.attn | 4 | 64:80 | 5.51616e-02 | 5.51616e-02 |
| mod.blocks.7.attn | 4 | 64:80 | 5.02711e-02 | 5.02711e-02 |
| mod.blocks.5.attn | 6 | 96:112 | 4.74334e-02 | 4.74334e-02 |
| mod.blocks.7.attn | 7 | 112:128 | 4.28187e-02 | 4.28187e-02 |
| mod.blocks.6.attn | 4 | 64:80 | 3.75215e-02 | 3.75215e-02 |
| mod.blocks.2.attn | 6 | 96:112 | 3.63143e-02 | 3.63143e-02 |
| mod.cls_blocks.1.attn | 5 | 80:96 | 3.57685e-02 | 3.57685e-02 |
| mod.blocks.6.attn | 0 | 0:16 | 3.43923e-02 | 3.43923e-02 |
| mod.blocks.5.attn | 4 | 64:80 | 3.36596e-02 | 3.36596e-02 |
| mod.blocks.5.attn | 0 | 0:16 | 3.17738e-02 | 3.17738e-02 |
| mod.blocks.4.attn | 6 | 96:112 | 2.99267e-02 | 2.99267e-02 |
| mod.blocks.1.attn | 0 | 0:16 | 2.94790e-02 | 2.94790e-02 |
| mod.blocks.4.attn | 4 | 64:80 | 2.92817e-02 | 2.92817e-02 |

## Top negative gates
| module | head | channels | grad | abs |
| --- | --- | --- | --- | --- |
| mod.cls_blocks.0.attn | 3 | 48:64 | -1.62059e+00 | 1.62059e+00 |
| mod.cls_blocks.1.attn | 3 | 48:64 | -3.15787e-01 | 3.15787e-01 |
| mod.cls_blocks.1.attn | 2 | 32:48 | -6.45742e-02 | 6.45742e-02 |
| mod.blocks.4.attn | 7 | 112:128 | -4.74474e-02 | 4.74474e-02 |
| mod.blocks.5.attn | 1 | 16:32 | -4.24067e-02 | 4.24067e-02 |
| mod.blocks.3.attn | 1 | 16:32 | -4.08628e-02 | 4.08628e-02 |
| mod.cls_blocks.0.attn | 0 | 0:16 | -4.07242e-02 | 4.07242e-02 |
| mod.blocks.0.attn | 1 | 16:32 | -3.86329e-02 | 3.86329e-02 |
| mod.blocks.1.attn | 1 | 16:32 | -3.63581e-02 | 3.63581e-02 |
| mod.blocks.6.attn | 1 | 16:32 | -3.56888e-02 | 3.56888e-02 |
| mod.blocks.7.attn | 3 | 48:64 | -2.85647e-02 | 2.85647e-02 |
| mod.blocks.5.attn | 2 | 32:48 | -2.79028e-02 | 2.79028e-02 |
| mod.blocks.5.attn | 7 | 112:128 | -2.68885e-02 | 2.68885e-02 |
| mod.blocks.2.attn | 1 | 16:32 | -2.65708e-02 | 2.65708e-02 |
| mod.blocks.2.attn | 2 | 32:48 | -2.54062e-02 | 2.54062e-02 |
| mod.blocks.5.attn | 5 | 80:96 | -2.33427e-02 | 2.33427e-02 |
| mod.blocks.7.attn | 1 | 16:32 | -2.26236e-02 | 2.26236e-02 |
| mod.blocks.1.attn | 7 | 112:128 | -2.16983e-02 | 2.16983e-02 |
| mod.blocks.0.attn | 5 | 80:96 | -2.14141e-02 | 2.14141e-02 |
| mod.blocks.4.attn | 2 | 32:48 | -2.08225e-02 | 2.08225e-02 |

## Top pseudocode rules with differentiable gate support
| rule | module | head | route | type | rule_strength | gate_grad |
| --- | --- | --- | --- | --- | --- | --- |
| R001_B_to_Tbl | mod.blocks.7.attn | 4 | muon<-muon | LEPTON_LEPTON_ROUTE | 0.99983 | 5.02711e-02 |
| R003_B_to_Tbl | mod.blocks.7.attn | 4 | muon<-electron | LEPTON_LEPTON_ROUTE | 0.99689 | 5.02711e-02 |
| R001_anomaly | mod.blocks.7.attn | 4 | muon<-muon | LEPTON_LEPTON_ROUTE | 0.99966 | 5.02711e-02 |
| R002_anomaly | mod.blocks.7.attn | 4 | muon<-electron | LEPTON_LEPTON_ROUTE | 0.99379 | 5.02711e-02 |
| R016_B_to_Tbl | mod.blocks.5.attn | 6 | muon<-neutral_hadron | LEPTON_READS_HADRON_ROUTE | 0.92837 | 4.74334e-02 |
| R007_B_to_Tbl | mod.blocks.6.attn | 4 | electron<-electron | LEPTON_LEPTON_ROUTE | 0.98895 | 3.75215e-02 |
| R011_B_to_Tbl | mod.blocks.6.attn | 4 | muon<-muon | LEPTON_LEPTON_ROUTE | 0.97966 | 3.75215e-02 |
| R007_A_protect | mod.blocks.6.attn | 4 | neutral_hadron<-charged_hadron | HADRON_HADRON_TOPOLOGY_ROUTE | 0.97475 | 3.75215e-02 |
| R008_A_protect | mod.blocks.6.attn | 4 | photon<-neutral_hadron | PHOTON_HADRON_ROUTE | 0.95746 | 3.75215e-02 |
| R010_A_protect | mod.blocks.6.attn | 4 | photon<-charged_hadron | PHOTON_HADRON_ROUTE | 0.94236 | 3.75215e-02 |
| R014_A_protect | mod.blocks.6.attn | 4 | charged_hadron<-neutral_hadron | HADRON_HADRON_TOPOLOGY_ROUTE | 0.90792 | 3.75215e-02 |
| R002_B_to_Tbl | mod.blocks.6.attn | 0 | electron<-electron | LEPTON_LEPTON_ROUTE | 0.99959 | 3.43923e-02 |
| R009_B_to_Tbl | mod.blocks.6.attn | 0 | photon<-neutral_hadron | PHOTON_HADRON_ROUTE | 0.98736 | 3.43923e-02 |
| R010_B_to_Tbl | mod.blocks.6.attn | 0 | muon<-electron | LEPTON_LEPTON_ROUTE | 0.9866 | 3.43923e-02 |
| R014_B_to_Tbl | mod.blocks.6.attn | 0 | electron<-muon | LEPTON_LEPTON_ROUTE | 0.94817 | 3.43923e-02 |
| R001_A_protect | mod.blocks.7.attn | 3 | electron<-muon | LEPTON_LEPTON_ROUTE | 0.99912 | -2.85647e-02 |
| R004_anomaly | mod.blocks.7.attn | 3 | electron<-muon | LEPTON_LEPTON_ROUTE | 0.9273 | -2.85647e-02 |
| R008_anomaly | mod.blocks.4.attn | 0 | muon<-electron | LEPTON_LEPTON_ROUTE | 0.84365 | 2.81589e-02 |
| R004_B_to_Tbl | mod.blocks.5.attn | 2 | electron<-neutral_hadron | LEPTON_READS_HADRON_ROUTE | 0.99519 | -2.79028e-02 |
| R008_B_to_Tbl | mod.blocks.5.attn | 7 | muon<-muon | LEPTON_LEPTON_ROUTE | 0.98828 | -2.68885e-02 |
| R015_A_protect | mod.blocks.5.attn | 7 | photon<-neutral_hadron | PHOTON_HADRON_ROUTE | 0.89928 | -2.68885e-02 |
| R018_A_protect | mod.blocks.2.attn | 1 | muon<-photon | LEPTON_PHOTON_ROUTE | 0.85991 | -2.65708e-02 |
| R009_anomaly | mod.blocks.2.attn | 1 | muon<-photon | LEPTON_PHOTON_ROUTE | 0.8424 | -2.65708e-02 |
| R009_A_protect | mod.blocks.5.attn | 5 | electron<-electron | LEPTON_LEPTON_ROUTE | 0.95416 | -2.33427e-02 |
| R006_B_to_Tbl | mod.blocks.7.attn | 6 | muon<-muon | LEPTON_LEPTON_ROUTE | 0.99142 | -2.06408e-02 |
| R003_anomaly | mod.blocks.7.attn | 6 | muon<-muon | LEPTON_LEPTON_ROUTE | 0.98291 | -2.06408e-02 |
| R003_A_protect | mod.blocks.6.attn | 5 | electron<-electron | LEPTON_LEPTON_ROUTE | 0.98862 | -1.78863e-02 |
| R002_A_protect | mod.blocks.2.attn | 3 | muon<-muon | LEPTON_LEPTON_ROUTE | 0.99357 | 1.63883e-02 |
| R011_A_protect | mod.blocks.3.attn | 2 | electron<-neutral_hadron | LEPTON_READS_HADRON_ROUTE | 0.94233 | -1.27831e-02 |
| R016_A_protect | mod.blocks.3.attn | 2 | neutral_hadron<-muon | HADRON_READS_LEPTON_ROUTE | 0.89318 | -1.27831e-02 |

## Next

Run exact route patch for the top joined rules: R001_B_to_Tbl, R002_B_to_Tbl, R003_B_to_Tbl, and the top A_protect rules.
