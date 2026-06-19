# INTERNAL_ACTIVATION_CONTRAST_V2

Direct hook-based A/B/C activation contrast. Includes approximate class-direction projection and safer zero-slice ablation contribution.

- A protected_highiso: **32**
- B confused_highiso: **11**
- C Tbl_correct: **128**
- projection: `effective_linear_approx_from_2_linear_layers`

## Head diagnosis summary
| head | diag | B_close_C | B-A hqql_proj | B-A tbl_proj | B-A hqql_contrib | B-A tbl_contrib | A hqql/tbl | B hqql/tbl | C hqql/tbl |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| L1_ch64:80 | mixed_or_unclear | -512.9345 | 103.2327 | -2.9195 | -0.2563 | 0.5563 | 1202.7847/1134.7649 | 1306.0174/1131.8454 | 855.9197/710.9832 |
| L0_ch40:48 | lost_hqql_evidence_candidate | -250.2544 | -64.0338 | -59.7507 | -1.1540 | -0.4085 | 239.7006/455.9772 | 175.6668/396.2265 | 373.1311/670.3446 |
| L1_ch0:16 | active_tbl_like_readout_candidate | 142.8701 | 109.1258 | 146.3761 | -0.6993 | 0.9044 | 29.3283/300.5078 | 138.4541/446.8839 | 161.0856/414.2578 |
| L0_ch16:24 | active_tbl_like_readout_candidate | 128.3890 | 104.3919 | 106.6270 | -0.9464 | 0.6641 | 183.9267/122.1589 | 288.3186/228.7859 | 273.3910/214.2549 |
| L1_ch80:96 | active_tbl_like_readout_candidate | 107.7441 | 170.7955 | 103.4572 | -0.1101 | 1.1220 | 1190.1986/1152.2983 | 1360.9941/1255.7555 | 1313.4933/1334.4764 |
| L1_ch96:112 | mixed_or_unclear | -68.5056 | 35.9003 | 8.3811 | 0.0511 | 0.6187 | 522.3985/394.4106 | 558.2988/402.7918 | 459.8424/440.3341 |
| L1_ch16:32 | mixed_or_unclear | 59.3826 | -41.1248 | -61.8498 | -0.2824 | -0.2786 | 735.3578/528.2865 | 694.2330/466.4367 | 690.6886/451.9732 |
| L0_ch32:40 | lost_hqql_evidence_candidate | -53.1247 | -42.7046 | -19.0347 | -0.0299 | -0.2610 | 143.5804/119.7167 | 100.8758/100.6820 | 194.6644/135.0273 |
| L1_ch112:128 | mixed_or_unclear | -46.6943 | 34.8343 | -11.9021 | -0.3454 | 0.3501 | 371.4060/341.5263 | 406.2403/329.6241 | 345.6649/387.1032 |
| L0_ch56:64 | lost_hqql_evidence_candidate | -28.1347 | -33.7694 | -30.5388 | -0.5519 | 0.7307 | 243.1364/214.5506 | 209.3670/184.0118 | 268.6863/227.6893 |
| L2_ch224:256 | lost_hqql_evidence_candidate | -27.9287 | -1.6834 | -0.7152 | 0.2378 | -0.4670 | 22.3679/21.0772 | 20.6845/20.3620 | 41.9434/41.1847 |
| L0_ch0:8 | mixed_or_unclear | -24.8408 | 0.1096 | -6.6729 | -1.0447 | 1.2137 | 326.2717/326.0858 | 326.3813/319.4129 | 326.9371/287.9031 |
| L2_ch32:64 | mixed_or_unclear | -19.2769 | 4.6974 | 8.0105 | -0.4246 | 0.3246 | 9.3685/9.9281 | 14.0659/17.9386 | 29.3177/42.0889 |
| L0_ch24:32 | lost_hqql_evidence_candidate | 16.2202 | -28.4926 | -20.8607 | 0.3537 | 1.1543 | 164.9247/22.3815 | 136.4321/1.5208 | 155.4746/2.9038 |
| L0_ch8:16 | mixed_or_unclear | -11.2570 | 32.5676 | 26.9247 | -2.3435 | 0.1079 | 286.5570/251.0037 | 319.1246/277.9284 | 266.7641/288.9754 |
| L2_ch160:192 | mixed_or_unclear | -8.3213 | 3.1764 | 4.4483 | -1.0202 | -0.0235 | 15.3746/19.2787 | 18.5511/23.7270 | 26.5158/34.9811 |
| L1_ch32:48 | active_tbl_like_readout_candidate | 7.8095 | 140.4912 | 167.3082 | -0.2127 | 0.3607 | 304.3802/347.0692 | 444.8714/514.3775 | 654.1567/538.4224 |
| L2_ch128:160 | lost_hqql_evidence_candidate | -6.6534 | -4.1474 | 0.9384 | -0.2256 | -0.0576 | 24.6162/23.3001 | 20.4688/24.2385 | 21.5606/35.0894 |
| L2_ch0:32 | lost_hqql_evidence_candidate | -2.3092 | -0.8316 | 1.6008 | 0.0875 | 0.0778 | 9.9492/7.7741 | 9.1176/9.3749 | 10.8239/13.1174 |
| L2_ch96:128 | mixed_or_unclear | -2.0797 | -0.1712 | 0.1739 | 0.0626 | -0.1330 | 4.5937/4.0101 | 4.4225/4.1839 | 2.1309/3.7991 |
| L1_ch48:64 | active_tbl_like_readout_candidate | 1.1887 | 99.0371 | 90.2134 | -0.3795 | 0.0326 | -503.1660/-400.9695 | -404.1289/-310.7560 | -290.8083/-241.5595 |
| L0_ch48:56 | mixed_or_unclear | -0.4934 | 25.4438 | 7.7421 | -0.1276 | 0.8918 | -171.6099/-38.7928 | -146.1661/-31.0506 | -141.8750/-4.3036 |
| L2_ch192:224 | lost_hqql_evidence_candidate | -0.3476 | -2.4081 | -0.6468 | 0.2617 | 0.5661 | 9.4511/6.9341 | 7.0430/6.2873 | 4.2037/6.3892 |
| L2_ch64:96 | lost_hqql_evidence_candidate | -0.3136 | -7.3034 | -3.4831 | -0.4580 | -0.3468 | 21.1734/18.6731 | 13.8700/15.1899 | 18.1262/22.4377 |

## Interpretation guide

- `active_tbl_like_readout_candidate`: B is closer to C than A in projected class-evidence space.
- `lost_hqql_evidence_candidate`: B loses Hqql projection/contribution without clean Tbl-like activation.
- `mixed_or_unclear`: inspect event rows and top particles.

Use `internal_activation_contrast_v2_top_particles.csv` to check whether top activations in B land on second leptons, particle0/lepton, or hadronic neighbors.
