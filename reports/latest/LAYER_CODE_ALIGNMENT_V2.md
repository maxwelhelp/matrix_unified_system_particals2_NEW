# Layer Code Alignment v2

Corrected alignment: pseudo-heads map to EdgeConvBlock outputs, not inner conv sublayers.

## EdgeConv outputs
| module | input | output |
| --- | --- | --- |
| edge_convs.0 | [[160, 2, 128], [160, 13, 128]] | [160, 64, 128] |
| edge_convs.1 | [[160, 64, 128], [160, 64, 128]] | [160, 128, 128] |
| edge_convs.2 | [[160, 128, 128], [160, 128, 128]] | [160, 256, 128] |

## Pseudo-head alignment
| head | module | slice | operation | shape |
| --- | --- | --- | --- | --- |
| L0_ch40:48 | edge_convs.0 | output[:, 40:48, :] | EdgeConvBlock 0 output: local particle-edge feature map | [160, 64, 128] |
| L0_ch0:8 | edge_convs.0 | output[:, 0:8, :] | EdgeConvBlock 0 output: local particle-edge feature map | [160, 64, 128] |
| L0_ch48:56 | edge_convs.0 | output[:, 48:56, :] | EdgeConvBlock 0 output: local particle-edge feature map | [160, 64, 128] |
| L0_ch16:24 | edge_convs.0 | output[:, 16:24, :] | EdgeConvBlock 0 output: local particle-edge feature map | [160, 64, 128] |
| L0_ch24:32 | edge_convs.0 | output[:, 24:32, :] | EdgeConvBlock 0 output: local particle-edge feature map | [160, 64, 128] |
| L0_ch8:16 | edge_convs.0 | output[:, 8:16, :] | EdgeConvBlock 0 output: local particle-edge feature map | [160, 64, 128] |
| L0_ch56:64 | edge_convs.0 | output[:, 56:64, :] | EdgeConvBlock 0 output: local particle-edge feature map | [160, 64, 128] |
| L0_ch32:40 | edge_convs.0 | output[:, 32:40, :] | EdgeConvBlock 0 output: local particle-edge feature map | [160, 64, 128] |
| L1_ch16:32 | edge_convs.1 | output[:, 16:32, :] | EdgeConvBlock 1 output: neighborhood/context relay map | [160, 128, 128] |
| L1_ch32:48 | edge_convs.1 | output[:, 32:48, :] | EdgeConvBlock 1 output: neighborhood/context relay map | [160, 128, 128] |
| L1_ch112:128 | edge_convs.1 | output[:, 112:128, :] | EdgeConvBlock 1 output: neighborhood/context relay map | [160, 128, 128] |
| L1_ch0:16 | edge_convs.1 | output[:, 0:16, :] | EdgeConvBlock 1 output: neighborhood/context relay map | [160, 128, 128] |
| L1_ch96:112 | edge_convs.1 | output[:, 96:112, :] | EdgeConvBlock 1 output: neighborhood/context relay map | [160, 128, 128] |
| L1_ch64:80 | edge_convs.1 | output[:, 64:80, :] | EdgeConvBlock 1 output: neighborhood/context relay map | [160, 128, 128] |
| L1_ch80:96 | edge_convs.1 | output[:, 80:96, :] | EdgeConvBlock 1 output: neighborhood/context relay map | [160, 128, 128] |
| L1_ch48:64 | edge_convs.1 | output[:, 48:64, :] | EdgeConvBlock 1 output: neighborhood/context relay map | [160, 128, 128] |
| L2_ch128:160 | edge_convs.2 | output[:, 128:160, :] | EdgeConvBlock 2 output: high-level class-evidence map before pooling | [160, 256, 128] |
| L2_ch224:256 | edge_convs.2 | output[:, 224:256, :] | EdgeConvBlock 2 output: high-level class-evidence map before pooling | [160, 256, 128] |
| L2_ch0:32 | edge_convs.2 | output[:, 0:32, :] | EdgeConvBlock 2 output: high-level class-evidence map before pooling | [160, 256, 128] |
| L2_ch64:96 | edge_convs.2 | output[:, 64:96, :] | EdgeConvBlock 2 output: high-level class-evidence map before pooling | [160, 256, 128] |
| L2_ch160:192 | edge_convs.2 | output[:, 160:192, :] | EdgeConvBlock 2 output: high-level class-evidence map before pooling | [160, 256, 128] |
| L2_ch32:64 | edge_convs.2 | output[:, 32:64, :] | EdgeConvBlock 2 output: high-level class-evidence map before pooling | [160, 256, 128] |
| L2_ch192:224 | edge_convs.2 | output[:, 192:224, :] | EdgeConvBlock 2 output: high-level class-evidence map before pooling | [160, 256, 128] |
| L2_ch96:128 | edge_convs.2 | output[:, 96:128, :] | EdgeConvBlock 2 output: high-level class-evidence map before pooling | [160, 256, 128] |
