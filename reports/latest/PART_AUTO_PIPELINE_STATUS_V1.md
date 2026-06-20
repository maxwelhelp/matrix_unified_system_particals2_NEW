# PART_AUTO_PIPELINE_STATUS_V1
Automated Hqql/Tbl program-graph pipeline status.

- status: **OK**
- program_graph_nodes: **133**
- program_graph_edges: **219**
- pair_validation_summary_rows: **24**

## Required artifacts
| stage | exists | size | path |
| --- | ---: | ---: | --- |
| direct_groups | True | 1228 | `reports/latest/PART_DIRECT_REPLAY_GROUP_BUILDER_V1.md` |
| natural_attention | True | 7266 | `reports/latest/PART_NATURAL_ATTENTION_MANUAL_GRAD_REAL_CONTRACT_V1.md` |
| value_write | True | 9224 | `reports/latest/PART_VALUE_WRITE_GRAD_REAL_CONTRACT_V1.md` |
| discovery | True | 24921 | `reports/latest/PART_DISCOVERY_CANDIDATES_REAL_CONTRACT_V1.md` |
| pair_validation | True | 4715 | `reports/latest/PART_CANDIDATE_PAIR_VALIDATION_BALANCED_V1.md` |
| final_mechanisms | True | 7218 | `reports/latest/PART_MECHANISM_DISCOVERY_FINAL_V1.md` |
| residual_v2 | True | 17108 | `reports/latest/PART_RESIDUAL_PATH_TRACE_REAL_CONTRACT_V2.md` |
| classifier | True | 15166 | `reports/latest/PART_CLASSIFIER_LOGIT_DECODER_REAL_CONTRACT_V1.md` |
| program_graph | True | 10506 | `reports/latest/PART_PROGRAM_GRAPH_EXPORT_V1.md` |

## JSON metrics
| stage | ok | events | rows | summary_rows | nodes | edges | candidates | validated |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| natural_attention | True | 128 | 10352 | 4240 |  |  |  |  |
| value_write | True | 128 | 10352 | 4240 |  |  |  |  |
| discovery | True |  |  |  |  |  | 2176 |  |
| pair_validation | True | 128 | 24 | 24 |  |  |  |  |
| residual_v2 | True | 128 | 1600 | 50 |  |  |  |  |
| classifier | True | 128 | 640 | 20 |  |  |  |  |
| program_graph | True |  |  |  | 133 | 219 |  |  |

## CSV counts
| name | rows |
| --- | ---: |
| program_graph_nodes | 133 |
| program_graph_edges | 219 |
| pair_validation_summary | 24 |
| discovery_candidates | 2176 |
