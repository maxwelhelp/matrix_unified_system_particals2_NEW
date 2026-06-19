# PART_INFERENCE_V1

ParT inference smoke test on local JetClass balanced sample. No training.

- checkpoint: `external/particle_transformer/models/ParT_kinpid.pt`
- events: **5120**
- accuracy: **0.1008**
- forward signature: `points,features,vectors,mask`
- missing keys: **0**
- unexpected keys: **0**
- Hqql_to_Tbl: **2**
- Tbl_to_Hqql: **8**

## Top confusion pairs
| true | pred | n |
| --- | --- | --- |
| label_Tbqq | label_QCD | 498 |
| label_Hgg | label_QCD | 410 |
| label_H4q | label_QCD | 410 |
| label_Hbb | label_QCD | 406 |
| label_Hcc | label_QCD | 398 |
| label_Wqq | label_Zqq | 321 |
| label_QCD | label_Zqq | 300 |
| label_Zqq | label_Zqq | 294 |
| label_Tbl | label_QCD | 264 |
| label_Hqql | label_Zqq | 226 |
| label_Hqql | label_QCD | 210 |
| label_Zqq | label_QCD | 189 |
| label_QCD | label_QCD | 175 |
| label_Wqq | label_QCD | 132 |
| label_Tbl | label_Zqq | 108 |
| label_Hcc | label_Zqq | 85 |
| label_Hbb | label_Zqq | 72 |
| label_H4q | label_Zqq | 63 |
| label_Tbl | label_Hbb | 61 |
| label_Hgg | label_Zqq | 57 |
| label_Wqq | label_Hcc | 45 |
| label_Hqql | label_Hcc | 42 |
| label_Tbl | label_Hcc | 39 |
| label_H4q | label_H4q | 22 |
| label_Hgg | label_Hcc | 21 |
| label_Zqq | label_Hcc | 21 |
| label_QCD | label_Hcc | 20 |
| label_Hgg | label_H4q | 19 |
| label_Hcc | label_Wqq | 18 |
| label_Hqql | label_Hbb | 17 |

## Next

If accuracy/logits are sane and Hqql/Tbl events exist, build `PART_ATTENTION_TRACE_V1` to export attention heads and pairwise particle flows for A/B/C.
