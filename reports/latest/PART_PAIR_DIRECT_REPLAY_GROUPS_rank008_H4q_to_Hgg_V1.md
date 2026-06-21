# PART_PAIR_DIRECT_REPLAY_GROUPS_rank008_H4q_to_Hgg_V1

Generic direct replay pair groups for all-class atlas. Builds A/B/C/D groups for an arbitrary `src_label -> tgt_label` pair using replay-consistent model forward.

- atlas_rank: **8**
- src_label: `label_H4q` / src_group: `HToWW4Q`
- tgt_label: `label_Hgg` / tgt_group: `HToGG`
- scan_limit: **20000**
- max_per_group: **256**
- output_csv: `reports/latest/tables/part_pair_groups_rank008_H4q_to_Hgg_v1.csv`

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
| HToWW4Q | 20000 | {'label_QCD': 204, 'label_H4q': 16134, 'label_Hgg': 1842, 'label_Hcc': 637, 'label_Wqq': 228, 'label_Hbb': 263, 'label_Tbqq': 334, 'label_Zqq': 325, 'label_Hqql': 31, 'label_Tbl': 2} |
| HToGG | 3200 | {'label_Hgg': 2382, 'label_QCD': 116, 'label_Wqq': 22, 'label_H4q': 263, 'label_Hbb': 157, 'label_Hcc': 159, 'label_Tbqq': 28, 'label_Zqq': 71, 'label_Tbl': 2} |

## Decision

`PAIR_DIRECT_GROUPS_OK`: enough direct replay events for generic pair decoding.
