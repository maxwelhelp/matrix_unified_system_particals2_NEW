# Layer Code Alignment v1

Maps semantic pseudocode rows to actual ParticleNet code path and runtime tensor shapes.

## Captured modules
| module | type | input | output |
| --- | --- | --- | --- |
| edge_convs.0.convs.0 | Conv2d | [[160, 26, 128, 16]] | [160, 64, 128, 16] |
| edge_convs.0.convs.1 | Conv2d | [[160, 64, 128, 16]] | [160, 64, 128, 16] |
| edge_convs.0.convs.2 | Conv2d | [[160, 64, 128, 16]] | [160, 64, 128, 16] |
| edge_convs.0.sc | Conv1d | [[160, 13, 128]] | [160, 64, 128] |
| edge_convs.0 | EdgeConvBlock | [[160, 2, 128], [160, 13, 128]] | [160, 64, 128] |
| edge_convs.1.convs.0 | Conv2d | [[160, 128, 128, 16]] | [160, 128, 128, 16] |
| edge_convs.1.convs.1 | Conv2d | [[160, 128, 128, 16]] | [160, 128, 128, 16] |
| edge_convs.1.convs.2 | Conv2d | [[160, 128, 128, 16]] | [160, 128, 128, 16] |
| edge_convs.1.sc | Conv1d | [[160, 64, 128]] | [160, 128, 128] |
| edge_convs.1 | EdgeConvBlock | [[160, 64, 128], [160, 64, 128]] | [160, 128, 128] |
| edge_convs.2.convs.0 | Conv2d | [[160, 256, 128, 16]] | [160, 256, 128, 16] |
| edge_convs.2.convs.1 | Conv2d | [[160, 256, 128, 16]] | [160, 256, 128, 16] |
| edge_convs.2.convs.2 | Conv2d | [[160, 256, 128, 16]] | [160, 256, 128, 16] |
| edge_convs.2.sc | Conv1d | [[160, 128, 128]] | [160, 256, 128] |
| edge_convs.2 | EdgeConvBlock | [[160, 128, 128], [160, 128, 128]] | [160, 256, 128] |
| fc | Sequential | [[160, 256]] | [160, 10] |

## Pseudo-head alignment
| head | module | operation | shape | confidence |
| --- | --- | --- | --- | --- |
| L0_ch40:48 | edge_convs.0.convs.0 | KNN edge construction + first EdgeConv local feature extraction | [160, 64, 128, 16] | MEDIUM |
| L0_ch0:8 | edge_convs.0.convs.0 | KNN edge construction + first EdgeConv local feature extraction | [160, 64, 128, 16] | MEDIUM |
| L0_ch48:56 | edge_convs.0.convs.0 | KNN edge construction + first EdgeConv local feature extraction | [160, 64, 128, 16] | MEDIUM |
| L0_ch16:24 | edge_convs.0.convs.0 | KNN edge construction + first EdgeConv local feature extraction | [160, 64, 128, 16] | MEDIUM |
| L0_ch24:32 | edge_convs.0.convs.0 | KNN edge construction + first EdgeConv local feature extraction | [160, 64, 128, 16] | MEDIUM |
| L0_ch8:16 | edge_convs.0.convs.0 | KNN edge construction + first EdgeConv local feature extraction | [160, 64, 128, 16] | MEDIUM |
| L0_ch56:64 | edge_convs.0.convs.0 | KNN edge construction + first EdgeConv local feature extraction | [160, 64, 128, 16] | MEDIUM |
| L0_ch32:40 | edge_convs.0.convs.0 | KNN edge construction + first EdgeConv local feature extraction | [160, 64, 128, 16] | MEDIUM |
| L1_ch16:32 | edge_convs.0.convs.1 | EdgeConv neighborhood/context relay over L0 features | [160, 64, 128, 16] | MEDIUM |
| L1_ch32:48 | edge_convs.0.convs.1 | EdgeConv neighborhood/context relay over L0 features | [160, 64, 128, 16] | MEDIUM |
| L1_ch112:128 | edge_convs.0.convs.1 | EdgeConv neighborhood/context relay over L0 features | [160, 64, 128, 16] | MEDIUM |
| L1_ch0:16 | edge_convs.0.convs.1 | EdgeConv neighborhood/context relay over L0 features | [160, 64, 128, 16] | MEDIUM |
| L1_ch96:112 | edge_convs.0.convs.1 | EdgeConv neighborhood/context relay over L0 features | [160, 64, 128, 16] | MEDIUM |
| L1_ch64:80 | edge_convs.0.convs.1 | EdgeConv neighborhood/context relay over L0 features | [160, 64, 128, 16] | MEDIUM |
| L1_ch80:96 | edge_convs.0.convs.1 | EdgeConv neighborhood/context relay over L0 features | [160, 64, 128, 16] | MEDIUM |
| L1_ch48:64 | edge_convs.0.convs.1 | EdgeConv neighborhood/context relay over L0 features | [160, 64, 128, 16] | MEDIUM |
| L2_ch128:160 | edge_convs.0.convs.2 | EdgeConv high-level aggregation before pooling/classifier | [160, 64, 128, 16] | MEDIUM |
| L2_ch224:256 | edge_convs.0.convs.2 | EdgeConv high-level aggregation before pooling/classifier | [160, 64, 128, 16] | MEDIUM |
| L2_ch0:32 | edge_convs.0.convs.2 | EdgeConv high-level aggregation before pooling/classifier | [160, 64, 128, 16] | MEDIUM |
| L2_ch64:96 | edge_convs.0.convs.2 | EdgeConv high-level aggregation before pooling/classifier | [160, 64, 128, 16] | MEDIUM |
| L2_ch160:192 | edge_convs.0.convs.2 | EdgeConv high-level aggregation before pooling/classifier | [160, 64, 128, 16] | MEDIUM |
| L2_ch32:64 | edge_convs.0.convs.2 | EdgeConv high-level aggregation before pooling/classifier | [160, 64, 128, 16] | MEDIUM |
| L2_ch192:224 | edge_convs.0.convs.2 | EdgeConv high-level aggregation before pooling/classifier | [160, 64, 128, 16] | MEDIUM |
| L2_ch96:128 | edge_convs.0.convs.2 | EdgeConv high-level aggregation before pooling/classifier | [160, 64, 128, 16] | MEDIUM |

## Interpretation

This file ties pseudocode to real code. Next improvement: exact sub-operation tracing inside EdgeConvBlock: knn indices, graph features, conv stack output, aggregation, and channel slicing.
