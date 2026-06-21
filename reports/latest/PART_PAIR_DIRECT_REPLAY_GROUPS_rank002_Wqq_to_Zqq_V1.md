# PART_PAIR_DIRECT_REPLAY_GROUPS_rank002_Wqq_to_Zqq_V1

Generic direct replay pair groups for all-class atlas. Builds A/B/C/D groups for an arbitrary `src_label -> tgt_label` pair using replay-consistent model forward.

- atlas_rank: **2**
- src_label: `label_Wqq` / src_group: `WToQQ`
- tgt_label: `label_Zqq` / tgt_group: `ZToQQ`
- scan_limit: **20000**
- max_per_group: **256**
- output_csv: `reports/latest/tables/part_pair_groups_rank002_Wqq_to_Zqq_v1.csv`

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
| WToQQ | 20000 | {'label_Wqq': 14927, 'label_Zqq': 2803, 'label_QCD': 1208, 'label_Tbqq': 331, 'label_Hqql': 60, 'label_H4q': 310, 'label_Hgg': 129, 'label_Hbb': 57, 'label_Hcc': 164, 'label_Tbl': 11} |
| ZToQQ | 1216 | {'label_Zqq': 745, 'label_Wqq': 259, 'label_QCD': 58, 'label_H4q': 29, 'label_Tbqq': 16, 'label_Hgg': 31, 'label_Hcc': 41, 'label_Hbb': 30, 'label_Hqql': 6, 'label_Tbl': 1} |

## Decision

`PAIR_DIRECT_GROUPS_OK`: enough direct replay events for generic pair decoding.
