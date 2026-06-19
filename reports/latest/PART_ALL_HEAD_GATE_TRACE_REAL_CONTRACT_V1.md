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
| mod.cls_blocks.0.attn | 6 | 96:112 | 1.56014e-01 | 1.56014e-01 |
| mod.cls_blocks.0.attn | 2 | 32:48 | 8.99893e-02 | 8.99893e-02 |
| mod.blocks.0.attn | 4 | 64:80 | 6.41254e-02 | 6.41254e-02 |
| mod.blocks.3.attn | 5 | 80:96 | 3.99713e-02 | 3.99713e-02 |
| mod.blocks.4.attn | 4 | 64:80 | 3.62452e-02 | 3.62452e-02 |
| mod.blocks.5.attn | 4 | 64:80 | 3.28927e-02 | 3.28927e-02 |
| mod.blocks.7.attn | 5 | 80:96 | 3.24707e-02 | 3.24707e-02 |
| mod.blocks.1.attn | 6 | 96:112 | 2.98586e-02 | 2.98586e-02 |
| mod.blocks.4.attn | 6 | 96:112 | 2.74751e-02 | 2.74751e-02 |
| mod.blocks.4.attn | 5 | 80:96 | 2.52030e-02 | 2.52030e-02 |
| mod.blocks.2.attn | 5 | 80:96 | 2.41127e-02 | 2.41127e-02 |
| mod.blocks.3.attn | 4 | 64:80 | 2.19290e-02 | 2.19290e-02 |
| mod.blocks.2.attn | 4 | 64:80 | 1.85251e-02 | 1.85251e-02 |
| mod.blocks.6.attn | 0 | 0:16 | 1.81166e-02 | 1.81166e-02 |
| mod.blocks.6.attn | 6 | 96:112 | 1.78371e-02 | 1.78371e-02 |
| mod.blocks.7.attn | 0 | 0:16 | 1.43761e-02 | 1.43761e-02 |
| mod.blocks.1.attn | 4 | 64:80 | 1.39264e-02 | 1.39264e-02 |
| mod.blocks.0.attn | 6 | 96:112 | 1.36798e-02 | 1.36798e-02 |
| mod.blocks.3.attn | 6 | 96:112 | 1.28666e-02 | 1.28666e-02 |
| mod.blocks.6.attn | 4 | 64:80 | 1.28367e-02 | 1.28367e-02 |

## Top negative gates
| module | head | channels | grad | abs |
| --- | --- | --- | --- | --- |
| mod.cls_blocks.0.attn | 3 | 48:64 | -1.54685e-01 | 1.54685e-01 |
| mod.cls_blocks.0.attn | 0 | 0:16 | -5.29767e-02 | 5.29767e-02 |
| mod.cls_blocks.0.attn | 1 | 16:32 | -4.71361e-02 | 4.71361e-02 |
| mod.blocks.0.attn | 2 | 32:48 | -4.43739e-02 | 4.43739e-02 |
| mod.blocks.2.attn | 1 | 16:32 | -4.06106e-02 | 4.06106e-02 |
| mod.blocks.1.attn | 2 | 32:48 | -3.32289e-02 | 3.32289e-02 |
| mod.blocks.6.attn | 3 | 48:64 | -3.19600e-02 | 3.19600e-02 |
| mod.blocks.3.attn | 2 | 32:48 | -2.97834e-02 | 2.97834e-02 |
| mod.blocks.5.attn | 3 | 48:64 | -2.88464e-02 | 2.88464e-02 |
| mod.blocks.2.attn | 2 | 32:48 | -2.73659e-02 | 2.73659e-02 |
| mod.blocks.0.attn | 1 | 16:32 | -2.70505e-02 | 2.70505e-02 |
| mod.blocks.7.attn | 1 | 16:32 | -2.66224e-02 | 2.66224e-02 |
| mod.blocks.7.attn | 4 | 64:80 | -2.49522e-02 | 2.49522e-02 |
| mod.blocks.4.attn | 0 | 0:16 | -2.45860e-02 | 2.45860e-02 |
| mod.blocks.4.attn | 1 | 16:32 | -2.40504e-02 | 2.40504e-02 |
| mod.blocks.4.attn | 2 | 32:48 | -2.32343e-02 | 2.32343e-02 |
| mod.blocks.4.attn | 7 | 112:128 | -2.29315e-02 | 2.29315e-02 |
| mod.blocks.3.attn | 1 | 16:32 | -2.04502e-02 | 2.04502e-02 |
| mod.blocks.6.attn | 5 | 80:96 | -1.76990e-02 | 1.76990e-02 |
| mod.blocks.3.attn | 3 | 48:64 | -1.70311e-02 | 1.70311e-02 |

## Top pseudocode rules with differentiable gate support
| rule | module | head | route | type | rule_strength | gate_grad |
| --- | --- | --- | --- | --- | --- | --- |
| R013_B_to_Tbl | mod.blocks.3.attn | 5 | neutral_hadron<-muon | HADRON_READS_LEPTON_ROUTE | 0.7758 | 3.99713e-02 |
| R011_anomaly | mod.blocks.3.attn | 5 | neutral_hadron<-muon | HADRON_READS_LEPTON_ROUTE | 0.60186 | 3.99713e-02 |
| R004_B_to_Tbl | mod.blocks.4.attn | 4 | muon<-electron | LEPTON_LEPTON_ROUTE | 0.95476 | 3.62452e-02 |
| R010_B_to_Tbl | mod.blocks.4.attn | 4 | muon<-muon | LEPTON_LEPTON_ROUTE | 0.81415 | 3.62452e-02 |
| R002_anomaly | mod.blocks.4.attn | 4 | muon<-electron | LEPTON_LEPTON_ROUTE | 0.91156 | 3.62452e-02 |
| R006_B_to_Tbl | mod.blocks.5.attn | 4 | muon<-electron | LEPTON_LEPTON_ROUTE | 0.84707 | 3.28927e-02 |
| R007_anomaly | mod.blocks.5.attn | 4 | muon<-electron | LEPTON_LEPTON_ROUTE | 0.71753 | 3.28927e-02 |
| R005_B_to_Tbl | mod.blocks.7.attn | 5 | electron<-electron | LEPTON_LEPTON_ROUTE | 0.91416 | 3.24707e-02 |
| R003_A_protect | mod.blocks.7.attn | 5 | muon<-electron | LEPTON_LEPTON_ROUTE | 0.97671 | 3.24707e-02 |
| R007_A_protect | mod.blocks.7.attn | 5 | electron<-muon | LEPTON_LEPTON_ROUTE | 0.88279 | 3.24707e-02 |
| R012_B_to_Tbl | mod.blocks.3.attn | 2 | charged_hadron<-muon | HADRON_READS_LEPTON_ROUTE | 0.77901 | -2.97834e-02 |
| R002_A_protect | mod.blocks.7.attn | 1 | muon<-muon | LEPTON_LEPTON_ROUTE | 0.97833 | -2.66224e-02 |
| R004_anomaly | mod.blocks.7.attn | 1 | muon<-muon | LEPTON_LEPTON_ROUTE | 0.88499 | -2.66224e-02 |
| R001_B_to_Tbl | mod.blocks.7.attn | 4 | electron<-muon | LEPTON_LEPTON_ROUTE | 0.99492 | -2.49522e-02 |
| R004_A_protect | mod.blocks.7.attn | 4 | electron<-electron | LEPTON_LEPTON_ROUTE | 0.96647 | -2.49522e-02 |
| R001_anomaly | mod.blocks.7.attn | 4 | electron<-electron | LEPTON_LEPTON_ROUTE | 0.96368 | -2.49522e-02 |
| R018_A_protect | mod.blocks.3.attn | 1 | electron<-electron | LEPTON_LEPTON_ROUTE | 0.7618 | -2.04502e-02 |
| R014_A_protect | mod.blocks.2.attn | 4 | muon<-electron | LEPTON_LEPTON_ROUTE | 0.81026 | 1.85251e-02 |
| R009_B_to_Tbl | mod.blocks.6.attn | 0 | electron<-muon | LEPTON_LEPTON_ROUTE | 0.82479 | 1.81166e-02 |
| R008_B_to_Tbl | mod.blocks.6.attn | 6 | neutral_hadron<-neutral_hadron | HADRON_HADRON_TOPOLOGY_ROUTE | 0.8375 | 1.78371e-02 |
| R016_B_to_Tbl | mod.blocks.6.attn | 6 | muon<-neutral_hadron | LEPTON_READS_HADRON_ROUTE | 0.76327 | 1.78371e-02 |
| R010_A_protect | mod.blocks.6.attn | 6 | electron<-neutral_hadron | LEPTON_READS_HADRON_ROUTE | 0.86733 | 1.78371e-02 |
| R008_anomaly | mod.blocks.6.attn | 6 | electron<-neutral_hadron | LEPTON_READS_HADRON_ROUTE | 0.68285 | 1.78371e-02 |
| R010_anomaly | mod.blocks.6.attn | 6 | muon<-muon | LEPTON_LEPTON_ROUTE | 0.63324 | 1.78371e-02 |
| R009_A_protect | mod.blocks.6.attn | 5 | muon<-electron | LEPTON_LEPTON_ROUTE | 0.8719 | -1.76990e-02 |
| R016_A_protect | mod.blocks.1.attn | 4 | muon<-muon | LEPTON_LEPTON_ROUTE | 0.78356 | 1.39264e-02 |
| R012_A_protect | mod.blocks.0.attn | 6 | muon<-charged_hadron | LEPTON_READS_HADRON_ROUTE | 0.84918 | 1.36798e-02 |
| R002_B_to_Tbl | mod.blocks.6.attn | 4 | muon<-photon | LEPTON_PHOTON_ROUTE | 0.97246 | 1.28367e-02 |
| R011_B_to_Tbl | mod.blocks.6.attn | 4 | photon<-charged_hadron | PHOTON_HADRON_ROUTE | 0.79398 | 1.28367e-02 |
| R005_A_protect | mod.blocks.6.attn | 4 | muon<-muon | LEPTON_LEPTON_ROUTE | 0.93515 | 1.28367e-02 |

## Next

Run exact route patch for the top joined rules: R001_B_to_Tbl, R002_B_to_Tbl, R003_B_to_Tbl, and the top A_protect rules.
