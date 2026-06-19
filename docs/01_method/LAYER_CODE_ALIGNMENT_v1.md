# Layer Code Alignment v1

The pseudocode layer must be tied to real model code.

Without code alignment, pseudocode is only a semantic story. With alignment, each pseudo-head row should point to:

```text
source module
source function
actual forward path
tensor shape
channel range
real operation family
semantic pseudocode
```

## ParticleNet code path to align

Expected path:

```text
ParticleNet.forward(points, features, mask)
  -> SequenceTrimmer / padding mask
  -> EdgeConvBlock.forward for layer 0
      -> knn(points, k)
      -> graph/edge feature construction
      -> conv/bn/relu stack
      -> aggregation over neighbors
  -> EdgeConvBlock.forward for layer 1
  -> EdgeConvBlock.forward for layer 2
  -> pooling / fusion / fc classifier
```

## Alignment rows

Every pseudo-head should get:

```text
head_id
layer
channels
source_file
source_module
source_function
module_path
actual_tensor_stage
input_shape
output_shape
code_operation
semantic_pseudocode
alignment_confidence
remaining_gap
```

## Why this matters

This allows us to say:

```text
L1_ch112:128 is not an abstract head.
It is channels 112:128 of EdgeConv layer 1 output after KNN neighborhood mixing and before layer 2/readout.
```

That is much stronger than saliency.
