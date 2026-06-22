# PART_PAIR_DIRECT_REPLAY_GROUPS_rank014_Tbl_to_Hqql_V1

Generic direct replay pair groups for all-class atlas. Builds A/B/C/D groups for an arbitrary `src_label -> tgt_label` pair using replay-consistent model forward.

- atlas_rank: **14**
- src_label: `label_Tbl` / src_group: `TTBarLep`
- tgt_label: `label_Hqql` / tgt_group: `HToWW2Q1L`
- scan_limit: **20000**
- max_per_group: **256**
- output_csv: `reports/latest/tables/part_pair_groups_rank014_Tbl_to_Hqql_v1.csv`

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
| TTBarLep | 20000 | {'label_Tbl': 19248, 'label_Hqql': 633, 'label_Wqq': 8, 'label_Hbb': 38, 'label_QCD': 36, 'label_Tbqq': 14, 'label_Zqq': 14, 'label_Hcc': 6, 'label_Hgg': 1, 'label_H4q': 2} |
| HToWW2Q1L | 8960 | {'label_Hqql': 8548, 'label_Hbb': 31, 'label_Zqq': 39, 'label_Tbl': 260, 'label_QCD': 9, 'label_Wqq': 37, 'label_Hcc': 13, 'label_Tbqq': 14, 'label_H4q': 9} |

## Decision

`PAIR_DIRECT_GROUPS_OK`: enough direct replay events for generic pair decoding.
