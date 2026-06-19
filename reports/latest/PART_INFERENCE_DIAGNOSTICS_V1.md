# PART_INFERENCE_DIAGNOSTICS_V1

Diagnostic for low ParT inference accuracy. Tests all executable forward signatures and label-permutation upper bound.

- events: **2560**
- missing keys: **0**
- unexpected keys: **0**
- executable variants: `points_features_vectors_mask`

## Variant results
| variant | acc | perm_acc | pred_counts |
| --- | --- | --- | --- |
| points_features_vectors_mask | 0.1051 | 0.1902 | {"label_QCD": 1534, "label_Hbb": 45, "label_Hcc": 106, "label_Hgg": 3, "label_H4q": 41, "label_Hqql": 7, "label_Zqq": 771, "label_Wqq": 34, "label_Tbqq": 1, "label_Tbl": 18} |

## Interpretation

- If raw accuracy is low but permutation accuracy is high, label order is wrong.
- If both raw and permutation accuracy are low, input preprocessing/model config/data split is wrong.
- If another forward variant is much better, update PART_INFERENCE_V1 to use that signature.
