# PART_ATTENTION_CLEAN_RANK_V2

Clean post-rank over existing ParT top-K pair flows. Filters pad pairs and CLS-only paths, adds per-group occurrence counts/frequencies, and reranks trigger/loss/Tbl-like/anomaly paths.

- raw rows: **8960000**
- used rows: **7388753**
- dropped pad rows: **1570481**
- dropped CLS-only rows: **766**
- clean summary rows: **1364**

## Top clean B>A triggers
| module | head | pair | A_mean | B_mean | C_mean | A_freq | B_freq | C_freq | score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| mod.blocks.5.attn | 3 | charged_hadron<-charged_hadron | 0.3152 | 0.3838 | 0.3643 | 2.0446 | 1.4525 | 0.0456 | 0.099618 |
| mod.blocks.0.attn | 1 | photon<-photon | 0.1976 | 0.2462 | 0.239 | 1.5706 | 1.9095 | 1.2826 | 0.092788 |
| mod.blocks.3.attn | 1 | charged_hadron<-charged_hadron | 0.3506 | 0.4145 | 0.4032 | 1.3724 | 1.451 | 0.8124 | 0.092709 |
| mod.blocks.1.attn | 4 | charged_hadron<-charged_hadron | 0.4929 | 0.5353 | 0.4908 | 3.0008 | 2.1415 | 1.5762 | 0.090904 |
| mod.blocks.1.attn | 1 | photon<-photon | 0.2511 | 0.2908 | 0.2824 | 1.4534 | 2.076 | 1.5204 | 0.082408 |
| mod.blocks.7.attn | 1 | photon<-photon | 0.5508 | 0.7085 | 0.7238 | 0.2892 | 0.4915 | 0.6876 | 0.077547 |
| mod.blocks.3.attn | 0 | charged_hadron<-charged_hadron | 0.5346 | 0.5786 | 0.5908 | 2.2536 | 1.7555 | 1.0854 | 0.077187 |
| mod.blocks.3.attn | 1 | photon<-photon | 0.3771 | 0.4294 | 0.489 | 1.1168 | 1.4025 | 0.7394 | 0.073324 |
| mod.blocks.6.attn | 3 | charged_hadron<-charged_hadron | 0.468 | 0.5114 | 0.5447 | 2.3882 | 1.5765 | 0.05 | 0.068384 |
| mod.blocks.0.attn | 5 | charged_hadron<-charged_hadron | 0.5186 | 0.5389 | 0.5493 | 3.7486 | 3.361 | 2.6658 | 0.068048 |
| mod.blocks.1.attn | 0 | charged_hadron<-charged_hadron | 0.4758 | 0.5178 | 0.5574 | 1.9042 | 1.5835 | 1.121 | 0.066412 |
| mod.blocks.5.attn | 5 | charged_hadron<-charged_hadron | 0.5851 | 0.6356 | 0.6358 | 1.7102 | 1.3085 | 1.0372 | 0.066131 |
| mod.blocks.6.attn | 3 | charged_hadron<-neutral_hadron | 0.4395 | 0.5778 | 0.5087 | 0.107 | 0.4735 | 0.0054 | 0.065486 |
| mod.blocks.6.attn | 5 | charged_hadron<-charged_hadron | 0.4954 | 0.5273 | 0.5073 | 2.4572 | 2.031 | 1.4414 | 0.064897 |
| mod.blocks.5.attn | 1 | charged_hadron<-electron | 0.4696 | 0.544 | 0.5105 | 0.7176 | 0.8655 | 0.4198 | 0.064438 |
| mod.blocks.5.attn | 3 | photon<-charged_hadron | 0.3179 | 0.3918 | 0.3762 | 0.8288 | 0.867 | 0.0294 | 0.064034 |
| mod.cls_blocks.1.attn | 3 | CLS<-photon | 0.0676 | 0.088 | 0.0964 | 2.443 | 3.021 | 2.9388 | 0.061709 |
| mod.blocks.2.attn | 0 | charged_hadron<-charged_hadron | 0.5356 | 0.5798 | 0.5738 | 1.9624 | 1.398 | 0.7566 | 0.06167 |
| mod.blocks.0.attn | 7 | photon<-neutral_hadron | 0.2862 | 0.3747 | 0.4095 | 0.3736 | 0.69 | 0.274 | 0.06108 |
| mod.blocks.5.attn | 1 | charged_hadron<-muon | 0.4944 | 0.5533 | 0.5279 | 0.8384 | 1.033 | 0.5014 | 0.060762 |
| mod.blocks.0.attn | 2 | charged_hadron<-charged_hadron | 0.5183 | 0.5415 | 0.5299 | 3.107 | 2.615 | 2.413 | 0.0607 |
| mod.blocks.5.attn | 4 | charged_hadron<-photon | 0.624 | 0.6679 | 0.6175 | 1.2256 | 1.364 | 0.6268 | 0.059855 |
| mod.blocks.1.attn | 5 | charged_hadron<-charged_hadron | 0.5616 | 0.5961 | 0.6506 | 2.137 | 1.7375 | 0.7274 | 0.059833 |
| mod.blocks.6.attn | 3 | photon<-neutral_hadron | 0.4247 | 0.5532 | 0.5119 | 0.0818 | 0.448 | 0.0042 | 0.057543 |
| mod.blocks.6.attn | 4 | charged_hadron<-charged_hadron | 0.6555 | 0.6748 | 0.6601 | 3.6832 | 2.953 | 1.8118 | 0.056993 |

## Top clean Hqql-loss paths
| module | head | pair | A_mean | B_mean | C_mean | A_freq | B_freq | score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| mod.blocks.2.attn | 6 | charged_hadron<-charged_hadron | 0.5451 | 0.5103 | 0.5375 | 3.898 | 3.0735 | 0.135479 |
| mod.cls_blocks.1.attn | 6 | CLS<-charged_hadron | 0.097 | 0.0642 | 0.0549 | 3.9134 | 3.336 | 0.128213 |
| mod.blocks.3.attn | 6 | charged_hadron<-charged_hadron | 0.6318 | 0.6039 | 0.6332 | 3.9028 | 2.6315 | 0.10907 |
| mod.cls_blocks.1.attn | 3 | CLS<-muon | 0.579 | 0.2373 | 0.1526 | 0.2956 | 0.121 | 0.101026 |
| mod.cls_blocks.1.attn | 3 | CLS<-electron | 0.5217 | 0.2209 | 0.1444 | 0.2952 | 0.153 | 0.088796 |
| mod.blocks.4.attn | 7 | charged_hadron<-charged_hadron | 0.4651 | 0.4393 | 0.5475 | 3.2276 | 3.2 | 0.083213 |
| mod.cls_blocks.1.attn | 2 | CLS<-charged_hadron | 0.1005 | 0.0823 | 0.1147 | 4.1164 | 3.595 | 0.074849 |
| mod.blocks.2.attn | 7 | charged_hadron<-muon | 0.497 | 0.4539 | 0.6354 | 1.5778 | 1.1615 | 0.067988 |
| mod.cls_blocks.1.attn | 4 | CLS<-charged_hadron | 0.119 | 0.1045 | 0.1236 | 4.3368 | 3.8145 | 0.062667 |
| mod.blocks.7.attn | 2 | charged_hadron<-charged_hadron | 0.5519 | 0.5306 | 0.5237 | 2.9186 | 2.153 | 0.062163 |
| mod.blocks.2.attn | 7 | charged_hadron<-electron | 0.4951 | 0.4588 | 0.6324 | 1.5026 | 1.091 | 0.054528 |
| mod.blocks.1.attn | 6 | charged_hadron<-charged_hadron | 0.4426 | 0.4227 | 0.4443 | 2.5948 | 1.6315 | 0.05167 |
| mod.blocks.2.attn | 6 | photon<-charged_hadron | 0.5426 | 0.4997 | 0.5318 | 1.0164 | 0.864 | 0.043655 |
| mod.cls_blocks.1.attn | 1 | CLS<-charged_hadron | 0.0974 | 0.0875 | 0.0938 | 4.3572 | 3.8725 | 0.043043 |
| mod.blocks.4.attn | 6 | photon<-charged_hadron | 0.5797 | 0.5549 | 0.5445 | 1.6294 | 1.352 | 0.04042 |
| mod.blocks.0.attn | 6 | photon<-charged_hadron | 0.4003 | 0.373 | 0.4102 | 1.474 | 1.1585 | 0.040141 |
| mod.cls_blocks.1.attn | 0 | CLS<-muon | 0.303 | 0.1462 | 0.2445 | 0.2464 | 0.2095 | 0.038636 |
| mod.cls_blocks.1.attn | 1 | CLS<-muon | 0.2955 | 0.1583 | 0.1935 | 0.2776 | 0.247 | 0.038092 |
| mod.blocks.7.attn | 6 | photon<-muon | 0.6547 | 0.5837 | 0.552 | 0.5364 | 0.4875 | 0.038086 |
| mod.blocks.2.attn | 3 | charged_hadron<-muon | 0.5319 | 0.5036 | 0.9409 | 1.2934 | 0.9035 | 0.036657 |
| mod.cls_blocks.1.attn | 5 | CLS<-photon | 0.0945 | 0.0773 | 0.0886 | 2.13 | 2.377 | 0.036647 |
| mod.cls_blocks.1.attn | 2 | CLS<-photon | 0.086 | 0.072 | 0.0553 | 2.4324 | 2.7265 | 0.034194 |
| mod.blocks.4.attn | 7 | charged_hadron<-muon | 0.5802 | 0.5526 | 0.6466 | 1.2178 | 0.766 | 0.03361 |
| mod.blocks.7.attn | 6 | photon<-electron | 0.6528 | 0.5822 | 0.5547 | 0.4444 | 0.4755 | 0.031348 |
| mod.blocks.4.attn | 0 | charged_hadron<-charged_hadron | 0.435 | 0.4253 | 0.4896 | 3.1664 | 2.1225 | 0.030703 |

## Top clean Tbl-like paths
| module | head | pair | A_mean | B_mean | C_mean | B_freq | score |
| --- | --- | --- | --- | --- | --- | --- | --- |
| mod.blocks.3.attn | 4 | charged_hadron<-charged_hadron | 0.7115 | 0.7255 | 0.6725 | 3.3725 | 2.267914 |
| mod.blocks.2.attn | 4 | charged_hadron<-charged_hadron | 0.7173 | 0.7262 | 0.6945 | 3.26 | 2.26405 |
| mod.blocks.6.attn | 4 | charged_hadron<-charged_hadron | 0.6555 | 0.6748 | 0.6601 | 2.953 | 1.949308 |
| mod.blocks.0.attn | 5 | charged_hadron<-charged_hadron | 0.5186 | 0.5389 | 0.5493 | 3.361 | 1.776158 |
| mod.blocks.5.attn | 2 | charged_hadron<-charged_hadron | 0.6293 | 0.6472 | 0.6901 | 2.8 | 1.691642 |
| mod.blocks.3.attn | 2 | charged_hadron<-charged_hadron | 0.5874 | 0.6034 | 0.5444 | 3.1045 | 1.690224 |
| mod.blocks.3.attn | 6 | charged_hadron<-charged_hadron | 0.6318 | 0.6039 | 0.6332 | 2.6315 | 1.512097 |
| mod.blocks.4.attn | 5 | charged_hadron<-charged_hadron | 0.5317 | 0.5413 | 0.5356 | 2.7825 | 1.490245 |
| mod.blocks.2.attn | 6 | charged_hadron<-charged_hadron | 0.5451 | 0.5103 | 0.5375 | 3.0735 | 1.485089 |
| mod.blocks.0.attn | 2 | charged_hadron<-charged_hadron | 0.5183 | 0.5415 | 0.5299 | 2.615 | 1.385808 |
| mod.blocks.0.attn | 4 | charged_hadron<-charged_hadron | 0.5065 | 0.5172 | 0.5244 | 2.6665 | 1.360047 |
| mod.blocks.2.attn | 2 | charged_hadron<-charged_hadron | 0.621 | 0.6341 | 0.6833 | 2.2485 | 1.315251 |
| mod.blocks.5.attn | 6 | charged_hadron<-charged_hadron | 0.5782 | 0.5944 | 0.5974 | 2.166 | 1.280858 |
| mod.blocks.4.attn | 2 | charged_hadron<-charged_hadron | 0.562 | 0.5734 | 0.637 | 2.5075 | 1.278178 |
| mod.blocks.4.attn | 4 | charged_hadron<-charged_hadron | 0.6788 | 0.6778 | 0.6273 | 1.935 | 1.213873 |
| mod.blocks.7.attn | 2 | charged_hadron<-charged_hadron | 0.5519 | 0.5306 | 0.5237 | 2.153 | 1.127432 |
| mod.blocks.3.attn | 5 | charged_hadron<-charged_hadron | 0.5722 | 0.5847 | 0.5754 | 1.934 | 1.112787 |
| mod.blocks.5.attn | 4 | charged_hadron<-charged_hadron | 0.6176 | 0.6407 | 0.6226 | 1.7835 | 1.110406 |
| mod.blocks.1.attn | 2 | charged_hadron<-charged_hadron | 0.5073 | 0.5327 | 0.5257 | 2.05 | 1.077785 |
| mod.blocks.4.attn | 6 | charged_hadron<-charged_hadron | 0.5632 | 0.5604 | 0.5495 | 1.958 | 1.07601 |
| mod.blocks.4.attn | 7 | charged_hadron<-charged_hadron | 0.4651 | 0.4393 | 0.5475 | 3.2 | 1.059333 |
| mod.blocks.1.attn | 4 | charged_hadron<-charged_hadron | 0.4929 | 0.5353 | 0.4908 | 2.1415 | 1.050966 |
| mod.blocks.6.attn | 5 | charged_hadron<-charged_hadron | 0.4954 | 0.5273 | 0.5073 | 2.031 | 1.030323 |
| mod.blocks.7.attn | 4 | charged_hadron<-charged_hadron | 0.6033 | 0.6133 | 0.5261 | 1.9525 | 1.027144 |
| mod.blocks.6.attn | 4 | photon<-charged_hadron | 0.6547 | 0.6602 | 0.629 | 1.63 | 1.025191 |

## Top clean anomaly paths
| module | head | pair | A_mean | B_mean | C_mean | B_freq | score |
| --- | --- | --- | --- | --- | --- | --- | --- |
| mod.blocks.0.attn | 3 | photon<-electron | 0.5203 | 0.5686 | 0.9533 | 1.178 | 0.021901 |
| mod.blocks.5.attn | 3 | charged_hadron<-photon | 0.3127 | 0.4047 | 0.7124 | 0.429 | 0.012144 |
| mod.blocks.2.attn | 3 | charged_hadron<-muon | 0.5319 | 0.5036 | 0.9409 | 0.9035 | 0.011197 |
| mod.blocks.0.attn | 3 | photon<-photon | 0.393 | 0.4883 | 0.7719 | 0.381 | 0.010294 |
| mod.blocks.4.attn | 3 | photon<-muon | 0.6497 | 0.6109 | 0.9399 | 0.8 | 0.010213 |
| mod.blocks.0.attn | 3 | charged_hadron<-electron | 0.5407 | 0.5627 | 0.9507 | 1.181 | 0.010077 |
| mod.blocks.2.attn | 3 | charged_hadron<-photon | 0.3658 | 0.4436 | 0.7512 | 0.4195 | 0.010027 |
| mod.blocks.0.attn | 3 | photon<-muon | 0.556 | 0.5748 | 0.9609 | 1.256 | 0.009103 |
| mod.blocks.2.attn | 7 | charged_hadron<-muon | 0.497 | 0.4539 | 0.6354 | 1.1615 | 0.009085 |
| mod.blocks.4.attn | 7 | charged_hadron<-charged_hadron | 0.4651 | 0.4393 | 0.5475 | 3.2 | 0.008931 |
| mod.blocks.3.attn | 3 | photon<-muon | 0.5728 | 0.5161 | 0.8863 | 0.422 | 0.008859 |
| mod.blocks.1.attn | 3 | photon<-muon | 0.5622 | 0.5482 | 0.9308 | 1.5645 | 0.008334 |
| mod.blocks.2.attn | 3 | photon<-electron | 0.4858 | 0.5136 | 0.9321 | 0.702 | 0.008142 |
| mod.blocks.1.attn | 3 | charged_hadron<-muon | 0.5622 | 0.5357 | 0.9141 | 0.777 | 0.007792 |
| mod.blocks.2.attn | 3 | charged_hadron<-neutral_hadron | 0.3557 | 0.4542 | 0.0 | 0.1715 | 0.007672 |
| mod.blocks.5.attn | 3 | charged_hadron<-electron | 0.4822 | 0.5095 | 0.8881 | 0.73 | 0.007549 |
| mod.blocks.6.attn | 3 | charged_hadron<-photon | 0.3985 | 0.4598 | 0.7329 | 0.441 | 0.007388 |
| mod.blocks.0.attn | 0 | charged_hadron<-charged_hadron | 0.4829 | 0.5106 | 0.6472 | 1.827 | 0.006902 |
| mod.blocks.2.attn | 7 | charged_hadron<-electron | 0.4951 | 0.4588 | 0.6324 | 1.091 | 0.006873 |
| mod.blocks.6.attn | 3 | photon<-photon | 0.3977 | 0.4533 | 0.7723 | 0.384 | 0.006804 |
| mod.blocks.7.attn | 3 | photon<-electron | 0.6436 | 0.6698 | 0.9173 | 1.033 | 0.006701 |
| mod.blocks.2.attn | 3 | photon<-photon | 0.3614 | 0.4419 | 0.7371 | 0.282 | 0.0067 |
| mod.blocks.2.attn | 3 | photon<-neutral_hadron | 0.3409 | 0.4488 | 0.0 | 0.138 | 0.006687 |
| mod.blocks.5.attn | 3 | photon<-muon | 0.5131 | 0.4876 | 0.8856 | 0.6465 | 0.006566 |
| mod.blocks.1.attn | 3 | charged_hadron<-photon | 0.315 | 0.4184 | 0.7622 | 0.1775 | 0.006308 |
