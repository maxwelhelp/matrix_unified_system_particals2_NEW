import torch
from .base_adapter import ModelAdapter

class ParticleTransformerAdapter(ModelAdapter):
    """Adapter skeleton for weaver ParticleTransformer / ParT.

    Expected core modules from weaver.nn.model.ParticleTransformer:
    - embed / pf_embed / sv_embed
    - pair_embed
    - blocks: particle self-attention blocks
    - cls_blocks: class-token attention blocks
    - cls_token
    - norm
    - fc classifier
    - Block.attn: torch.nn.MultiheadAttention
    - Block.fc1/fc2: MLP
    - Block.pre_attn_norm, post_attn_norm, pre_fc_norm, post_fc_norm
    - Block.c_attn, w_resid optional scaling params
    """
    def __init__(self, model):
        self.model = model
        self.part = getattr(model, 'mod', model)
        if hasattr(self.part, 'part'):
            self.part = self.part.part

    def get_layers(self):
        return list(getattr(self.part, 'blocks'))

    def get_cls_layers(self):
        return list(getattr(self.part, 'cls_blocks', []))

    def get_input_embed(self):
        return getattr(self.part, 'embed', None)

    def get_pair_embed(self):
        return getattr(self.part, 'pair_embed', None)

    def get_attention(self, layer):
        return self.get_layers()[layer].attn

    def get_qkv(self, layer):
        attn = self.get_attention(layer)
        # PyTorch MultiheadAttention often stores packed QKV in in_proj_weight/in_proj_bias.
        return {
            'packed_in_proj_weight': getattr(attn, 'in_proj_weight', None),
            'packed_in_proj_bias': getattr(attn, 'in_proj_bias', None),
            'q_proj_weight': getattr(attn, 'q_proj_weight', None),
            'k_proj_weight': getattr(attn, 'k_proj_weight', None),
            'v_proj_weight': getattr(attn, 'v_proj_weight', None),
        }

    def get_o_proj(self, layer):
        return self.get_attention(layer).out_proj

    def get_mlp(self, layer):
        b = self.get_layers()[layer]
        return {'fc1': b.fc1, 'act': b.act, 'fc2': b.fc2}

    def get_mlp_up(self, layer):
        return self.get_layers()[layer].fc1

    def get_mlp_down(self, layer):
        return self.get_layers()[layer].fc2

    def get_norms(self, layer):
        b = self.get_layers()[layer]
        return {
            'pre_attn_norm': getattr(b, 'pre_attn_norm', None),
            'post_attn_norm': getattr(b, 'post_attn_norm', None),
            'pre_fc_norm': getattr(b, 'pre_fc_norm', None),
            'post_fc_norm': getattr(b, 'post_fc_norm', None),
        }

    def get_pooling_or_cls(self):
        return {'cls_token': getattr(self.part, 'cls_token', None), 'norm': getattr(self.part, 'norm', None)}

    def get_classifier_head(self):
        return getattr(self.part, 'fc', None)

    def describe(self):
        return {
            'n_blocks': len(self.get_layers()),
            'n_cls_blocks': len(self.get_cls_layers()),
            'has_pair_embed': self.get_pair_embed() is not None,
            'has_classifier': self.get_classifier_head() is not None,
            'has_cls_token': getattr(self.part, 'cls_token', None) is not None,
        }
