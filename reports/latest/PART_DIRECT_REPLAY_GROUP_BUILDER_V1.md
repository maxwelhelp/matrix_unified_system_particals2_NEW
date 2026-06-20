# PART_DIRECT_REPLAY_GROUP_BUILDER_V1

Builds A/B/C/D Hqql/Tbl groups directly from reproducible legacy-wrapper forward, not from prediction ROOT row indices.

- network_file: `external/particle_transformer/networks/example_ParticleTransformer_legacy.py`
- checkpoint: `external/particle_transformer/models/ParT_kinpid.pt`
- data_config: `external/particle_transformer/data/JetClass/JetClass_kinpid.yaml`
- scan_limit: **20000**
- max_per_group: **256**
- output csv: `reports/latest/tables/part_hqql_tbl_groups_direct_replay_v1.csv`

## Group counts
| group | selected |
| --- | --- |
| A_Hqql_correct | 256 |
| B_Hqql_to_Tbl | 256 |
| C_Tbl_correct | 256 |
| D_Tbl_to_Hqql | 256 |

## Source scan counts
| source_group | scanned | pred_counts |
| --- | --- | --- |
| HToWW2Q1L | 20000 | {'label_Hqql': 19037, 'label_Hbb': 61, 'label_Zqq': 81, 'label_Tbl': 611, 'label_QCD': 21, 'label_Wqq': 99, 'label_Hcc': 41, 'label_Tbqq': 27, 'label_H4q': 22} |
| TTBarLep | 7744 | {'label_Tbl': 7435, 'label_Hqql': 256, 'label_Wqq': 5, 'label_Hbb': 19, 'label_QCD': 15, 'label_Tbqq': 5, 'label_Zqq': 5, 'label_Hcc': 4} |

## Decision

`DIRECT_REPLAY_GROUPS_OK`: use this CSV for supertrace/gate/patch. It is internally replay-consistent.
