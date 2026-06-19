# Confusion Monitor v1

Automatic stream monitor for class-pair confusion shifts. No LLM is used.

- events: **40960**
- accuracy: **0.7683**
- signals: **36**
- baseline: `manifests/latest/confusion_monitor_v1_baseline.json`
- update_baseline: `False`

## Signal board
| status | class_pair | score | reason | next |
| --- | --- | --- | --- | --- |
| ALERT | label_Zqq->label_Wqq | 1.4303 | confusion_rate=0.2114, delta=-0.0122, count=866 | run feature ranker for this class pair |
| ALERT | label_Wqq->label_Zqq | 0.9211 | confusion_rate=0.1443, delta=-0.0022, count=591 | run feature ranker for this class pair |
| ALERT | label_Hcc->label_Hbb | 0.7150 | confusion_rate=0.1160, delta=-0.0002, count=475 | run feature ranker for this class pair |
| ALERT | label_Hbb->label_Hcc | 0.7132 | confusion_rate=0.1157, delta=-0.0083, count=474 | run feature ranker for this class pair |
| ALERT | label_Hgg->label_H4q | 0.6506 | confusion_rate=0.1069, delta=-0.0005, count=438 | run feature ranker for this class pair |
| ALERT | label_Hbb->label_Hgg | 0.5990 | confusion_rate=0.0916, delta=0.0056, count=375 | run feature ranker for this class pair |
| ALERT | label_H4q->label_Hgg | 0.5125 | confusion_rate=0.0872, delta=-0.0085, count=357 | run feature ranker for this class pair |
| ALERT | label_Hcc->label_Hgg | 0.4625 | confusion_rate=0.0798, delta=-0.0012, count=327 | run feature ranker for this class pair |
| ALERT | label_Hcc->label_Zqq | 0.4610 | confusion_rate=0.0605, delta=0.0127, count=248 | run feature ranker for this class pair |
| ALERT | label_QCD->label_Hgg | 0.4090 | confusion_rate=0.0686, delta=0.0022, count=281 | run feature ranker for this class pair |
| ALERT | label_Hcc->label_H4q | 0.3612 | confusion_rate=0.0647, delta=-0.0125, count=265 | run feature ranker for this class pair |
| ALERT | label_Hgg->label_Hbb | 0.3536 | confusion_rate=0.0605, delta=0.0020, count=248 | run feature ranker for this class pair |
| ALERT | label_Hgg->label_Hcc | 0.3468 | confusion_rate=0.0625, delta=-0.0020, count=256 | run feature ranker for this class pair |
| ALERT | label_Wqq->label_QCD | 0.3325 | confusion_rate=0.0603, delta=-0.0002, count=247 | run feature ranker for this class pair |
| ALERT | label_Zqq->label_QCD | 0.3068 | confusion_rate=0.0518, delta=0.0029, count=212 | run feature ranker for this class pair |
| ALERT | label_QCD->label_Wqq | 0.2682 | confusion_rate=0.0503, delta=-0.0005, count=206 | run feature ranker for this class pair |
| WATCH | label_QCD->label_Zqq | 0.2254 | confusion_rate=0.0435, delta=-0.0054, count=178 | run feature ranker for this class pair |
| WATCH | label_Hqql->label_Tbl | 0.2238 | confusion_rate=0.0376, delta=0.0034, count=154 | run feature ranker for this class pair |
| WATCH | label_QCD->label_Tbqq | 0.2180 | confusion_rate=0.0378, delta=0.0027, count=155 | run feature ranker for this class pair |
| WATCH | label_Hbb->label_Zqq | 0.2089 | confusion_rate=0.0408, delta=-0.0032, count=167 | run feature ranker for this class pair |

## Top confusion pairs
| status | pair | count | rate | baseline | delta | conf | score |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ALERT | label_Zqq->label_Wqq | 866 | 0.2114 | 0.2236 | -0.0122 | 0.6431 | 1.4303 |
| ALERT | label_Wqq->label_Zqq | 591 | 0.1443 | 0.1465 | -0.0022 | 0.5849 | 0.9211 |
| ALERT | label_Hcc->label_Hbb | 475 | 0.1160 | 0.1162 | -0.0002 | 0.6094 | 0.7150 |
| ALERT | label_Hbb->label_Hcc | 474 | 0.1157 | 0.1240 | -0.0083 | 0.5932 | 0.7132 |
| ALERT | label_Hgg->label_H4q | 438 | 0.1069 | 0.1074 | -0.0005 | 0.6069 | 0.6506 |
| ALERT | label_Hbb->label_Hgg | 375 | 0.0916 | 0.0859 | 0.0056 | 0.5782 | 0.5990 |
| ALERT | label_H4q->label_Hgg | 357 | 0.0872 | 0.0957 | -0.0085 | 0.5420 | 0.5125 |
| ALERT | label_Hcc->label_Hgg | 327 | 0.0798 | 0.0811 | -0.0012 | 0.5407 | 0.4625 |
| ALERT | label_Hcc->label_Zqq | 248 | 0.0605 | 0.0479 | 0.0127 | 0.5694 | 0.4610 |
| ALERT | label_QCD->label_Hgg | 281 | 0.0686 | 0.0664 | 0.0022 | 0.5608 | 0.4090 |
| ALERT | label_Hcc->label_H4q | 265 | 0.0647 | 0.0771 | -0.0125 | 0.5784 | 0.3612 |
| ALERT | label_Hgg->label_Hbb | 248 | 0.0605 | 0.0586 | 0.0020 | 0.5505 | 0.3536 |
| ALERT | label_Hgg->label_Hcc | 256 | 0.0625 | 0.0645 | -0.0020 | 0.5371 | 0.3468 |
| ALERT | label_Wqq->label_QCD | 247 | 0.0603 | 0.0605 | -0.0002 | 0.5986 | 0.3325 |
| ALERT | label_Zqq->label_QCD | 212 | 0.0518 | 0.0488 | 0.0029 | 0.5682 | 0.3068 |
| ALERT | label_QCD->label_Wqq | 206 | 0.0503 | 0.0508 | -0.0005 | 0.5411 | 0.2682 |
| WATCH | label_QCD->label_Zqq | 178 | 0.0435 | 0.0488 | -0.0054 | 0.4961 | 0.2254 |
| WATCH | label_Hqql->label_Tbl | 154 | 0.0376 | 0.0342 | 0.0034 | 0.7353 | 0.2238 |
| WATCH | label_QCD->label_Tbqq | 155 | 0.0378 | 0.0352 | 0.0027 | 0.5990 | 0.2180 |
| WATCH | label_Hbb->label_Zqq | 167 | 0.0408 | 0.0439 | -0.0032 | 0.5802 | 0.2089 |
| WATCH | label_Zqq->label_H4q | 104 | 0.0254 | 0.0186 | 0.0068 | 0.5140 | 0.1865 |
| WATCH | label_Tbl->label_Hqql | 145 | 0.0354 | 0.0420 | -0.0066 | 0.7349 | 0.1764 |
| WATCH | label_QCD->label_Hcc | 134 | 0.0327 | 0.0352 | -0.0024 | 0.5420 | 0.1605 |
| WATCH | label_H4q->label_Hcc | 131 | 0.0320 | 0.0352 | -0.0032 | 0.5055 | 0.1562 |
| WATCH | label_Zqq->label_Hcc | 120 | 0.0293 | 0.0303 | -0.0010 | 0.5560 | 0.1405 |
| WATCH | label_Hgg->label_QCD | 117 | 0.0286 | 0.0312 | -0.0027 | 0.5373 | 0.1363 |
| WATCH | label_Hbb->label_H4q | 115 | 0.0281 | 0.0293 | -0.0012 | 0.5746 | 0.1335 |
| WATCH | label_Tbqq->label_H4q | 107 | 0.0261 | 0.0254 | 0.0007 | 0.5603 | 0.1296 |
| WATCH | label_Hbb->label_Tbqq | 89 | 0.0217 | 0.0186 | 0.0032 | 0.6554 | 0.1295 |
| WATCH | label_Hcc->label_QCD | 83 | 0.0203 | 0.0166 | 0.0037 | 0.5167 | 0.1264 |

## Interpretation

WATCH/ALERT rows should be passed to the Feature Ranker. Deep probes should run only after a feature candidate passes contrastive/monotonic filters.
