# Head Output Trace v1

Actual pseudo-head output statistics from EdgeConvBlock outputs. This answers what each pseudo-head writes, not only what its gradient suggests.

## Summary
| head | layer | mean_abs | top_class | contrast | particle0_top | lead_pt_match | logit_corr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| L0_ch0:8 | 0 | 3.2325 | label_Tbqq | 0.3261 | 0.0031 | 0.0031 | label_Hqql:-0.2814 |
| L0_ch40:48 | 0 | 2.8218 | label_Tbqq | 0.5538 | 0.1648 | 0.1648 | label_Tbqq:0.1292 |
| L0_ch56:64 | 0 | 2.4235 | label_Tbqq | 0.4066 | 0.0031 | 0.0031 | label_Tbqq:0.2599 |
| L0_ch8:16 | 0 | 1.8327 | label_Tbqq | 0.8413 | 0.0078 | 0.0078 | label_Tbqq:0.2794 |
| L0_ch16:24 | 0 | 1.7899 | label_Tbqq | 1.0140 | 0.0195 | 0.0195 | label_Tbqq:0.2299 |
| L0_ch48:56 | 0 | 1.7075 | label_Tbqq | 0.4501 | 0.0461 | 0.0461 | label_Tbqq:0.1998 |
| L0_ch24:32 | 0 | 1.3348 | label_QCD | 0.3859 | 0.0797 | 0.0797 | label_H4q:-0.1225 |
| L0_ch32:40 | 0 | 1.3153 | label_QCD | 0.4785 | 0.1195 | 0.1195 | label_Hqql:-0.3183 |
| L1_ch112:128 | 1 | 2.7225 | label_Tbl | 0.1777 | 0.1727 | 0.1727 | label_Wqq:-0.2462 |
| L1_ch64:80 | 1 | 2.4876 | label_Tbqq | 0.4332 | 0.0000 | 0.0000 | label_Tbqq:0.2741 |
| L1_ch80:96 | 1 | 2.4748 | label_Tbl | 0.7204 | 0.0414 | 0.0414 | label_Tbl:0.1208 |
| L1_ch32:48 | 1 | 2.3011 | label_Tbqq | 0.6440 | 0.0656 | 0.0656 | label_Hqql:-0.2501 |
| L1_ch16:32 | 1 | 2.0420 | label_QCD | 0.1613 | 0.0383 | 0.0383 | label_QCD:0.1070 |
| L1_ch96:112 | 1 | 1.9396 | label_QCD | 0.5805 | 0.1289 | 0.1289 | label_H4q:-0.1061 |
| L1_ch48:64 | 1 | 1.9169 | label_Tbqq | 0.2301 | 0.0969 | 0.0969 | label_Tbqq:0.2433 |
| L1_ch0:16 | 1 | 1.6411 | label_Tbl | 0.4483 | 0.3016 | 0.3016 | label_H4q:-0.3682 |
| L2_ch32:64 | 2 | 0.4696 | label_Tbl | 0.1780 | 0.3812 | 0.3812 | label_QCD:-0.5493 |
| L2_ch224:256 | 2 | 0.4095 | label_Tbl | 0.1585 | 0.7180 | 0.7180 | label_Hgg:-0.6442 |
| L2_ch192:224 | 2 | 0.3914 | label_Tbqq | 0.0700 | 0.3055 | 0.3055 | label_QCD:-0.3177 |
| L2_ch128:160 | 2 | 0.3500 | label_Tbl | 0.2491 | 0.3852 | 0.3852 | label_Tbl:0.6627 |
| L2_ch64:96 | 2 | 0.3257 | label_Tbl | 0.0883 | 0.2336 | 0.2336 | label_QCD:-0.5693 |
| L2_ch0:32 | 2 | 0.2594 | label_Hqql | 0.0475 | 0.4227 | 0.4227 | label_Hbb:-0.3352 |
| L2_ch160:192 | 2 | 0.2364 | label_Tbl | 0.1978 | 0.2477 | 0.2477 | label_Tbl:0.5801 |
| L2_ch96:128 | 2 | 0.1905 | label_Hbb | 0.0210 | 0.2094 | 0.2094 | label_Wqq:-0.1734 |

## Interpretation

If `lead_pt_match` is high, this pseudo-head output is core/leading-particle aligned. If class contrast and logit correlation are high, it writes class-relevant evidence. Next: route-neighbor trace for exact neighbor sources.
