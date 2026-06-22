# PART_PAIR_DIRECT_REPLAY_GROUPS_rank017_Zqq_to_Hbb_V1

Generic direct replay pair groups for all-class atlas. Builds A/B/C/D groups for an arbitrary `src_label -> tgt_label` pair using replay-consistent model forward.

- atlas_rank: **17**
- src_label: `label_Zqq` / src_group: `ZToQQ`
- tgt_label: `label_Hbb` / tgt_group: `HToBB`
- scan_limit: **20000**
- max_per_group: **256**
- output_csv: `reports/latest/tables/part_pair_groups_rank017_Zqq_to_Hbb_v1.csv`

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
| HToBB | 5696 | {'label_Hcc': 542, 'label_Tbqq': 105, 'label_Hbb': 4100, 'label_Hgg': 455, 'label_Hqql': 11, 'label_Zqq': 256, 'label_Wqq': 40, 'label_QCD': 80, 'label_H4q': 103, 'label_Tbl': 4} |

## Decision

`PAIR_DIRECT_GROUPS_OK`: enough direct replay events for generic pair decoding.
