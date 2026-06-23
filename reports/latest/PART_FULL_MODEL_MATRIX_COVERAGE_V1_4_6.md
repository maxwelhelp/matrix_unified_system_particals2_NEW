# PART_FULL_MODEL_MATRIX_COVERAGE_V1_4_6

STATUS: **FULL_MODEL_MATRIX_COVERAGE_CLOSED**
FULL_FORWARD_STATUS: **FULL_FORWARD_NOT_CLOSED**
NOTE: full forward replay is separate Stage 2.

- version: **1.4.6**
- run_ok: **True**
- stage1_ok / matrix coverage: **True**
- full_forward_ok: **False**
- all_named_parameters_covered: **True**
- uncovered_named_parameters: **0**
- final_reason: `generic decoded Python graph replay not implemented; structural containers/control flow not claimed`

## Gates

- uncovered_parameterized: `0`
- structural_not_traced: `8`
- rejected_modules: `0`
- rejected_heads: `0`
- attention_heads: `80`
- accepted_attention_heads: `80`
- linear_modules: `24`
- accepted_linear_modules: `24`
- dynamic_modules: `77`
- accepted_dynamic_modules: `77`
- decoder_kind_counts: `{'STRUCTURAL_NOT_EXPLICITLY_TRACED': 8, 'UNCOVERED': 21, 'STRUCTURAL_EXACT': 21, 'EXACT_DYNAMIC_OPERATOR': 60, 'EXACT_CONSTANT_MATRIX': 24, 'EXACT_ELEMENTWISE_FORMULA': 17, 'EXACT_CONSTANT_CONVOLUTION': 4}`
- primitive_fit_summary: `{'total': 188, 'strong': 7, 'partial': 5, 'weak': 176, 'target_mined_used': 162}`
- shared_primitives: `{'count': 0, 'accepted': 0, 'info': {'candidates': 486, 'clusters': 0, 'shape_groups': {'64x64': 6, '128x128': 480}, 'skipped_shape_groups': {}, 'skipped_records': 0, 'heldout_gate': 'real_base_plus_shared_decode_gain_grouped_by_shape', 'gain_threshold': 0.02, 'decode_gain_threshold': 0.01}}`

## Honesty rules

- `stage1_ok=True` means matrix parameter coverage is closed. `FULL_FORWARD_CLOSED` is separate Stage 2 and is not claimed here.
- SVD is compression/pattern fit, not trusted primitive interpretation.
- Target-mined atoms are target-specific until shared/heldout gate accepts them.
- Containers are `STRUCTURAL_NOT_EXPLICITLY_TRACED`, not silently accepted.
- Pair-bias tensor fit is approximate unless exact producing module is decoded.

## Uncovered parameterized modules

_No uncovered direct-parameter modules._

## Rejected decoded modules

_No rejected decoded modules._

## Structural not explicitly traced

| module | type | reason |
| --- | --- | --- |
| `<root>` | `ParticleTransformerWrapper` | `container_or_python_forward_not_replayed` |
| `mod` | `ParticleTransformer` | `direct_parameters_covered_but_container_graph_not_replayed` |
| `mod.embed` | `Embed` | `container_or_python_forward_not_replayed` |
| `mod.embed.embed` | `Sequential` | `container_or_python_forward_not_replayed` |
| `mod.pair_embed` | `PairEmbed` | `container_or_python_forward_not_replayed` |
| `mod.pair_embed.embed` | `Sequential` | `container_or_python_forward_not_replayed` |
| `mod.blocks` | `ModuleList` | `container_or_python_forward_not_replayed` |
| `mod.blocks.0` | `Block` | `direct_parameters_covered_but_container_graph_not_replayed` |
| `mod.blocks.1` | `Block` | `direct_parameters_covered_but_container_graph_not_replayed` |
| `mod.blocks.2` | `Block` | `direct_parameters_covered_but_container_graph_not_replayed` |
| `mod.blocks.3` | `Block` | `direct_parameters_covered_but_container_graph_not_replayed` |
| `mod.blocks.4` | `Block` | `direct_parameters_covered_but_container_graph_not_replayed` |
| `mod.blocks.5` | `Block` | `direct_parameters_covered_but_container_graph_not_replayed` |
| `mod.blocks.6` | `Block` | `direct_parameters_covered_but_container_graph_not_replayed` |
| `mod.blocks.7` | `Block` | `direct_parameters_covered_but_container_graph_not_replayed` |
| `mod.cls_blocks` | `ModuleList` | `container_or_python_forward_not_replayed` |
| `mod.cls_blocks.0` | `Block` | `direct_parameters_covered_but_container_graph_not_replayed` |
| `mod.cls_blocks.1` | `Block` | `direct_parameters_covered_but_container_graph_not_replayed` |
| `mod.fc` | `Sequential` | `container_or_python_forward_not_replayed` |

## Attention head sample

| head | accept | full_out | qk | vo | qk_fit | qk_quality | mined | pair_bias_trusted |
| --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- |
| `mod.blocks.0.attn.h0` | True | 2.259e-07 | 4.731e-07 | 2.393e-07 | 0.531626 | `PRIMITIVE_EXPLANATION_WEAK` | True | False |
| `mod.blocks.0.attn.h1` | True | 2.259e-07 | 3.030e-07 | 3.239e-07 | 0.449257 | `PRIMITIVE_EXPLANATION_WEAK` | True | False |
| `mod.blocks.0.attn.h2` | True | 2.259e-07 | 2.593e-07 | 1.755e-07 | 0.395921 | `PRIMITIVE_EXPLANATION_WEAK` | True | True |
| `mod.blocks.0.attn.h3` | True | 2.259e-07 | 3.223e-07 | 2.705e-07 | 0.507036 | `PRIMITIVE_EXPLANATION_WEAK` | True | False |
| `mod.blocks.0.attn.h4` | True | 2.259e-07 | 4.278e-07 | 2.131e-07 | 0.558270 | `PRIMITIVE_EXPLANATION_WEAK` | True | False |
| `mod.blocks.0.attn.h5` | True | 2.259e-07 | 3.664e-07 | 2.198e-07 | 0.553793 | `PRIMITIVE_EXPLANATION_WEAK` | True | False |
| `mod.blocks.0.attn.h6` | True | 2.259e-07 | 3.207e-07 | 2.378e-07 | 0.553038 | `PRIMITIVE_EXPLANATION_WEAK` | True | True |
| `mod.blocks.0.attn.h7` | True | 2.259e-07 | 3.262e-07 | 2.806e-07 | 0.541808 | `PRIMITIVE_EXPLANATION_WEAK` | True | False |
| `mod.blocks.1.attn.h0` | True | 3.088e-07 | 3.639e-07 | 3.104e-07 | 0.671886 | `PRIMITIVE_EXPLANATION_WEAK` | True | False |
| `mod.blocks.1.attn.h1` | True | 3.088e-07 | 3.368e-07 | 2.878e-07 | 0.579671 | `PRIMITIVE_EXPLANATION_WEAK` | True | False |
| `mod.blocks.1.attn.h2` | True | 3.088e-07 | 3.569e-07 | 3.036e-07 | 0.690933 | `PRIMITIVE_EXPLANATION_WEAK` | True | True |
| `mod.blocks.1.attn.h3` | True | 3.088e-07 | 3.599e-07 | 2.474e-07 | 0.655098 | `PRIMITIVE_EXPLANATION_WEAK` | True | False |
| `mod.blocks.1.attn.h4` | True | 3.088e-07 | 3.195e-07 | 2.390e-07 | 0.590134 | `PRIMITIVE_EXPLANATION_WEAK` | True | False |
| `mod.blocks.1.attn.h5` | True | 3.088e-07 | 3.998e-07 | 2.989e-07 | 0.707194 | `PRIMITIVE_EXPLANATION_WEAK` | True | False |
| `mod.blocks.1.attn.h6` | True | 3.088e-07 | 3.888e-07 | 2.498e-07 | 0.709502 | `PRIMITIVE_EXPLANATION_WEAK` | True | True |
| `mod.blocks.1.attn.h7` | True | 3.088e-07 | 3.563e-07 | 2.991e-07 | 0.530329 | `PRIMITIVE_EXPLANATION_WEAK` | True | False |
| `mod.blocks.2.attn.h0` | True | 3.611e-07 | 4.135e-07 | 2.888e-07 | 0.704671 | `PRIMITIVE_EXPLANATION_WEAK` | True | False |
| `mod.blocks.2.attn.h1` | True | 3.611e-07 | 3.952e-07 | 3.199e-07 | 0.546014 | `PRIMITIVE_EXPLANATION_WEAK` | True | False |
| `mod.blocks.2.attn.h2` | True | 3.611e-07 | 4.083e-07 | 2.670e-07 | 0.709115 | `PRIMITIVE_EXPLANATION_WEAK` | True | True |
| `mod.blocks.2.attn.h3` | True | 3.611e-07 | 3.953e-07 | 2.863e-07 | 0.712164 | `PRIMITIVE_EXPLANATION_WEAK` | True | False |
| `mod.blocks.2.attn.h4` | True | 3.611e-07 | 3.871e-07 | 2.624e-07 | 0.603944 | `PRIMITIVE_EXPLANATION_WEAK` | True | False |
| `mod.blocks.2.attn.h5` | True | 3.611e-07 | 4.119e-07 | 2.713e-07 | 0.718034 | `PRIMITIVE_EXPLANATION_WEAK` | True | False |
| `mod.blocks.2.attn.h6` | True | 3.611e-07 | 3.745e-07 | 2.345e-07 | 0.720539 | `PRIMITIVE_EXPLANATION_WEAK` | True | True |
| `mod.blocks.2.attn.h7` | True | 3.611e-07 | 3.177e-07 | 3.076e-07 | 0.607547 | `PRIMITIVE_EXPLANATION_WEAK` | True | False |
| `mod.blocks.3.attn.h0` | True | 3.485e-07 | 4.160e-07 | 2.672e-07 | 0.689765 | `PRIMITIVE_EXPLANATION_WEAK` | True | False |
| `mod.blocks.3.attn.h1` | True | 3.485e-07 | 3.469e-07 | 3.487e-07 | 0.635550 | `PRIMITIVE_EXPLANATION_WEAK` | True | False |
| `mod.blocks.3.attn.h2` | True | 3.485e-07 | 4.212e-07 | 2.257e-07 | 0.732328 | `PRIMITIVE_EXPLANATION_WEAK` | True | True |
| `mod.blocks.3.attn.h3` | True | 3.485e-07 | 4.211e-07 | 2.744e-07 | 0.687763 | `PRIMITIVE_EXPLANATION_WEAK` | True | False |
| `mod.blocks.3.attn.h4` | True | 3.485e-07 | 3.768e-07 | 3.069e-07 | 0.635576 | `PRIMITIVE_EXPLANATION_WEAK` | True | False |
| `mod.blocks.3.attn.h5` | True | 3.485e-07 | 4.203e-07 | 3.055e-07 | 0.706500 | `PRIMITIVE_EXPLANATION_WEAK` | True | False |
| `mod.blocks.3.attn.h6` | True | 3.485e-07 | 4.066e-07 | 2.549e-07 | 0.696538 | `PRIMITIVE_EXPLANATION_WEAK` | True | True |
| `mod.blocks.3.attn.h7` | True | 3.485e-07 | 3.786e-07 | 3.079e-07 | 0.662777 | `PRIMITIVE_EXPLANATION_WEAK` | True | False |
| `mod.blocks.4.attn.h0` | True | 3.474e-07 | 4.091e-07 | 2.881e-07 | 0.709229 | `PRIMITIVE_EXPLANATION_WEAK` | True | False |
| `mod.blocks.4.attn.h1` | True | 3.474e-07 | 3.713e-07 | 3.334e-07 | 0.702096 | `PRIMITIVE_EXPLANATION_WEAK` | True | False |
| `mod.blocks.4.attn.h2` | True | 3.474e-07 | 4.256e-07 | 2.751e-07 | 0.725306 | `PRIMITIVE_EXPLANATION_WEAK` | True | True |
| `mod.blocks.4.attn.h3` | True | 3.474e-07 | 3.352e-07 | 3.028e-07 | 0.616791 | `PRIMITIVE_EXPLANATION_WEAK` | True | False |
| `mod.blocks.4.attn.h4` | True | 3.474e-07 | 2.818e-07 | 3.251e-07 | 0.547912 | `PRIMITIVE_EXPLANATION_WEAK` | True | False |
| `mod.blocks.4.attn.h5` | True | 3.474e-07 | 3.738e-07 | 2.691e-07 | 0.745083 | `PRIMITIVE_EXPLANATION_WEAK` | True | False |
| `mod.blocks.4.attn.h6` | True | 3.474e-07 | 3.916e-07 | 2.747e-07 | 0.707566 | `PRIMITIVE_EXPLANATION_WEAK` | True | True |
| `mod.blocks.4.attn.h7` | True | 3.474e-07 | 3.919e-07 | 3.338e-07 | 0.534562 | `PRIMITIVE_EXPLANATION_WEAK` | True | False |
| `mod.blocks.5.attn.h0` | True | 3.203e-07 | 4.274e-07 | 2.863e-07 | 0.654512 | `PRIMITIVE_EXPLANATION_WEAK` | True | False |
| `mod.blocks.5.attn.h1` | True | 3.203e-07 | 3.523e-07 | 3.091e-07 | 0.609232 | `PRIMITIVE_EXPLANATION_WEAK` | True | False |
| `mod.blocks.5.attn.h2` | True | 3.203e-07 | 3.747e-07 | 3.178e-07 | 0.711522 | `PRIMITIVE_EXPLANATION_WEAK` | True | True |
| `mod.blocks.5.attn.h3` | True | 3.203e-07 | 3.735e-07 | 2.912e-07 | 0.667556 | `PRIMITIVE_EXPLANATION_WEAK` | True | False |
| `mod.blocks.5.attn.h4` | True | 3.203e-07 | 3.875e-07 | 3.582e-07 | 0.597021 | `PRIMITIVE_EXPLANATION_WEAK` | True | False |
| `mod.blocks.5.attn.h5` | True | 3.203e-07 | 4.039e-07 | 2.861e-07 | 0.728491 | `PRIMITIVE_EXPLANATION_WEAK` | True | False |
| `mod.blocks.5.attn.h6` | True | 3.203e-07 | 3.729e-07 | 2.464e-07 | 0.660047 | `PRIMITIVE_EXPLANATION_WEAK` | True | True |
| `mod.blocks.5.attn.h7` | True | 3.203e-07 | 3.630e-07 | 2.736e-07 | 0.640743 | `PRIMITIVE_EXPLANATION_WEAK` | True | False |
| `mod.blocks.6.attn.h0` | True | 3.235e-07 | 4.206e-07 | 2.749e-07 | 0.627761 | `PRIMITIVE_EXPLANATION_WEAK` | True | False |
| `mod.blocks.6.attn.h1` | True | 3.235e-07 | 4.014e-07 | 3.044e-07 | 0.684686 | `PRIMITIVE_EXPLANATION_WEAK` | True | False |
| `mod.blocks.6.attn.h2` | True | 3.235e-07 | 4.172e-07 | 2.401e-07 | 0.724101 | `PRIMITIVE_EXPLANATION_WEAK` | True | True |
| `mod.blocks.6.attn.h3` | True | 3.235e-07 | 3.965e-07 | 3.087e-07 | 0.649079 | `PRIMITIVE_EXPLANATION_WEAK` | True | False |
| `mod.blocks.6.attn.h4` | True | 3.235e-07 | 3.910e-07 | 3.104e-07 | 0.672295 | `PRIMITIVE_EXPLANATION_WEAK` | True | False |
| `mod.blocks.6.attn.h5` | True | 3.235e-07 | 4.217e-07 | 2.581e-07 | 0.729751 | `PRIMITIVE_EXPLANATION_WEAK` | True | False |
| `mod.blocks.6.attn.h6` | True | 3.235e-07 | 4.329e-07 | 2.790e-07 | 0.722636 | `PRIMITIVE_EXPLANATION_WEAK` | True | True |
| `mod.blocks.6.attn.h7` | True | 3.235e-07 | 3.520e-07 | 2.653e-07 | 0.704414 | `PRIMITIVE_EXPLANATION_WEAK` | True | False |
| `mod.blocks.7.attn.h0` | True | 2.863e-07 | 4.172e-07 | 2.900e-07 | 0.716021 | `PRIMITIVE_EXPLANATION_WEAK` | True | False |
| `mod.blocks.7.attn.h1` | True | 2.863e-07 | 4.033e-07 | 3.226e-07 | 0.684334 | `PRIMITIVE_EXPLANATION_WEAK` | True | False |
| `mod.blocks.7.attn.h2` | True | 2.863e-07 | 4.239e-07 | 2.491e-07 | 0.691135 | `PRIMITIVE_EXPLANATION_WEAK` | True | True |
| `mod.blocks.7.attn.h3` | True | 2.863e-07 | 3.385e-07 | 2.783e-07 | 0.639061 | `PRIMITIVE_EXPLANATION_WEAK` | True | False |
| `mod.blocks.7.attn.h4` | True | 2.863e-07 | 3.086e-07 | 3.544e-07 | 0.580699 | `PRIMITIVE_EXPLANATION_WEAK` | True | False |
| `mod.blocks.7.attn.h5` | True | 2.863e-07 | 3.567e-07 | 2.507e-07 | 0.674484 | `PRIMITIVE_EXPLANATION_WEAK` | True | False |
| `mod.blocks.7.attn.h6` | True | 2.863e-07 | 4.664e-07 | 2.510e-07 | 0.693010 | `PRIMITIVE_EXPLANATION_WEAK` | True | True |
| `mod.blocks.7.attn.h7` | True | 2.863e-07 | 3.842e-07 | 2.651e-07 | 0.682027 | `PRIMITIVE_EXPLANATION_WEAK` | True | False |
| `mod.cls_blocks.0.attn.h0` | True | 1.776e-07 | 2.208e-07 | 1.799e-07 | 0.174555 | `PARTIAL_INTERPRETATION` | True | False |
| `mod.cls_blocks.0.attn.h1` | True | 1.776e-07 | 2.400e-07 | 2.476e-07 | 0.228634 | `PARTIAL_INTERPRETATION` | True | False |
| `mod.cls_blocks.0.attn.h2` | True | 1.776e-07 | 3.833e-07 | 1.485e-07 | 0.088454 | `STRONG_INTERPRETATION` | True | False |
| `mod.cls_blocks.0.attn.h3` | True | 1.776e-07 | 1.924e-07 | 1.789e-07 | 0.110164 | `STRONG_INTERPRETATION` | True | False |
| `mod.cls_blocks.0.attn.h4` | True | 1.776e-07 | 2.426e-07 | 3.489e-07 | 0.131078 | `STRONG_INTERPRETATION` | True | False |
| `mod.cls_blocks.0.attn.h5` | True | 1.776e-07 | 2.858e-07 | 1.697e-07 | 0.159268 | `PARTIAL_INTERPRETATION` | True | False |
| `mod.cls_blocks.0.attn.h6` | True | 1.776e-07 | 2.149e-07 | 3.774e-07 | 0.156801 | `PARTIAL_INTERPRETATION` | True | False |
| `mod.cls_blocks.0.attn.h7` | True | 1.776e-07 | 2.487e-07 | 1.982e-07 | 0.176122 | `PARTIAL_INTERPRETATION` | True | False |
| `mod.cls_blocks.1.attn.h0` | True | 1.271e-07 | 3.245e-07 | 2.379e-07 | 0.639100 | `PRIMITIVE_EXPLANATION_WEAK` | True | False |
| `mod.cls_blocks.1.attn.h1` | True | 1.271e-07 | 2.365e-07 | 2.271e-07 | 0.634460 | `PRIMITIVE_EXPLANATION_WEAK` | True | False |
| `mod.cls_blocks.1.attn.h2` | True | 1.271e-07 | 2.614e-07 | 1.740e-07 | 0.664013 | `PRIMITIVE_EXPLANATION_WEAK` | True | False |
| `mod.cls_blocks.1.attn.h3` | True | 1.271e-07 | 1.466e-07 | 2.708e-07 | 0.601674 | `PRIMITIVE_EXPLANATION_WEAK` | True | False |
| `mod.cls_blocks.1.attn.h4` | True | 1.271e-07 | 2.408e-07 | 2.012e-07 | 0.611815 | `PRIMITIVE_EXPLANATION_WEAK` | True | False |
| `mod.cls_blocks.1.attn.h5` | True | 1.271e-07 | 2.598e-07 | 1.816e-07 | 0.632724 | `PRIMITIVE_EXPLANATION_WEAK` | True | False |
| `mod.cls_blocks.1.attn.h6` | True | 1.271e-07 | 1.382e-07 | 3.775e-07 | 0.624063 | `PRIMITIVE_EXPLANATION_WEAK` | True | False |
| `mod.cls_blocks.1.attn.h7` | True | 1.271e-07 | 2.925e-07 | 2.799e-07 | 0.637388 | `PRIMITIVE_EXPLANATION_WEAK` | True | False |

## Primitive fit sample

| record | target | fit_kind | err | quality | target_mined | note |
| --- | --- | --- | ---: | --- | --- | --- |
| `mod.embed.embed.1.LinearW` | `linear` | `APPROX_PATTERN_FIT_RECTANGULAR_SVD` | 0.102918 | `STRONG_INTERPRETATION` | False | `SVD is compression/pattern fit, not human primitive interpretation.` |
| `mod.embed.embed.4.LinearW` | `linear` | `APPROX_PATTERN_FIT_RECTANGULAR_SVD` | 0.521782 | `PRIMITIVE_EXPLANATION_WEAK` | False | `SVD is compression/pattern fit, not human primitive interpretation.` |
| `mod.embed.embed.7.LinearW` | `linear` | `APPROX_PATTERN_FIT_RECTANGULAR_SVD` | 0.682997 | `PRIMITIVE_EXPLANATION_WEAK` | False | `SVD is compression/pattern fit, not human primitive interpretation.` |
| `mod.pair_embed.embed.1.Conv1dW` | `conv1d` | `APPROX_PATTERN_FIT_RECTANGULAR_SVD` | 3.432e-07 | `STRONG_INTERPRETATION` | False | `SVD is compression/pattern fit, not human primitive interpretation.` |
| `mod.pair_embed.embed.4.Conv1dW` | `conv1d` | `SPARSE_OMP_BASE_PLUS_TARGET_MINED` | 0.637816 | `PRIMITIVE_EXPLANATION_WEAK` | True | `Target-mined atoms are target-specific. Not shared physics unless shared/heldout gate accepts.` |
| `mod.pair_embed.embed.7.Conv1dW` | `conv1d` | `SPARSE_OMP_BASE_PLUS_TARGET_MINED` | 0.736693 | `PRIMITIVE_EXPLANATION_WEAK` | True | `Target-mined atoms are target-specific. Not shared physics unless shared/heldout gate accepts.` |
| `mod.pair_embed.embed.10.Conv1dW` | `conv1d` | `APPROX_PATTERN_FIT_RECTANGULAR_SVD` | 6.305e-07 | `STRONG_INTERPRETATION` | False | `SVD is compression/pattern fit, not human primitive interpretation.` |
| `mod.blocks.0.attn.h0.attention_qk` | `attention_qk` | `SPARSE_OMP_BASE_PLUS_TARGET_MINED` | 0.531626 | `PRIMITIVE_EXPLANATION_WEAK` | True | `Target-mined atoms are target-specific. Not shared physics unless shared/heldout gate accepts.` |
| `mod.blocks.0.attn.h0.attention_vo` | `attention_vo` | `SPARSE_OMP_BASE_PLUS_TARGET_MINED` | 0.595097 | `PRIMITIVE_EXPLANATION_WEAK` | True | `Target-mined atoms are target-specific. Not shared physics unless shared/heldout gate accepts.` |
| `mod.blocks.0.attn.h1.attention_qk` | `attention_qk` | `SPARSE_OMP_BASE_PLUS_TARGET_MINED` | 0.449257 | `PRIMITIVE_EXPLANATION_WEAK` | True | `Target-mined atoms are target-specific. Not shared physics unless shared/heldout gate accepts.` |
| `mod.blocks.0.attn.h1.attention_vo` | `attention_vo` | `SPARSE_OMP_BASE_PLUS_TARGET_MINED` | 0.514830 | `PRIMITIVE_EXPLANATION_WEAK` | True | `Target-mined atoms are target-specific. Not shared physics unless shared/heldout gate accepts.` |
| `mod.blocks.0.attn.h2.attention_qk` | `attention_qk` | `SPARSE_OMP_BASE_PLUS_TARGET_MINED` | 0.395921 | `PRIMITIVE_EXPLANATION_WEAK` | True | `Target-mined atoms are target-specific. Not shared physics unless shared/heldout gate accepts.` |
| `mod.blocks.0.attn.h2.attention_vo` | `attention_vo` | `SPARSE_OMP_BASE_PLUS_TARGET_MINED` | 0.600079 | `PRIMITIVE_EXPLANATION_WEAK` | True | `Target-mined atoms are target-specific. Not shared physics unless shared/heldout gate accepts.` |
| `mod.blocks.0.attn.h3.attention_qk` | `attention_qk` | `SPARSE_OMP_BASE_PLUS_TARGET_MINED` | 0.507036 | `PRIMITIVE_EXPLANATION_WEAK` | True | `Target-mined atoms are target-specific. Not shared physics unless shared/heldout gate accepts.` |
| `mod.blocks.0.attn.h3.attention_vo` | `attention_vo` | `SPARSE_OMP_BASE_PLUS_TARGET_MINED` | 0.492277 | `PRIMITIVE_EXPLANATION_WEAK` | True | `Target-mined atoms are target-specific. Not shared physics unless shared/heldout gate accepts.` |
| `mod.blocks.0.attn.h4.attention_qk` | `attention_qk` | `SPARSE_OMP_BASE_PLUS_TARGET_MINED` | 0.558270 | `PRIMITIVE_EXPLANATION_WEAK` | True | `Target-mined atoms are target-specific. Not shared physics unless shared/heldout gate accepts.` |
| `mod.blocks.0.attn.h4.attention_vo` | `attention_vo` | `SPARSE_OMP_BASE_PLUS_TARGET_MINED` | 0.470937 | `PRIMITIVE_EXPLANATION_WEAK` | True | `Target-mined atoms are target-specific. Not shared physics unless shared/heldout gate accepts.` |
| `mod.blocks.0.attn.h5.attention_qk` | `attention_qk` | `SPARSE_OMP_BASE_PLUS_TARGET_MINED` | 0.553793 | `PRIMITIVE_EXPLANATION_WEAK` | True | `Target-mined atoms are target-specific. Not shared physics unless shared/heldout gate accepts.` |
| `mod.blocks.0.attn.h5.attention_vo` | `attention_vo` | `SPARSE_OMP_BASE_PLUS_TARGET_MINED` | 0.587242 | `PRIMITIVE_EXPLANATION_WEAK` | True | `Target-mined atoms are target-specific. Not shared physics unless shared/heldout gate accepts.` |
| `mod.blocks.0.attn.h6.attention_qk` | `attention_qk` | `SPARSE_OMP_BASE_PLUS_TARGET_MINED` | 0.553038 | `PRIMITIVE_EXPLANATION_WEAK` | True | `Target-mined atoms are target-specific. Not shared physics unless shared/heldout gate accepts.` |
| `mod.blocks.0.attn.h6.attention_vo` | `attention_vo` | `SPARSE_OMP_BASE_PLUS_TARGET_MINED` | 0.622893 | `PRIMITIVE_EXPLANATION_WEAK` | True | `Target-mined atoms are target-specific. Not shared physics unless shared/heldout gate accepts.` |
| `mod.blocks.0.attn.h7.attention_qk` | `attention_qk` | `SPARSE_OMP_BASE_PLUS_TARGET_MINED` | 0.541808 | `PRIMITIVE_EXPLANATION_WEAK` | True | `Target-mined atoms are target-specific. Not shared physics unless shared/heldout gate accepts.` |
| `mod.blocks.0.attn.h7.attention_vo` | `attention_vo` | `SPARSE_OMP_BASE_PLUS_TARGET_MINED` | 0.554075 | `PRIMITIVE_EXPLANATION_WEAK` | True | `Target-mined atoms are target-specific. Not shared physics unless shared/heldout gate accepts.` |
| `mod.blocks.0.fc1.LinearW` | `linear` | `APPROX_PATTERN_FIT_RECTANGULAR_SVD` | 0.770774 | `PRIMITIVE_EXPLANATION_WEAK` | False | `SVD is compression/pattern fit, not human primitive interpretation.` |
| `mod.blocks.0.fc2.LinearW` | `linear` | `APPROX_PATTERN_FIT_RECTANGULAR_SVD` | 0.827870 | `PRIMITIVE_EXPLANATION_WEAK` | False | `SVD is compression/pattern fit, not human primitive interpretation.` |
| `mod.blocks.1.attn.h0.attention_qk` | `attention_qk` | `SPARSE_OMP_BASE_PLUS_TARGET_MINED` | 0.671886 | `PRIMITIVE_EXPLANATION_WEAK` | True | `Target-mined atoms are target-specific. Not shared physics unless shared/heldout gate accepts.` |
| `mod.blocks.1.attn.h0.attention_vo` | `attention_vo` | `SPARSE_OMP_BASE_PLUS_TARGET_MINED` | 0.651938 | `PRIMITIVE_EXPLANATION_WEAK` | True | `Target-mined atoms are target-specific. Not shared physics unless shared/heldout gate accepts.` |
| `mod.blocks.1.attn.h1.attention_qk` | `attention_qk` | `SPARSE_OMP_BASE_PLUS_TARGET_MINED` | 0.579671 | `PRIMITIVE_EXPLANATION_WEAK` | True | `Target-mined atoms are target-specific. Not shared physics unless shared/heldout gate accepts.` |
| `mod.blocks.1.attn.h1.attention_vo` | `attention_vo` | `SPARSE_OMP_BASE_PLUS_TARGET_MINED` | 0.569195 | `PRIMITIVE_EXPLANATION_WEAK` | True | `Target-mined atoms are target-specific. Not shared physics unless shared/heldout gate accepts.` |
| `mod.blocks.1.attn.h2.attention_qk` | `attention_qk` | `SPARSE_OMP_BASE_PLUS_TARGET_MINED` | 0.690933 | `PRIMITIVE_EXPLANATION_WEAK` | True | `Target-mined atoms are target-specific. Not shared physics unless shared/heldout gate accepts.` |
| `mod.blocks.1.attn.h2.attention_vo` | `attention_vo` | `SPARSE_OMP_BASE_PLUS_TARGET_MINED` | 0.640776 | `PRIMITIVE_EXPLANATION_WEAK` | True | `Target-mined atoms are target-specific. Not shared physics unless shared/heldout gate accepts.` |
| `mod.blocks.1.attn.h3.attention_qk` | `attention_qk` | `SPARSE_OMP_BASE_PLUS_TARGET_MINED` | 0.655098 | `PRIMITIVE_EXPLANATION_WEAK` | True | `Target-mined atoms are target-specific. Not shared physics unless shared/heldout gate accepts.` |
| `mod.blocks.1.attn.h3.attention_vo` | `attention_vo` | `SPARSE_OMP_BASE_PLUS_TARGET_MINED` | 0.562940 | `PRIMITIVE_EXPLANATION_WEAK` | True | `Target-mined atoms are target-specific. Not shared physics unless shared/heldout gate accepts.` |
| `mod.blocks.1.attn.h4.attention_qk` | `attention_qk` | `SPARSE_OMP_BASE_PLUS_TARGET_MINED` | 0.590134 | `PRIMITIVE_EXPLANATION_WEAK` | True | `Target-mined atoms are target-specific. Not shared physics unless shared/heldout gate accepts.` |
| `mod.blocks.1.attn.h4.attention_vo` | `attention_vo` | `SPARSE_OMP_BASE_PLUS_TARGET_MINED` | 0.562734 | `PRIMITIVE_EXPLANATION_WEAK` | True | `Target-mined atoms are target-specific. Not shared physics unless shared/heldout gate accepts.` |
| `mod.blocks.1.attn.h5.attention_qk` | `attention_qk` | `SPARSE_OMP_BASE_PLUS_TARGET_MINED` | 0.707194 | `PRIMITIVE_EXPLANATION_WEAK` | True | `Target-mined atoms are target-specific. Not shared physics unless shared/heldout gate accepts.` |
| `mod.blocks.1.attn.h5.attention_vo` | `attention_vo` | `SPARSE_OMP_BASE_PLUS_TARGET_MINED` | 0.639359 | `PRIMITIVE_EXPLANATION_WEAK` | True | `Target-mined atoms are target-specific. Not shared physics unless shared/heldout gate accepts.` |
| `mod.blocks.1.attn.h6.attention_qk` | `attention_qk` | `SPARSE_OMP_BASE_PLUS_TARGET_MINED` | 0.709502 | `PRIMITIVE_EXPLANATION_WEAK` | True | `Target-mined atoms are target-specific. Not shared physics unless shared/heldout gate accepts.` |
| `mod.blocks.1.attn.h6.attention_vo` | `attention_vo` | `SPARSE_OMP_BASE_PLUS_TARGET_MINED` | 0.635674 | `PRIMITIVE_EXPLANATION_WEAK` | True | `Target-mined atoms are target-specific. Not shared physics unless shared/heldout gate accepts.` |
| `mod.blocks.1.attn.h7.attention_qk` | `attention_qk` | `SPARSE_OMP_BASE_PLUS_TARGET_MINED` | 0.530329 | `PRIMITIVE_EXPLANATION_WEAK` | True | `Target-mined atoms are target-specific. Not shared physics unless shared/heldout gate accepts.` |
| `mod.blocks.1.attn.h7.attention_vo` | `attention_vo` | `SPARSE_OMP_BASE_PLUS_TARGET_MINED` | 0.608103 | `PRIMITIVE_EXPLANATION_WEAK` | True | `Target-mined atoms are target-specific. Not shared physics unless shared/heldout gate accepts.` |
| `mod.blocks.1.fc1.LinearW` | `linear` | `APPROX_PATTERN_FIT_RECTANGULAR_SVD` | 0.787290 | `PRIMITIVE_EXPLANATION_WEAK` | False | `SVD is compression/pattern fit, not human primitive interpretation.` |
| `mod.blocks.1.fc2.LinearW` | `linear` | `APPROX_PATTERN_FIT_RECTANGULAR_SVD` | 0.838494 | `PRIMITIVE_EXPLANATION_WEAK` | False | `SVD is compression/pattern fit, not human primitive interpretation.` |
| `mod.blocks.2.attn.h0.attention_qk` | `attention_qk` | `SPARSE_OMP_BASE_PLUS_TARGET_MINED` | 0.704671 | `PRIMITIVE_EXPLANATION_WEAK` | True | `Target-mined atoms are target-specific. Not shared physics unless shared/heldout gate accepts.` |
| `mod.blocks.2.attn.h0.attention_vo` | `attention_vo` | `SPARSE_OMP_BASE_PLUS_TARGET_MINED` | 0.693236 | `PRIMITIVE_EXPLANATION_WEAK` | True | `Target-mined atoms are target-specific. Not shared physics unless shared/heldout gate accepts.` |
| `mod.blocks.2.attn.h1.attention_qk` | `attention_qk` | `SPARSE_OMP_BASE_PLUS_TARGET_MINED` | 0.546014 | `PRIMITIVE_EXPLANATION_WEAK` | True | `Target-mined atoms are target-specific. Not shared physics unless shared/heldout gate accepts.` |
| `mod.blocks.2.attn.h1.attention_vo` | `attention_vo` | `SPARSE_OMP_BASE_PLUS_TARGET_MINED` | 0.581967 | `PRIMITIVE_EXPLANATION_WEAK` | True | `Target-mined atoms are target-specific. Not shared physics unless shared/heldout gate accepts.` |
| `mod.blocks.2.attn.h2.attention_qk` | `attention_qk` | `SPARSE_OMP_BASE_PLUS_TARGET_MINED` | 0.709115 | `PRIMITIVE_EXPLANATION_WEAK` | True | `Target-mined atoms are target-specific. Not shared physics unless shared/heldout gate accepts.` |
| `mod.blocks.2.attn.h2.attention_vo` | `attention_vo` | `SPARSE_OMP_BASE_PLUS_TARGET_MINED` | 0.667877 | `PRIMITIVE_EXPLANATION_WEAK` | True | `Target-mined atoms are target-specific. Not shared physics unless shared/heldout gate accepts.` |
| `mod.blocks.2.attn.h3.attention_qk` | `attention_qk` | `SPARSE_OMP_BASE_PLUS_TARGET_MINED` | 0.712164 | `PRIMITIVE_EXPLANATION_WEAK` | True | `Target-mined atoms are target-specific. Not shared physics unless shared/heldout gate accepts.` |
| `mod.blocks.2.attn.h3.attention_vo` | `attention_vo` | `SPARSE_OMP_BASE_PLUS_TARGET_MINED` | 0.638150 | `PRIMITIVE_EXPLANATION_WEAK` | True | `Target-mined atoms are target-specific. Not shared physics unless shared/heldout gate accepts.` |
| `mod.blocks.2.attn.h4.attention_qk` | `attention_qk` | `SPARSE_OMP_BASE_PLUS_TARGET_MINED` | 0.603944 | `PRIMITIVE_EXPLANATION_WEAK` | True | `Target-mined atoms are target-specific. Not shared physics unless shared/heldout gate accepts.` |
| `mod.blocks.2.attn.h4.attention_vo` | `attention_vo` | `SPARSE_OMP_BASE_PLUS_TARGET_MINED` | 0.587337 | `PRIMITIVE_EXPLANATION_WEAK` | True | `Target-mined atoms are target-specific. Not shared physics unless shared/heldout gate accepts.` |
| `mod.blocks.2.attn.h5.attention_qk` | `attention_qk` | `SPARSE_OMP_BASE_PLUS_TARGET_MINED` | 0.718034 | `PRIMITIVE_EXPLANATION_WEAK` | True | `Target-mined atoms are target-specific. Not shared physics unless shared/heldout gate accepts.` |
| `mod.blocks.2.attn.h5.attention_vo` | `attention_vo` | `SPARSE_OMP_BASE_PLUS_TARGET_MINED` | 0.682522 | `PRIMITIVE_EXPLANATION_WEAK` | True | `Target-mined atoms are target-specific. Not shared physics unless shared/heldout gate accepts.` |
| `mod.blocks.2.attn.h6.attention_qk` | `attention_qk` | `SPARSE_OMP_BASE_PLUS_TARGET_MINED` | 0.720539 | `PRIMITIVE_EXPLANATION_WEAK` | True | `Target-mined atoms are target-specific. Not shared physics unless shared/heldout gate accepts.` |
| `mod.blocks.2.attn.h6.attention_vo` | `attention_vo` | `SPARSE_OMP_BASE_PLUS_TARGET_MINED` | 0.597829 | `PRIMITIVE_EXPLANATION_WEAK` | True | `Target-mined atoms are target-specific. Not shared physics unless shared/heldout gate accepts.` |
| `mod.blocks.2.attn.h7.attention_qk` | `attention_qk` | `SPARSE_OMP_BASE_PLUS_TARGET_MINED` | 0.607547 | `PRIMITIVE_EXPLANATION_WEAK` | True | `Target-mined atoms are target-specific. Not shared physics unless shared/heldout gate accepts.` |
| `mod.blocks.2.attn.h7.attention_vo` | `attention_vo` | `SPARSE_OMP_BASE_PLUS_TARGET_MINED` | 0.596308 | `PRIMITIVE_EXPLANATION_WEAK` | True | `Target-mined atoms are target-specific. Not shared physics unless shared/heldout gate accepts.` |
| `mod.blocks.2.fc1.LinearW` | `linear` | `APPROX_PATTERN_FIT_RECTANGULAR_SVD` | 0.766263 | `PRIMITIVE_EXPLANATION_WEAK` | False | `SVD is compression/pattern fit, not human primitive interpretation.` |
| `mod.blocks.2.fc2.LinearW` | `linear` | `APPROX_PATTERN_FIT_RECTANGULAR_SVD` | 0.843735 | `PRIMITIVE_EXPLANATION_WEAK` | False | `SVD is compression/pattern fit, not human primitive interpretation.` |
| `mod.blocks.3.attn.h0.attention_qk` | `attention_qk` | `SPARSE_OMP_BASE_PLUS_TARGET_MINED` | 0.689765 | `PRIMITIVE_EXPLANATION_WEAK` | True | `Target-mined atoms are target-specific. Not shared physics unless shared/heldout gate accepts.` |
| `mod.blocks.3.attn.h0.attention_vo` | `attention_vo` | `SPARSE_OMP_BASE_PLUS_TARGET_MINED` | 0.691107 | `PRIMITIVE_EXPLANATION_WEAK` | True | `Target-mined atoms are target-specific. Not shared physics unless shared/heldout gate accepts.` |
| `mod.blocks.3.attn.h1.attention_qk` | `attention_qk` | `SPARSE_OMP_BASE_PLUS_TARGET_MINED` | 0.635550 | `PRIMITIVE_EXPLANATION_WEAK` | True | `Target-mined atoms are target-specific. Not shared physics unless shared/heldout gate accepts.` |
| `mod.blocks.3.attn.h1.attention_vo` | `attention_vo` | `SPARSE_OMP_BASE_PLUS_TARGET_MINED` | 0.554155 | `PRIMITIVE_EXPLANATION_WEAK` | True | `Target-mined atoms are target-specific. Not shared physics unless shared/heldout gate accepts.` |
| `mod.blocks.3.attn.h2.attention_qk` | `attention_qk` | `SPARSE_OMP_BASE_PLUS_TARGET_MINED` | 0.732328 | `PRIMITIVE_EXPLANATION_WEAK` | True | `Target-mined atoms are target-specific. Not shared physics unless shared/heldout gate accepts.` |
| `mod.blocks.3.attn.h2.attention_vo` | `attention_vo` | `SPARSE_OMP_BASE_PLUS_TARGET_MINED` | 0.695621 | `PRIMITIVE_EXPLANATION_WEAK` | True | `Target-mined atoms are target-specific. Not shared physics unless shared/heldout gate accepts.` |
| `mod.blocks.3.attn.h3.attention_qk` | `attention_qk` | `SPARSE_OMP_BASE_PLUS_TARGET_MINED` | 0.687763 | `PRIMITIVE_EXPLANATION_WEAK` | True | `Target-mined atoms are target-specific. Not shared physics unless shared/heldout gate accepts.` |
| `mod.blocks.3.attn.h3.attention_vo` | `attention_vo` | `SPARSE_OMP_BASE_PLUS_TARGET_MINED` | 0.614955 | `PRIMITIVE_EXPLANATION_WEAK` | True | `Target-mined atoms are target-specific. Not shared physics unless shared/heldout gate accepts.` |
| `mod.blocks.3.attn.h4.attention_qk` | `attention_qk` | `SPARSE_OMP_BASE_PLUS_TARGET_MINED` | 0.635576 | `PRIMITIVE_EXPLANATION_WEAK` | True | `Target-mined atoms are target-specific. Not shared physics unless shared/heldout gate accepts.` |
| `mod.blocks.3.attn.h4.attention_vo` | `attention_vo` | `SPARSE_OMP_BASE_PLUS_TARGET_MINED` | 0.622024 | `PRIMITIVE_EXPLANATION_WEAK` | True | `Target-mined atoms are target-specific. Not shared physics unless shared/heldout gate accepts.` |
| `mod.blocks.3.attn.h5.attention_qk` | `attention_qk` | `SPARSE_OMP_BASE_PLUS_TARGET_MINED` | 0.706500 | `PRIMITIVE_EXPLANATION_WEAK` | True | `Target-mined atoms are target-specific. Not shared physics unless shared/heldout gate accepts.` |
| `mod.blocks.3.attn.h5.attention_vo` | `attention_vo` | `SPARSE_OMP_BASE_PLUS_TARGET_MINED` | 0.714316 | `PRIMITIVE_EXPLANATION_WEAK` | True | `Target-mined atoms are target-specific. Not shared physics unless shared/heldout gate accepts.` |
| `mod.blocks.3.attn.h6.attention_qk` | `attention_qk` | `SPARSE_OMP_BASE_PLUS_TARGET_MINED` | 0.696538 | `PRIMITIVE_EXPLANATION_WEAK` | True | `Target-mined atoms are target-specific. Not shared physics unless shared/heldout gate accepts.` |
| `mod.blocks.3.attn.h6.attention_vo` | `attention_vo` | `SPARSE_OMP_BASE_PLUS_TARGET_MINED` | 0.669047 | `PRIMITIVE_EXPLANATION_WEAK` | True | `Target-mined atoms are target-specific. Not shared physics unless shared/heldout gate accepts.` |
| `mod.blocks.3.attn.h7.attention_qk` | `attention_qk` | `SPARSE_OMP_BASE_PLUS_TARGET_MINED` | 0.662777 | `PRIMITIVE_EXPLANATION_WEAK` | True | `Target-mined atoms are target-specific. Not shared physics unless shared/heldout gate accepts.` |
| `mod.blocks.3.attn.h7.attention_vo` | `attention_vo` | `SPARSE_OMP_BASE_PLUS_TARGET_MINED` | 0.699185 | `PRIMITIVE_EXPLANATION_WEAK` | True | `Target-mined atoms are target-specific. Not shared physics unless shared/heldout gate accepts.` |
| `mod.blocks.3.fc1.LinearW` | `linear` | `APPROX_PATTERN_FIT_RECTANGULAR_SVD` | 0.794698 | `PRIMITIVE_EXPLANATION_WEAK` | False | `SVD is compression/pattern fit, not human primitive interpretation.` |
| `mod.blocks.3.fc2.LinearW` | `linear` | `APPROX_PATTERN_FIT_RECTANGULAR_SVD` | 0.840200 | `PRIMITIVE_EXPLANATION_WEAK` | False | `SVD is compression/pattern fit, not human primitive interpretation.` |
| `mod.blocks.4.attn.h0.attention_qk` | `attention_qk` | `SPARSE_OMP_BASE_PLUS_TARGET_MINED` | 0.709229 | `PRIMITIVE_EXPLANATION_WEAK` | True | `Target-mined atoms are target-specific. Not shared physics unless shared/heldout gate accepts.` |
| `mod.blocks.4.attn.h0.attention_vo` | `attention_vo` | `SPARSE_OMP_BASE_PLUS_TARGET_MINED` | 0.728466 | `PRIMITIVE_EXPLANATION_WEAK` | True | `Target-mined atoms are target-specific. Not shared physics unless shared/heldout gate accepts.` |
| `mod.blocks.4.attn.h1.attention_qk` | `attention_qk` | `SPARSE_OMP_BASE_PLUS_TARGET_MINED` | 0.702096 | `PRIMITIVE_EXPLANATION_WEAK` | True | `Target-mined atoms are target-specific. Not shared physics unless shared/heldout gate accepts.` |
| `mod.blocks.4.attn.h1.attention_vo` | `attention_vo` | `SPARSE_OMP_BASE_PLUS_TARGET_MINED` | 0.665987 | `PRIMITIVE_EXPLANATION_WEAK` | True | `Target-mined atoms are target-specific. Not shared physics unless shared/heldout gate accepts.` |
| `mod.blocks.4.attn.h2.attention_qk` | `attention_qk` | `SPARSE_OMP_BASE_PLUS_TARGET_MINED` | 0.725306 | `PRIMITIVE_EXPLANATION_WEAK` | True | `Target-mined atoms are target-specific. Not shared physics unless shared/heldout gate accepts.` |
| `mod.blocks.4.attn.h2.attention_vo` | `attention_vo` | `SPARSE_OMP_BASE_PLUS_TARGET_MINED` | 0.700899 | `PRIMITIVE_EXPLANATION_WEAK` | True | `Target-mined atoms are target-specific. Not shared physics unless shared/heldout gate accepts.` |
| `mod.blocks.4.attn.h3.attention_qk` | `attention_qk` | `SPARSE_OMP_BASE_PLUS_TARGET_MINED` | 0.616791 | `PRIMITIVE_EXPLANATION_WEAK` | True | `Target-mined atoms are target-specific. Not shared physics unless shared/heldout gate accepts.` |
| `mod.blocks.4.attn.h3.attention_vo` | `attention_vo` | `SPARSE_OMP_BASE_PLUS_TARGET_MINED` | 0.594211 | `PRIMITIVE_EXPLANATION_WEAK` | True | `Target-mined atoms are target-specific. Not shared physics unless shared/heldout gate accepts.` |
| `mod.blocks.4.attn.h4.attention_qk` | `attention_qk` | `SPARSE_OMP_BASE_PLUS_TARGET_MINED` | 0.547912 | `PRIMITIVE_EXPLANATION_WEAK` | True | `Target-mined atoms are target-specific. Not shared physics unless shared/heldout gate accepts.` |
| `mod.blocks.4.attn.h4.attention_vo` | `attention_vo` | `SPARSE_OMP_BASE_PLUS_TARGET_MINED` | 0.620233 | `PRIMITIVE_EXPLANATION_WEAK` | True | `Target-mined atoms are target-specific. Not shared physics unless shared/heldout gate accepts.` |
| `mod.blocks.4.attn.h5.attention_qk` | `attention_qk` | `SPARSE_OMP_BASE_PLUS_TARGET_MINED` | 0.745083 | `PRIMITIVE_EXPLANATION_WEAK` | True | `Target-mined atoms are target-specific. Not shared physics unless shared/heldout gate accepts.` |
| `mod.blocks.4.attn.h5.attention_vo` | `attention_vo` | `SPARSE_OMP_BASE_PLUS_TARGET_MINED` | 0.714666 | `PRIMITIVE_EXPLANATION_WEAK` | True | `Target-mined atoms are target-specific. Not shared physics unless shared/heldout gate accepts.` |
| `mod.blocks.4.attn.h6.attention_qk` | `attention_qk` | `SPARSE_OMP_BASE_PLUS_TARGET_MINED` | 0.707566 | `PRIMITIVE_EXPLANATION_WEAK` | True | `Target-mined atoms are target-specific. Not shared physics unless shared/heldout gate accepts.` |
| `mod.blocks.4.attn.h6.attention_vo` | `attention_vo` | `SPARSE_OMP_BASE_PLUS_TARGET_MINED` | 0.627539 | `PRIMITIVE_EXPLANATION_WEAK` | True | `Target-mined atoms are target-specific. Not shared physics unless shared/heldout gate accepts.` |
| `mod.blocks.4.attn.h7.attention_qk` | `attention_qk` | `SPARSE_OMP_BASE_PLUS_TARGET_MINED` | 0.534562 | `PRIMITIVE_EXPLANATION_WEAK` | True | `Target-mined atoms are target-specific. Not shared physics unless shared/heldout gate accepts.` |
| `mod.blocks.4.attn.h7.attention_vo` | `attention_vo` | `SPARSE_OMP_BASE_PLUS_TARGET_MINED` | 0.660786 | `PRIMITIVE_EXPLANATION_WEAK` | True | `Target-mined atoms are target-specific. Not shared physics unless shared/heldout gate accepts.` |
| `mod.blocks.4.fc1.LinearW` | `linear` | `APPROX_PATTERN_FIT_RECTANGULAR_SVD` | 0.804495 | `PRIMITIVE_EXPLANATION_WEAK` | False | `SVD is compression/pattern fit, not human primitive interpretation.` |
| `mod.blocks.4.fc2.LinearW` | `linear` | `APPROX_PATTERN_FIT_RECTANGULAR_SVD` | 0.837087 | `PRIMITIVE_EXPLANATION_WEAK` | False | `SVD is compression/pattern fit, not human primitive interpretation.` |
| `mod.blocks.5.attn.h0.attention_qk` | `attention_qk` | `SPARSE_OMP_BASE_PLUS_TARGET_MINED` | 0.654512 | `PRIMITIVE_EXPLANATION_WEAK` | True | `Target-mined atoms are target-specific. Not shared physics unless shared/heldout gate accepts.` |
| `mod.blocks.5.attn.h0.attention_vo` | `attention_vo` | `SPARSE_OMP_BASE_PLUS_TARGET_MINED` | 0.658485 | `PRIMITIVE_EXPLANATION_WEAK` | True | `Target-mined atoms are target-specific. Not shared physics unless shared/heldout gate accepts.` |
| `mod.blocks.5.attn.h1.attention_qk` | `attention_qk` | `SPARSE_OMP_BASE_PLUS_TARGET_MINED` | 0.609232 | `PRIMITIVE_EXPLANATION_WEAK` | True | `Target-mined atoms are target-specific. Not shared physics unless shared/heldout gate accepts.` |
| `mod.blocks.5.attn.h1.attention_vo` | `attention_vo` | `SPARSE_OMP_BASE_PLUS_TARGET_MINED` | 0.656660 | `PRIMITIVE_EXPLANATION_WEAK` | True | `Target-mined atoms are target-specific. Not shared physics unless shared/heldout gate accepts.` |
| `mod.blocks.5.attn.h2.attention_qk` | `attention_qk` | `SPARSE_OMP_BASE_PLUS_TARGET_MINED` | 0.711522 | `PRIMITIVE_EXPLANATION_WEAK` | True | `Target-mined atoms are target-specific. Not shared physics unless shared/heldout gate accepts.` |
| `mod.blocks.5.attn.h2.attention_vo` | `attention_vo` | `SPARSE_OMP_BASE_PLUS_TARGET_MINED` | 0.653907 | `PRIMITIVE_EXPLANATION_WEAK` | True | `Target-mined atoms are target-specific. Not shared physics unless shared/heldout gate accepts.` |
| `mod.blocks.5.attn.h3.attention_qk` | `attention_qk` | `SPARSE_OMP_BASE_PLUS_TARGET_MINED` | 0.667556 | `PRIMITIVE_EXPLANATION_WEAK` | True | `Target-mined atoms are target-specific. Not shared physics unless shared/heldout gate accepts.` |
| `mod.blocks.5.attn.h3.attention_vo` | `attention_vo` | `SPARSE_OMP_BASE_PLUS_TARGET_MINED` | 0.627075 | `PRIMITIVE_EXPLANATION_WEAK` | True | `Target-mined atoms are target-specific. Not shared physics unless shared/heldout gate accepts.` |
| `mod.blocks.5.attn.h4.attention_qk` | `attention_qk` | `SPARSE_OMP_BASE_PLUS_TARGET_MINED` | 0.597021 | `PRIMITIVE_EXPLANATION_WEAK` | True | `Target-mined atoms are target-specific. Not shared physics unless shared/heldout gate accepts.` |
| `mod.blocks.5.attn.h4.attention_vo` | `attention_vo` | `SPARSE_OMP_BASE_PLUS_TARGET_MINED` | 0.631603 | `PRIMITIVE_EXPLANATION_WEAK` | True | `Target-mined atoms are target-specific. Not shared physics unless shared/heldout gate accepts.` |
| `mod.blocks.5.attn.h5.attention_qk` | `attention_qk` | `SPARSE_OMP_BASE_PLUS_TARGET_MINED` | 0.728491 | `PRIMITIVE_EXPLANATION_WEAK` | True | `Target-mined atoms are target-specific. Not shared physics unless shared/heldout gate accepts.` |
| `mod.blocks.5.attn.h5.attention_vo` | `attention_vo` | `SPARSE_OMP_BASE_PLUS_TARGET_MINED` | 0.643345 | `PRIMITIVE_EXPLANATION_WEAK` | True | `Target-mined atoms are target-specific. Not shared physics unless shared/heldout gate accepts.` |
| `mod.blocks.5.attn.h6.attention_qk` | `attention_qk` | `SPARSE_OMP_BASE_PLUS_TARGET_MINED` | 0.660047 | `PRIMITIVE_EXPLANATION_WEAK` | True | `Target-mined atoms are target-specific. Not shared physics unless shared/heldout gate accepts.` |
| `mod.blocks.5.attn.h6.attention_vo` | `attention_vo` | `SPARSE_OMP_BASE_PLUS_TARGET_MINED` | 0.615039 | `PRIMITIVE_EXPLANATION_WEAK` | True | `Target-mined atoms are target-specific. Not shared physics unless shared/heldout gate accepts.` |
| `mod.blocks.5.attn.h7.attention_qk` | `attention_qk` | `SPARSE_OMP_BASE_PLUS_TARGET_MINED` | 0.640743 | `PRIMITIVE_EXPLANATION_WEAK` | True | `Target-mined atoms are target-specific. Not shared physics unless shared/heldout gate accepts.` |
| `mod.blocks.5.attn.h7.attention_vo` | `attention_vo` | `SPARSE_OMP_BASE_PLUS_TARGET_MINED` | 0.656784 | `PRIMITIVE_EXPLANATION_WEAK` | True | `Target-mined atoms are target-specific. Not shared physics unless shared/heldout gate accepts.` |
| `mod.blocks.5.fc1.LinearW` | `linear` | `APPROX_PATTERN_FIT_RECTANGULAR_SVD` | 0.808709 | `PRIMITIVE_EXPLANATION_WEAK` | False | `SVD is compression/pattern fit, not human primitive interpretation.` |
| `mod.blocks.5.fc2.LinearW` | `linear` | `APPROX_PATTERN_FIT_RECTANGULAR_SVD` | 0.837353 | `PRIMITIVE_EXPLANATION_WEAK` | False | `SVD is compression/pattern fit, not human primitive interpretation.` |
| `mod.blocks.6.attn.h0.attention_qk` | `attention_qk` | `SPARSE_OMP_BASE_PLUS_TARGET_MINED` | 0.627761 | `PRIMITIVE_EXPLANATION_WEAK` | True | `Target-mined atoms are target-specific. Not shared physics unless shared/heldout gate accepts.` |
| `mod.blocks.6.attn.h0.attention_vo` | `attention_vo` | `SPARSE_OMP_BASE_PLUS_TARGET_MINED` | 0.642990 | `PRIMITIVE_EXPLANATION_WEAK` | True | `Target-mined atoms are target-specific. Not shared physics unless shared/heldout gate accepts.` |
| `mod.blocks.6.attn.h1.attention_qk` | `attention_qk` | `SPARSE_OMP_BASE_PLUS_TARGET_MINED` | 0.684686 | `PRIMITIVE_EXPLANATION_WEAK` | True | `Target-mined atoms are target-specific. Not shared physics unless shared/heldout gate accepts.` |
| `mod.blocks.6.attn.h1.attention_vo` | `attention_vo` | `SPARSE_OMP_BASE_PLUS_TARGET_MINED` | 0.671601 | `PRIMITIVE_EXPLANATION_WEAK` | True | `Target-mined atoms are target-specific. Not shared physics unless shared/heldout gate accepts.` |
| `mod.blocks.6.attn.h2.attention_qk` | `attention_qk` | `SPARSE_OMP_BASE_PLUS_TARGET_MINED` | 0.724101 | `PRIMITIVE_EXPLANATION_WEAK` | True | `Target-mined atoms are target-specific. Not shared physics unless shared/heldout gate accepts.` |

## Exact formulas

```text
Linear: y = x_aug @ W_aug.T, W_aug=[W|b]
LayerNorm: y = ((x-mean)/sqrt(var+eps))*gamma + beta, dynamic per input
Activation: exact elementwise formula, not constant matrix
Attention: score_ij = [x_i,1] @ M_qk_aug @ [x_j,1].T + pair_bias + padding_mask
Attention write: Y_i = sum_j softmax(score)_ij * ([x_j,1] @ C_vo_aug.T)
```
