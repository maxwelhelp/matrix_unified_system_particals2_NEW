# Particle accuracy diagnostic v4

Checks whether low accuracy is caused by trim mode or label-order permutation. If `label_permutation_upper_bound` is also low, label order is not the main problem; input preprocessing/model-data format is still wrong.

| trim | acc | label_perm_upper | pred_counts |
| --- | ---: | ---: | --- |
| False | 0.1051 | 0.6781 | `[1534, 45, 106, 3, 41, 7, 771, 34, 1, 18]` |
| True | 0.1051 | 0.6781 | `[1534, 45, 106, 3, 41, 7, 771, 34, 1, 18]` |

## Best per true class

- label_QCD: [('label_Zqq', 143), ('label_QCD', 94), ('label_Hcc', 11)]
- label_Hbb: [('label_QCD', 197), ('label_Zqq', 39), ('label_Wqq', 11)]
- label_Hcc: [('label_QCD', 200), ('label_Zqq', 41), ('label_Wqq', 10)]
- label_Hgg: [('label_QCD', 198), ('label_Zqq', 31), ('label_Hcc', 13)]
- label_H4q: [('label_QCD', 207), ('label_Zqq', 27), ('label_H4q', 13)]
- label_Hqql: [('label_Zqq', 116), ('label_QCD', 108), ('label_Hcc', 14)]
- label_Zqq: [('label_Zqq', 144), ('label_QCD', 94), ('label_Hcc', 14)]
- label_Wqq: [('label_Zqq', 161), ('label_QCD', 66), ('label_Hcc', 24)]
- label_Tbqq: [('label_QCD', 251), ('label_Zqq', 5), ('label_Hbb', 0)]
- label_Tbl: [('label_QCD', 119), ('label_Zqq', 64), ('label_Hbb', 32)]

## Confusion matrix best run

```json
[
  [
    94,
    0,
    11,
    0,
    6,
    0,
    143,
    1,
    0,
    1
  ],
  [
    197,
    0,
    4,
    1,
    2,
    0,
    39,
    11,
    0,
    2
  ],
  [
    200,
    1,
    1,
    0,
    3,
    0,
    41,
    10,
    0,
    0
  ],
  [
    198,
    0,
    13,
    0,
    12,
    0,
    31,
    2,
    0,
    0
  ],
  [
    207,
    0,
    8,
    0,
    13,
    0,
    27,
    1,
    0,
    0
  ],
  [
    108,
    9,
    14,
    0,
    2,
    4,
    116,
    2,
    0,
    1
  ],
  [
    94,
    0,
    14,
    0,
    2,
    0,
    144,
    0,
    0,
    2
  ],
  [
    66,
    3,
    24,
    1,
    0,
    0,
    161,
    1,
    0,
    0
  ],
  [
    251,
    0,
    0,
    0,
    0,
    0,
    5,
    0,
    0,
    0
  ],
  [
    119,
    32,
    17,
    1,
    1,
    3,
    64,
    6,
    1,
    12
  ]
]
```
