class ModelAdapter:
    """Common interface for model-specific causal tracing adapters."""
    def load_model(self): raise NotImplementedError
    def load_data(self, *args, **kwargs): raise NotImplementedError
    def get_layers(self): raise NotImplementedError
    def get_input_embed(self): raise NotImplementedError
    def get_attention(self, layer): raise NotImplementedError
    def get_qkv(self, layer): raise NotImplementedError
    def get_o_proj(self, layer): raise NotImplementedError
    def get_pair_embed(self): return None
    def get_pair_bias_source(self, layer): return self.get_pair_embed()
    def get_mlp(self, layer): raise NotImplementedError
    def get_mlp_up(self, layer): raise NotImplementedError
    def get_mlp_down(self, layer): raise NotImplementedError
    def get_norms(self, layer): return {}
    def get_pooling_or_cls(self): return None
    def get_classifier_head(self): raise NotImplementedError
    def forward_with_cache(self, batch): raise NotImplementedError
    def patch_head(self, layer, head, mode): raise NotImplementedError
    def patch_mlp_group(self, layer, neurons): raise NotImplementedError
    def patch_particle_group(self, particle_indices): raise NotImplementedError
    def patch_pair_group(self, pair_indices): raise NotImplementedError
