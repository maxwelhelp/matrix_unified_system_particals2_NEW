# Research Dashboard Latest

This is the compact dashboard for quick analysis before opening full logs.

## Executive summary
- Validated ParticleNet baseline acc=0.7574 on current balanced subset.
- Strongest current pseudo-head: L1_ch16:32 acc_drop=0.2641; role=middle learned-neighborhood / route-composition head.
- Weight-projection scan found physical-feature, block-interaction, and class-contrast questions.
- Current strongest research direction: triangulate weight projection + route/activation + causal patch for EdgeConv pseudo-heads.

## Top hypotheses
| id | priority | status | score | title | next test |
| --- | --- | --- | --- | --- | --- |
| H2 | P0 | CAUSAL_PATCHED | 78.0000 | EdgeConv pseudo-head specialization | Add activation-cluster pseudo-heads and random channel-group controls. |
| H4 | P0 | CAUSAL_PATCHED | 72.0000 | Leading-particle core hypothesis | Run k sweep k=1,2,4,8,16 and per-class particle ablation. |
| H1 | P0 | CAUSAL_PATCHED | 34.0000 | EdgeConv learned-neighborhood separator | Cluster EdgeConv activations and patch learned clusters; run heldout stability. |
| H5 | P1 | CAUSAL_PATCHED | 74.0000 | Explicit feature-channel class codes | Permutation/noise controls and class contrast reports. |
| H6 | P1 | OBSERVED | 66.0000 | Known-observable alignment | Residual analysis after controlling for sdmass/nparticles/tau variables. |
| H3 | P1 | OBSERVED | 63.0000 | Wqq compact route vs Tbqq wide route | Causal route-group patch: compact vs wide edges; regress against jet mass and nparticles. |
| H7 | P2 | TODO | 35.0000 | Error-route hypothesis | Build error atlas true->pred pairs with route stats and signed competing logits. |
| H8 | P2 | PAUSED | 20.0000 | Transformer attention route hypothesis | Find/train valid ParT checkpoint, then extract attention heads / pair bias. |

## Top heads / pseudo-head questions
| head | acc_drop | role | question | semantic_hint | next |
| --- | --- | --- | --- | --- | --- |
| L1_ch16:32 | 0.2641 | middle learned-neighborhood / route-composition head | Does this pseudo-head combine previous learned features into a class-separating particle-neighborhood answer? | kinematic/energy, class-specific: label_Hbb, label_Hcc, label_Zqq | Test route-width/leading-particle composite: compact/wide/top-pT routes -> L1 ch16:32 -> class contrast. |
| L0_ch24:32 | 0.1996 | early feature/geometry/PID reader | Does this pseudo-head convert raw particle features and local geometry into first-stage message evidence? | kinematic/energy, class-specific: label_Hbb, label_Hcc, label_Hgg | Activation-cluster this head and compare against random channel groups; then project its activation into class contrast directions. |
| L0_ch0:8 | 0.1602 | early feature/geometry/PID reader | Does this pseudo-head convert raw particle features and local geometry into first-stage message evidence? | kinematic/energy, class-specific: label_Tbl, label_Hcc, label_Hbb | Activation-cluster this head and compare against random channel groups; then project its activation into class contrast directions. |
| L0_ch40:48 | 0.1371 | early feature/geometry/PID reader | Does this pseudo-head convert raw particle features and local geometry into first-stage message evidence? | kinematic/energy, class-specific: label_Hqql, label_Zqq, label_Wqq | Activation-cluster this head and compare against random channel groups; then project its activation into class contrast directions. |
| L0_ch48:56 | 0.1359 | early feature/geometry/PID reader | Does this pseudo-head convert raw particle features and local geometry into first-stage message evidence? | kinematic/energy, class-specific: label_H4q, label_Hcc, label_Hbb | Activation-cluster this head and compare against random channel groups; then project its activation into class contrast directions. |
| L0_ch8:16 | 0.1348 | early feature/geometry/PID reader | Does this pseudo-head convert raw particle features and local geometry into first-stage message evidence? | kinematic/energy, class-specific: label_Wqq, label_Hcc, label_Hbb | Activation-cluster this head and compare against random channel groups; then project its activation into class contrast directions. |
| L0_ch16:24 | 0.1277 | early feature/geometry/PID reader | Does this pseudo-head convert raw particle features and local geometry into first-stage message evidence? | kinematic/energy, class-specific: label_Tbqq, label_Hgg, label_Zqq | Activation-cluster this head and compare against random channel groups; then project its activation into class contrast directions. |
| L1_ch112:128 | 0.1156 | middle learned-neighborhood / route-composition head | Does this pseudo-head combine previous learned features into a class-separating particle-neighborhood answer? | kinematic/energy, class-specific: label_Hbb, label_H4q, label_Hgg | Test route-width/leading-particle composite: compact/wide/top-pT routes -> L1 ch112:128 -> class contrast. |
| L0_ch56:64 | 0.0852 | early feature/geometry/PID reader | Does this pseudo-head convert raw particle features and local geometry into first-stage message evidence? | kinematic/energy, class-specific: label_Hqql, label_H4q, label_Hgg | Activation-cluster this head and compare against random channel groups; then project its activation into class contrast directions. |
| L2_ch0:32 | 0.0797 | late aggregation / class-evidence head | Does this pseudo-head aggregate higher-level particle-neighborhood evidence before the classifier? | kinematic/energy, class-specific: label_H4q, label_Hgg, label_Tbl | Activation-cluster this head and compare against random channel groups; then project its activation into class contrast directions. |
| L1_ch96:112 | 0.0734 | middle learned-neighborhood / route-composition head | Does this pseudo-head combine previous learned features into a class-separating particle-neighborhood answer? | kinematic/energy, class-specific: label_H4q, label_Hgg, label_Hqql | Test route-width/leading-particle composite: compact/wide/top-pT routes -> L1 ch96:112 -> class contrast. |
| L2_ch224:256 | 0.0629 | late aggregation / class-evidence head | Does this pseudo-head aggregate higher-level particle-neighborhood evidence before the classifier? | kinematic/energy, class-specific: label_Hbb, label_Wqq, label_Zqq | Activation-cluster this head and compare against random channel groups; then project its activation into class contrast directions. |

## Top weight projection buckets

### physical_feature_projection
| component | score | question | answer |
| --- | --- | --- | --- |
| edge_convs.0.sc | 0.8060 | Does module `edge_convs.0.sc` read physical feature group `pid_charge_5_10`? | Feature group `pid_charge_5_10` carries 0.8060 of module weight energy. |
| edge_convs.0.sc | 0.5489 | Does module `edge_convs.0.sc` read physical feature group `kin_logs_0_4`? | Feature group `kin_logs_0_4` carries 0.5489 of module weight energy. |
| edge_convs.0.convs.0 | 0.4291 | Does module `edge_convs.0.convs.0` read physical feature group `kin_logs_0_4`? | Feature group `kin_logs_0_4` carries 0.4291 of module weight energy. |
| edge_convs.0.convs.0 | 0.4259 | Does module `edge_convs.0.convs.0` read physical feature group `pid_charge_5_10`? | Feature group `pid_charge_5_10` carries 0.4259 of module weight energy. |
| edge_convs.0.sc | 0.4183 | Does module `edge_convs.0.sc` read physical feature group `part_isMuon`? | Feature group `part_isMuon` carries 0.4183 of module weight energy. |
| edge_convs.0.sc | 0.3618 | Does module `edge_convs.0.sc` read physical feature group `part_isElectron`? | Feature group `part_isElectron` carries 0.3618 of module weight energy. |

### block_interaction
| component | score | question | answer |
| --- | --- | --- | --- |
| edge_convs.0.sc | 0.3740 | Does source slice 9:11 feed output pseudo-head 0:8? | Block 9:11->0:8 carries 0.3740 of module weight energy. |
| edge_convs.0.convs.0 | 0.3275 | Does source slice 22:26 feed output pseudo-head 16:24? | Block 22:26->16:24 carries 0.3275 of module weight energy. |
| edge_convs.0.convs.0 | 0.3226 | Does source slice 22:26 feed output pseudo-head 32:40? | Block 22:26->32:40 carries 0.3226 of module weight energy. |
| edge_convs.0.convs.0 | 0.2992 | Does source slice 22:26 feed output pseudo-head 40:48? | Block 22:26->40:48 carries 0.2992 of module weight energy. |

### class_contrast
| component | score | question | answer |
| --- | --- | --- | --- |
| fc.1 | 0.3555 | What hidden directions separate `label_Tbqq` from `label_Tbl`? | Contrast row label_Tbqq-label_Tbl has relative norm 0.3555. |
| fc.1 | 0.3502 | What hidden directions separate `label_H4q` from `label_Hqql`? | Contrast row label_H4q-label_Hqql has relative norm 0.3502. |

### output_pseudo_head
| component | score | question | answer |
| --- | --- | --- | --- |
| fc.1 | 0.5196 | Does output channel group 8:10 behave like a strong internal question/head? | Output group 8:10 carries 0.5196 of module weight energy. |
| edge_convs.0.sc | 0.4766 | Does output channel group 0:8 behave like a strong internal question/head? | Output group 0:8 carries 0.4766 of module weight energy. |
| fc.1 | 0.4405 | Does output channel group 3:5 behave like a strong internal question/head? | Output group 3:5 carries 0.4405 of module weight energy. |
| edge_convs.0.convs.1 | 0.4241 | Does output channel group 8:16 behave like a strong internal question/head? | Output group 8:16 carries 0.4241 of module weight energy. |
| edge_convs.0.convs.0 | 0.4167 | Does output channel group 32:40 behave like a strong internal question/head? | Output group 32:40 carries 0.4167 of module weight energy. |
| edge_convs.0.convs.0 | 0.4144 | Does output channel group 16:24 behave like a strong internal question/head? | Output group 16:24 carries 0.4144 of module weight energy. |

### weight_energy
| component | score | question | answer |
| --- | --- | --- | --- |
| edge_convs.2.convs.0 | 701.4615 | How much raw weight energy is stored in module `edge_convs.2.convs.0`? | Module has ||W||=701.4615 with shape (256, 256, 1, 1). |
| edge_convs.2.convs.1 | 633.9674 | How much raw weight energy is stored in module `edge_convs.2.convs.1`? | Module has ||W||=633.9674 with shape (256, 256, 1, 1). |
| edge_convs.2.sc | 520.6008 | How much raw weight energy is stored in module `edge_convs.2.sc`? | Module has ||W||=520.6008 with shape (256, 128, 1). |
| edge_convs.2.convs.2 | 510.1265 | How much raw weight energy is stored in module `edge_convs.2.convs.2`? | Module has ||W||=510.1265 with shape (256, 256, 1, 1). |
| edge_convs.1.convs.0 | 467.4026 | How much raw weight energy is stored in module `edge_convs.1.convs.0`? | Module has ||W||=467.4026 with shape (128, 128, 1, 1). |
| edge_convs.1.convs.1 | 434.7332 | How much raw weight energy is stored in module `edge_convs.1.convs.1`? | Module has ||W||=434.7332 with shape (128, 128, 1, 1). |

## Route / particle findings
| layer | compact | wide | gap |
| --- | --- | --- | --- |
| 0 | label_Wqq 0.1317 | label_Tbqq 0.2550 | 0.1232 |
| 1 | label_Wqq 0.1572 | label_Tbqq 0.2793 | 0.1220 |
| 2 | label_Wqq 0.1599 | label_Tbqq 0.2873 | 0.1274 |

## Next actions
- Run activation-cluster pseudo-head lens and compare against random channel groups.
- Run route-group causal patch: compact/wide/top-pT/random neighbor routes.
- Run top-k particle sweep k=1,2,4,8,16 with per-class effects.
- Project pseudo-head activations into class contrast directions Wqq-vs-Zqq, Tbqq-vs-Tbl, Hbb-vs-Hcc/Hgg.
- Build error-route atlas for wrong predictions true->pred.
- Find/train valid ParT checkpoint before attention-head claims.

## JSON

Main machine-readable file: `manifests/latest/research_dashboard_latest.json`.
