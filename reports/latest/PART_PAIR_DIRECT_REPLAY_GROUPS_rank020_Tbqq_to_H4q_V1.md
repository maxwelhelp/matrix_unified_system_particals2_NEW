# PART_PAIR_DIRECT_REPLAY_GROUPS_rank020_Tbqq_to_H4q_V1

Generic direct replay pair groups for all-class atlas. Builds A/B/C/D groups for an arbitrary `src_label -> tgt_label` pair using replay-consistent model forward.

- atlas_rank: **20**
- src_label: `label_Tbqq` / src_group: `TTBar`
- tgt_label: `label_H4q` / tgt_group: `HToWW4Q`
- scan_limit: **20000**
- max_per_group: **256**
- output_csv: `reports/latest/tables/part_pair_groups_rank020_Tbqq_to_H4q_v1.csv`

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
| TTBar | 20000 | {'label_Tbqq': 18237, 'label_QCD': 380, 'label_Wqq': 101, 'label_Hbb': 316, 'label_H4q': 363, 'label_Hcc': 275, 'label_Hgg': 227, 'label_Zqq': 80, 'label_Hqql': 13, 'label_Tbl': 8} |
| HToWW4Q | 15680 | {'label_QCD': 161, 'label_H4q': 12673, 'label_Hgg': 1424, 'label_Hcc': 503, 'label_Wqq': 170, 'label_Hbb': 210, 'label_Tbqq': 256, 'label_Zqq': 253, 'label_Hqql': 28, 'label_Tbl': 2} |

## Decision

`PAIR_DIRECT_GROUPS_OK`: enough direct replay events for generic pair decoding.
