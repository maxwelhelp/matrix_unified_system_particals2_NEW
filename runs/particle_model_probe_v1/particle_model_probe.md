# Particle model probe v1

{
  "status": "skeleton",
  "note": "Import actual ParT model, then wrap it with adapters.part_adapter.ParticleTransformerAdapter.",
  "expected_modules": {
    "embed": "input particle feature embedding",
    "pair_embed": "pairwise particle interaction bias before softmax",
    "blocks": "particle self-attention transformer blocks",
    "cls_blocks": "class-token attention blocks",
    "cls_token": "learned class token",
    "norm": "final class token norm",
    "fc": "classifier head",
    "block.attn": "torch MultiheadAttention with packed qkv",
    "block.fc1/fc2": "MLP up/down",
    "block norms": "pre/post attention and MLP norms",
    "block scales": "c_attn and w_resid if enabled"
  }
}