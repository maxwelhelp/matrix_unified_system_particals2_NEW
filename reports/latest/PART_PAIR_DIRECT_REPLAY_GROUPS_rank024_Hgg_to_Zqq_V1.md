# PART_PAIR_DIRECT_REPLAY_GROUPS_rank024_Hgg_to_Zqq_V1

Generic direct replay pair groups for all-class atlas. Builds A/B/C/D groups for an arbitrary `src_label -> tgt_label` pair using replay-consistent model forward.

- atlas_rank: **24**
- src_label: `label_Hgg` / src_group: `HToGG`
- tgt_label: `label_Zqq` / tgt_group: `ZToQQ`
- scan_limit: **20000**
- max_per_group: **256**
- output_csv: `reports/latest/tables/part_pair_groups_rank024_Hgg_to_Zqq_v1.csv`

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
| HToGG | 20000 | {'label_Hgg': 14851, 'label_QCD': 772, 'label_Wqq': 143, 'label_H4q': 1605, 'label_Hbb': 969, 'label_Hcc': 993, 'label_Tbqq': 221, 'label_Zqq': 430, 'label_Tbl': 6, 'label_Hqql': 10} |
| ZToQQ | 12096 | {'label_Zqq': 7605, 'label_Wqq': 2451, 'label_QCD': 605, 'label_H4q': 247, 'label_Tbqq': 166, 'label_Hgg': 257, 'label_Hcc': 366, 'label_Hbb': 349, 'label_Hqql': 43, 'label_Tbl': 7} |

## Decision

`PAIR_DIRECT_GROUPS_OK`: enough direct replay events for generic pair decoding.
