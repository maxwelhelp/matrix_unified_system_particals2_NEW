# Event Forecast Explainer v1

Event-level mechanistic forecasts: prediction, active routes, particles, and route-aware pseudocode context.

## Forecasts
| event | true | pred | conf | active_heads | tag | explanation |
| --- | --- | --- | --- | --- | --- | --- |
| 197 | label_Hqql | label_Tbl | 0.9905 | L0_ch40:48, L1_ch112:128, L1_ch0:16, L2_ch224:256, L2_ch32:64 | Hqql activates Tbl-like core route | Model predicts label_Tbl because active route heads L0_ch40:48, L1_ch112:128, L1_ch0:16 write evidence through particles [24, 0, 0]; tag=Hqql activates Tbl-like core route. |
| 369 | label_Tbl | label_Tbl | 0.9999 | L1_ch0:16, L0_ch40:48, L1_ch112:128, L2_ch32:64, L2_ch224:256 | Tbl-like core-neighborhood route | Model predicts label_Tbl because active route heads L1_ch0:16, L0_ch40:48, L1_ch112:128 write evidence through particles [2, 27, 0]; tag=Tbl-like core-neighborhood route. |
| 355 | label_Tbl | label_Tbl | 1.0000 | L1_ch112:128, L0_ch40:48, L1_ch0:16, L2_ch224:256, L2_ch32:64 | Tbl-like core-neighborhood route | Model predicts label_Tbl because active route heads L1_ch112:128, L0_ch40:48, L1_ch0:16 write evidence through particles [0, 14, 0]; tag=Tbl-like core-neighborhood route. |
| 332 | label_Tbl | label_Tbl | 0.9242 | L0_ch40:48, L1_ch0:16, L1_ch112:128, L2_ch32:64, L2_ch160:192 | Tbl-like core-neighborhood route | Model predicts label_Tbl because active route heads L0_ch40:48, L1_ch0:16, L1_ch112:128 write evidence through particles [75, 4, 12]; tag=Tbl-like core-neighborhood route. |
| 323 | label_Tbl | label_Tbl | 0.9999 | L0_ch40:48, L1_ch112:128, L1_ch0:16, L2_ch224:256, L2_ch160:192 | Tbl-like core-neighborhood route | Model predicts label_Tbl because active route heads L0_ch40:48, L1_ch112:128, L1_ch0:16 write evidence through particles [1, 0, 0]; tag=Tbl-like core-neighborhood route. |
| 334 | label_Tbl | label_Tbl | 1.0000 | L0_ch40:48, L1_ch112:128, L1_ch0:16, L2_ch224:256, L2_ch128:160 | Tbl-like core-neighborhood route | Model predicts label_Tbl because active route heads L0_ch40:48, L1_ch112:128, L1_ch0:16 write evidence through particles [18, 0, 1]; tag=Tbl-like core-neighborhood route. |
| 340 | label_Tbl | label_Tbl | 0.9999 | L1_ch112:128, L0_ch40:48, L1_ch0:16, L2_ch32:64, L2_ch128:160 | Tbl-like core-neighborhood route | Model predicts label_Tbl because active route heads L1_ch112:128, L0_ch40:48, L1_ch0:16 write evidence through particles [0, 1, 0]; tag=Tbl-like core-neighborhood route. |
| 337 | label_Tbl | label_Tbl | 1.0000 | L0_ch40:48, L1_ch0:16, L1_ch112:128, L2_ch224:256, L2_ch128:160 | Tbl-like core-neighborhood route | Model predicts label_Tbl because active route heads L0_ch40:48, L1_ch0:16, L1_ch112:128 write evidence through particles [19, 19, 0]; tag=Tbl-like core-neighborhood route. |
| 327 | label_Tbl | label_Tbl | 1.0000 | L1_ch112:128, L1_ch0:16, L0_ch40:48, L2_ch128:160, L2_ch224:256 | Tbl-like core-neighborhood route | Model predicts label_Tbl because active route heads L1_ch112:128, L1_ch0:16, L0_ch40:48 write evidence through particles [3, 20, 4]; tag=Tbl-like core-neighborhood route. |
| 376 | label_Tbl | label_Tbl | 0.9999 | L1_ch112:128, L1_ch0:16, L0_ch40:48, L2_ch128:160, L2_ch160:192 | Tbl-like core-neighborhood route | Model predicts label_Tbl because active route heads L1_ch112:128, L1_ch0:16, L0_ch40:48 write evidence through particles [11, 0, 5]; tag=Tbl-like core-neighborhood route. |
| 362 | label_Tbl | label_Tbl | 1.0000 | L1_ch0:16, L0_ch40:48, L1_ch112:128, L2_ch128:160, L2_ch160:192 | Tbl-like core-neighborhood route | Model predicts label_Tbl because active route heads L1_ch0:16, L0_ch40:48, L1_ch112:128 write evidence through particles [8, 7, 18]; tag=Tbl-like core-neighborhood route. |
| 373 | label_Tbl | label_Tbl | 0.9986 | L0_ch40:48, L1_ch112:128, L1_ch0:16, L2_ch128:160, L2_ch160:192 | Tbl-like core-neighborhood route | Model predicts label_Tbl because active route heads L0_ch40:48, L1_ch112:128, L1_ch0:16 write evidence through particles [53, 12, 49]; tag=Tbl-like core-neighborhood route. |
| 356 | label_Tbl | label_Tbl | 1.0000 | L0_ch40:48, L1_ch112:128, L1_ch0:16, L2_ch128:160, L2_ch160:192 | Tbl-like core-neighborhood route | Model predicts label_Tbl because active route heads L0_ch40:48, L1_ch112:128, L1_ch0:16 write evidence through particles [3, 9, 9]; tag=Tbl-like core-neighborhood route. |
| 342 | label_Tbl | label_Tbl | 0.9999 | L0_ch40:48, L1_ch0:16, L1_ch112:128, L2_ch128:160, L2_ch32:64 | Tbl-like core-neighborhood route | Model predicts label_Tbl because active route heads L0_ch40:48, L1_ch0:16, L1_ch112:128 write evidence through particles [31, 1, 0]; tag=Tbl-like core-neighborhood route. |
| 365 | label_Tbl | label_Tbl | 0.9998 | L0_ch40:48, L1_ch0:16, L1_ch112:128, L2_ch160:192, L2_ch128:160 | Tbl-like core-neighborhood route | Model predicts label_Tbl because active route heads L0_ch40:48, L1_ch0:16, L1_ch112:128 write evidence through particles [25, 1, 5]; tag=Tbl-like core-neighborhood route. |
| 379 | label_Tbl | label_Tbl | 0.9802 | L0_ch40:48, L1_ch112:128, L1_ch0:16, L2_ch160:192, L2_ch128:160 | Tbl-like core-neighborhood route | Model predicts label_Tbl because active route heads L0_ch40:48, L1_ch112:128, L1_ch0:16 write evidence through particles [4, 2, 59]; tag=Tbl-like core-neighborhood route. |
| 351 | label_Tbl | label_Tbl | 0.8107 | L1_ch112:128, L1_ch0:16, L0_ch40:48, L2_ch160:192, L2_ch32:64 | Tbl-like core-neighborhood route | Model predicts label_Tbl because active route heads L1_ch112:128, L1_ch0:16, L0_ch40:48 write evidence through particles [29, 0, 4]; tag=Tbl-like core-neighborhood route. |
| 341 | label_Tbl | label_Tbl | 1.0000 | L0_ch40:48, L1_ch0:16, L1_ch112:128, L2_ch128:160, L2_ch32:64 | Tbl-like core-neighborhood route | Model predicts label_Tbl because active route heads L0_ch40:48, L1_ch0:16, L1_ch112:128 write evidence through particles [37, 0, 2]; tag=Tbl-like core-neighborhood route. |
| 434 | label_Tbqq | label_Tbqq | 0.8333 | L0_ch40:48, L1_ch0:16, L1_ch112:128, L2_ch0:32, L2_ch192:224 | late L2 core-readout route | Model predicts label_Tbqq because active route heads L0_ch40:48, L1_ch0:16, L1_ch112:128 write evidence through particles [40, 12, 4]; tag=late L2 core-readout route. |
| 445 | label_Tbqq | label_Tbqq | 0.9944 | L1_ch0:16, L0_ch40:48, L1_ch112:128, L2_ch0:32, L2_ch192:224 | late L2 core-readout route | Model predicts label_Tbqq because active route heads L1_ch0:16, L0_ch40:48, L1_ch112:128 write evidence through particles [0, 2, 0]; tag=late L2 core-readout route. |

## Active routes
| event | rank | head | score | top_particle | p0 | lead | knn_p0 | knn_lead | role |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 197 | 1 | L0_ch40:48 | 8.4616 | 24 | 0 | 0 | 0 | 0 | context builder / relay away from direct core readout |
| 197 | 2 | L1_ch112:128 | 5.0561 | 0 | 1 | 1 | 1 | 1 | context builder / relay away from direct core readout |
| 197 | 3 | L1_ch0:16 | 4.5061 | 0 | 1 | 1 | 1 | 1 | context builder / relay away from direct core readout |
| 197 | 4 | L2_ch224:256 | 0.4960 | 0 | 1 | 1 | 1 | 1 | route-aware late core readout |
| 197 | 5 | L2_ch32:64 | 0.3257 | 0 | 1 | 1 | 1 | 1 | route-aware late core readout |
| 197 | 6 | L2_ch128:160 | 0.2986 | 0 | 1 | 1 | 1 | 1 | route-aware late core readout |
| 197 | 7 | L2_ch160:192 | 0.2326 | 0 | 1 | 1 | 1 | 1 | route-aware late core readout |
| 197 | 8 | L2_ch0:32 | 0.1585 | 0 | 1 | 1 | 1 | 1 | late readout moderately core-aligned |
| 197 | 9 | L2_ch64:96 | 0.0812 | 0 | 1 | 1 | 1 | 1 | route-aware late core readout |
| 197 | 10 | L2_ch192:224 | 0.0628 | 2 | 0 | 0 | 0 | 0 | late readout moderately core-aligned |
| 369 | 1 | L1_ch0:16 | 6.7681 | 2 | 0 | 0 | 0 | 0 | context builder / relay away from direct core readout |
| 369 | 2 | L0_ch40:48 | 5.6413 | 27 | 0 | 0 | 0 | 0 | context builder / relay away from direct core readout |
| 369 | 3 | L1_ch112:128 | 5.0240 | 0 | 1 | 1 | 1 | 1 | context builder / relay away from direct core readout |
| 369 | 4 | L2_ch32:64 | 0.7211 | 0 | 1 | 1 | 1 | 1 | route-aware late core readout |
| 369 | 5 | L2_ch224:256 | 0.6458 | 0 | 1 | 1 | 1 | 1 | route-aware late core readout |
| 369 | 6 | L2_ch128:160 | 0.5193 | 0 | 1 | 1 | 1 | 1 | route-aware late core readout |
| 369 | 7 | L2_ch0:32 | 0.4082 | 0 | 1 | 1 | 1 | 1 | late readout moderately core-aligned |
| 369 | 8 | L2_ch160:192 | 0.3859 | 0 | 1 | 1 | 1 | 1 | route-aware late core readout |
| 369 | 9 | L2_ch64:96 | 0.1711 | 0 | 1 | 1 | 1 | 1 | route-aware late core readout |
| 369 | 10 | L2_ch192:224 | 0.1680 | 0 | 1 | 1 | 1 | 1 | late readout moderately core-aligned |
| 355 | 1 | L1_ch112:128 | 5.8467 | 0 | 1 | 1 | 1 | 1 | context builder / relay away from direct core readout |
| 355 | 2 | L0_ch40:48 | 5.2937 | 14 | 0 | 0 | 0 | 0 | context builder / relay away from direct core readout |
| 355 | 3 | L1_ch0:16 | 4.7856 | 0 | 1 | 1 | 1 | 1 | context builder / relay away from direct core readout |
| 355 | 4 | L2_ch224:256 | 0.5429 | 0 | 1 | 1 | 1 | 1 | route-aware late core readout |
| 355 | 5 | L2_ch32:64 | 0.2732 | 0 | 1 | 1 | 1 | 1 | route-aware late core readout |
| 355 | 6 | L2_ch128:160 | 0.2519 | 0 | 1 | 1 | 1 | 1 | route-aware late core readout |
| 355 | 7 | L2_ch160:192 | 0.2472 | 0 | 1 | 1 | 1 | 1 | route-aware late core readout |
| 355 | 8 | L2_ch64:96 | 0.1841 | 0 | 1 | 1 | 1 | 1 | route-aware late core readout |
| 355 | 9 | L2_ch0:32 | 0.1302 | 0 | 1 | 1 | 1 | 1 | late readout moderately core-aligned |
| 355 | 10 | L2_ch192:224 | 0.0565 | 0 | 1 | 1 | 1 | 1 | late readout moderately core-aligned |
| 332 | 1 | L0_ch40:48 | 9.0128 | 75 | 0 | 0 | 1 | 1 | context builder / relay away from direct core readout |
| 332 | 2 | L1_ch0:16 | 6.4890 | 4 | 0 | 0 | 0 | 0 | context builder / relay away from direct core readout |
| 332 | 3 | L1_ch112:128 | 4.6702 | 12 | 0 | 0 | 0 | 0 | context builder / relay away from direct core readout |
| 332 | 4 | L2_ch32:64 | 0.6587 | 0 | 1 | 1 | 0 | 0 | route-aware late core readout |
| 332 | 5 | L2_ch160:192 | 0.5925 | 0 | 1 | 1 | 0 | 0 | route-aware late core readout |
| 332 | 6 | L2_ch128:160 | 0.5906 | 0 | 1 | 1 | 0 | 0 | route-aware late core readout |
| 332 | 7 | L2_ch224:256 | 0.5683 | 0 | 1 | 1 | 0 | 0 | route-aware late core readout |
| 332 | 8 | L2_ch192:224 | 0.4874 | 0 | 1 | 1 | 0 | 0 | late readout moderately core-aligned |
| 332 | 9 | L2_ch0:32 | 0.3955 | 0 | 1 | 1 | 0 | 0 | late readout moderately core-aligned |
| 332 | 10 | L2_ch64:96 | 0.1420 | 0 | 1 | 1 | 0 | 0 | route-aware late core readout |
| 323 | 1 | L0_ch40:48 | 5.6587 | 1 | 0 | 0 | 0 | 0 | context builder / relay away from direct core readout |
| 323 | 2 | L1_ch112:128 | 5.3442 | 0 | 1 | 1 | 1 | 1 | context builder / relay away from direct core readout |
| 323 | 3 | L1_ch0:16 | 4.7280 | 0 | 1 | 1 | 1 | 1 | context builder / relay away from direct core readout |
| 323 | 4 | L2_ch224:256 | 0.5153 | 0 | 1 | 1 | 1 | 1 | route-aware late core readout |
| 323 | 5 | L2_ch160:192 | 0.3935 | 0 | 1 | 1 | 1 | 1 | route-aware late core readout |
| 323 | 6 | L2_ch128:160 | 0.3934 | 0 | 1 | 1 | 1 | 1 | route-aware late core readout |
| 323 | 7 | L2_ch32:64 | 0.3686 | 0 | 1 | 1 | 1 | 1 | route-aware late core readout |
| 323 | 8 | L2_ch64:96 | 0.2343 | 0 | 1 | 1 | 1 | 1 | route-aware late core readout |
| 323 | 9 | L2_ch0:32 | 0.1797 | 0 | 1 | 1 | 1 | 1 | late readout moderately core-aligned |
| 323 | 10 | L2_ch192:224 | 0.0895 | 2 | 0 | 0 | 0 | 0 | late readout moderately core-aligned |
| 334 | 1 | L0_ch40:48 | 5.1589 | 18 | 0 | 0 | 0 | 0 | context builder / relay away from direct core readout |
| 334 | 2 | L1_ch112:128 | 5.0659 | 0 | 1 | 1 | 1 | 1 | context builder / relay away from direct core readout |
| 334 | 3 | L1_ch0:16 | 4.6065 | 1 | 0 | 0 | 0 | 0 | context builder / relay away from direct core readout |
| 334 | 4 | L2_ch224:256 | 0.5128 | 0 | 1 | 1 | 1 | 1 | route-aware late core readout |
| 334 | 5 | L2_ch128:160 | 0.4330 | 0 | 1 | 1 | 1 | 1 | route-aware late core readout |
| 334 | 6 | L2_ch160:192 | 0.3892 | 0 | 1 | 1 | 1 | 1 | route-aware late core readout |
| 334 | 7 | L2_ch32:64 | 0.3434 | 0 | 1 | 1 | 1 | 1 | route-aware late core readout |
| 334 | 8 | L2_ch64:96 | 0.2880 | 0 | 1 | 1 | 1 | 1 | route-aware late core readout |
| 334 | 9 | L2_ch0:32 | 0.1504 | 0 | 1 | 1 | 1 | 1 | late readout moderately core-aligned |
| 334 | 10 | L2_ch192:224 | 0.0667 | 0 | 1 | 1 | 1 | 1 | late readout moderately core-aligned |
| 340 | 1 | L1_ch112:128 | 5.0344 | 0 | 1 | 1 | 1 | 1 | context builder / relay away from direct core readout |
| 340 | 2 | L0_ch40:48 | 4.9895 | 1 | 0 | 0 | 0 | 0 | context builder / relay away from direct core readout |
| 340 | 3 | L1_ch0:16 | 4.6258 | 0 | 1 | 1 | 1 | 1 | context builder / relay away from direct core readout |
| 340 | 4 | L2_ch32:64 | 0.6397 | 0 | 1 | 1 | 1 | 1 | route-aware late core readout |
| 340 | 5 | L2_ch128:160 | 0.5213 | 0 | 1 | 1 | 1 | 1 | route-aware late core readout |
| 340 | 6 | L2_ch224:256 | 0.4992 | 0 | 1 | 1 | 1 | 1 | route-aware late core readout |
| 340 | 7 | L2_ch160:192 | 0.4451 | 0 | 1 | 1 | 1 | 1 | route-aware late core readout |
| 340 | 8 | L2_ch0:32 | 0.3713 | 0 | 1 | 1 | 1 | 1 | late readout moderately core-aligned |
| 340 | 9 | L2_ch64:96 | 0.1524 | 0 | 1 | 1 | 1 | 1 | route-aware late core readout |
| 340 | 10 | L2_ch192:224 | 0.1284 | 1 | 0 | 0 | 0 | 0 | late readout moderately core-aligned |
| 337 | 1 | L0_ch40:48 | 10.9784 | 19 | 0 | 0 | 0 | 0 | context builder / relay away from direct core readout |
| 337 | 2 | L1_ch0:16 | 5.4517 | 19 | 0 | 0 | 0 | 0 | context builder / relay away from direct core readout |
| 337 | 3 | L1_ch112:128 | 4.9120 | 0 | 1 | 1 | 1 | 1 | context builder / relay away from direct core readout |
| 337 | 4 | L2_ch224:256 | 0.4978 | 0 | 1 | 1 | 1 | 1 | route-aware late core readout |
| 337 | 5 | L2_ch128:160 | 0.4783 | 0 | 1 | 1 | 1 | 1 | route-aware late core readout |
| 337 | 6 | L2_ch160:192 | 0.3525 | 0 | 1 | 1 | 1 | 1 | route-aware late core readout |
| 337 | 7 | L2_ch32:64 | 0.3513 | 0 | 1 | 1 | 1 | 1 | route-aware late core readout |
| 337 | 8 | L2_ch64:96 | 0.3299 | 0 | 1 | 1 | 1 | 1 | route-aware late core readout |
| 337 | 9 | L2_ch192:224 | 0.1311 | 0 | 1 | 1 | 1 | 1 | late readout moderately core-aligned |
| 337 | 10 | L2_ch0:32 | 0.1062 | 0 | 1 | 1 | 1 | 1 | late readout moderately core-aligned |
| 327 | 1 | L1_ch112:128 | 4.9888 | 3 | 0 | 0 | 0 | 0 | context builder / relay away from direct core readout |
| 327 | 2 | L1_ch0:16 | 4.4993 | 20 | 0 | 0 | 0 | 0 | context builder / relay away from direct core readout |
| 327 | 3 | L0_ch40:48 | 4.4364 | 4 | 0 | 0 | 0 | 0 | context builder / relay away from direct core readout |
| 327 | 4 | L2_ch128:160 | 0.6819 | 0 | 1 | 1 | 1 | 1 | route-aware late core readout |
| 327 | 5 | L2_ch224:256 | 0.4616 | 0 | 1 | 1 | 1 | 1 | route-aware late core readout |
| 327 | 6 | L2_ch160:192 | 0.4405 | 0 | 1 | 1 | 1 | 1 | route-aware late core readout |
| 327 | 7 | L2_ch32:64 | 0.3926 | 0 | 1 | 1 | 1 | 1 | route-aware late core readout |
| 327 | 8 | L2_ch0:32 | 0.2362 | 0 | 1 | 1 | 1 | 1 | late readout moderately core-aligned |
| 327 | 9 | L2_ch64:96 | 0.1914 | 0 | 1 | 1 | 1 | 1 | route-aware late core readout |
| 327 | 10 | L2_ch192:224 | 0.1319 | 0 | 1 | 1 | 1 | 1 | late readout moderately core-aligned |
| 376 | 1 | L1_ch112:128 | 4.4614 | 11 | 0 | 0 | 0 | 0 | context builder / relay away from direct core readout |
| 376 | 2 | L1_ch0:16 | 4.0710 | 0 | 1 | 1 | 1 | 1 | context builder / relay away from direct core readout |
| 376 | 3 | L0_ch40:48 | 3.9030 | 5 | 0 | 0 | 0 | 0 | context builder / relay away from direct core readout |
| 376 | 4 | L2_ch128:160 | 0.6815 | 0 | 1 | 1 | 1 | 1 | route-aware late core readout |
| 376 | 5 | L2_ch160:192 | 0.5447 | 0 | 1 | 1 | 1 | 1 | route-aware late core readout |
| 376 | 6 | L2_ch32:64 | 0.4131 | 0 | 1 | 1 | 1 | 1 | route-aware late core readout |
| 376 | 7 | L2_ch64:96 | 0.2729 | 0 | 1 | 1 | 1 | 1 | route-aware late core readout |
| 376 | 8 | L2_ch224:256 | 0.2680 | 0 | 1 | 1 | 1 | 1 | route-aware late core readout |
| 376 | 9 | L2_ch0:32 | 0.2462 | 0 | 1 | 1 | 1 | 1 | late readout moderately core-aligned |
| 376 | 10 | L2_ch192:224 | 0.1418 | 0 | 1 | 1 | 1 | 1 | late readout moderately core-aligned |
| 362 | 1 | L1_ch0:16 | 4.3608 | 8 | 0 | 0 | 0 | 0 | context builder / relay away from direct core readout |
| 362 | 2 | L0_ch40:48 | 4.2888 | 7 | 0 | 0 | 0 | 0 | context builder / relay away from direct core readout |
| 362 | 3 | L1_ch112:128 | 4.0413 | 18 | 0 | 0 | 0 | 0 | context builder / relay away from direct core readout |
| 362 | 4 | L2_ch128:160 | 0.6496 | 0 | 1 | 1 | 1 | 1 | route-aware late core readout |
| 362 | 5 | L2_ch160:192 | 0.4018 | 0 | 1 | 1 | 1 | 1 | route-aware late core readout |
| 362 | 6 | L2_ch32:64 | 0.3461 | 0 | 1 | 1 | 1 | 1 | route-aware late core readout |
| 362 | 7 | L2_ch224:256 | 0.3108 | 0 | 1 | 1 | 1 | 1 | route-aware late core readout |
| 362 | 8 | L2_ch64:96 | 0.2651 | 0 | 1 | 1 | 1 | 1 | route-aware late core readout |
| 362 | 9 | L2_ch0:32 | 0.1583 | 0 | 1 | 1 | 1 | 1 | late readout moderately core-aligned |
| 362 | 10 | L2_ch192:224 | 0.1176 | 0 | 1 | 1 | 1 | 1 | late readout moderately core-aligned |
| 373 | 1 | L0_ch40:48 | 11.8237 | 53 | 0 | 0 | 1 | 1 | context builder / relay away from direct core readout |
| 373 | 2 | L1_ch112:128 | 4.0041 | 12 | 0 | 0 | 0 | 0 | context builder / relay away from direct core readout |
| 373 | 3 | L1_ch0:16 | 3.8127 | 49 | 0 | 0 | 0 | 0 | context builder / relay away from direct core readout |
| 373 | 4 | L2_ch128:160 | 0.6484 | 0 | 1 | 1 | 1 | 1 | route-aware late core readout |
| 373 | 5 | L2_ch160:192 | 0.3915 | 0 | 1 | 1 | 1 | 1 | route-aware late core readout |
| 373 | 6 | L2_ch32:64 | 0.3685 | 0 | 1 | 1 | 1 | 1 | route-aware late core readout |
| 373 | 7 | L2_ch64:96 | 0.1711 | 0 | 1 | 1 | 1 | 1 | route-aware late core readout |
| 373 | 8 | L2_ch192:224 | 0.1595 | 0 | 1 | 1 | 1 | 1 | late readout moderately core-aligned |
| 373 | 9 | L2_ch224:256 | 0.1594 | 0 | 1 | 1 | 1 | 1 | route-aware late core readout |
| 373 | 10 | L2_ch0:32 | 0.1432 | 0 | 1 | 1 | 1 | 1 | late readout moderately core-aligned |

## Next

Use this report to choose events for route-specific patching and richer residual validation.
