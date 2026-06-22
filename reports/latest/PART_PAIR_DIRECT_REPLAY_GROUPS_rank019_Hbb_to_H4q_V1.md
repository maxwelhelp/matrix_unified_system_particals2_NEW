# PART_PAIR_DIRECT_REPLAY_GROUPS_rank019_Hbb_to_H4q_V1

Generic direct replay pair groups for all-class atlas. Builds A/B/C/D groups for an arbitrary `src_label -> tgt_label` pair using replay-consistent model forward.

- atlas_rank: **19**
- src_label: `label_Hbb` / src_group: `HToBB`
- tgt_label: `label_H4q` / tgt_group: `HToWW4Q`
- scan_limit: **20000**
- max_per_group: **256**
- output_csv: `reports/latest/tables/part_pair_groups_rank019_Hbb_to_H4q_v1.csv`

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
| HToBB | 20000 | {'label_Hcc': 1888, 'label_Tbqq': 376, 'label_Hbb': 14361, 'label_Hgg': 1668, 'label_Hqql': 43, 'label_Zqq': 851, 'label_Wqq': 117, 'label_QCD': 296, 'label_H4q': 381, 'label_Tbl': 19} |
| HToWW4Q | 19520 | {'label_QCD': 198, 'label_H4q': 15745, 'label_Hgg': 1807, 'label_Hcc': 619, 'label_Wqq': 220, 'label_Hbb': 256, 'label_Tbqq': 326, 'label_Zqq': 316, 'label_Hqql': 31, 'label_Tbl': 2} |

## Decision

`PAIR_DIRECT_GROUPS_OK`: enough direct replay events for generic pair decoding.
