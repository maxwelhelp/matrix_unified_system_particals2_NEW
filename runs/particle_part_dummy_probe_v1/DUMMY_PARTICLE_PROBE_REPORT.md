# Particle dummy ParT probe v1

ok=True logits_shape=[4, 10]

## Adapter
{
  "n_blocks": 2,
  "n_cls_blocks": 1,
  "has_pair_embed": true,
  "has_classifier": true,
  "has_cls_token": true
}

## Captures
{
  "embed": {
    "input": [
      [
        4,
        16,
        32
      ]
    ],
    "output": [
      4,
      32,
      64
    ]
  },
  "pair_embed": {
    "input": [
      [
        4,
        4,
        32
      ]
    ],
    "output": [
      4,
      4,
      32,
      32
    ]
  },
  "block_0": {
    "input": [
      [
        4,
        32,
        64
      ]
    ],
    "output": [
      4,
      32,
      64
    ]
  },
  "block_1": {
    "input": [
      [
        4,
        32,
        64
      ]
    ],
    "output": [
      4,
      32,
      64
    ]
  },
  "cls_block_0": {
    "input": [
      [
        4,
        32,
        64
      ]
    ],
    "output": [
      4,
      1,
      64
    ]
  },
  "classifier": {
    "input": [
      [
        4,
        64
      ]
    ],
    "output": [
      4,
      10
    ]
  }
}