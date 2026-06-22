# PART_PAIR_DIRECT_REPLAY_GROUPS_rank009_Hcc_to_H4q_V1

Generic direct replay pair groups for all-class atlas. Builds A/B/C/D groups for an arbitrary `src_label -> tgt_label` pair using replay-consistent model forward.

- atlas_rank: **9**
- src_label: `label_Hcc` / src_group: `HToCC`
- tgt_label: `label_H4q` / tgt_group: `HToWW4Q`
- scan_limit: **20000**
- max_per_group: **256**
- output_csv: `reports/latest/tables/part_pair_groups_rank009_Hcc_to_H4q_v1.csv`

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
| HToCC | 20000 | {'label_Hcc': 13922, 'label_Hbb': 1715, 'label_H4q': 994, 'label_Hgg': 1418, 'label_Zqq': 908, 'label_QCD': 391, 'label_Wqq': 252, 'label_Tbqq': 344, 'label_Hqql': 44, 'label_Tbl': 12} |
| HToWW4Q | 8000 | {'label_QCD': 86, 'label_H4q': 6444, 'label_Hgg': 740, 'label_Hcc': 258, 'label_Wqq': 91, 'label_Hbb': 88, 'label_Tbqq': 152, 'label_Zqq': 126, 'label_Hqql': 13, 'label_Tbl': 2} |

## Decision

`PAIR_DIRECT_GROUPS_OK`: enough direct replay events for generic pair decoding.
