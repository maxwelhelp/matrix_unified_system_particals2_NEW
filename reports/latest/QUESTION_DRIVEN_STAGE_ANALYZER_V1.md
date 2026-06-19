# Question Driven Stage Analyzer v1

Automatic answers over staged evidence: pseudocode v2, code alignment, head outputs, controls, confusion, residual, and scope guard.

## Answers
| id | question | answer | evidence | next |
| --- | --- | --- | --- | --- |
| Q1 | Where is the late particle0/core readout? | The strongest core readout is in L2 pseudo-heads. L2 rows have the highest leading-pT/particle0 match and are mapped to edge_convs.2 outputs before pooling/classifier. | pseudocode_v2 + code_alignment_v2 + head_output_trace + particle0_controls | run route-neighbor trace on top L2 heads and heldout stability |
| Q2 | What do L0/L1 compute before the L2 readout? | L0/L1 mostly act as local feature builders and context relays. Their outputs often activate on non-leading particles, so they likely build edge/PID/radial/neighborhood context that L2 later reads through core-aligned heads. | pseudocode_v2 + head_output_trace + class_gradients | trace EdgeConv inner tensors: knn indices, graph features, conv outputs, neighbor aggregation |
| Q3 | Is Hqql/Tbl residual axis explained by simple known observables? | No for v1 surrogate: residual remains. Simple observable surrogate has low agreement with ParticleNet, so Hqql/Tbl and related structured classes need deeper head/circuit analysis. | known_observable_residual_v1 + confusion_atlas + pseudocode_v2 | run richer residual v2 with pair/ECF-like features and class-specific head trace |
| Q4 | Which heads should be inspected next inside EdgeConv? | Prioritize heads with high class gradients, strong output/logit links, and clear code alignment. These heads should get inner trace: KNN neighbor source, edge feature, conv stack, aggregation, channel slice. | pseudocode_v2 + code_alignment_v2 + head_output_trace + class_gradients | run EDGE_CONV_INNER_TRACE_V1 for ranked heads |
| Q5 | What is the current evidence chain for the core/top-k mechanism? | Stream suggested particle0/core dominance; targeted controls confirmed local causality; order control reduced index artifact; confusion atlas showed structured class collapse; residual v1 says simple observables do not reproduce decisions; pseudocode/output trace shows L0/L1 context builders feeding L2 core readouts. | stream + controls + order + confusion + residual + pseudocode_v2 + scope_guard | do heldout/per-file and cross-model agreement before strong claim |

## Ranked heads by question

### Q1_core_readout
| rank | head | score | role | top_class | lead | corr | code |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | L2_ch224:256 | 3.3592 | late readout strongly anchored on particle0/leading-pT core | label_Tbl | 0.7180 | label_Hgg:-0.6442 | edge_convs.2 output[:, 224:256, :] |
| 2 | L2_ch128:160 | 2.7533 | late readout moderately core-aligned | label_Tbl | 0.3852 | label_Tbl:0.6627 | edge_convs.2 output[:, 128:160, :] |
| 3 | L2_ch0:32 | 2.1304 | late readout moderately core-aligned | label_Hqql | 0.4227 | label_Hbb:-0.3352 | edge_convs.2 output[:, 0:32, :] |
| 4 | L2_ch32:64 | 1.9213 | late readout moderately core-aligned | label_Tbl | 0.3812 | label_QCD:-0.5493 | edge_convs.2 output[:, 32:64, :] |
| 5 | L2_ch64:96 | 1.7248 | late readout with distributed/non-core particle evidence | label_Tbl | 0.2336 | label_QCD:-0.5693 | edge_convs.2 output[:, 64:96, :] |
| 6 | L2_ch160:192 | 1.5614 | late readout with distributed/non-core particle evidence | label_Tbl | 0.2477 | label_Tbl:0.5801 | edge_convs.2 output[:, 160:192, :] |
| 7 | L1_ch0:16 | 1.5609 | middle relay mixing context with some core alignment | label_Tbl | 0.3016 | label_H4q:-0.3682 | edge_convs.1 output[:, 0:16, :] |
| 8 | L2_ch192:224 | 1.3987 | late readout moderately core-aligned | label_Tbqq | 0.3055 | label_QCD:-0.3177 | edge_convs.2 output[:, 192:224, :] |
| 9 | L1_ch112:128 | 1.3849 | middle context relay mostly away from literal leading particle | label_Tbl | 0.1727 | label_Wqq:-0.2462 | edge_convs.1 output[:, 112:128, :] |
| 10 | L0_ch40:48 | 1.2072 | early local/context feature builder over non-leading neighbor particles | label_Tbqq | 0.1648 | label_Tbqq:0.1292 | edge_convs.0 output[:, 40:48, :] |

### Q2_local_builders
| rank | head | score | role | top_class | lead | corr | code |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | L1_ch16:32 | 2.5396 | middle context relay mostly away from literal leading particle | label_QCD | 0.0383 | label_QCD:0.1070 | edge_convs.1 output[:, 16:32, :] |
| 2 | L1_ch112:128 | 2.3170 | middle context relay mostly away from literal leading particle | label_Tbl | 0.1727 | label_Wqq:-0.2462 | edge_convs.1 output[:, 112:128, :] |
| 3 | L0_ch40:48 | 2.1342 | early local/context feature builder over non-leading neighbor particles | label_Tbqq | 0.1648 | label_Tbqq:0.1292 | edge_convs.0 output[:, 40:48, :] |
| 4 | L1_ch32:48 | 1.8448 | middle context relay mostly away from literal leading particle | label_Tbqq | 0.0656 | label_Hqql:-0.2501 | edge_convs.1 output[:, 32:48, :] |
| 5 | L0_ch48:56 | 1.8204 | early local/context feature builder over non-leading neighbor particles | label_Tbqq | 0.0461 | label_Tbqq:0.1998 | edge_convs.0 output[:, 48:56, :] |
| 6 | L0_ch0:8 | 1.7796 | early local/context feature builder over non-leading neighbor particles | label_Tbqq | 0.0031 | label_Hqql:-0.2814 | edge_convs.0 output[:, 0:8, :] |
| 7 | L0_ch8:16 | 1.7364 | early local/context feature builder over non-leading neighbor particles | label_Tbqq | 0.0078 | label_Tbqq:0.2794 | edge_convs.0 output[:, 8:16, :] |
| 8 | L0_ch16:24 | 1.5455 | early local/context feature builder over non-leading neighbor particles | label_Tbqq | 0.0195 | label_Tbqq:0.2299 | edge_convs.0 output[:, 16:24, :] |
| 9 | L0_ch24:32 | 1.5428 | early local/context feature builder over non-leading neighbor particles | label_QCD | 0.0797 | label_H4q:-0.1225 | edge_convs.0 output[:, 24:32, :] |
| 10 | L1_ch64:80 | 1.4505 | middle context relay mostly away from literal leading particle | label_Tbqq | 0.0000 | label_Tbqq:0.2741 | edge_convs.1 output[:, 64:80, :] |

### Q3_residual_axis
| rank | head | score | role | top_class | lead | corr | code |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | L2_ch128:160 | 4.5328 | late readout moderately core-aligned | label_Tbl | 0.3852 | label_Tbl:0.6627 | edge_convs.2 output[:, 128:160, :] |
| 2 | L2_ch224:256 | 3.7663 | late readout strongly anchored on particle0/leading-pT core | label_Tbl | 0.7180 | label_Hgg:-0.6442 | edge_convs.2 output[:, 224:256, :] |
| 3 | L1_ch32:48 | 3.6495 | middle context relay mostly away from literal leading particle | label_Tbqq | 0.0656 | label_Hqql:-0.2501 | edge_convs.1 output[:, 32:48, :] |
| 4 | L1_ch112:128 | 3.4876 | middle context relay mostly away from literal leading particle | label_Tbl | 0.1727 | label_Wqq:-0.2462 | edge_convs.1 output[:, 112:128, :] |
| 5 | L2_ch64:96 | 3.4788 | late readout with distributed/non-core particle evidence | label_Tbl | 0.2336 | label_QCD:-0.5693 | edge_convs.2 output[:, 64:96, :] |
| 6 | L0_ch0:8 | 3.4385 | early local/context feature builder over non-leading neighbor particles | label_Tbqq | 0.0031 | label_Hqql:-0.2814 | edge_convs.0 output[:, 0:8, :] |
| 7 | L2_ch0:32 | 3.3897 | late readout moderately core-aligned | label_Hqql | 0.4227 | label_Hbb:-0.3352 | edge_convs.2 output[:, 0:32, :] |
| 8 | L0_ch16:24 | 3.1807 | early local/context feature builder over non-leading neighbor particles | label_Tbqq | 0.0195 | label_Tbqq:0.2299 | edge_convs.0 output[:, 16:24, :] |
| 9 | L0_ch48:56 | 3.1791 | early local/context feature builder over non-leading neighbor particles | label_Tbqq | 0.0461 | label_Tbqq:0.1998 | edge_convs.0 output[:, 48:56, :] |
| 10 | L2_ch160:192 | 3.0569 | late readout with distributed/non-core particle evidence | label_Tbl | 0.2477 | label_Tbl:0.5801 | edge_convs.2 output[:, 160:192, :] |

### Q4_trace_priority
| rank | head | score | role | top_class | lead | corr | code |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | L2_ch128:160 | 3.8749 | late readout moderately core-aligned | label_Tbl | 0.3852 | label_Tbl:0.6627 | edge_convs.2 output[:, 128:160, :] |
| 2 | L1_ch16:32 | 3.5147 | middle context relay mostly away from literal leading particle | label_QCD | 0.0383 | label_QCD:0.1070 | edge_convs.1 output[:, 16:32, :] |
| 3 | L2_ch224:256 | 3.4747 | late readout strongly anchored on particle0/leading-pT core | label_Tbl | 0.7180 | label_Hgg:-0.6442 | edge_convs.2 output[:, 224:256, :] |
| 4 | L1_ch112:128 | 3.3565 | middle context relay mostly away from literal leading particle | label_Tbl | 0.1727 | label_Wqq:-0.2462 | edge_convs.1 output[:, 112:128, :] |
| 5 | L0_ch40:48 | 3.0117 | early local/context feature builder over non-leading neighbor particles | label_Tbqq | 0.1648 | label_Tbqq:0.1292 | edge_convs.0 output[:, 40:48, :] |
| 6 | L1_ch32:48 | 2.8602 | middle context relay mostly away from literal leading particle | label_Tbqq | 0.0656 | label_Hqql:-0.2501 | edge_convs.1 output[:, 32:48, :] |
| 7 | L2_ch0:32 | 2.6507 | late readout moderately core-aligned | label_Hqql | 0.4227 | label_Hbb:-0.3352 | edge_convs.2 output[:, 0:32, :] |
| 8 | L0_ch0:8 | 2.6427 | early local/context feature builder over non-leading neighbor particles | label_Tbqq | 0.0031 | label_Hqql:-0.2814 | edge_convs.0 output[:, 0:8, :] |
| 9 | L2_ch64:96 | 1.7844 | late readout with distributed/non-core particle evidence | label_Tbl | 0.2336 | label_QCD:-0.5693 | edge_convs.2 output[:, 64:96, :] |
| 10 | L0_ch48:56 | 1.5560 | early local/context feature builder over non-leading neighbor particles | label_Tbqq | 0.0461 | label_Tbqq:0.1998 | edge_convs.0 output[:, 48:56, :] |

## Use

This report should be the first file to open when deciding what to inspect next. It turns staged evidence into question-specific head rankings and next experiments.
