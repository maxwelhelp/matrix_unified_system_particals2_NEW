# PART_PAIR_DIRECT_REPLAY_GROUPS_rank015_Hqql_to_Tbl_V1

Generic direct replay pair groups for all-class atlas. Builds A/B/C/D groups for an arbitrary `src_label -> tgt_label` pair using replay-consistent model forward.

- atlas_rank: **15**
- src_label: `label_Hqql` / src_group: `HToWW2Q1L`
- tgt_label: `label_Tbl` / tgt_group: `TTBarLep`
- scan_limit: **20000**
- max_per_group: **256**
- output_csv: `reports/latest/tables/part_pair_groups_rank015_Hqql_to_Tbl_v1.csv`

## Group counts
| group | selected |
| --- | --- |
| A_src_correct | 256 |
| B_src_to_tgt | 256 |
| C_tgt_correct | 256 |
| D_tgt_to_src | 256 |

## Source scan counts
| source_group | scanned | pred_counts |
| --- | --- | --- |
| HToWW2Q1L | 20000 | {'label_Hqql': 19037, 'label_Hbb': 61, 'label_Zqq': 81, 'label_Tbl': 611, 'label_QCD': 21, 'label_Wqq': 99, 'label_Hcc': 41, 'label_Tbqq': 27, 'label_H4q': 22} |
| TTBarLep | 7744 | {'label_Tbl': 7435, 'label_Hqql': 256, 'label_Wqq': 5, 'label_Hbb': 19, 'label_QCD': 15, 'label_Tbqq': 5, 'label_Zqq': 5, 'label_Hcc': 4} |

## Decision

`PAIR_DIRECT_GROUPS_OK`: enough direct replay events for generic pair decoding.
