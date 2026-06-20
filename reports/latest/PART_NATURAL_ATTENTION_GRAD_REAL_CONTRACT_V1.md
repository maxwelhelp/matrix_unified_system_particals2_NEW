# PART_NATURAL_ATTENTION_GRAD_REAL_CONTRACT_V1

Natural attention A×grad trace over current direct-replay ParT groups. This captures real per-head attention weights from nn.MultiheadAttention, retains gradients on them, and aggregates A, grad_A, and A*grad_A by physical role-pairs. No synthetic route gate is inserted.

- events: **128**
- events_per_group: **32**
- micro_batch: **4**
- roles: `['CLS', 'electron', 'muon', 'charged_hadron', 'neutral_hadron', 'photon']`
- role_pairs: **36**
- objectives: `['signed_hqql_tbl', 'B_tbl_minus_hqql']`
- rows: **0**

## Top natural attention role-links: `signed_hqql_tbl`
_No rows._

## Top natural attention role-links: `B_tbl_minus_hqql`
_No rows._

## Interpretation

- `mean_A`: how much natural attention mass uses this role-link.
- `mean_AxGrad`: attention mass weighted by objective gradient. This is the important one: active links that also matter for Hqql/Tbl.
- For `B_tbl_minus_hqql`, positive B_AxGrad means the natural link pushes Hqql mistakes toward Tbl; negative means it resists that margin.
- This is the missing bridge between attention visualization and matrix-program evidence: real A, real grad_A, physical role-pair aggregation.
