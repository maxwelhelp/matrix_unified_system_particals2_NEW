# PART_PAIR_DIRECT_REPLAY_GROUPS_rank001_Zqq_to_Wqq_V1

Generic direct replay pair groups for all-class atlas. Builds A/B/C/D groups for an arbitrary `src_label -> tgt_label` pair using replay-consistent model forward.

- atlas_rank: **1**
- src_label: `label_Zqq` / src_group: `ZToQQ`
- tgt_label: `label_Wqq` / tgt_group: `WToQQ`
- scan_limit: **20000**
- max_per_group: **256**
- output_csv: `reports/latest/tables/part_pair_groups_rank001_Zqq_to_Wqq_v1.csv`

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
| ZToQQ | 20000 | {'label_Zqq': 12507, 'label_Wqq': 4070, 'label_QCD': 1057, 'label_H4q': 406, 'label_Tbqq': 293, 'label_Hgg': 400, 'label_Hcc': 615, 'label_Hbb': 581, 'label_Hqql': 60, 'label_Tbl': 11} |
| WToQQ | 1856 | {'label_Wqq': 1376, 'label_Zqq': 259, 'label_QCD': 118, 'label_Tbqq': 38, 'label_Hqql': 5, 'label_H4q': 19, 'label_Hgg': 17, 'label_Hbb': 4, 'label_Hcc': 19, 'label_Tbl': 1} |

## Decision

`PAIR_DIRECT_GROUPS_OK`: enough direct replay events for generic pair decoding.
