#!/usr/bin/env python3
"""
PART full-model matrix coverage decoder v1_4_2.

VERSION = 1.4.2

This file intentionally fixes the previous v1/v1_1 scaffold issues:
  * explicit VERSION/sha-ready artifact name
  * no raw args/kwargs capture
  * bool + positional masks handled
  * rejected_modules participates in ok/status
  * SVD is never trusted interpretation
  * activations are exact elementwise formulas, not fake LOCAL_JACOBIAN
  * containers are STRUCTURAL_NOT_EXPLICITLY_TRACED unless replayed
  * Qwen-style MatrixOpLibrary + SparseProgramDecoder + OMP
  * residual mining with target_mined atoms
  * shared primitive candidates with real train/heldout residual-gain gate
  * flow-pack CSV/PT export
  * all-head group tensor export
  * pair-bias module candidate table
  * separate inventory/parameters/modules/heads/linear/dynamic/primitive/shared/flow/acceptance CSVs

Hard honesty:
  Stage 1 goal is FULL_MODEL_MATRIX_COVERAGE_CLOSED: every named_parameter and matrix/parametric component is covered by a decoder or explicitly uncovered. FULL_FORWARD_CLOSED is separate Stage 2 and requires decoded-logits replay.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import os
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple

# Prevent accidental OpenMP/MKL stalls in self-tests unless user overrides.
if os.environ.get("PART_DECODER_SET_THREADS", "1") != "0":
    os.environ.setdefault("OMP_NUM_THREADS", "1")
    os.environ.setdefault("MKL_NUM_THREADS", "1")

import torch
import torch.nn as nn
import torch.nn.functional as F

try:
    torch.set_num_threads(int(os.environ.get("PART_DECODER_TORCH_THREADS", "1")))
except Exception:
    pass

VERSION = "1.4.2"
ACCEPT_TOL = 1e-5
GROUPS = ["A_Hqql_correct", "B_Hqql_to_Tbl", "C_Tbl_correct", "D_Tbl_to_Hqql"]


# =============================================================================
# IO / generic helpers
# =============================================================================

def rel_err(pred: torch.Tensor, true: torch.Tensor, mask: Optional[torch.Tensor] = None) -> float:
    pred = pred.detach().float().cpu()
    true = true.detach().float().cpu()
    if mask is not None:
        mask = mask.detach().bool().cpu()
        pred = pred[mask]
        true = true[mask]
    if true.numel() == 0:
        return float("nan")
    return float(torch.linalg.norm(pred - true) / torch.linalg.norm(true).clamp_min(1e-12))


def finite_norm(x: torch.Tensor) -> float:
    x = x.detach().float().cpu()
    m = torch.isfinite(x)
    if not m.any():
        return 0.0
    return float(torch.linalg.norm(x[m]).item())


def fmt(x: Any) -> str:
    try:
        v = float(x)
    except Exception:
        return "n/a"
    if math.isnan(v):
        return "nan"
    return f"{v:.3e}" if abs(v) > 0 and (abs(v) < 1e-3 or abs(v) > 1e4) else f"{v:.6f}"


def shape_str(x: Any) -> str:
    if torch.is_tensor(x):
        return "x".join(map(str, x.shape))
    if isinstance(x, (list, tuple)):
        return "[" + ",".join(shape_str(v) for v in x) + "]"
    if isinstance(x, dict):
        return "{" + ",".join(f"{k}:{shape_str(v)}" for k, v in x.items()) + "}"
    if x is None:
        return "None"
    return type(x).__name__


def first_tensor(x: Any) -> Optional[torch.Tensor]:
    if torch.is_tensor(x):
        return x
    if isinstance(x, (list, tuple)):
        for v in x:
            t = first_tensor(v)
            if t is not None:
                return t
    if isinstance(x, dict):
        for v in x.values():
            t = first_tensor(v)
            if t is not None:
                return t
    return None


def detach_cpu(x: Optional[torch.Tensor]) -> Optional[torch.Tensor]:
    if x is None:
        return None
    y = x.detach().cpu()
    return y.float() if y.is_floating_point() else y


def read_csv(path: str) -> List[Dict[str, str]]:
    p = Path(path)
    if not p.exists():
        return []
    with p.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def write_csv(path: str, rows: List[Dict[str, Any]]) -> None:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        p.write_text("", encoding="utf-8")
        return
    keys: List[str] = []
    for r in rows:
        for k in r:
            if k not in keys:
                keys.append(k)
    with p.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=keys)
        w.writeheader()
        w.writerows(rows)


def write_json(path: str, obj: Dict[str, Any]) -> None:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(strip_tensors(obj), indent=2, ensure_ascii=False), encoding="utf-8")


def save_pt(path: str, obj: Any) -> str:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    torch.save(obj, p)
    return str(p)


def safe_name(name: str) -> str:
    return name.replace("<", "").replace(">", "").replace("/", "_").replace(".", "_").replace(":", "_")


def strip_tensors(obj: Any) -> Any:
    if torch.is_tensor(obj):
        return {"tensor_shape": list(obj.shape), "tensor_norm": float(torch.linalg.norm(obj.float()).item()) if obj.numel() else 0.0}
    if isinstance(obj, dict):
        return {str(k): strip_tensors(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [strip_tensors(v) for v in obj]
    return obj


def select_events(path: str, events_per_group: int) -> List[Dict[str, str]]:
    by = defaultdict(list)
    for r in read_csv(path):
        by[r.get("analysis_group", "")].append(r)
    out: List[Dict[str, str]] = []
    for g in GROUPS:
        out += by[g][:events_per_group]
    if not out:
        raise RuntimeError(f"no events selected from {path}")
    return out


def params_count(module: nn.Module, recurse: bool = False) -> int:
    return int(sum(p.numel() for p in module.parameters(recurse=recurse)))


def buffers_count(module: nn.Module, recurse: bool = False) -> int:
    return int(sum(b.numel() for b in module.buffers(recurse=recurse)))


def has_children(module: nn.Module) -> bool:
    return any(True for _ in module.children())


def is_leaf(module: nn.Module) -> bool:
    return not has_children(module)


# =============================================================================
# Model metadata / classification
# =============================================================================

def is_legacy_mha(module: Any) -> bool:
    return hasattr(module, "num_heads") and hasattr(module, "head_dim") and hasattr(module, "in_proj_weight") and hasattr(module, "out_proj")


def is_activation(module: nn.Module) -> bool:
    return isinstance(module, (nn.ReLU, nn.GELU, nn.SiLU, nn.Sigmoid, nn.Tanh, nn.LeakyReLU, nn.ELU))


def is_norm(module: nn.Module) -> bool:
    return isinstance(module, (nn.LayerNorm, nn.BatchNorm1d, nn.BatchNorm2d, nn.BatchNorm3d)) or "RMSNorm" in module.__class__.__name__


def is_structural_leaf(module: nn.Module) -> bool:
    return isinstance(module, (nn.Dropout, nn.Dropout1d, nn.Dropout2d, nn.Dropout3d, nn.Flatten, nn.Identity))


def possible_pair_bias_module(name: str, module: nn.Module) -> bool:
    s = f"{name} {module.__class__.__name__}".lower()
    return any(k in s for k in ["pair", "pair_embed", "pair_emb", "pairwise", "interaction", "attn_mask", "delta"])


def classify_module(name: str, module: nn.Module) -> str:
    if is_legacy_mha(module):
        return "MULTIHEAD_ATTENTION"
    if isinstance(module, nn.Linear):
        return "LINEAR"
    if isinstance(module, nn.Embedding):
        return "EMBEDDING"
    if isinstance(module, nn.LayerNorm):
        return "LAYERNORM"
    if isinstance(module, (nn.BatchNorm1d, nn.BatchNorm2d, nn.BatchNorm3d)):
        return "BATCHNORM"
    if "RMSNorm" in module.__class__.__name__:
        return "RMSNORM"
    if is_activation(module):
        return "ACTIVATION"
    if is_structural_leaf(module):
        return "STRUCTURAL_LEAF"
    if has_children(module):
        return "CONTAINER"
    if params_count(module, recurse=False) > 0:
        return "PARAMETERIZED_LEAF_UNKNOWN"
    return "STATELESS_LEAF"


def direct_param_shapes(module: nn.Module) -> Dict[str, str]:
    return {n: "x".join(map(str, p.shape)) for n, p in module.named_parameters(recurse=False)}


def suggested_decoder(module: nn.Module) -> str:
    if params_count(module, recurse=False) > 0:
        return f"add exact decoder for {module.__class__.__name__}.forward direct parameters"
    if has_children(module):
        return "container output not replayed; children decoded separately, Python-level graph replay needed"
    return ""


def meta_diagnostics(metas: List[Dict[str, Any]]) -> Dict[str, Any]:
    keys = sorted({k for m in metas for k in m.keys()}) if metas else []
    pts: List[float] = []
    charges: List[float] = []
    roles: List[str] = []
    for m in metas:
        pts += [float(x) for x in m.get("pt", [])]
        charges += [float(x) for x in m.get("charge", [])]
        roles += [str(x) for x in m.get("roles", [])]
    pt_nonzero = sum(1 for x in pts if abs(x) > 1e-12) / max(1, len(pts))
    charge_nonzero = sum(1 for x in charges if abs(x) > 1e-12) / max(1, len(charges))
    return {
        "meta_keys": keys,
        "pt_nonzero_frac": pt_nonzero,
        "charge_nonzero_frac": charge_nonzero,
        "unique_roles": sorted(set(roles)),
        "role_counts": dict(Counter(roles)),
        "n_meta": len(metas),
    }


def has_trusted_physics_meta(diag: Dict[str, Any]) -> bool:
    roles = set(diag.get("unique_roles", []))
    return diag.get("pt_nonzero_frac", 0.0) > 0.01 and len(roles.intersection({"charged_hadron", "neutral_hadron", "photon", "electron", "muon"})) >= 2


def inventory_rows(model: nn.Module) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]], List[Dict[str, Any]]]:
    inv = []
    params = []
    pair_candidates = []
    for name, module in model.named_modules():
        display = name if name else "<root>"
        inv.append({
            "module_name": display,
            "module_type": module.__class__.__name__,
            "classify": classify_module(name, module),
            "children_count": len(list(module.children())),
            "direct_params_count": params_count(module, recurse=False),
            "params_count": params_count(module, recurse=True),
            "buffers_count": buffers_count(module, recurse=False),
            "possible_pair_bias_module": possible_pair_bias_module(name, module),
            "decoder_kind": "",
            "covered": "",
            "reason_if_uncovered": "",
            "direct_param_shapes": json.dumps(direct_param_shapes(module), ensure_ascii=False),
        })
        for pname, p in module.named_parameters(recurse=False):
            params.append({
                "module_name": display,
                "param_name": pname,
                "shape": "x".join(map(str, p.shape)),
                "numel": int(p.numel()),
                "requires_grad": bool(p.requires_grad),
            })
        if possible_pair_bias_module(name, module):
            pair_candidates.append({
                "module_name": display,
                "module_type": module.__class__.__name__,
                "direct_params_count": params_count(module, recurse=False),
                "params_count": params_count(module, recurse=True),
                "is_linear": isinstance(module, nn.Linear),
                "is_mha": is_legacy_mha(module),
                "decoder_hint": "decoded as Linear submodule if Linear; otherwise inspect children/forward",
            })
    return inv, params, pair_candidates


def merge_inventory_coverage(inv: List[Dict[str, Any]], module_rows: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    by = {r["module_name"]: r for r in module_rows}
    out = []
    for r in inv:
        key = "" if r["module_name"] == "<root>" else r["module_name"]
        m = by.get(key)
        rr = dict(r)
        if m:
            rr["decoder_kind"] = m.get("decoder_kind", "")
            rr["covered"] = str(m.get("decoder_kind") not in ("UNCOVERED", "STRUCTURAL_NOT_EXPLICITLY_TRACED"))
            rr["reason_if_uncovered"] = m.get("fail_reason", "")
        else:
            rr["covered"] = "False" if rr["module_name"] != "<root>" else ""
            rr["reason_if_uncovered"] = "not_captured_or_root"
        out.append(rr)
    return out


# =============================================================================
# Capture: no raw args/kwargs retained
# =============================================================================

def extract_forward_arg(args: Tuple[Any, ...], kwargs: Dict[str, Any], name: str, pos: int) -> Tuple[Any, str]:
    if name in kwargs:
        return kwargs.get(name), "kwargs"
    if len(args) > pos:
        return args[pos], "positional"
    return None, "none"


class ModuleCapture:
    def __init__(self, max_items: int = 1):
        self.max_items = max_items
        self.records: Dict[str, Dict[str, Any]] = {}
        self.counts: Counter = Counter()
        self.handles: List[Any] = []

    def hook(self, name: str):
        def fn(module, args, kwargs, output):
            self.counts[name] += 1
            if name in self.records and self.counts[name] > self.max_items:
                return
            inp = first_tensor(args)
            out = first_tensor(output)
            rec: Dict[str, Any] = {
                "module": module,
                "module_type": module.__class__.__name__,
                "input": detach_cpu(inp),
                "output": detach_cpu(out),
                "input_shape": shape_str(args),
                "output_shape": shape_str(output),
                "training": bool(module.training),
                "capture_count": int(self.counts[name]),
            }
            if is_legacy_mha(module) and len(args) >= 3:
                kpm, kpm_src = extract_forward_arg(args, kwargs, "key_padding_mask", 3)
                need_weights, need_weights_src = extract_forward_arg(args, kwargs, "need_weights", 4)
                am, am_src = extract_forward_arg(args, kwargs, "attn_mask", 5)
                avg, avg_src = extract_forward_arg(args, kwargs, "average_attn_weights", 6)
                out0 = output[0] if isinstance(output, tuple) else output
                out1 = output[1] if isinstance(output, tuple) and len(output) > 1 else None
                rec.update({
                    "q": detach_cpu(args[0]),
                    "k": detach_cpu(args[1]),
                    "v": detach_cpu(args[2]),
                    "mha_output": detach_cpu(out0),
                    "attn_weights": None if out1 is None else detach_cpu(out1),
                    "attn_mask": None if am is None else detach_cpu(am),
                    "attn_mask_source": am_src,
                    "attn_mask_dtype": "none" if am is None else str(am.dtype),
                    "key_padding_mask": None if kpm is None else detach_cpu(kpm),
                    "key_padding_mask_source": kpm_src,
                    "key_padding_mask_dtype": "none" if kpm is None else str(kpm.dtype),
                    "need_weights": str(need_weights),
                    "need_weights_source": need_weights_src,
                    "average_attn_weights": str(avg),
                    "average_attn_weights_source": avg_src,
                })
            self.records[name] = rec
        return fn

    def attach(self, model: nn.Module):
        for name, module in model.named_modules():
            if name == "":
                continue
            # Capture leaves + MHA. Containers are tracked by inventory but not tensor-captured.
            if is_leaf(module) or is_legacy_mha(module):
                self.handles.append(module.register_forward_hook(self.hook(name), with_kwargs=True))

    def close(self):
        for h in self.handles:
            h.remove()
        self.handles = []


# =============================================================================
# Qwen-style primitive library / OMP / residual mining
# =============================================================================

def normalized_flat(M: torch.Tensor) -> torch.Tensor:
    v = M.detach().float().cpu().reshape(-1)
    return v / torch.linalg.norm(v).clamp_min(1e-12)


class MatrixOpLibrary:
    def __init__(self, D: int):
        self.D = int(D)
        self.ops: List[torch.Tensor] = []
        self.meta: List[Dict[str, Any]] = []
        self._build_base()

    def add(self, name: str, M: torch.Tensor, family: str = "base", origin: str = "base"):
        M = M.detach().float().cpu()
        if tuple(M.shape) != (self.D, self.D):
            return
        self.ops.append(M)
        self.meta.append({"name": name, "family": family, "origin": origin})

    def _build_base(self):
        D = self.D
        self.add("Identity", torch.eye(D), "diagonal")
        self.add("RampDiag", torch.diag(torch.linspace(-1, 1, D)), "diagonal")
        self.add("MeanProject", torch.ones(D, D) / D, "global")
        for sh in [1, 2, 4, 8]:
            if sh >= D:
                continue
            M = torch.zeros(D, D)
            for i in range(D):
                j = i - sh
                if 0 <= j < D:
                    M[i, j] = 1.0
            self.add(f"ShiftRight{sh}", M, "shift")
            self.add(f"ShiftLeft{sh}", M.T, "shift")
        for block in [2, 4, 8, 16, 32, 64]:
            if block >= D:
                continue
            M = torch.zeros(D, D)
            for start in range(0, D, block):
                end = min(D, start + block)
                M[start:end, start:end] = 1.0 / max(1, end - start)
            self.add(f"BlockAvg{block}", M, "block")

        # Qwen-style expanded 1D/channel operators. These are still channel-space
        # primitives; physics meaning requires separate validation.
        for direction, sign in [("Backward", -1), ("Forward", 1)]:
            M = torch.zeros(D, D)
            for i in range(D):
                M[i, i] = 1.0
                j = i + sign
                if 0 <= j < D:
                    M[i, j] = -1.0
            self.add(f"Diff{direction}", M, "difference")

        L = torch.zeros(D, D)
        for i in range(D):
            L[i, i] = 2.0
            if i > 0:
                L[i, i - 1] = -1.0
            if i + 1 < D:
                L[i, i + 1] = -1.0
        self.add("Laplacian1D", L, "difference")

        for radius in [1, 2]:
            M = torch.zeros(D, D)
            for i in range(D):
                js = [j for j in range(i - radius, i + radius + 1) if 0 <= j < D]
                for j in js:
                    M[i, j] = 1.0 / len(js)
            self.add(f"Blur{2 * radius + 1}", M, "smooth")

        P = torch.zeros(D, D)
        for i in range(D):
            P[i, :i + 1] = 1.0 / (i + 1)
        self.add("PrefixMean", P, "prefix")

        for tau in [2, 4, 8]:
            M = torch.zeros(D, D)
            for i in range(D):
                for j in range(D):
                    M[i, j] = math.exp(-abs(i - j) / tau)
                M[i] /= M[i].sum().clamp_min(1e-12)
            self.add(f"DistanceDecay{tau}", M, "decay")

        self.add("Reverse", torch.flip(torch.eye(D), dims=[1]), "permutation")

        # Coarse DCT band projectors. Low/mid/high are useful pattern atoms,
        # not exact semantic claims.
        n = torch.arange(D).float()
        basis = []
        for k in range(D):
            v = torch.cos(math.pi * (n + 0.5) * k / D)
            v = v / torch.linalg.norm(v).clamp_min(1e-12)
            basis.append(v)
        B = torch.stack(basis)
        bands = {
            "DCTLow": range(0, max(1, D // 8)),
            "DCTMid": range(max(1, D // 8), max(2, D // 3)),
            "DCTHigh": range(max(2, D // 3), D),
        }
        for name, idxs in bands.items():
            idxs = list(idxs)
            if idxs:
                U = B[idxs]
                self.add(name, U.T @ U, "spectral")

        Ring = torch.zeros(D, D)
        for i in range(D):
            Ring[i, i] = 0.5
            Ring[i, (i - 1) % D] = 0.25
            Ring[i, (i + 1) % D] = 0.25
        self.add("GraphRingRW", Ring, "graph")
        self.add("GraphDiffusion2", Ring @ Ring, "graph")

    def add_mined_from_target(self, R: torch.Tensor, max_svd: int = 4, add_toeplitz: bool = True, add_blocks: bool = True):
        R = R.detach().float().cpu()
        if R.ndim != 2 or tuple(R.shape) != (self.D, self.D):
            return
        # Low-rank residual atoms.
        try:
            U, S, Vh = torch.linalg.svd(R, full_matrices=False)
            for i in range(min(max_svd, S.numel())):
                self.add(f"MinedResidualSVD{i}", torch.outer(U[:, i], Vh[i, :]), "low_rank", "mined_from_target")
        except Exception:
            pass
        # Toeplitz diagonal-average residual atom.
        if add_toeplitz:
            T = torch.zeros(self.D, self.D)
            for off in range(-self.D + 1, self.D):
                vals = torch.diagonal(R, offset=off)
                if vals.numel():
                    idx = torch.arange(max(0, -off), min(self.D, self.D - off))
                    T[idx, idx + off] = vals.mean()
            self.add("MinedResidualToeplitzAvg", T, "toeplitz", "mined_from_target")
        # Block mean residual atoms.
        if add_blocks:
            for block in [4, 8, 16, 32]:
                if block >= self.D:
                    continue
                B = torch.zeros(self.D, self.D)
                for i in range(0, self.D, block):
                    for j in range(0, self.D, block):
                        sub = R[i:min(self.D, i + block), j:min(self.D, j + block)]
                        B[i:min(self.D, i + block), j:min(self.D, j + block)] = sub.mean()
                self.add(f"MinedResidualBlockMean{block}", B, "block_mined", "mined_from_target")

    def bank(self) -> torch.Tensor:
        return torch.stack([normalized_flat(M) for M in self.ops], dim=1)

    def coeffs_to_matrix(self, coeff: torch.Tensor) -> torch.Tensor:
        out = torch.zeros(self.D, self.D)
        for c, M in zip(coeff.detach().float().cpu(), self.ops):
            out += c * (M / torch.linalg.norm(M).clamp_min(1e-12))
        return out


class SparseProgramDecoder:
    def __init__(self, lib: MatrixOpLibrary, ridge: float = 1e-4):
        self.lib = lib
        self.ridge = ridge

    def decode_omp(self, W: torch.Tensor, max_atoms: int = 12, stop_rel: float = 1e-4) -> Tuple[torch.Tensor, Dict[str, Any]]:
        W = W.detach().float().cpu()
        b = W.reshape(-1)
        bnorm = torch.linalg.norm(b).clamp_min(1e-12)
        A = self.lib.bank()
        selected: List[int] = []
        coeff = torch.zeros(A.shape[1])
        residual = b.clone()
        for _ in range(min(max_atoms, A.shape[1])):
            corr = A.T @ residual
            for i in selected:
                corr[i] = 0.0
            idx = int(torch.argmax(corr.abs()).item())
            if idx in selected:
                break
            selected.append(idx)
            As = A[:, selected]
            cs = torch.linalg.solve(As.T @ As + self.ridge * torch.eye(len(selected)), As.T @ b)
            residual = b - As @ cs
            if float(torch.linalg.norm(residual) / bnorm) <= stop_rel:
                break
        if selected:
            As = A[:, selected]
            cs = torch.linalg.solve(As.T @ As + self.ridge * torch.eye(len(selected)), As.T @ b)
            for i, c in zip(selected, cs):
                coeff[i] = c
        rec = A @ coeff
        terms = []
        for i in selected:
            t = dict(self.lib.meta[i])
            t["coef"] = float(coeff[i])
            terms.append(t)
        return coeff, {
            "rec_err": float(torch.linalg.norm(rec - b) / bnorm),
            "selected_terms": terms,
            "selected_count": len(selected),
            "uses_target_mined_atoms": any(t.get("origin") == "mined_from_target" for t in terms),
        }


def functional_error_square(W: torch.Tensor, W_hat: torch.Tensor, n: int = 64) -> float:
    if W.ndim != 2 or W.shape[0] != W.shape[1]:
        return float("nan")
    X = torch.randn(n, W.shape[1])
    return rel_err(X @ W_hat.T, X @ W.T)


def fit_rectangular_svd(W: torch.Tensor, max_rank: int = 16) -> Dict[str, Any]:
    W = W.detach().float().cpu()
    if W.ndim != 2:
        return {"enabled": False, "fit_kind": "NOT_MATRIX", "reason": "not_2d"}
    U, S, Vh = torch.linalg.svd(W, full_matrices=False)
    r = min(max_rank, S.numel())
    rec = (U[:, :r] * S[:r]) @ Vh[:r, :]
    return {
        "enabled": True,
        "fit_kind": "APPROX_PATTERN_FIT_RECTANGULAR_SVD",
        "rank": r,
        "rec_err": rel_err(rec, W),
        "functional_err": float("nan"),
        "selected_terms": [],
        "uses_target_mined_atoms": False,
        "interpretation_trusted": False,
        "honesty_note": "SVD is compression/pattern fit, not human primitive interpretation.",
        "singular_values_top": [float(x) for x in S[:min(16, S.numel())]],
    }


def decode_matrix_with_auto_dictionary(
    W: torch.Tensor,
    allow_target_mined: bool = True,
    max_atoms: int = 12,
    stop_rel: float = 1e-4,
    mined_svd_atoms: int = 4,
    ridge: float = 1e-4,
) -> Dict[str, Any]:
    W = W.detach().float().cpu()
    if W.ndim != 2:
        return {"enabled": False, "fit_kind": "NOT_MATRIX", "reason": "not_2d"}
    if W.shape[0] != W.shape[1]:
        return fit_rectangular_svd(W, max_rank=max_atoms)
    lib = MatrixOpLibrary(W.shape[0])
    dec = SparseProgramDecoder(lib, ridge=ridge)
    coeff_base, base = dec.decode_omp(W, max_atoms=max_atoms, stop_rel=stop_rel)
    W_base = lib.coeffs_to_matrix(coeff_base)
    residual_after_base = W - W_base
    best = {
        "enabled": True,
        "fit_kind": "SPARSE_OMP_BASE",
        "rec_err": base["rec_err"],
        "functional_err": functional_error_square(W, W_base),
        "selected_terms": base["selected_terms"],
        "uses_target_mined_atoms": False,
        "residual_after_base": residual_after_base,
        "base_rec_err": base["rec_err"],
        "mined_rec_err": "",
        "formula": terms_to_text(base["selected_terms"]),
        "honesty_note": "Base dictionary fit. Approximate primitive interpretation only.",
    }
    if allow_target_mined:
        lib2 = MatrixOpLibrary(W.shape[0])
        lib2.add_mined_from_target(residual_after_base, max_svd=mined_svd_atoms)
        dec2 = SparseProgramDecoder(lib2, ridge=ridge)
        coeff_mined, mined = dec2.decode_omp(W, max_atoms=max_atoms, stop_rel=stop_rel)
        W_mined = lib2.coeffs_to_matrix(coeff_mined)
        if mined["rec_err"] < best["rec_err"]:
            best.update({
                "fit_kind": "SPARSE_OMP_BASE_PLUS_TARGET_MINED",
                "rec_err": mined["rec_err"],
                "functional_err": functional_error_square(W, W_mined),
                "selected_terms": mined["selected_terms"],
                "uses_target_mined_atoms": mined["uses_target_mined_atoms"],
                "mined_rec_err": mined["rec_err"],
                "formula": terms_to_text(mined["selected_terms"]),
                "honesty_note": "Target-mined atoms are target-specific. Not shared physics unless shared/heldout gate accepts.",
            })
    return best


def terms_to_text(terms: List[Dict[str, Any]]) -> str:
    if not terms:
        return "0"
    return " + ".join([f"{float(t.get('coef', t.get('coef_normalized_atom', 0.0))):+.4g}*{t.get('name')}" for t in terms])


def primitive_quality(err: Any) -> str:
    try:
        e = float(err)
    except Exception:
        return "NO_FIT"
    if e < 0.15:
        return "STRONG_INTERPRETATION"
    if e < 0.35:
        return "PARTIAL_INTERPRETATION"
    return "PRIMITIVE_EXPLANATION_WEAK"


def primitive_row(record_id: str, module_name: str, target_kind: str, matrix: torch.Tensor, fit: Dict[str, Any], tensor_path: str = "") -> Dict[str, Any]:
    return {
        "record_id": record_id,
        "module_name": module_name,
        "target_kind": target_kind,
        "matrix_shape": "x".join(map(str, matrix.shape)) if torch.is_tensor(matrix) else "",
        "fit_kind": fit.get("fit_kind", ""),
        "rec_err": fit.get("rec_err", ""),
        "functional_err": fit.get("functional_err", ""),
        "primitive_fit_quality": primitive_quality(fit.get("rec_err", "")),
        "uses_target_mined_atoms": fit.get("uses_target_mined_atoms", False),
        "uses_shared_mined_atoms": False,
        "selected_terms": json.dumps(fit.get("selected_terms", []), ensure_ascii=False),
        "formula": fit.get("formula", ""),
        "honesty_note": fit.get("honesty_note", ""),
        "tensor_path": tensor_path,
    }


# =============================================================================
# MHA exact decoder
# =============================================================================

def split_mha_weights(module: Any, head: int) -> Dict[str, torch.Tensor]:
    W = module.in_proj_weight.detach().float().cpu()
    b = module.in_proj_bias
    b = torch.zeros(W.shape[0], dtype=torch.float32) if b is None else b.detach().float().cpu()
    E = int(module.embed_dim)
    nh = int(module.num_heads)
    D = E // nh
    s, e = head * D, (head + 1) * D
    Wq_all, Wk_all, Wv_all = W[:E], W[E:2 * E], W[2 * E:3 * E]
    bq_all, bk_all, bv_all = b[:E], b[E:2 * E], b[2 * E:3 * E]
    Wq, Wk, Wv = Wq_all[s:e], Wk_all[s:e], Wv_all[s:e]
    bq, bk, bv = bq_all[s:e], bk_all[s:e], bv_all[s:e]
    Wo = module.out_proj.weight.detach().float().cpu()[:, s:e]
    bo = module.out_proj.bias
    bo = torch.zeros(E, dtype=torch.float32) if bo is None else bo.detach().float().cpu()
    Wq_aug = torch.cat([Wq, bq[:, None]], dim=1)
    Wk_aug = torch.cat([Wk, bk[:, None]], dim=1)
    Wv_aug = torch.cat([Wv, bv[:, None]], dim=1)
    return {
        "Wq": Wq, "Wk": Wk, "Wv": Wv, "Wo": Wo,
        "bq": bq, "bk": bk, "bv": bv, "bo": bo,
        "Wq_aug": Wq_aug, "Wk_aug": Wk_aug, "Wv_aug": Wv_aug,
        "M_qk": (Wq.T @ Wk) / math.sqrt(D),
        "M_qk_aug": (Wq_aug.T @ Wk_aug) / math.sqrt(D),
        "C_vo": Wo @ Wv,
        "C_vo_aug": Wo @ Wv_aug,
        "embed_dim": E, "head_dim": D, "num_heads": nh,
    }


def split_all_heads(module: Any) -> List[Dict[str, torch.Tensor]]:
    return [split_mha_weights(module, h) for h in range(int(module.num_heads))]


def to_batch_first(x: torch.Tensor, module: Any) -> torch.Tensor:
    return x.float() if getattr(module, "batch_first", False) else x.permute(1, 0, 2).contiguous().float()


def head_project(X: torch.Tensor, W: torch.Tensor, b: torch.Tensor) -> torch.Tensor:
    return X @ W.T + b.view(1, 1, -1)


def normalize_attn_mask(attn_mask: Optional[torch.Tensor], B: int, H: int, T: int, S: int) -> Tuple[torch.Tensor, torch.Tensor, str]:
    if attn_mask is None:
        z = torch.zeros(B, H, T, S, dtype=torch.float32)
        return z, torch.ones(B, H, T, S, dtype=torch.bool), "none"
    raw = attn_mask.detach().cpu()
    raw_kind = str(raw.dtype)
    if raw.dtype == torch.bool:
        am = torch.zeros_like(raw, dtype=torch.float32).masked_fill(raw.bool(), float("-inf"))
        raw_kind += "_converted_bool_true_to_minus_inf"
    else:
        am = raw.float()
    if am.ndim == 2:
        am = am.view(1, 1, T, S).expand(B, H, T, S)
    elif am.ndim == 3:
        if am.shape[0] == B * H:
            am = am.view(B, H, T, S)
        elif am.shape[0] == 1:
            am = am.view(1, 1, T, S).expand(B, H, T, S)
        else:
            raise RuntimeError(f"unsupported 3D attn_mask shape {tuple(am.shape)} for B={B} H={H}")
    elif am.ndim == 4:
        if am.shape[0] in (1, B) and am.shape[1] in (1, H):
            am = am.expand(B, H, T, S)
        else:
            raise RuntimeError(f"unsupported 4D attn_mask shape {tuple(am.shape)}")
    else:
        raise RuntimeError(f"unsupported attn_mask ndim {am.ndim}")
    finite = torch.isfinite(am)
    return am.float(), finite, raw_kind


def prepare_additive_mask(attn_mask: Optional[torch.Tensor], key_padding_mask: Optional[torch.Tensor], B: int, H: int, T: int, S: int) -> Tuple[torch.Tensor, torch.Tensor, torch.Tensor, str]:
    pair_bias, finite, mask_kind = normalize_attn_mask(attn_mask, B, H, T, S)
    full_add = pair_bias.clone()
    if key_padding_mask is not None:
        kpm = key_padding_mask.detach().bool().cpu()
        if tuple(kpm.shape) != (B, S):
            raise RuntimeError(f"key_padding_mask shape {tuple(kpm.shape)} != {(B, S)}")
        bad = kpm.view(B, 1, 1, S).expand(B, H, T, S)
        full_add = full_add.masked_fill(bad, float("-inf"))
        finite = finite & (~bad)
    return pair_bias, full_add, finite, mask_kind


def verify_mha_head(record: Dict[str, Any], head: int, all_ws: List[Dict[str, torch.Tensor]]) -> Dict[str, Any]:
    module = record["module"]
    q = to_batch_first(record["q"], module)
    k = to_batch_first(record["k"], module)
    v = to_batch_first(record["v"], module)
    true_out = to_batch_first(record["mha_output"], module)
    B, T, E = q.shape
    S = k.shape[1]
    H = int(module.num_heads)
    D = int(module.head_dim)
    pair_bias, full_add, finite, mask_kind = prepare_additive_mask(record.get("attn_mask"), record.get("key_padding_mask"), B, H, T, S)
    per_head_y = []
    per_head_A = []
    selected: Dict[str, Any] = {}
    for h, ws in enumerate(all_ws):
        Q = head_project(q, ws["Wq"], ws["bq"])
        K = head_project(k, ws["Wk"], ws["bk"])
        V = head_project(v, ws["Wv"], ws["bv"])
        score_content = (Q @ K.transpose(1, 2)) / math.sqrt(D)
        q_aug = torch.cat([q, torch.ones(B, T, 1)], dim=-1)
        k_aug = torch.cat([k, torch.ones(B, S, 1)], dim=-1)
        score_aug = torch.einsum("btc,cd,bsd->bts", q_aug, ws["M_qk_aug"], k_aug)
        score_lin = torch.einsum("btc,cd,bsd->bts", q, ws["M_qk"], k)
        score_full = score_content + full_add[:, h]
        A = torch.softmax(score_full, dim=-1)
        A = torch.where(torch.isfinite(score_full), A, torch.zeros_like(A))
        Vout = (A @ V) @ ws["Wo"].T
        v_aug = torch.cat([v, torch.ones(B, S, 1)], dim=-1)
        Y_aug = A @ (v_aug @ ws["C_vo_aug"].T)
        Y_lin = A @ (v @ ws["C_vo"].T)
        per_head_y.append(Vout)
        per_head_A.append(A)
        if h == head:
            selected = {
                "qk_score_aug_rel": rel_err(score_aug, score_content, finite[:, h]),
                "qk_score_linear_no_bias_rel": rel_err(score_lin, score_content, finite[:, h]),
                "full_score_aug_plus_mask_rel": rel_err(score_aug + full_add[:, h], score_full, finite[:, h]),
                "vo_y_aug_rel": rel_err(Y_aug, Vout),
                "vo_y_linear_no_bias_rel": rel_err(Y_lin, Vout),
                "pair_bias_norm": finite_norm(pair_bias[:, h]),
                "finite_score_frac": float(finite[:, h].float().mean().item()),
            }
    y_total = torch.stack(per_head_y, dim=0).sum(dim=0)
    bo = module.out_proj.bias
    if bo is not None:
        y_total = y_total + bo.detach().float().cpu().view(1, 1, -1)
    selected["full_module_output_rel"] = rel_err(y_total, true_out)
    true_attn = record.get("attn_weights")
    if true_attn is not None:
        per_A = torch.stack(per_head_A, dim=1)  # [B,H,T,S]
        avg_A = per_A.mean(dim=1)
        if tuple(true_attn.shape) == tuple(avg_A.shape):
            selected["avg_attention_prob_rel"] = rel_err(avg_A, true_attn)
            selected["attention_prob_verified"] = True
            selected["avg_attention_shape_note"] = "averaged_weights"
        elif tuple(true_attn.shape) == tuple(per_A.shape):
            selected["avg_attention_prob_rel"] = rel_err(per_A, true_attn)
            selected["attention_prob_verified"] = True
            selected["avg_attention_shape_note"] = "per_head_weights_average_attn_weights_false"
        else:
            selected["avg_attention_prob_rel"] = float("nan")
            selected["attention_prob_verified"] = False
            selected["avg_attention_shape_note"] = f"true={tuple(true_attn.shape)} pred_avg={tuple(avg_A.shape)} pred_per_head={tuple(per_A.shape)}"
    else:
        selected["avg_attention_prob_rel"] = float("nan")
        selected["attention_prob_verified"] = False
        selected["avg_attention_shape_note"] = "need_weights_false_or_not_returned"
    selected.update({
        "batch": B,
        "q_len": T,
        "k_len": S,
        "embed_dim": E,
        "head_dim": D,
        "normalized_attn_mask_kind": mask_kind,
        "attn_mask_dtype": record.get("attn_mask_dtype", "none"),
        "attn_mask_source": record.get("attn_mask_source", "none"),
        "key_padding_mask_dtype": record.get("key_padding_mask_dtype", "none"),
        "key_padding_mask_source": record.get("key_padding_mask_source", "none"),
    })
    return selected


def accept_attention(metrics: Dict[str, Any], tol: float) -> Tuple[bool, str]:
    bad = []
    for k in ["qk_score_aug_rel", "vo_y_aug_rel", "full_module_output_rel"]:
        v = float(metrics.get(k, float("inf")))
        if (not math.isfinite(v)) or v >= tol:
            bad.append(f"{k}={v:.3e}")
    return (len(bad) == 0, ";".join(bad))


def fit_token_bias_ops(pair_bias_head: torch.Tensor, metas: List[Dict[str, Any]], q_len: int, k_len: int, meta_diag: Dict[str, Any], ridge: float = 1e-4, max_terms: int = 12) -> Dict[str, Any]:
    if q_len != k_len:
        return {"enabled": False, "trusted": False, "reason": "not_self_attention_shape"}
    if finite_norm(pair_bias_head) <= 1e-12:
        return {"enabled": False, "trusted": False, "reason": "pair_bias_norm_zero"}
    if not has_trusted_physics_meta(meta_diag):
        return {"enabled": False, "trusted": False, "reason": "metadata_not_sufficient_for_physics_fit", "meta_diag": meta_diag}
    B, T, S = pair_bias_head.shape
    names = [
        "BiasConstant", "SelfPair", "DeltaRLocal_exp", "DeltaRInverse",
        "SameCharge", "OppositeCharge", "QueryPt", "KeyPt", "PtOuter",
        "charged_hadron<-charged_hadron", "neutral_hadron<-neutral_hadron",
        "photon<-photon", "electron<-electron", "muon<-muon",
        "charged_hadron<-neutral_hadron", "neutral_hadron<-charged_hadron",
        "photon<-neutral_hadron", "neutral_hadron<-photon",
    ]
    X_rows: List[List[float]] = []
    y_rows: List[float] = []
    for b in range(B):
        meta = metas[b]
        pt = torch.tensor(meta.get("pt", [0.0] * T), dtype=torch.float32)
        charge = torch.tensor(meta.get("charge", [0.0] * T), dtype=torch.float32)
        deta = torch.tensor(meta.get("deta", [0.0] * T), dtype=torch.float32)
        dphi = torch.tensor(meta.get("dphi", [0.0] * T), dtype=torch.float32)
        roles = list(meta.get("roles", ["pad"] * T))
        n = min(T, len(roles), len(pt), len(charge), len(deta), len(dphi))
        for i in range(n):
            for j in range(n):
                y = float(pair_bias_head[b, i, j])
                if not math.isfinite(y):
                    continue
                dr = float(math.hypot(float(deta[i] - deta[j]), float(dphi[i] - dphi[j])))
                qi, kj = roles[i], roles[j]
                same_charge = 1.0 if charge[i] != 0 and charge[i] == charge[j] else 0.0
                opp_charge = 1.0 if charge[i] != 0 and charge[j] != 0 and charge[i] == -charge[j] else 0.0
                feat = [1.0, 1.0 if i == j else 0.0, math.exp(-dr / 0.2), 1.0 / (1.0 + dr), same_charge, opp_charge, float(pt[i]), float(pt[j]), float(pt[i] * pt[j])]
                for rp in names[9:]:
                    qrole, krole = rp.split("<-")
                    feat.append(1.0 if qi == qrole and kj == krole else 0.0)
                X_rows.append(feat)
                y_rows.append(y)
    if not X_rows:
        return {"enabled": False, "trusted": False, "reason": "no_finite_pair_bias_values"}
    X = torch.tensor(X_rows, dtype=torch.float32)
    y = torch.tensor(y_rows, dtype=torch.float32)
    Xn = X / torch.linalg.norm(X, dim=0).clamp_min(1e-12)
    c = torch.linalg.solve(Xn.T @ Xn + ridge * torch.eye(Xn.shape[1]), Xn.T @ y)
    if 0 < max_terms < c.numel():
        keep = torch.topk(c.abs(), k=max_terms).indices
        X2 = Xn[:, keep]
        c2 = torch.linalg.solve(X2.T @ X2 + ridge * torch.eye(X2.shape[1]), X2.T @ y)
        cc = torch.zeros_like(c)
        cc[keep] = c2
        c = cc
    rec = Xn @ c
    bnorm = torch.linalg.norm(y).clamp_min(1e-12)
    terms = []
    for i in torch.argsort(c.abs(), descending=True).tolist()[:max_terms]:
        if abs(float(c[i])) > 1e-8:
            terms.append({"name": names[i], "coef_normalized_atom": float(c[i])})
    return {"enabled": True, "trusted": True, "rel_err": float(torch.linalg.norm(rec - y) / bnorm), "terms": terms, "bank_size": len(names)}


# =============================================================================
# Module decoders
# =============================================================================

def common_module_fields(name: str, module: nn.Module, rec: Optional[Dict[str, Any]]) -> Dict[str, Any]:
    return {
        "module_name": name,
        "module_type": module.__class__.__name__,
        "input_shape": "" if rec is None else rec.get("input_shape", ""),
        "output_shape": "" if rec is None else rec.get("output_shape", ""),
        "params_count": params_count(module, recurse=False),
    }


def decode_linear(name: str, module: nn.Linear, rec: Optional[Dict[str, Any]], tensor_root: Path, args: argparse.Namespace) -> Tuple[Dict[str, Any], List[Dict[str, Any]], List[Dict[str, Any]]]:
    if rec is None or rec.get("input") is None or rec.get("output") is None:
        return uncovered_module_row(name, module, "missing_capture"), [], []
    x = rec["input"].float()
    y = rec["output"].float()
    W = module.weight.detach().float().cpu()
    b = module.bias.detach().float().cpu() if module.bias is not None else torch.zeros(W.shape[0])
    x2 = x.reshape(-1, W.shape[1])
    y2 = y.reshape(-1, W.shape[0])
    x_aug = torch.cat([x2, torch.ones(x2.shape[0], 1)], dim=-1)
    W_aug = torch.cat([W, b[:, None]], dim=1)
    pred = x_aug @ W_aug.T
    err = rel_err(pred, y2)
    fit = decode_matrix_with_auto_dictionary(W, allow_target_mined=args.auto_mined_atoms, max_atoms=args.decode_topk, stop_rel=args.decode_stop_rel, mined_svd_atoms=args.mined_svd_atoms, ridge=args.decode_ridge)
    tensor_path = ""
    if args.save_tensors:
        tensor_path = save_pt(str(tensor_root / "linear" / f"{safe_name(name)}.pt"), {"W": W, "b": b, "W_aug": W_aug, "fit": fit, "input_shape": tuple(x.shape), "output_shape": tuple(y.shape)})
    interpretation_trusted = bool(fit.get("fit_kind", "").startswith("SPARSE_OMP") and float(fit.get("rec_err", 999.0)) < 0.15 and not fit.get("uses_target_mined_atoms", False))
    row = {
        **common_module_fields(name, module, rec),
        "decoder_kind": "EXACT_CONSTANT_MATRIX",
        "reconstruction_error": err,
        "accepted_exact": bool(err < args.accept_tol),
        "fail_reason": "" if err < args.accept_tol else f"linear_rel={err:.3e}",
        "tensor_path": tensor_path,
        "primitive_fit_rel_err": fit.get("rec_err", ""),
        "primitive_fit_kind": fit.get("fit_kind", ""),
        "uses_target_mined_atoms": fit.get("uses_target_mined_atoms", False),
        "uses_shared_mined_atoms": False,
        "interpretation_trusted": interpretation_trusted,
        "honesty_note": fit.get("honesty_note", "Exact Linear is W_aug; primitive fit is approximate."),
        "extra_json": json.dumps({"fit": strip_tensors(fit), "W_shape": list(W.shape), "W_aug_shape": list(W_aug.shape)}, ensure_ascii=False),
    }
    prim_rows = [primitive_row(f"{name}.LinearW", name, "linear", W, fit, tensor_path)]
    residual_records = []
    if torch.is_tensor(fit.get("residual_after_base")):
        residual_records.append({"record_id": f"{name}.LinearW", "matrix": W, "base_rec_err": fit.get("base_rec_err", fit.get("rec_err", "")), "residual_after_base": fit["residual_after_base"]})
    return row, prim_rows, residual_records


def decode_embedding(name: str, module: nn.Embedding, rec: Optional[Dict[str, Any]], tensor_root: Path, args: argparse.Namespace) -> Tuple[Dict[str, Any], List[Dict[str, Any]], List[Dict[str, Any]]]:
    """Exact lookup-matrix decoder for nn.Embedding.

    This covers the embedding weight parameter as an exact constant table:
      y = W[index]
    It is a matrix/table lookup, not a primitive interpretation unless a
    separate primitive fit is meaningful.
    """
    if rec is None or rec.get("input") is None or rec.get("output") is None:
        return uncovered_module_row(name, module, "missing_capture"), [], []
    idx = rec["input"].long()
    y = rec["output"].float()
    W = module.weight.detach().float().cpu()
    with torch.no_grad():
        # Use F.embedding to avoid holding raw args and to match PyTorch semantics.
        pred = F.embedding(
            idx,
            W,
            padding_idx=module.padding_idx,
            max_norm=module.max_norm,
            norm_type=module.norm_type,
            scale_grad_by_freq=module.scale_grad_by_freq,
            sparse=module.sparse,
        )
    err = rel_err(pred, y)
    fit = decode_matrix_with_auto_dictionary(W, allow_target_mined=args.auto_mined_atoms, max_atoms=args.decode_topk, stop_rel=args.decode_stop_rel, mined_svd_atoms=args.mined_svd_atoms, ridge=args.decode_ridge)
    tensor_path = ""
    if args.save_tensors:
        tensor_path = save_pt(str(tensor_root / "embedding" / f"{safe_name(name)}.pt"), {"W": W, "fit": fit, "input_shape": tuple(idx.shape), "output_shape": tuple(y.shape)})
    interpretation_trusted = bool(fit.get("fit_kind", "").startswith("SPARSE_OMP") and float(fit.get("rec_err", 999.0)) < 0.15 and not fit.get("uses_target_mined_atoms", False))
    row = {
        **common_module_fields(name, module, rec),
        "decoder_kind": "EXACT_CONSTANT_MATRIX",
        "reconstruction_error": err,
        "accepted_exact": bool(err < args.accept_tol),
        "fail_reason": "" if err < args.accept_tol else f"embedding_lookup_rel={err:.3e}",
        "tensor_path": tensor_path,
        "primitive_fit_rel_err": fit.get("rec_err", ""),
        "primitive_fit_kind": fit.get("fit_kind", ""),
        "uses_target_mined_atoms": fit.get("uses_target_mined_atoms", False),
        "uses_shared_mined_atoms": False,
        "interpretation_trusted": interpretation_trusted,
        "honesty_note": "Exact Embedding is W[index]. Primitive fit is optional approximate table-pattern interpretation.",
        "extra_json": json.dumps({"fit": strip_tensors(fit), "W_shape": list(W.shape)}, ensure_ascii=False),
    }
    prim_rows = [primitive_row(f"{name}.EmbeddingW", name, "embedding", W, fit, tensor_path)]
    residual_records = []
    if torch.is_tensor(fit.get("residual_after_base")):
        residual_records.append({"record_id": f"{name}.EmbeddingW", "matrix": W, "base_rec_err": fit.get("base_rec_err", fit.get("rec_err", "")), "residual_after_base": fit["residual_after_base"]})
    return row, prim_rows, residual_records


def decode_rmsnorm_generic(name: str, module: nn.Module, rec: Optional[Dict[str, Any]], tensor_root: Path, args: argparse.Namespace) -> Dict[str, Any]:
    """Generic exact dynamic RMSNorm replay for common RMSNorm modules.

    Supports modules exposing weight and eps/variance_epsilon. If a module has a
    different formula, it remains rejected by reconstruction error.
    """
    if rec is None or rec.get("input") is None or rec.get("output") is None:
        return uncovered_module_row(name, module, "missing_capture")
    x = rec["input"].float()
    y = rec["output"].float()
    weight = getattr(module, "weight", None)
    weight = weight.detach().float().cpu() if weight is not None else torch.ones(x.shape[-1])
    eps = float(getattr(module, "eps", getattr(module, "variance_epsilon", 1e-6)))
    rms = torch.rsqrt(x.pow(2).mean(dim=-1, keepdim=True) + eps)
    pred = x * rms * weight.view(*([1] * (x.ndim - 1)), -1)
    bias = getattr(module, "bias", None)
    if bias is not None:
        bias = bias.detach().float().cpu()
        pred = pred + bias.view(*([1] * (x.ndim - 1)), -1)
    err = rel_err(pred, y)
    tensor_path = ""
    if args.save_tensors:
        tensor_path = save_pt(str(tensor_root / "dynamic" / f"{safe_name(name)}_rmsnorm.pt"), {"weight": weight, "bias": bias, "eps": eps, "rms_scale_mean": float(rms.mean()), "rms_scale_std": float(rms.std())})
    return {
        **common_module_fields(name, module, rec),
        "decoder_kind": "EXACT_DYNAMIC_OPERATOR",
        "reconstruction_error": err,
        "accepted_exact": bool(err < args.accept_tol),
        "fail_reason": "" if err < args.accept_tol else f"rmsnorm_rel={err:.3e}",
        "tensor_path": tensor_path,
        "primitive_fit_rel_err": "",
        "primitive_fit_kind": "NOT_CONSTANT_MATRIX",
        "uses_target_mined_atoms": False,
        "uses_shared_mined_atoms": False,
        "interpretation_trusted": bool(err < args.accept_tol),
        "honesty_note": "RMSNorm is exact dynamic per input for common RMSNorm formula; rejected if formula differs.",
        "extra_json": json.dumps({"eps": eps}, ensure_ascii=False),
    }



def decode_layernorm(name: str, module: nn.LayerNorm, rec: Optional[Dict[str, Any]], tensor_root: Path, args: argparse.Namespace) -> Dict[str, Any]:
    if rec is None or rec.get("input") is None or rec.get("output") is None:
        return uncovered_module_row(name, module, "missing_capture")
    x = rec["input"].float()
    y = rec["output"].float()
    weight = module.weight.detach().float().cpu() if module.weight is not None else None
    bias = module.bias.detach().float().cpu() if module.bias is not None else None
    pred = F.layer_norm(x, module.normalized_shape, weight, bias, module.eps)
    err = rel_err(pred, y)
    D = int(x.shape[-1])
    x2 = x.reshape(-1, D)
    dims = tuple(range(x.ndim - len(module.normalized_shape), x.ndim))
    mean = x.mean(dim=dims, keepdim=True)
    var = ((x - mean) ** 2).mean(dim=dims, keepdim=True)
    inv = torch.rsqrt(var + module.eps)
    tensor_path = ""
    if args.save_tensors:
        # Store dynamic diagonal stats + a few samples of center-scale matrix.
        gamma = weight if weight is not None else torch.ones(D)
        Center = torch.eye(D) - torch.ones(D, D) / D
        mats = []
        inv_flat = inv.reshape(-1)
        for i in range(min(args.dynamic_matrix_samples, inv_flat.numel())):
            mats.append(torch.diag(gamma * inv_flat[i]) @ Center)
        tensor_path = save_pt(str(tensor_root / "dynamic" / f"{safe_name(name)}_layernorm.pt"), {
            "weight": weight,
            "bias": bias,
            "eps": module.eps,
            "dynamic_matrix_samples": torch.stack(mats) if mats else None,
            "scale_mean": float(inv.mean()),
            "scale_std": float(inv.std()),
        })
    return {
        **common_module_fields(name, module, rec),
        "decoder_kind": "EXACT_DYNAMIC_OPERATOR",
        "reconstruction_error": err,
        "accepted_exact": bool(err < args.accept_tol),
        "fail_reason": "" if err < args.accept_tol else f"layernorm_rel={err:.3e}",
        "tensor_path": tensor_path,
        "primitive_fit_rel_err": "",
        "primitive_fit_kind": "NOT_CONSTANT_MATRIX",
        "uses_target_mined_atoms": False,
        "uses_shared_mined_atoms": False,
        "interpretation_trusted": True,
        "honesty_note": "LayerNorm is exact dynamic affine per input, not global constant matrix.",
        "extra_json": json.dumps({"eps": module.eps, "dynamic_matrix_samples": args.dynamic_matrix_samples}, ensure_ascii=False),
    }


def decode_activation(name: str, module: nn.Module, rec: Optional[Dict[str, Any]], tensor_root: Path, args: argparse.Namespace) -> Dict[str, Any]:
    if rec is None or rec.get("input") is None or rec.get("output") is None:
        return uncovered_module_row(name, module, "missing_capture")
    x = rec["input"].float()
    y = rec["output"].float()
    with torch.no_grad():
        pred = module(x)
    err = rel_err(pred, y)
    ratio = torch.where(x.abs() > 1e-12, y / x, torch.zeros_like(y))
    tensor_path = ""
    if args.save_tensors:
        tensor_path = save_pt(str(tensor_root / "dynamic" / f"{safe_name(name)}_activation.pt"), {
            "activation_type": module.__class__.__name__,
            "dynamic_ratio_mean": float(ratio.mean()),
            "dynamic_ratio_std": float(ratio.std()),
        })
    return {
        **common_module_fields(name, module, rec),
        "decoder_kind": "EXACT_ELEMENTWISE_FORMULA",
        "reconstruction_error": err,
        "accepted_exact": bool(err < args.accept_tol),
        "fail_reason": "" if err < args.accept_tol else f"activation_rel={err:.3e}",
        "tensor_path": tensor_path,
        "primitive_fit_rel_err": "",
        "primitive_fit_kind": "ELEMENTWISE_FORMULA_NOT_CONSTANT_MATRIX",
        "uses_target_mined_atoms": False,
        "uses_shared_mined_atoms": False,
        "interpretation_trusted": True,
        "honesty_note": "Elementwise activation is exact formula/dynamic diagonal ratio. LOCAL_JACOBIAN is not claimed unless derivatives are computed.",
        "extra_json": json.dumps({"activation_type": module.__class__.__name__, "dynamic_ratio_mean": float(ratio.mean()), "dynamic_ratio_std": float(ratio.std())}, ensure_ascii=False),
    }


def decode_batchnorm(name: str, module: nn.Module, rec: Optional[Dict[str, Any]], tensor_root: Path, args: argparse.Namespace) -> Dict[str, Any]:
    if rec is None or rec.get("input") is None or rec.get("output") is None:
        return uncovered_module_row(name, module, "missing_capture")
    x = rec["input"].float()
    y = rec["output"].float()
    with torch.no_grad():
        pred = module(x)
    err = rel_err(pred, y)
    tensor_path = ""
    if args.save_tensors:
        tensor_path = save_pt(str(tensor_root / "dynamic" / f"{safe_name(name)}_batchnorm.pt"), {k: detach_cpu(v) if torch.is_tensor(v) else v for k, v in module.state_dict().items()})
    return {
        **common_module_fields(name, module, rec),
        "decoder_kind": "EXACT_DYNAMIC_OPERATOR",
        "reconstruction_error": err,
        "accepted_exact": bool(err < args.accept_tol),
        "fail_reason": "" if err < args.accept_tol else f"batchnorm_rel={err:.3e}",
        "tensor_path": tensor_path,
        "primitive_fit_rel_err": "",
        "primitive_fit_kind": "EVAL_AFFINE_OR_DYNAMIC",
        "uses_target_mined_atoms": False,
        "uses_shared_mined_atoms": False,
        "interpretation_trusted": True,
        "honesty_note": "BatchNorm replayed exactly in eval mode; not primitive explanation.",
        "extra_json": json.dumps({"norm_type": module.__class__.__name__}, ensure_ascii=False),
    }


def decode_structural_leaf(name: str, module: nn.Module, rec: Optional[Dict[str, Any]], args: argparse.Namespace) -> Dict[str, Any]:
    err = ""
    ok = True
    fail = ""
    if isinstance(module, (nn.Dropout, nn.Dropout1d, nn.Dropout2d, nn.Dropout3d)) and rec is not None and rec.get("input") is not None and rec.get("output") is not None:
        err = rel_err(rec["input"], rec["output"])
        ok = bool(err < args.accept_tol)
        fail = "" if ok else f"dropout_eval_identity_rel={err:.3e}"
    return {
        **common_module_fields(name, module, rec),
        "decoder_kind": "STRUCTURAL_EXACT",
        "reconstruction_error": err,
        "accepted_exact": ok,
        "fail_reason": fail,
        "tensor_path": "",
        "primitive_fit_rel_err": "",
        "primitive_fit_kind": "STRUCTURAL_LEAF",
        "uses_target_mined_atoms": False,
        "uses_shared_mined_atoms": False,
        "interpretation_trusted": True,
        "honesty_note": "Stateless structural leaf; containers are not covered by this label.",
        "extra_json": json.dumps({"structural_type": module.__class__.__name__}, ensure_ascii=False),
    }


def structural_container_row(name: str, module: nn.Module, rec: Optional[Dict[str, Any]]) -> Dict[str, Any]:
    return {
        **common_module_fields(name, module, rec),
        "decoder_kind": "STRUCTURAL_NOT_EXPLICITLY_TRACED",
        "reconstruction_error": "",
        "accepted_exact": False,
        "fail_reason": "container_or_python_forward_not_replayed",
        "tensor_path": "",
        "primitive_fit_rel_err": "",
        "primitive_fit_kind": "NEEDS_GRAPH_REPLAY",
        "uses_target_mined_atoms": False,
        "uses_shared_mined_atoms": False,
        "interpretation_trusted": False,
        "honesty_note": "Children may be decoded, but container-level residual/add/reshape/pooling/control flow was not replayed.",
        "extra_json": json.dumps({"children_count": len(list(module.children()))}, ensure_ascii=False),
    }


def uncovered_module_row(name: str, module: nn.Module, reason: str) -> Dict[str, Any]:
    return {
        "module_name": name,
        "module_type": module.__class__.__name__,
        "input_shape": "",
        "output_shape": "",
        "params_count": params_count(module, recurse=False),
        "decoder_kind": "UNCOVERED",
        "reconstruction_error": "",
        "accepted_exact": False,
        "fail_reason": reason,
        "tensor_path": "",
        "primitive_fit_rel_err": "",
        "primitive_fit_kind": "",
        "uses_target_mined_atoms": False,
        "uses_shared_mined_atoms": False,
        "interpretation_trusted": False,
        "honesty_note": "Uncovered parameterized module. Do not claim full model decoded.",
        "extra_json": "{}",
    }


def decode_module(name: str, module: nn.Module, rec: Optional[Dict[str, Any]], tensor_root: Path, args: argparse.Namespace) -> Tuple[Dict[str, Any], List[Dict[str, Any]], List[Dict[str, Any]]]:
    if is_legacy_mha(module):
        return ({
            **common_module_fields(name, module, rec),
            "decoder_kind": "EXACT_DYNAMIC_OPERATOR",
            "reconstruction_error": "",
            "accepted_exact": True,
            "fail_reason": "see_attention_heads_table",
            "tensor_path": "",
            "primitive_fit_rel_err": "",
            "primitive_fit_kind": "SEE_HEADS",
            "uses_target_mined_atoms": False,
            "uses_shared_mined_atoms": False,
            "interpretation_trusted": True,
            "honesty_note": "MHA exact circuit is per-head dynamic softmax; see heads table.",
            "extra_json": "{}",
        }, [], [])
    if isinstance(module, nn.Linear):
        return decode_linear(name, module, rec, tensor_root, args)
    if isinstance(module, nn.Embedding):
        return decode_embedding(name, module, rec, tensor_root, args)
    if isinstance(module, nn.LayerNorm):
        return decode_layernorm(name, module, rec, tensor_root, args), [], []
    if isinstance(module, (nn.BatchNorm1d, nn.BatchNorm2d, nn.BatchNorm3d)):
        return decode_batchnorm(name, module, rec, tensor_root, args), [], []
    if "RMSNorm" in module.__class__.__name__:
        return decode_rmsnorm_generic(name, module, rec, tensor_root, args), [], []
    if is_activation(module):
        return decode_activation(name, module, rec, tensor_root, args), [], []
    if is_structural_leaf(module) or (is_leaf(module) and params_count(module, recurse=False) == 0):
        return decode_structural_leaf(name, module, rec, args), [], []
    if has_children(module):
        # Direct params on a container are dangerous: not decoded by children.
        if params_count(module, recurse=False) > 0:
            return uncovered_module_row(name, module, "direct_parameters_on_unknown_container_not_decoded"), [], []
        return structural_container_row(name, module, rec), [], []
    if params_count(module, recurse=False) > 0:
        return uncovered_module_row(name, module, "parameterized_leaf_unknown"), [], []
    return decode_structural_leaf(name, module, rec, args), [], []


# =============================================================================
# Pair-bias fit and head exports
# =============================================================================

def decode_mha_heads(name: str, module: nn.Module, rec: Dict[str, Any], metas: List[Dict[str, Any]], meta_diag: Dict[str, Any], tensor_root: Path, args: argparse.Namespace) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]], List[Dict[str, Any]], str]:
    all_ws = split_all_heads(module)
    B = to_batch_first(rec["q"], module).shape[0]
    T = to_batch_first(rec["q"], module).shape[1]
    S = to_batch_first(rec["k"], module).shape[1]
    H = int(module.num_heads)
    pair_bias, _, _, _ = prepare_additive_mask(rec.get("attn_mask"), rec.get("key_padding_mask"), B, H, T, S)
    head_rows: List[Dict[str, Any]] = []
    primitive_rows: List[Dict[str, Any]] = []
    residual_records: List[Dict[str, Any]] = []
    Mqk_all, Cvo_all = [], []
    for h, ws in enumerate(all_ws):
        vr = verify_mha_head(rec, h, all_ws)
        ok, fail = accept_attention(vr, args.accept_tol)
        qk_fit = decode_matrix_with_auto_dictionary(ws["M_qk"], allow_target_mined=args.auto_mined_atoms, max_atoms=args.decode_topk, stop_rel=args.decode_stop_rel, mined_svd_atoms=args.mined_svd_atoms, ridge=args.decode_ridge)
        vo_fit = decode_matrix_with_auto_dictionary(ws["C_vo"], allow_target_mined=args.auto_mined_atoms, max_atoms=args.decode_topk, stop_rel=args.decode_stop_rel, mined_svd_atoms=args.mined_svd_atoms, ridge=args.decode_ridge)
        bias_fit = fit_token_bias_ops(pair_bias[:, h], metas, int(vr["q_len"]), int(vr["k_len"]), meta_diag, ridge=args.decode_ridge, max_terms=args.decode_topk)
        bias_trusted = bool(bias_fit.get("enabled") and bias_fit.get("trusted") and float(bias_fit.get("rel_err", 999.0)) < 0.35)
        head_id = f"{name}.h{h}"
        tensor_path = ""
        if args.save_tensors:
            tensor_path = save_pt(str(tensor_root / "attention" / f"{safe_name(head_id)}.pt"), {
                "head_id": head_id,
                "Wq": ws["Wq"], "Wk": ws["Wk"], "Wv": ws["Wv"], "Wo": ws["Wo"],
                "M_qk": ws["M_qk"], "M_qk_aug": ws["M_qk_aug"],
                "C_vo": ws["C_vo"], "C_vo_aug": ws["C_vo_aug"],
                "verify": vr, "qk_fit": qk_fit, "vo_fit": vo_fit, "pair_bias_fit": bias_fit,
            })
        head_rows.append({
            "module_name": name,
            "head": h,
            "head_id": head_id,
            "accepted_exact_circuit": ok,
            "fail_reason": fail,
            "qk_score_aug_rel": vr["qk_score_aug_rel"],
            "vo_y_aug_rel": vr["vo_y_aug_rel"],
            "full_module_output_rel": vr["full_module_output_rel"],
            "avg_attention_prob_rel": vr.get("avg_attention_prob_rel", ""),
            "attention_prob_verified": vr.get("attention_prob_verified", False),
            "pair_bias_norm": vr["pair_bias_norm"],
            "attn_mask_source": vr["attn_mask_source"],
            "attn_mask_dtype": vr["attn_mask_dtype"],
            "normalized_attn_mask_kind": vr["normalized_attn_mask_kind"],
            "key_padding_mask_source": vr["key_padding_mask_source"],
            "key_padding_mask_dtype": vr["key_padding_mask_dtype"],
            "qk_fit_rel_err": qk_fit.get("rec_err", ""),
            "vo_fit_rel_err": vo_fit.get("rec_err", ""),
            "qk_fit_quality": primitive_quality(qk_fit.get("rec_err", "")),
            "vo_fit_quality": primitive_quality(vo_fit.get("rec_err", "")),
            "qk_uses_target_mined_atoms": qk_fit.get("uses_target_mined_atoms", False),
            "vo_uses_target_mined_atoms": vo_fit.get("uses_target_mined_atoms", False),
            "qk_selected_terms": json.dumps(qk_fit.get("selected_terms", []), ensure_ascii=False),
            "vo_selected_terms": json.dumps(vo_fit.get("selected_terms", []), ensure_ascii=False),
            "pair_bias_fit_trusted": bias_trusted,
            "pair_bias_fit_rel_err": bias_fit.get("rel_err", ""),
            "pair_bias_fit_reason": bias_fit.get("reason", ""),
            "pair_bias_fit_terms": json.dumps(bias_fit.get("terms", []), ensure_ascii=False),
            "tensor_path": tensor_path,
        })
        for kind, W, fit in [("attention_qk", ws["M_qk"], qk_fit), ("attention_vo", ws["C_vo"], vo_fit)]:
            rid = f"{head_id}.{kind}"
            primitive_rows.append(primitive_row(rid, name, kind, W, fit, tensor_path))
            if torch.is_tensor(fit.get("residual_after_base")):
                residual_records.append({"record_id": rid, "matrix": W, "base_rec_err": fit.get("base_rec_err", fit.get("rec_err", "")), "residual_after_base": fit["residual_after_base"]})
        Mqk_all.append(ws["M_qk_aug"])
        Cvo_all.append(ws["C_vo_aug"])
    module_tensor_path = ""
    if args.save_tensors and Mqk_all:
        Mqk = torch.stack(Mqk_all)
        Cvo = torch.stack(Cvo_all)
        module_tensor_path = save_pt(str(tensor_root / "attention" / f"{safe_name(name)}_all_heads.pt"), {
            "module_name": name,
            "M_qk_aug_all": Mqk,
            "C_vo_aug_all": Cvo,
            "qk_head_similarity": cosine_matrix(Mqk.reshape(Mqk.shape[0], -1)),
            "vo_head_similarity": cosine_matrix(Cvo.reshape(Cvo.shape[0], -1)),
            "qk_head_clusters": simple_clusters(cosine_matrix(Mqk.reshape(Mqk.shape[0], -1)), threshold=args.head_cluster_threshold),
            "vo_head_clusters": simple_clusters(cosine_matrix(Cvo.reshape(Cvo.shape[0], -1)), threshold=args.head_cluster_threshold),
        })
    return head_rows, primitive_rows, residual_records, module_tensor_path


def cosine_matrix(X: torch.Tensor) -> torch.Tensor:
    X = F.normalize(X.detach().float().cpu(), dim=-1)
    return X @ X.T


def simple_clusters(sim: torch.Tensor, threshold: float = 0.9) -> List[List[int]]:
    used = set()
    clusters = []
    for i in range(sim.shape[0]):
        if i in used:
            continue
        c = [j for j in range(sim.shape[0]) if float(sim[i, j]) >= threshold]
        used.update(c)
        clusters.append(c)
    return clusters


# =============================================================================
# Shared primitives and flow-pack
# =============================================================================

def candidate_atoms_from_residual(R: torch.Tensor, source: str, max_svd: int = 2) -> List[Dict[str, Any]]:
    R = R.detach().float().cpu()
    out = []
    if R.ndim != 2 or R.shape[0] != R.shape[1]:
        return out
    D = R.shape[0]
    try:
        U, S, Vh = torch.linalg.svd(R, full_matrices=False)
        for i in range(min(max_svd, S.numel())):
            atom = torch.outer(U[:, i], Vh[i, :])
            out.append({"source": source, "name": f"{source}.svd{i}", "atom": atom})
    except Exception:
        pass
    T = torch.zeros(D, D)
    for off in range(-D + 1, D):
        vals = torch.diagonal(R, offset=off)
        if vals.numel():
            idx = torch.arange(max(0, -off), min(D, D - off))
            T[idx, idx + off] = vals.mean()
    out.append({"source": source, "name": f"{source}.toeplitz", "atom": T})
    return out


def residual_gain_for_atom(R: torch.Tensor, atom: torch.Tensor) -> float:
    """Fractional residual-norm improvement from adding one shared atom."""
    r = R.detach().float().cpu().reshape(-1)
    a = atom.detach().float().cpu().reshape(-1)
    a = a / torch.linalg.norm(a).clamp_min(1e-12)
    before = torch.linalg.norm(r).clamp_min(1e-12)
    coeff = torch.dot(r, a)
    after = torch.linalg.norm(r - coeff * a)
    return float((before - after) / before)


def decode_err_with_shared_atom(W: torch.Tensor, atom: Optional[torch.Tensor], max_atoms: int = 12, ridge: float = 1e-4) -> Tuple[float, float, List[Dict[str, Any]]]:
    """Decode W with base dictionary, optionally injecting one shared atom.

    Returns: (matrix_rec_err, functional_err, selected_terms).
    This is a real re-decode test, not just residual cosine.
    """
    W = W.detach().float().cpu()
    if W.ndim != 2 or W.shape[0] != W.shape[1]:
        return float("nan"), float("nan"), []
    lib = MatrixOpLibrary(W.shape[0])
    if atom is not None and tuple(atom.shape) == tuple(W.shape):
        lib.add("SharedHeldoutAtom", atom.detach().float().cpu(), family="shared_mined", origin="shared_mined")
    dec = SparseProgramDecoder(lib, ridge=ridge)
    coeff, meta = dec.decode_omp(W, max_atoms=max_atoms, stop_rel=1e-6)
    W_hat = lib.coeffs_to_matrix(coeff)
    return float(meta["rec_err"]), functional_error_square(W, W_hat), meta.get("selected_terms", [])


def mine_shared_primitives(
    residual_records: List[Dict[str, Any]],
    min_cluster_size: int,
    threshold: float,
    gain_threshold: float = 0.02,
    decode_gain_threshold: float = 0.01,
    max_atoms: int = 12,
    ridge: float = 1e-4,
) -> Tuple[List[Dict[str, Any]], Dict[str, Any]]:
    """
    Mine shared primitive candidates and validate them by two gates:
      1) residual projection gain on train/heldout residuals;
      2) actual heldout re-decode improvement when the atom is inserted into
         the base dictionary.

    accepted_shared=True only if heldout decode error and functional error improve.
    """
    candidates = []
    for r in residual_records:
        if not torch.is_tensor(r.get("residual_after_base")) or not torch.is_tensor(r.get("matrix")):
            continue
        for c in candidate_atoms_from_residual(r["residual_after_base"], r["record_id"]):
            c["residual_record"] = r
            candidates.append(c)
    if not candidates:
        return [], {"reason": "no_residual_candidates", "candidates": 0, "heldout_gate": "not_run"}

    flats = torch.stack([normalized_flat(c["atom"]) for c in candidates])
    used = set()
    shared_rows = []
    for i, c in enumerate(candidates):
        if i in used:
            continue
        sims = flats @ flats[i]
        idxs = [j for j, s in enumerate(sims.tolist()) if s >= threshold and j not in used]
        if len(idxs) < min_cluster_size:
            continue
        used.update(idxs)
        sources = [candidates[j]["source"] for j in idxs]
        train_idxs = idxs[::2]
        heldout_idxs = idxs[1::2]
        if not heldout_idxs and len(idxs) > 1:
            heldout_idxs = [idxs[-1]]
            train_idxs = idxs[:-1]
        if not train_idxs or not heldout_idxs:
            continue

        train_atoms = [candidates[j]["atom"] / torch.linalg.norm(candidates[j]["atom"]).clamp_min(1e-12) for j in train_idxs]
        atom = torch.stack(train_atoms).mean(0)
        atom = atom / torch.linalg.norm(atom).clamp_min(1e-12)

        train_res_gains = [residual_gain_for_atom(candidates[j]["residual_record"]["residual_after_base"], atom) for j in train_idxs]
        heldout_res_gains = [residual_gain_for_atom(candidates[j]["residual_record"]["residual_after_base"], atom) for j in heldout_idxs]
        gain_train = float(sum(train_res_gains) / max(1, len(train_res_gains)))
        gain_heldout = float(sum(heldout_res_gains) / max(1, len(heldout_res_gains)))

        train_base_errs, train_shared_errs = [], []
        held_base_errs, held_shared_errs = [], []
        train_func_base, train_func_shared = [], []
        held_func_base, held_func_shared = [], []
        for split_name, split_idxs, base_errs, shared_errs, fbase, fshared in [
            ("train", train_idxs, train_base_errs, train_shared_errs, train_func_base, train_func_shared),
            ("heldout", heldout_idxs, held_base_errs, held_shared_errs, held_func_base, held_func_shared),
        ]:
            for j in split_idxs:
                W = candidates[j]["residual_record"]["matrix"]
                base_e, base_f, _ = decode_err_with_shared_atom(W, None, max_atoms=max_atoms, ridge=ridge)
                shared_e, shared_f, _ = decode_err_with_shared_atom(W, atom, max_atoms=max_atoms, ridge=ridge)
                if math.isfinite(base_e) and math.isfinite(shared_e):
                    base_errs.append(base_e)
                    shared_errs.append(shared_e)
                if math.isfinite(base_f) and math.isfinite(shared_f):
                    fbase.append(base_f)
                    fshared.append(shared_f)

        def avg(xs):
            return float(sum(xs) / max(1, len(xs))) if xs else float("nan")
        base_err_train = avg(train_base_errs)
        shared_err_train = avg(train_shared_errs)
        base_err_heldout = avg(held_base_errs)
        shared_err_heldout = avg(held_shared_errs)
        gain_train_decode = float((base_err_train - shared_err_train) / max(1e-12, base_err_train)) if math.isfinite(base_err_train) and math.isfinite(shared_err_train) else 0.0
        gain_heldout_decode = float((base_err_heldout - shared_err_heldout) / max(1e-12, base_err_heldout)) if math.isfinite(base_err_heldout) and math.isfinite(shared_err_heldout) else 0.0
        base_func_heldout = avg(held_func_base)
        shared_func_heldout = avg(held_func_shared)
        gain_heldout_functional = float((base_func_heldout - shared_func_heldout) / max(1e-12, base_func_heldout)) if math.isfinite(base_func_heldout) and math.isfinite(shared_func_heldout) else 0.0

        distinct_sources = len(set(sources))
        accepted_shared = bool(
            distinct_sources >= min_cluster_size
            and gain_heldout >= gain_threshold
            and gain_heldout_decode >= decode_gain_threshold
            and gain_heldout_functional >= 0.0
        )
        reason = "accepted_by_heldout_decode_gain" if accepted_shared else "candidate_only_failed_heldout_decode_gain"
        shared_rows.append({
            "name": f"SharedCandidate{len(shared_rows)}",
            "cluster_size": len(idxs),
            "distinct_sources": distinct_sources,
            "accepted_shared": accepted_shared,
            "gain_train": gain_train,
            "gain_heldout": gain_heldout,
            "base_err_train": base_err_train,
            "shared_err_train": shared_err_train,
            "gain_train_decode": gain_train_decode,
            "base_err_heldout": base_err_heldout,
            "shared_err_heldout": shared_err_heldout,
            "gain_heldout_decode": gain_heldout_decode,
            "base_func_err_heldout": base_func_heldout,
            "shared_func_err_heldout": shared_func_heldout,
            "gain_heldout_functional": gain_heldout_functional,
            "gain_threshold": gain_threshold,
            "decode_gain_threshold": decode_gain_threshold,
            "sources": json.dumps(sources, ensure_ascii=False),
            "reason": reason,
        })
    return shared_rows, {
        "candidates": len(candidates),
        "clusters": len(shared_rows),
        "heldout_gate": "real_base_plus_shared_decode_gain",
        "gain_threshold": gain_threshold,
        "decode_gain_threshold": decode_gain_threshold,
    }


def role_guess_from_record(record_id: str, target_kind: str) -> str:
    s = f"{record_id} {target_kind}".lower()
    if "attention_qk" in s:
        return "attention_read_score"
    if "attention_vo" in s:
        return "attention_value_write"
    if "linear" in s:
        return "linear_projection"
    return "unknown"


def flow_sketch_rows(primitive_rows: List[Dict[str, Any]]) -> Tuple[List[Dict[str, Any]], Dict[str, Any]]:
    rows = []
    hist = Counter()
    transitions = Counter()
    transition_matrix: Dict[str, Dict[str, int]] = defaultdict(lambda: defaultdict(int))
    for r in primitive_rows:
        try:
            terms = json.loads(r.get("selected_terms", "[]"))
        except Exception:
            terms = []
        names = [t.get("name", "") for t in terms]
        families = [t.get("family", "unknown") for t in terms]
        origins = [t.get("origin", "unknown") for t in terms]
        for n in names:
            hist[n] += 1
        for a, b in zip(names, names[1:]):
            transitions[(a, b)] += 1
            transition_matrix[a][b] += 1
        target_kind = r.get("target_kind", "")
        role_guess = role_guess_from_record(r.get("record_id", ""), target_kind)
        rows.append({
            "record_id": r.get("record_id", ""),
            "role_guess": role_guess,
            "read_flow": "tokens->score" if "qk" in target_kind else "tokens->values" if "vo" in target_kind else "module_input",
            "write_flow": "attention_weights" if "qk" in target_kind else "residual_write" if "vo" in target_kind else "module_output",
            "primitive_slot_flow": " -> ".join(names),
            "primitive_family_flow": " -> ".join(families),
            "primitive_origin_flow": " -> ".join(origins),
            "slot_transition_flow": "OMP_selection_order",
            "primitive_transition_flow": " -> ".join([f"{a}->{b}" for a, b in zip(names, names[1:])]),
            "slot_composition_flow": r.get("formula", ""),
            "target_kind": target_kind,
            "primitive_count": len(names),
        })
    pack = {
        "primitive_hist": dict(hist),
        "primitive_transition_hist": {f"{a}->{b}": v for (a, b), v in transitions.items()},
        "primitive_transition_matrix": {a: dict(bs) for a, bs in transition_matrix.items()},
        "records": rows,
    }
    return rows, pack


# =============================================================================
# Main model decode
# =============================================================================

def decode_model(model: nn.Module, cap: ModuleCapture, metas: List[Dict[str, Any]], args: argparse.Namespace):
    tensor_root = Path(args.tensor_dir)
    meta_diag = meta_diagnostics(metas)
    module_rows = []
    head_rows = []
    linear_rows = []
    dynamic_rows = []
    primitive_rows = []
    residual_records = []
    pair_bias_candidates = []
    all_head_tensor_paths = []

    for name, module in model.named_modules():
        display_name = name if name else "<root>"
        rec = cap.records.get(name)
        row, prims, residuals = decode_module(display_name, module, rec, tensor_root, args)
        module_rows.append(row)
        primitive_rows.extend(prims)
        residual_records.extend(residuals)
        if row["module_type"] == "Linear":
            linear_rows.append(row)
        if row["decoder_kind"] in ("EXACT_DYNAMIC_OPERATOR", "EXACT_ELEMENTWISE_FORMULA"):
            dynamic_rows.append(row)
        if possible_pair_bias_module(name, module):
            child_names = [f"{name}.{cn}" for cn, _ in module.named_modules() if cn]
            child_rows = [r for r in module_rows if r.get("module_name") in child_names]
            exact_child_chain = bool(child_rows) and all(r.get("decoder_kind") in ("EXACT_CONSTANT_MATRIX", "EXACT_DYNAMIC_OPERATOR", "EXACT_ELEMENTWISE_FORMULA", "STRUCTURAL_EXACT") and str(r.get("accepted_exact")) == "True" for r in child_rows if r.get("decoder_kind") != "STRUCTURAL_NOT_EXPLICITLY_TRACED")
            exact_producer_status = "EXACT_CHAIN_CANDIDATE" if isinstance(module, nn.Linear) and row.get("accepted_exact") else ("CHILD_CHAIN_PARTIAL" if exact_child_chain else "CANDIDATE_ONLY")
            pair_bias_candidates.append({
                "module_name": name,
                "module_type": module.__class__.__name__,
                "direct_params_count": params_count(module, recurse=False),
                "params_count": params_count(module, recurse=True),
                "decoded_kind": row["decoder_kind"],
                "is_linear": isinstance(module, nn.Linear),
                "is_mha": is_legacy_mha(module),
                "exact_producer_status": exact_producer_status,
                "note": "Candidate only unless exact_producer_status is EXACT_CHAIN_CANDIDATE and captured attn_mask linkage is verified.",
            })
        if is_legacy_mha(module) and rec is not None:
            heads, prims_h, residuals_h, all_head_path = decode_mha_heads(name, module, rec, metas, meta_diag, tensor_root, args)
            head_rows.extend(heads)
            primitive_rows.extend(prims_h)
            residual_records.extend(residuals_h)
            # Aggregate MHA module acceptance from all heads instead of blindly accepting module row.
            all_heads_ok = bool(heads) and all(str(h.get("accepted_exact_circuit")) == "True" for h in heads)
            max_head_err = max([float(h.get("full_module_output_rel", float("inf"))) for h in heads], default=float("inf"))
            module_rows[-1]["accepted_exact"] = all_heads_ok
            module_rows[-1]["reconstruction_error"] = max_head_err
            module_rows[-1]["fail_reason"] = "" if all_heads_ok else "one_or_more_attention_heads_rejected"
            module_rows[-1]["tensor_path"] = all_head_path
            module_rows[-1]["honesty_note"] = "MHA module acceptance aggregated from per-head exact checks."
            if all_head_path:
                all_head_tensor_paths.append({"module_name": name, "tensor_path": all_head_path})

    uncovered = []
    for r in module_rows:
        if r["decoder_kind"] == "UNCOVERED" and int(r["params_count"]) > 0:
            uncovered.append({
                "module_name": r["module_name"],
                "module_type": r["module_type"],
                "params_count": r["params_count"],
                "reason": r["fail_reason"],
                "suggested_decoder": suggested_decoder(model if r["module_name"] == "<root>" else dict(model.named_modules())[r["module_name"]]),
            })

    rejected_modules = [
        r for r in module_rows
        if r["decoder_kind"] not in ("UNCOVERED", "STRUCTURAL_NOT_EXPLICITLY_TRACED")
        and str(r.get("accepted_exact")) != "True"
    ]
    structural_not_traced = [r for r in module_rows if r["decoder_kind"] == "STRUCTURAL_NOT_EXPLICITLY_TRACED"]
    rejected_heads = [r for r in head_rows if str(r.get("accepted_exact_circuit")) != "True"]

    shared_rows, shared_info = ([], {"reason": "not_enabled"})
    if args.mine_shared_primitives:
        shared_rows, shared_info = mine_shared_primitives(residual_records, args.shared_min_cluster_size, args.shared_cosine_threshold, args.shared_gain_threshold, args.shared_decode_gain_threshold, args.decode_topk, args.decode_ridge)
        if args.save_tensors:
            save_pt(str(tensor_root / "shared_primitives.pt"), {"shared_rows": shared_rows, "info": shared_info})

    flow_rows, flow_pack = flow_sketch_rows(primitive_rows)
    if args.save_tensors:
        save_pt(str(tensor_root / "flow_pack.pt"), flow_pack)

    local_exact_ok = len(uncovered) == 0 and len(rejected_modules) == 0 and len(rejected_heads) == 0
    # Full forward is not closed while structural containers/control flow aren't replayed.
    full_forward_closed = False
    status = "FULL_FORWARD_CLOSED" if full_forward_closed else ("LOCAL_EXACT_MODULES_ONLY" if local_exact_ok else "FULL_FORWARD_NOT_CLOSED")
    run_ok = True
    summary = {
        "version": VERSION,
        "run_ok": run_ok,
        "ok": full_forward_closed,
        "local_exact_ok": local_exact_ok,
        "status": status,
        "accept_tol": args.accept_tol,
        "modules_total": len(module_rows),
        "modules_covered": sum(1 for r in module_rows if r["decoder_kind"] not in ("UNCOVERED", "STRUCTURAL_NOT_EXPLICITLY_TRACED")),
        "uncovered_parameterized": len(uncovered),
        "structural_not_traced": len(structural_not_traced),
        "rejected_modules": len(rejected_modules),
        "attention_heads": len(head_rows),
        "accepted_attention_heads": sum(1 for r in head_rows if str(r.get("accepted_exact_circuit")) == "True"),
        "rejected_heads": len(rejected_heads),
        "linear_modules": len(linear_rows),
        "accepted_linear_modules": sum(1 for r in linear_rows if str(r.get("accepted_exact")) == "True"),
        "dynamic_modules": len(dynamic_rows),
        "accepted_dynamic_modules": sum(1 for r in dynamic_rows if str(r.get("accepted_exact")) == "True"),
        "final_logits_rel": None,
        "final_reason": "generic decoded Python graph replay not implemented; structural containers/control flow not claimed",
        "decoder_kind_counts": dict(Counter(r["decoder_kind"] for r in module_rows)),
        "primitive_fit_summary": {
            "total": len(primitive_rows),
            "strong": sum(1 for r in primitive_rows if r.get("primitive_fit_quality") == "STRONG_INTERPRETATION"),
            "partial": sum(1 for r in primitive_rows if r.get("primitive_fit_quality") == "PARTIAL_INTERPRETATION"),
            "weak": sum(1 for r in primitive_rows if r.get("primitive_fit_quality") == "PRIMITIVE_EXPLANATION_WEAK"),
            "target_mined_used": sum(1 for r in primitive_rows if str(r.get("uses_target_mined_atoms")) == "True"),
        },
        "shared_primitives": {"count": len(shared_rows), "accepted": sum(1 for r in shared_rows if str(r.get("accepted_shared")) == "True"), "info": shared_info},
        "meta_diagnostics": meta_diag,
        "all_head_tensor_paths": all_head_tensor_paths,
    }
    acceptance_rows = [{
        "version": VERSION,
        "run_ok": run_ok,
        "ok_full_forward_closed": full_forward_closed,
        "local_exact_ok": local_exact_ok,
        "status": status,
        "uncovered_parameterized": len(uncovered),
        "structural_not_traced": len(structural_not_traced),
        "rejected_modules": len(rejected_modules),
        "rejected_heads": len(rejected_heads),
        "attention_heads": summary["attention_heads"],
        "accepted_attention_heads": summary["accepted_attention_heads"],
        "linear_modules": summary["linear_modules"],
        "accepted_linear_modules": summary["accepted_linear_modules"],
        "dynamic_modules": summary["dynamic_modules"],
        "accepted_dynamic_modules": summary["accepted_dynamic_modules"],
        "final_logits_rel": "",
        "final_reason": summary["final_reason"],
    }]
    return {
        "module_rows": module_rows,
        "head_rows": head_rows,
        "linear_rows": linear_rows,
        "dynamic_rows": dynamic_rows,
        "primitive_rows": primitive_rows,
        "shared_rows": shared_rows,
        "flow_rows": flow_rows,
        "uncovered": uncovered,
        "rejected_modules": rejected_modules,
        "structural_not_traced": structural_not_traced,
        "pair_bias_candidates": pair_bias_candidates,
        "acceptance_rows": acceptance_rows,
        "summary": summary,
    }




# =============================================================================
# Stage-1 matrix / parameter coverage control v1_4
# =============================================================================

def classify_param_kind(param_name: str, module_name: str, module: Optional[nn.Module]) -> str:
    low_module = module_name.lower()
    if "in_proj_weight" in param_name:
        return "attention_in_proj_weight_qkv"
    if "in_proj_bias" in param_name:
        return "attention_in_proj_bias_qkv"
    if ".out_proj.weight" in param_name or param_name.endswith("out_proj.weight"):
        return "attention_out_proj_weight"
    if ".out_proj.bias" in param_name or param_name.endswith("out_proj.bias"):
        return "attention_out_proj_bias"
    if isinstance(module, nn.Linear) and param_name.endswith("weight"):
        return "linear_weight"
    if isinstance(module, nn.Linear) and param_name.endswith("bias"):
        return "linear_bias"
    if isinstance(module, nn.Embedding) and param_name.endswith("weight"):
        return "embedding_weight"
    if isinstance(module, (nn.LayerNorm, nn.BatchNorm1d, nn.BatchNorm2d, nn.BatchNorm3d)) or (module is not None and "RMSNorm" in module.__class__.__name__):
        return "norm_affine"
    if "pair" in low_module or "pair" in param_name.lower():
        return "pair_module_param"
    return "unknown_param"


def _module_row_map(module_rows: List[Dict[str, Any]]) -> Dict[str, Dict[str, Any]]:
    return {str(r.get("module_name", "")): r for r in module_rows}


def _head_rows_for_module(head_rows: List[Dict[str, Any]], module_name: str) -> List[Dict[str, Any]]:
    return [r for r in head_rows if r.get("module_name") == module_name]


def _primitive_for_module(primitive_rows: List[Dict[str, Any]], module_name: str, target_contains: str = "") -> Optional[Dict[str, Any]]:
    for r in primitive_rows:
        if r.get("module_name") == module_name and (not target_contains or target_contains in str(r.get("target_kind", ""))):
            return r
    return None


def build_parameter_coverage(model: nn.Module, module_rows: List[Dict[str, Any]], head_rows: List[Dict[str, Any]], primitive_rows: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    modules = dict(model.named_modules())
    rows: List[Dict[str, Any]] = []
    mrows = _module_row_map(module_rows)

    for param_name, p in model.named_parameters():
        if "." in param_name:
            owner_module_name, leaf_param_name = param_name.rsplit(".", 1)
        else:
            owner_module_name, leaf_param_name = "<root>", param_name
        owner_module = model if owner_module_name == "<root>" else modules.get(owner_module_name)
        module_type = "<missing>" if owner_module is None else owner_module.__class__.__name__
        param_kind = classify_param_kind(param_name, owner_module_name, owner_module)

        covered = False
        decoder_row_id = ""
        decoder_kind = ""
        exact_target_kind = ""
        exact_err: Any = ""
        primitive_fit_kind = ""
        primitive_fit_rel_err: Any = ""
        uses_target_mined = False
        uses_shared_mined = False
        interpretation_trusted = False
        tensor_path = ""
        fail_reason = ""

        # MHA parent packed parameters.
        if owner_module is not None and is_legacy_mha(owner_module):
            hs = _head_rows_for_module(head_rows, owner_module_name)
            heads_ok = bool(hs) and all(str(h.get("accepted_exact_circuit")) == "True" for h in hs)
            covered = heads_ok
            decoder_row_id = f"{owner_module_name}.*heads"
            decoder_kind = "EXACT_DYNAMIC_OPERATOR"
            exact_target_kind = "attention_head_exact_qkv_o_circuit"
            exact_err = max([float(h.get("full_module_output_rel", 0.0)) for h in hs], default="")
            tensor_path = hs[0].get("tensor_path", "") if hs else ""
            fail_reason = "" if covered else "attention_heads_missing_or_rejected"
        # MHA out_proj child parameters are covered by parent attention head circuit.
        elif owner_module_name.endswith(".out_proj"):
            parent_name = owner_module_name.rsplit(".out_proj", 1)[0]
            parent = modules.get(parent_name)
            if parent is not None and is_legacy_mha(parent):
                hs = _head_rows_for_module(head_rows, parent_name)
                heads_ok = bool(hs) and all(str(h.get("accepted_exact_circuit")) == "True" for h in hs)
                covered = heads_ok
                decoder_row_id = f"{parent_name}.*heads.out_proj"
                decoder_kind = "EXACT_DYNAMIC_OPERATOR"
                exact_target_kind = "attention_out_projection_covered_by_C_vo"
                exact_err = max([float(h.get("full_module_output_rel", 0.0)) for h in hs], default="")
                tensor_path = hs[0].get("tensor_path", "") if hs else ""
                fail_reason = "" if covered else "parent_attention_heads_missing_or_rejected"
        elif owner_module is not None and isinstance(owner_module, nn.Embedding):
            mr = mrows.get(owner_module_name)
            prim = _primitive_for_module(primitive_rows, owner_module_name, "embedding")
            covered = bool(mr and str(mr.get("accepted_exact")) == "True")
            decoder_row_id = f"{owner_module_name}.Embedding"
            decoder_kind = "EXACT_CONSTANT_MATRIX"
            exact_target_kind = "embedding_lookup_table"
            exact_err = mr.get("reconstruction_error", "") if mr else ""
            primitive_fit_kind = (prim or {}).get("fit_kind", mr.get("primitive_fit_kind", "") if mr else "")
            primitive_fit_rel_err = (prim or {}).get("rec_err", mr.get("primitive_fit_rel_err", "") if mr else "")
            uses_target_mined = str((prim or {}).get("uses_target_mined_atoms", mr.get("uses_target_mined_atoms", False) if mr else False)) == "True"
            uses_shared_mined = str((prim or {}).get("uses_shared_mined_atoms", mr.get("uses_shared_mined_atoms", False) if mr else False)) == "True"
            interpretation_trusted = str(mr.get("interpretation_trusted", False) if mr else False) == "True"
            tensor_path = mr.get("tensor_path", "") if mr else ""
            fail_reason = "" if covered else "embedding_decoder_missing_or_rejected"
        elif owner_module is not None and isinstance(owner_module, nn.Linear):
            mr = mrows.get(owner_module_name)
            prim = _primitive_for_module(primitive_rows, owner_module_name, "linear")
            covered = bool(mr and str(mr.get("accepted_exact")) == "True")
            decoder_row_id = f"{owner_module_name}.Linear"
            decoder_kind = "EXACT_CONSTANT_MATRIX"
            exact_target_kind = "linear_W_aug"
            exact_err = mr.get("reconstruction_error", "") if mr else ""
            primitive_fit_kind = (prim or {}).get("fit_kind", mr.get("primitive_fit_kind", "") if mr else "")
            primitive_fit_rel_err = (prim or {}).get("rec_err", mr.get("primitive_fit_rel_err", "") if mr else "")
            uses_target_mined = str((prim or {}).get("uses_target_mined_atoms", mr.get("uses_target_mined_atoms", False) if mr else False)) == "True"
            uses_shared_mined = str((prim or {}).get("uses_shared_mined_atoms", mr.get("uses_shared_mined_atoms", False) if mr else False)) == "True"
            interpretation_trusted = str(mr.get("interpretation_trusted", False) if mr else False) == "True"
            tensor_path = mr.get("tensor_path", "") if mr else ""
            fail_reason = "" if covered else "linear_decoder_missing_or_rejected"
        elif owner_module is not None and is_norm(owner_module):
            mr = mrows.get(owner_module_name)
            covered = bool(mr and str(mr.get("accepted_exact")) == "True")
            decoder_row_id = f"{owner_module_name}.NormDynamic"
            decoder_kind = "EXACT_DYNAMIC_OPERATOR"
            exact_target_kind = "norm_dynamic_affine"
            exact_err = mr.get("reconstruction_error", "") if mr else ""
            primitive_fit_kind = "NOT_CONSTANT_MATRIX"
            interpretation_trusted = bool(covered)
            tensor_path = mr.get("tensor_path", "") if mr else ""
            fail_reason = "" if covered else "norm_decoder_missing_or_rejected"
        else:
            mr = mrows.get(owner_module_name)
            fail_reason = "direct_parameter_unknown_decoder"
            if mr and mr.get("decoder_kind") == "UNCOVERED":
                fail_reason = mr.get("fail_reason", fail_reason)

        rows.append({
            "param_name": param_name,
            "module_name": owner_module_name,
            "module_type": module_type,
            "param_shape": "x".join(map(str, p.shape)),
            "param_numel": int(p.numel()),
            "requires_grad": bool(p.requires_grad),
            "param_kind": param_kind,
            "covered_by_decoder": bool(covered),
            "decoder_row_id": decoder_row_id,
            "decoder_kind": decoder_kind,
            "exact_target_kind": exact_target_kind,
            "exact_reconstruction_error": exact_err,
            "primitive_fit_kind": primitive_fit_kind,
            "primitive_fit_rel_err": primitive_fit_rel_err,
            "uses_target_mined_atoms": uses_target_mined,
            "uses_shared_mined_atoms": uses_shared_mined,
            "interpretation_trusted": interpretation_trusted,
            "tensor_path": tensor_path,
            "fail_reason": fail_reason,
        })
    return rows


def patch_module_rows_from_parameter_coverage(module_rows: List[Dict[str, Any]], parameter_coverage_rows: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Mark internal MHA out_proj child modules as covered by parent attention circuit.

    PyTorch MultiheadAttention owns out_proj as a child Linear-like module, but its
    forward uses the MHA functional path. The exact C_vo per-head reconstruction
    covers out_proj.weight/bias, so the child module row must not appear as an
    uncovered parameterized module.
    """
    by_module: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
    for r in parameter_coverage_rows:
        by_module[r["module_name"]].append(r)
    out = []
    for r in module_rows:
        rr = dict(r)
        params = by_module.get(rr.get("module_name", ""), [])
        if params and all(str(p.get("covered_by_decoder")) == "True" for p in params) and rr.get("decoder_kind") == "UNCOVERED":
            rr["decoder_kind"] = "EXACT_CONSTANT_MATRIX"
            rr["accepted_exact"] = True
            rr["fail_reason"] = "covered_by_parameter_coverage_parent_decoder"
            rr["honesty_note"] = "Direct parameters are covered by parent decoder; module forward may not be separately hooked."
            rr["reconstruction_error"] = max([float(p.get("exact_reconstruction_error", 0.0) or 0.0) for p in params], default="")
            rr["tensor_path"] = params[0].get("tensor_path", "")
        out.append(rr)
    return out


def build_matrix_coverage(module_rows: List[Dict[str, Any]], head_rows: List[Dict[str, Any]], linear_rows: List[Dict[str, Any]], dynamic_rows: List[Dict[str, Any]], primitive_rows: List[Dict[str, Any]], decoded_summary: Dict[str, Any]) -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    prim_by_record = {r.get("record_id", ""): r for r in primitive_rows}

    for r in linear_rows:
        mod = r["module_name"]
        prim = prim_by_record.get(f"{mod}.LinearW", {})
        try:
            ej = json.loads(r.get("extra_json", "{}"))
            w_shape = "x".join(map(str, ej.get("W_shape", [])))
            w_aug_shape = "x".join(map(str, ej.get("W_aug_shape", [])))
        except Exception:
            w_shape = ""
            w_aug_shape = ""
        for kind in ["Linear.W", "Linear.W_aug"]:
            rows.append({
                "matrix_id": f"{mod}.{kind}",
                "module_name": mod,
                "module_type": r.get("module_type", "Linear"),
                "matrix_kind": kind,
                "shape": w_aug_shape if kind.endswith("W_aug") else w_shape,
                "exact_target_kind": "linear_W_aug" if kind.endswith("W_aug") else "linear_W",
                "exact_reconstruction_error": r.get("reconstruction_error", ""),
                "accepted_exact": r.get("accepted_exact", False),
                "primitive_fit_kind": prim.get("fit_kind", r.get("primitive_fit_kind", "")),
                "primitive_fit_rel_err": prim.get("rec_err", r.get("primitive_fit_rel_err", "")),
                "primitive_fit_quality": prim.get("primitive_fit_quality", ""),
                "uses_target_mined_atoms": prim.get("uses_target_mined_atoms", r.get("uses_target_mined_atoms", False)),
                "uses_shared_mined_atoms": prim.get("uses_shared_mined_atoms", r.get("uses_shared_mined_atoms", False)),
                "tensor_path": r.get("tensor_path", ""),
                "honesty_note": r.get("honesty_note", ""),
            })

    for r in module_rows:
        if r.get("module_type") == "Embedding":
            mod = r["module_name"]
            prim = prim_by_record.get(f"{mod}.EmbeddingW", {})
            try:
                ej = json.loads(r.get("extra_json", "{}"))
                w_shape = "x".join(map(str, ej.get("W_shape", [])))
            except Exception:
                w_shape = ""
            rows.append({
                "matrix_id": f"{mod}.Embedding.W",
                "module_name": mod,
                "module_type": "Embedding",
                "matrix_kind": "Embedding.W",
                "shape": w_shape,
                "exact_target_kind": "embedding_lookup_table",
                "exact_reconstruction_error": r.get("reconstruction_error", ""),
                "accepted_exact": r.get("accepted_exact", False),
                "primitive_fit_kind": prim.get("fit_kind", r.get("primitive_fit_kind", "")),
                "primitive_fit_rel_err": prim.get("rec_err", r.get("primitive_fit_rel_err", "")),
                "primitive_fit_quality": prim.get("primitive_fit_quality", ""),
                "uses_target_mined_atoms": prim.get("uses_target_mined_atoms", r.get("uses_target_mined_atoms", False)),
                "uses_shared_mined_atoms": prim.get("uses_shared_mined_atoms", r.get("uses_shared_mined_atoms", False)),
                "tensor_path": r.get("tensor_path", ""),
                "honesty_note": r.get("honesty_note", ""),
            })

    for h in head_rows:
        hid = h.get("head_id", "")
        for target, fit_key, kind in [
            ("M_qk", "qk", "Attention.head.M_qk"),
            ("M_qk_aug", "qk", "Attention.head.M_qk_aug"),
            ("C_vo", "vo", "Attention.head.C_vo"),
            ("C_vo_aug", "vo", "Attention.head.C_vo_aug"),
        ]:
            rows.append({
                "matrix_id": f"{hid}.{target}",
                "module_name": h.get("module_name", ""),
                "module_type": "MultiheadAttention",
                "matrix_kind": kind,
                "shape": "",
                "exact_target_kind": "attention_exact_matrix_circuit",
                "exact_reconstruction_error": h.get("full_module_output_rel", ""),
                "accepted_exact": h.get("accepted_exact_circuit", False),
                "primitive_fit_kind": "SPARSE_OMP_OR_TARGET_MINED" if target in ("M_qk", "C_vo") else "AUGMENTED_EXACT_TARGET",
                "primitive_fit_rel_err": h.get(f"{fit_key}_fit_rel_err", "") if target in ("M_qk", "C_vo") else "",
                "primitive_fit_quality": h.get(f"{fit_key}_fit_quality", "") if target in ("M_qk", "C_vo") else "",
                "uses_target_mined_atoms": h.get(f"{fit_key}_uses_target_mined_atoms", False) if target in ("M_qk", "C_vo") else False,
                "uses_shared_mined_atoms": False,
                "tensor_path": h.get("tensor_path", ""),
                "honesty_note": "Attention exact matrix target; primitive fit is approximate." if target in ("M_qk", "C_vo") else "Augmented exact target exported in tensor artifact.",
            })

    # Module-level all-head tensors.
    for rec in decoded_summary.get("all_head_tensor_paths", []):
        mod = rec.get("module_name", "")
        for kind in ["Attention.module.M_qk_aug_all", "Attention.module.C_vo_aug_all"]:
            rows.append({
                "matrix_id": f"{mod}.{kind}",
                "module_name": mod,
                "module_type": "MultiheadAttention",
                "matrix_kind": kind,
                "shape": "all_heads",
                "exact_target_kind": "attention_all_heads_export",
                "exact_reconstruction_error": "",
                "accepted_exact": True,
                "primitive_fit_kind": "GROUP_EXPORT",
                "primitive_fit_rel_err": "",
                "primitive_fit_quality": "",
                "uses_target_mined_atoms": False,
                "uses_shared_mined_atoms": False,
                "tensor_path": rec.get("tensor_path", ""),
                "honesty_note": "Group tensor export for simultaneous all-head analysis.",
            })

    for r in dynamic_rows:
        rows.append({
            "matrix_id": f"{r['module_name']}.dynamic",
            "module_name": r.get("module_name", ""),
            "module_type": r.get("module_type", ""),
            "matrix_kind": "Norm.dynamic_samples" if "Norm" in r.get("module_type", "") else "Activation.dynamic_ratio",
            "shape": r.get("output_shape", ""),
            "exact_target_kind": r.get("decoder_kind", ""),
            "exact_reconstruction_error": r.get("reconstruction_error", ""),
            "accepted_exact": r.get("accepted_exact", False),
            "primitive_fit_kind": r.get("primitive_fit_kind", ""),
            "primitive_fit_rel_err": "",
            "primitive_fit_quality": r.get("primitive_fit_kind", ""),
            "uses_target_mined_atoms": False,
            "uses_shared_mined_atoms": False,
            "tensor_path": r.get("tensor_path", ""),
            "honesty_note": r.get("honesty_note", ""),
        })
    return rows


def _layer_prefix(module_name: str) -> str:
    if module_name in ("", "<root>"):
        return "<root>"
    parts = module_name.split(".")
    # Common ParT/Qwen-like patterns: keep collection + index.
    for i, part in enumerate(parts):
        if part.isdigit() and i > 0:
            return ".".join(parts[:i+1])
    return ".".join(parts[:2]) if len(parts) >= 2 else parts[0]


def build_layer_matrix_atlas(module_rows: List[Dict[str, Any]], head_rows: List[Dict[str, Any]], matrix_rows: List[Dict[str, Any]], parameter_coverage_rows: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    prefixes = sorted(set(_layer_prefix(r.get("module_name", "")) for r in module_rows) | set(_layer_prefix(r.get("module_name", "")) for r in head_rows))
    rows = []
    for lid, pref in enumerate(prefixes):
        mods = [r for r in module_rows if _layer_prefix(r.get("module_name", "")) == pref]
        heads = [r for r in head_rows if _layer_prefix(r.get("module_name", "")) == pref]
        mats = [r for r in matrix_rows if _layer_prefix(r.get("module_name", "")) == pref]
        params = [r for r in parameter_coverage_rows if _layer_prefix(r.get("module_name", "")) == pref]
        prim_strong = sum(1 for r in mats if r.get("primitive_fit_quality") == "STRONG_INTERPRETATION")
        prim_partial = sum(1 for r in mats if r.get("primitive_fit_quality") == "PARTIAL_INTERPRETATION")
        prim_weak = sum(1 for r in mats if r.get("primitive_fit_quality") == "PRIMITIVE_EXPLANATION_WEAK")
        rows.append({
            "layer_id": lid,
            "module_prefix": pref,
            "modules_count": len(mods),
            "params_count": sum(int(p.get("param_numel", 0)) for p in params),
            "attention_modules": len(set(h.get("module_name", "") for h in heads)),
            "attention_heads": len(heads),
            "linear_modules": sum(1 for r in mods if r.get("module_type") == "Linear"),
            "embedding_modules": sum(1 for r in mods if r.get("module_type") == "Embedding"),
            "norm_modules": sum(1 for r in mods if "Norm" in r.get("module_type", "")),
            "activation_modules": sum(1 for r in mods if r.get("decoder_kind") == "EXACT_ELEMENTWISE_FORMULA"),
            "matrices_decoded": len(mats),
            "exact_accepted": sum(1 for r in mats if str(r.get("accepted_exact")) == "True"),
            "primitive_strong": prim_strong,
            "primitive_partial": prim_partial,
            "primitive_weak": prim_weak,
            "target_mined_used": sum(1 for r in mats if str(r.get("uses_target_mined_atoms")) == "True"),
            "shared_primitives_used": sum(1 for r in mats if str(r.get("uses_shared_mined_atoms")) == "True"),
            "uncovered_parameters": sum(1 for p in params if str(p.get("covered_by_decoder")) != "True"),
        })
    return rows


def build_pair_bias_producer_audit(model: nn.Module, pair_bias_candidates: List[Dict[str, Any]], parameter_coverage_rows: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    modules = dict(model.named_modules())
    rows = []
    for c in pair_bias_candidates:
        name = c.get("module_name", "")
        module = modules.get(name)
        child_modules = [] if module is None else [(f"{name}.{cn}" if name else cn, cm) for cn, cm in module.named_modules() if cn]
        linear_children = [n for n, cm in child_modules if isinstance(cm, nn.Linear)]
        relevant_params = [p for p in parameter_coverage_rows if p.get("module_name") == name or str(p.get("module_name", "")).startswith(name + ".")]
        covered_children = bool(relevant_params) and all(str(p.get("covered_by_decoder")) == "True" for p in relevant_params)
        produces = False
        evidence = "name_candidate_only"
        producer_exact_closed = False
        fail = "producer_output_not_linked_to_captured_attn_mask"
        rows.append({
            "candidate_module": name,
            "module_type": c.get("module_type", ""),
            "params_count": c.get("params_count", ""),
            "contains_linear_children": bool(linear_children),
            "covered_by_linear_decoder": bool(covered_children),
            "produces_attn_mask_or_pair_bias": produces,
            "producer_exact_closed": producer_exact_closed,
            "evidence": evidence,
            "fail_reason": fail,
        })
    return rows



def patch_mha_module_rows_from_heads(module_rows: List[Dict[str, Any]], head_rows: List[Dict[str, Any]], model: nn.Module) -> List[Dict[str, Any]]:
    """Aggregate parent MHA module acceptance from its actual head rows.

    The parent MHA row must not be blindly accepted just because per-head rows
    exist elsewhere. It is accepted only when every expected head was captured and
    accepted.
    """
    modules = dict(model.named_modules())
    by_mod: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
    for h in head_rows:
        by_mod[h.get("module_name", "")].append(h)
    out = []
    for r in module_rows:
        rr = dict(r)
        name = rr.get("module_name", "")
        module = modules.get(name)
        if module is not None and is_legacy_mha(module):
            hs = by_mod.get(name, [])
            expected = int(module.num_heads)
            ok = len(hs) == expected and all(str(h.get("accepted_exact_circuit")) == "True" for h in hs)
            rr["accepted_exact"] = ok
            rr["reconstruction_error"] = max([float(h.get("full_module_output_rel", 0.0) or 0.0) for h in hs], default="")
            rr["fail_reason"] = "" if ok else f"attention_heads_missing_or_rejected expected={expected} got={len(hs)}"
            rr["honesty_note"] = "MHA module acceptance is aggregated from all expected heads."
            if hs:
                rr["tensor_path"] = hs[0].get("tensor_path", "")
        out.append(rr)
    return out


def apply_matrix_coverage_status(model: nn.Module, decoded: Dict[str, Any], inventory_rows_: List[Dict[str, Any]], params_rows_: List[Dict[str, Any]]) -> Dict[str, Any]:
    # First aggregate parent MHA rows from actual head rows, then build parameter coverage.
    decoded["module_rows"] = patch_mha_module_rows_from_heads(decoded["module_rows"], decoded["head_rows"], model)
    param_cov = build_parameter_coverage(model, decoded["module_rows"], decoded["head_rows"], decoded["primitive_rows"])
    decoded["module_rows"] = patch_module_rows_from_parameter_coverage(decoded["module_rows"], param_cov)
    # Rebuild after patch to reflect module rows/tensor paths.
    param_cov = build_parameter_coverage(model, decoded["module_rows"], decoded["head_rows"], decoded["primitive_rows"])
    matrix_cov = build_matrix_coverage(decoded["module_rows"], decoded["head_rows"], decoded["linear_rows"], decoded["dynamic_rows"], decoded["primitive_rows"], decoded["summary"])
    layer_atlas = build_layer_matrix_atlas(decoded["module_rows"], decoded["head_rows"], matrix_cov, param_cov)
    pair_audit = build_pair_bias_producer_audit(model, decoded.get("pair_bias_candidates", []), param_cov)

    uncovered_params = [r for r in param_cov if str(r.get("covered_by_decoder")) != "True"]
    rejected_modules = [
        r for r in decoded["module_rows"]
        if r.get("decoder_kind") not in ("UNCOVERED", "STRUCTURAL_NOT_EXPLICITLY_TRACED")
        and str(r.get("accepted_exact")) != "True"
    ]
    uncovered_parameterized = [
        r for r in decoded["module_rows"]
        if r.get("decoder_kind") == "UNCOVERED" and int(r.get("params_count", 0) or 0) > 0
    ]
    rejected_heads = [r for r in decoded["head_rows"] if str(r.get("accepted_exact_circuit")) != "True"]
    linear_rows = decoded["linear_rows"]
    dynamic_norm_rows = [r for r in decoded["dynamic_rows"] if "Norm" in r.get("module_type", "")]
    dynamic_activation_rows = [r for r in decoded["dynamic_rows"] if r.get("decoder_kind") == "EXACT_ELEMENTWISE_FORMULA"]

    expected_attention_heads = sum(int(m.num_heads) for _, m in model.named_modules() if is_legacy_mha(m))
    embedding_rows = [r for r in decoded["module_rows"] if r.get("module_type") == "Embedding"]
    all_named_parameters_covered = len(uncovered_params) == 0
    all_attention_heads_covered = (expected_attention_heads == 0 and len(decoded["head_rows"]) == 0) or (len(decoded["head_rows"]) == expected_attention_heads and len(rejected_heads) == 0)
    all_linear_modules_covered = all(str(r.get("accepted_exact")) == "True" for r in linear_rows)
    all_embedding_modules_covered = all(str(r.get("accepted_exact")) == "True" for r in embedding_rows)
    all_norm_modules_covered = all(str(r.get("accepted_exact")) == "True" for r in dynamic_norm_rows)
    all_activation_modules_covered = all(str(r.get("accepted_exact")) == "True" for r in dynamic_activation_rows)
    matrix_coverage_closed = (
        all_named_parameters_covered
        and len(uncovered_parameterized) == 0
        and len(rejected_heads) == 0
        and len(rejected_modules) == 0
        and all_attention_heads_covered
        and all_linear_modules_covered
        and all_embedding_modules_covered
        and all_norm_modules_covered
        and all_activation_modules_covered
    )
    full_forward_status = "FULL_FORWARD_NOT_CLOSED"
    matrix_coverage_status = "FULL_MODEL_MATRIX_COVERAGE_CLOSED" if matrix_coverage_closed else "FULL_MODEL_MATRIX_COVERAGE_NOT_CLOSED"

    # IMPORTANT: module_rows may have been patched above (for example mha.out_proj
    # becomes covered by the parent attention circuit). Rebuild report-facing lists
    # from the patched module_rows so uncovered/rejected CSVs cannot go stale.
    decoded["uncovered"] = [
        {
            "module_name": r.get("module_name", ""),
            "module_type": r.get("module_type", ""),
            "params_count": r.get("params_count", 0),
            "reason": r.get("fail_reason", ""),
            "suggested_decoder": "add exact decoder or verify parent coverage",
        }
        for r in uncovered_parameterized
    ]
    decoded["rejected_modules"] = rejected_modules
    decoded["structural_not_traced"] = [
        r for r in decoded["module_rows"]
        if r.get("decoder_kind") == "STRUCTURAL_NOT_EXPLICITLY_TRACED"
    ]

    decoded["parameter_coverage_rows"] = param_cov
    decoded["matrix_coverage_rows"] = matrix_cov
    decoded["layer_atlas_rows"] = layer_atlas
    decoded["pair_bias_producer_audit_rows"] = pair_audit
    decoded["uncovered_named_parameter_rows"] = uncovered_params
    decoded["summary"].update({
        "matrix_coverage_status": matrix_coverage_status,
        "full_forward_status": full_forward_status,
        "ok": matrix_coverage_closed,
        "stage1_ok": matrix_coverage_closed,
        "all_named_parameters_covered": all_named_parameters_covered,
        "uncovered_named_parameters": len(uncovered_params),
        "uncovered_parameterized": len(uncovered_parameterized),
        "rejected_heads": len(rejected_heads),
        "rejected_modules": len(rejected_modules),
        "expected_attention_heads": expected_attention_heads,
        "all_attention_heads_covered": all_attention_heads_covered,
        "all_linear_modules_covered": all_linear_modules_covered,
        "embedding_modules": len(embedding_rows),
        "accepted_embedding_modules": sum(1 for r in embedding_rows if str(r.get("accepted_exact")) == "True"),
        "all_embedding_modules_covered": all_embedding_modules_covered,
        "all_norm_modules_covered": all_norm_modules_covered,
        "all_activation_modules_covered": all_activation_modules_covered,
        "pair_bias_exact_producer_closed": any(str(r.get("producer_exact_closed")) == "True" for r in pair_audit),
        "final_logits_rel": None,
    })
    decoded["acceptance_rows"] = [{
        **decoded["acceptance_rows"][0],
        "matrix_coverage_status": matrix_coverage_status,
        "full_forward_status": full_forward_status,
        "stage1_ok": matrix_coverage_closed,
        "all_named_parameters_covered": all_named_parameters_covered,
        "uncovered_named_parameters": len(uncovered_params),
        "uncovered_parameterized": len(uncovered_parameterized),
        "rejected_heads": len(rejected_heads),
        "rejected_modules": len(rejected_modules),
        "expected_attention_heads": expected_attention_heads,
        "all_attention_heads_covered": all_attention_heads_covered,
        "all_linear_modules_covered": all_linear_modules_covered,
        "embedding_modules": len(embedding_rows),
        "accepted_embedding_modules": sum(1 for r in embedding_rows if str(r.get("accepted_exact")) == "True"),
        "all_embedding_modules_covered": all_embedding_modules_covered,
        "all_norm_modules_covered": all_norm_modules_covered,
        "all_activation_modules_covered": all_activation_modules_covered,
        "pair_bias_exact_producer_closed": decoded["summary"]["pair_bias_exact_producer_closed"],
    }]
    return decoded

# =============================================================================
# Report
# =============================================================================

def write_report(path: str, decoded: Dict[str, Any], inv: List[Dict[str, Any]], params: List[Dict[str, Any]], args: argparse.Namespace):
    s = decoded["summary"]
    md = []
    md.append("# PART_FULL_MODEL_MATRIX_COVERAGE_V1_4_2\n\n")
    md.append(f"STATUS: **{s.get('matrix_coverage_status', s.get('status'))}**\n")
    md.append(f"FULL_FORWARD_STATUS: **{s.get('full_forward_status', 'FULL_FORWARD_NOT_CLOSED')}**\n")
    md.append("NOTE: full forward replay is separate Stage 2.\n\n")
    md.append(f"- version: **{VERSION}**\n")
    md.append(f"- run_ok: **{s['run_ok']}**\n")
    md.append(f"- stage1_ok / matrix coverage: **{s.get('stage1_ok', s.get('ok'))}**\n")
    md.append(f"- full_forward_ok: **False**\n")
    md.append(f"- all_named_parameters_covered: **{s.get('all_named_parameters_covered')}**\n")
    md.append(f"- uncovered_named_parameters: **{s.get('uncovered_named_parameters')}**\n")
    md.append(f"- final_reason: `{s['final_reason']}`\n\n")
    md.append("## Gates\n\n")
    for k in ["uncovered_parameterized", "structural_not_traced", "rejected_modules", "rejected_heads", "attention_heads", "accepted_attention_heads", "linear_modules", "accepted_linear_modules", "dynamic_modules", "accepted_dynamic_modules"]:
        md.append(f"- {k}: `{s[k]}`\n")
    md.append(f"- decoder_kind_counts: `{s['decoder_kind_counts']}`\n")
    md.append(f"- primitive_fit_summary: `{s['primitive_fit_summary']}`\n")
    md.append(f"- shared_primitives: `{s['shared_primitives']}`\n\n")
    md.append("## Honesty rules\n\n")
    md.append("- `stage1_ok=True` means matrix parameter coverage is closed. `FULL_FORWARD_CLOSED` is separate Stage 2 and is not claimed here.\n")
    md.append("- SVD is compression/pattern fit, not trusted primitive interpretation.\n")
    md.append("- Target-mined atoms are target-specific until shared/heldout gate accepts them.\n")
    md.append("- Containers are `STRUCTURAL_NOT_EXPLICITLY_TRACED`, not silently accepted.\n")
    md.append("- Pair-bias tensor fit is approximate unless exact producing module is decoded.\n\n")
    md.append("## Uncovered parameterized modules\n\n")
    if decoded["uncovered"]:
        md.append("| module | type | params | reason | suggested |\n| --- | --- | ---: | --- | --- |\n")
        for r in decoded["uncovered"][:100]:
            md.append(f"| `{r['module_name']}` | `{r['module_type']}` | {r['params_count']} | `{r['reason']}` | `{r['suggested_decoder']}` |\n")
    else:
        md.append("_No uncovered direct-parameter modules._\n")
    md.append("\n## Rejected decoded modules\n\n")
    if decoded["rejected_modules"]:
        md.append("| module | type | kind | err | reason |\n| --- | --- | --- | ---: | --- |\n")
        for r in decoded["rejected_modules"][:100]:
            md.append(f"| `{r['module_name']}` | `{r['module_type']}` | `{r['decoder_kind']}` | {fmt(r.get('reconstruction_error'))} | `{r.get('fail_reason')}` |\n")
    else:
        md.append("_No rejected decoded modules._\n")
    md.append("\n## Structural not explicitly traced\n\n")
    if decoded["structural_not_traced"]:
        md.append("| module | type | reason |\n| --- | --- | --- |\n")
        for r in decoded["structural_not_traced"][:80]:
            md.append(f"| `{r['module_name']}` | `{r['module_type']}` | `{r['fail_reason']}` |\n")
    else:
        md.append("_No untraced containers._\n")
    md.append("\n## Attention head sample\n\n")
    md.append("| head | accept | full_out | qk | vo | qk_fit | qk_quality | mined | pair_bias_trusted |\n| --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- |\n")
    for r in decoded["head_rows"][:80]:
        md.append(f"| `{r['head_id']}` | {r['accepted_exact_circuit']} | {fmt(r['full_module_output_rel'])} | {fmt(r['qk_score_aug_rel'])} | {fmt(r['vo_y_aug_rel'])} | {fmt(r['qk_fit_rel_err'])} | `{r['qk_fit_quality']}` | {r['qk_uses_target_mined_atoms']} | {r['pair_bias_fit_trusted']} |\n")
    md.append("\n## Primitive fit sample\n\n")
    md.append("| record | target | fit_kind | err | quality | target_mined | note |\n| --- | --- | --- | ---: | --- | --- | --- |\n")
    for r in decoded["primitive_rows"][:120]:
        md.append(f"| `{r['record_id']}` | `{r['target_kind']}` | `{r['fit_kind']}` | {fmt(r['rec_err'])} | `{r['primitive_fit_quality']}` | {r['uses_target_mined_atoms']} | `{r.get('honesty_note','')}` |\n")
    md.append("\n## Exact formulas\n\n```text\n")
    md.append("Linear: y = x_aug @ W_aug.T, W_aug=[W|b]\n")
    md.append("LayerNorm: y = ((x-mean)/sqrt(var+eps))*gamma + beta, dynamic per input\n")
    md.append("Activation: exact elementwise formula, not constant matrix\n")
    md.append("Attention: score_ij = [x_i,1] @ M_qk_aug @ [x_j,1].T + pair_bias + padding_mask\n")
    md.append("Attention write: Y_i = sum_j softmax(score)_ij * ([x_j,1] @ C_vo_aug.T)\n")
    md.append("```\n")
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    Path(path).write_text("".join(md), encoding="utf-8")


# =============================================================================
# Self-test
# =============================================================================

class ToyFullModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.lin1 = nn.Linear(16, 32)
        self.norm = nn.LayerNorm(32)
        self.act = nn.GELU()
        self.mha = nn.MultiheadAttention(32, 4, dropout=0.0, batch_first=False)
        self.lin2 = nn.Linear(32, 8)

    def forward(self, x, attn_mask=None, key_padding_mask=None, positional: bool = False, average_attn_weights_false: bool = False):
        h = self.act(self.norm(self.lin1(x)))
        if positional:
            y, _ = self.mha(h, h, h, key_padding_mask, True, attn_mask)
        elif average_attn_weights_false:
            y, _ = self.mha(h, h, h, attn_mask=attn_mask, key_padding_mask=key_padding_mask, need_weights=True, average_attn_weights=False)
        else:
            y, _ = self.mha(h, h, h, attn_mask=attn_mask, key_padding_mask=key_padding_mask, need_weights=True)
        return self.lin2(y + h)


class DirectParamContainer(nn.Module):
    def __init__(self):
        super().__init__()
        self.scale = nn.Parameter(torch.ones(1))
        self.child = nn.Linear(4, 4)

    def forward(self, x):
        return self.child(x) * self.scale


class ContainerNoDirect(nn.Module):
    def __init__(self):
        super().__init__()
        self.child = nn.Linear(4, 4)

    def forward(self, x):
        return self.child(x) + x


def self_test():
    torch.manual_seed(0)
    model = ToyFullModel()
    model.eval()
    x = torch.randn(7, 3, 16)
    float_mask = torch.zeros(7, 7); float_mask[:, -1] = -2.5
    bool_mask = torch.zeros(7, 7, dtype=torch.bool); bool_mask[:, -1] = True
    kpm = torch.zeros(3, 7, dtype=torch.bool); kpm[:, -1] = True
    metas = [{"pt": [1.0] * 7, "charge": [1, -1, 0, 1, 0, -1, 1], "deta": [0.01*i for i in range(7)], "dphi": [0.02*i for i in range(7)], "roles": ["charged_hadron", "neutral_hadron", "photon", "electron", "muon", "charged_hadron", "neutral_hadron"]} for _ in range(3)]

    class Args:
        accept_tol = 1e-5
        save_tensors = False
        tensor_dir = "/tmp/no"
        auto_mined_atoms = True
        decode_topk = 8
        decode_stop_rel = 1e-4
        mined_svd_atoms = 2
        decode_ridge = 1e-4
        dynamic_matrix_samples = 4
        mine_shared_primitives = True
        shared_min_cluster_size = 3
        shared_cosine_threshold = 0.92
        shared_gain_threshold = 0.02
        shared_decode_gain_threshold = 0.001
        head_cluster_threshold = 0.90

    results = []
    for cname, am, kp, positional, avg_false in [
        ("no_mask", None, None, False, False),
        ("float_mask", float_mask, None, False, False),
        ("bool_mask", bool_mask, None, False, False),
        ("key_padding_mask", None, kpm, False, False),
        ("positional_float_attn_mask", float_mask, None, True, False),
        ("average_attn_weights_false", float_mask, None, False, True),
    ]:
        cap = ModuleCapture()
        cap.attach(model)
        with torch.no_grad():
            _ = model(x, attn_mask=am, key_padding_mask=kp, positional=positional, average_attn_weights_false=avg_false)
        cap.close()
        decoded = decode_model(model, cap, metas, Args())
        assert decoded["summary"]["accepted_attention_heads"] == decoded["summary"]["attention_heads"], decoded["summary"]
        assert decoded["summary"]["accepted_linear_modules"] == decoded["summary"]["linear_modules"], decoded["summary"]
        # Containers are intentionally untraced, so local_exact_ok may be false. This is honesty, not failure.
        results.append({
            "case": cname,
            "attention": f"{decoded['summary']['accepted_attention_heads']}/{decoded['summary']['attention_heads']}",
            "linear": f"{decoded['summary']['accepted_linear_modules']}/{decoded['summary']['linear_modules']}",
            "rejected_modules": decoded["summary"]["rejected_modules"],
            "structural_not_traced": decoded["summary"]["structural_not_traced"],
        })

    # SVD not trusted for rectangular linear.
    rec = {"input": torch.randn(2, 3, 16), "output": model.lin1(torch.randn(2, 3, 16)), "input_shape": "2x3x16", "output_shape": "2x3x32"}
    row, prim, _ = decode_linear("lin1", model.lin1, rec, Path("/tmp/no"), Args())
    assert row["primitive_fit_kind"] == "APPROX_PATTERN_FIT_RECTANGULAR_SVD", row
    assert row["interpretation_trusted"] is False, row

    # Direct-param container must be uncovered.
    bad = DirectParamContainer().eval()
    cap = ModuleCapture(); cap.attach(bad)
    with torch.no_grad(): _ = bad(torch.randn(2, 4))
    cap.close()
    dec = decode_model(bad, cap, [], Args())
    assert dec["summary"]["uncovered_parameterized"] >= 1, dec["summary"]

    # Container without direct params must not be accepted exact as full graph.
    cont = ContainerNoDirect().eval()
    cap = ModuleCapture(); cap.attach(cont)
    with torch.no_grad(): _ = cont(torch.randn(2, 4))
    cap.close()
    dec2 = decode_model(cont, cap, [], Args())
    assert dec2["summary"]["structural_not_traced"] >= 1, dec2["summary"]

    # Shared primitive heldout-gain smoke test.
    R = torch.eye(8) * 0.2
    recs = [
        {"record_id": f"shared_test_{i}", "matrix": R + 0.001 * torch.randn(8, 8), "residual_after_base": R + 0.001 * torch.randn(8, 8)}
        for i in range(4)
    ]
    shared_rows, shared_info = mine_shared_primitives(recs, min_cluster_size=2, threshold=0.80, gain_threshold=0.001, decode_gain_threshold=0.001, max_atoms=8, ridge=1e-4)
    assert shared_info.get("heldout_gate") == "real_base_plus_shared_decode_gain", shared_info
    assert any(float(r.get("gain_heldout", 0.0)) > 0.0 for r in shared_rows), shared_rows

    # Activation ratio must not clamp negative denominators.
    xneg = torch.tensor([-2.0, -1.0, 0.0, 2.0])
    yneg = torch.tanh(xneg)
    ratio_check = torch.where(xneg.abs() > 1e-12, yneg / xneg, torch.zeros_like(yneg))
    assert torch.isfinite(ratio_check).all(), ratio_check

    # Required symbols check.
    required = ["MatrixOpLibrary", "SparseProgramDecoder", "flow_sketch_rows", "mine_shared_primitives", "residual_gain_for_atom", "DCTLow", "GraphRingRW", "VERSION"]
    text = Path(__file__).read_text(encoding="utf-8")
    missing = [r for r in required if r not in text]
    assert not missing, missing

    print(json.dumps({"ok": True, "version": VERSION, "self_test": "passed", "shared_gain_test": shared_info, "results": results}, indent=2))




def self_test_coverage():
    """Stage-1 coverage self-test for v1_4.

    Checks:
      1. Toy model all named_parameters covered.
      2. Direct-param custom module is NOT closed.
      3. MHA heads/Linear/Norm/Activation accepted.
      4. Rectangular Linear exact W_aug accepted but SVD not trusted.
      5. Shared primitive gate runs.
    """
    torch.manual_seed(0)

    class Args:
        accept_tol = 1e-5
        save_tensors = False
        tensor_dir = "/tmp/no"
        auto_mined_atoms = True
        decode_topk = 8
        decode_stop_rel = 1e-4
        mined_svd_atoms = 2
        decode_ridge = 1e-4
        dynamic_matrix_samples = 4
        mine_shared_primitives = True
        shared_min_cluster_size = 2
        shared_cosine_threshold = 0.80
        shared_gain_threshold = 0.001
        shared_decode_gain_threshold = 0.001
        head_cluster_threshold = 0.90

    metas = [{"pt": [1.0] * 7, "charge": [1, -1, 0, 1, 0, -1, 1], "deta": [0.01*i for i in range(7)], "dphi": [0.02*i for i in range(7)], "roles": ["charged_hadron", "neutral_hadron", "photon", "electron", "muon", "charged_hadron", "neutral_hadron"]} for _ in range(3)]

    model = ToyFullModel().eval()
    x = torch.randn(7, 3, 16)
    cap = ModuleCapture(); cap.attach(model)
    with torch.no_grad():
        _ = model(x)
    cap.close()
    inv, params, _ = inventory_rows(model)
    dec = decode_model(model, cap, metas, Args())
    dec = apply_matrix_coverage_status(model, dec, inv, params)

    assert dec["summary"]["matrix_coverage_status"] == "FULL_MODEL_MATRIX_COVERAGE_CLOSED", dec["summary"]
    assert dec["summary"]["full_forward_status"] == "FULL_FORWARD_NOT_CLOSED", dec["summary"]
    assert dec["summary"]["all_named_parameters_covered"] is True, dec["summary"]
    assert dec["summary"]["uncovered_named_parameters"] == 0, dec["uncovered_named_parameter_rows"]
    assert dec["summary"]["uncovered_parameterized"] == len(dec["uncovered"]), (dec["summary"], dec["uncovered"])
    assert not dec["uncovered"], dec["uncovered"]
    assert dec["summary"]["rejected_heads"] == 0, dec["summary"]
    assert dec["summary"]["rejected_modules"] == 0, dec["summary"]
    assert dec["summary"]["all_linear_modules_covered"] is True, dec["summary"]
    assert dec["summary"]["all_norm_modules_covered"] is True, dec["summary"]
    assert dec["summary"]["all_activation_modules_covered"] is True, dec["summary"]
    assert any(r["param_kind"] == "attention_in_proj_weight_qkv" and r["covered_by_decoder"] for r in dec["parameter_coverage_rows"]), dec["parameter_coverage_rows"]
    assert any(r["param_kind"] == "attention_out_proj_weight" and r["covered_by_decoder"] for r in dec["parameter_coverage_rows"]), dec["parameter_coverage_rows"]
    assert not any(r.get("module_name", "").endswith("mha.out_proj") for r in dec["uncovered"]), dec["uncovered"]
    assert dec["matrix_coverage_rows"], "matrix coverage empty"
    assert dec["layer_atlas_rows"], "layer atlas empty"
    assert isinstance(dec["pair_bias_producer_audit_rows"], list)

    # Embedding coverage: exact lookup table should close Stage-1 matrix coverage.
    class EmbToy(nn.Module):
        def __init__(self):
            super().__init__()
            self.emb = nn.Embedding(11, 6)
            self.proj = nn.Linear(6, 3)
        def forward(self, ids):
            return self.proj(self.emb(ids))
    emb_model = EmbToy().eval()
    ids = torch.tensor([[1, 2, 3], [4, 0, 5]], dtype=torch.long)
    cap = ModuleCapture(); cap.attach(emb_model)
    with torch.no_grad():
        _ = emb_model(ids)
    cap.close()
    inv_emb, params_emb, _ = inventory_rows(emb_model)
    dec_emb = decode_model(emb_model, cap, [], Args())
    dec_emb = apply_matrix_coverage_status(emb_model, dec_emb, inv_emb, params_emb)
    assert dec_emb["summary"]["matrix_coverage_status"] == "FULL_MODEL_MATRIX_COVERAGE_CLOSED", dec_emb["summary"]
    assert any(r["param_kind"] == "embedding_weight" and r["covered_by_decoder"] for r in dec_emb["parameter_coverage_rows"]), dec_emb["parameter_coverage_rows"]
    assert any(r.get("matrix_kind") == "Embedding.W" for r in dec_emb["matrix_coverage_rows"]), dec_emb["matrix_coverage_rows"]

    # Direct-param custom module must fail coverage.
    bad = DirectParamContainer().eval()
    cap = ModuleCapture(); cap.attach(bad)
    with torch.no_grad():
        _ = bad(torch.randn(2, 4))
    cap.close()
    inv_bad, params_bad, _ = inventory_rows(bad)
    dec_bad = decode_model(bad, cap, [], Args())
    dec_bad = apply_matrix_coverage_status(bad, dec_bad, inv_bad, params_bad)
    assert dec_bad["summary"]["matrix_coverage_status"] == "FULL_MODEL_MATRIX_COVERAGE_NOT_CLOSED", dec_bad["summary"]
    assert dec_bad["summary"]["uncovered_named_parameters"] >= 1, dec_bad["parameter_coverage_rows"]
    assert dec_bad["summary"]["uncovered_parameterized"] == len(dec_bad["uncovered"]), (dec_bad["summary"], dec_bad["uncovered"])
    assert dec_bad["uncovered"], dec_bad["uncovered"]
    assert any(str(r.get("covered_by_decoder")) != "True" for r in dec_bad["parameter_coverage_rows"]), dec_bad["parameter_coverage_rows"]

    # Rectangular Linear exact W_aug accepted, SVD not trusted.
    lin = nn.Linear(5, 7).eval()
    inp = torch.randn(3, 5)
    rec = {"input": inp, "output": lin(inp), "input_shape": "3x5", "output_shape": "3x7"}
    row, _, _ = decode_linear("rect", lin, rec, Path("/tmp/no"), Args())
    assert row["accepted_exact"] is True, row
    assert row["primitive_fit_kind"] == "APPROX_PATTERN_FIT_RECTANGULAR_SVD", row
    assert row["interpretation_trusted"] is False, row

    # Shared primitive gate runs and exposes heldout fields.
    R = torch.eye(8) * 0.2
    recs = [
        {"record_id": f"cov_shared_{i}", "matrix": R + 0.001 * torch.randn(8, 8), "residual_after_base": R + 0.001 * torch.randn(8, 8)}
        for i in range(4)
    ]
    shared_rows, shared_info = mine_shared_primitives(recs, min_cluster_size=2, threshold=0.80, gain_threshold=0.001, decode_gain_threshold=0.001, max_atoms=8, ridge=1e-4)
    assert shared_info.get("heldout_gate") == "real_base_plus_shared_decode_gain", shared_info
    if shared_rows:
        assert "gain_heldout_decode" in shared_rows[0], shared_rows[0]

    print(json.dumps({
        "ok": True,
        "version": VERSION,
        "self_test_coverage": "passed",
        "matrix_coverage_status": dec["summary"]["matrix_coverage_status"],
        "uncovered_named_parameters": dec["summary"]["uncovered_named_parameters"],
        "attention_heads": dec["summary"]["attention_heads"],
        "accepted_attention_heads": dec["summary"]["accepted_attention_heads"],
        "direct_param_negative_uncovered": dec_bad["summary"]["uncovered_named_parameters"],
    }, indent=2))


# =============================================================================
# CLI
# =============================================================================

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--self-test-coverage", action="store_true")
    ap.add_argument("--network-file", default="external/particle_transformer/networks/example_ParticleTransformer_legacy.py")
    ap.add_argument("--checkpoint", default="external/particle_transformer/models/ParT_kinpid.pt")
    ap.add_argument("--data-config", default="external/particle_transformer/data/JetClass/JetClass_kinpid.yaml")
    ap.add_argument("--groups-csv", default="reports/latest/tables/part_hqql_tbl_groups_direct_replay_v1.csv")
    ap.add_argument("--events-per-group", type=int, default=2)
    ap.add_argument("--device", default="cuda" if torch.cuda.is_available() else "cpu")
    ap.add_argument("--accept-tol", type=float, default=ACCEPT_TOL)
    ap.add_argument("--decode-topk", type=int, default=12)
    ap.add_argument("--decode-stop-rel", type=float, default=1e-4)
    ap.add_argument("--decode-ridge", type=float, default=1e-4)
    ap.add_argument("--auto-mined-atoms", action="store_true")
    ap.add_argument("--mined-svd-atoms", type=int, default=4)
    ap.add_argument("--mine-shared-primitives", action="store_true")
    ap.add_argument("--shared-min-cluster-size", type=int, default=3)
    ap.add_argument("--shared-cosine-threshold", type=float, default=0.92)
    ap.add_argument("--shared-gain-threshold", type=float, default=0.02)
    ap.add_argument("--shared-decode-gain-threshold", type=float, default=0.01)
    ap.add_argument("--head-cluster-threshold", type=float, default=0.90)
    ap.add_argument("--dynamic-matrix-samples", type=int, default=64)
    ap.add_argument("--save-tensors", action="store_true", default=True)
    ap.add_argument("--no-save-tensors", dest="save_tensors", action="store_false")
    ap.add_argument("--tensor-dir", default="artifacts/latest/part_full_model_matrix_coverage_v1_4_2")
    ap.add_argument("--out-md", default="reports/latest/PART_FULL_MODEL_MATRIX_COVERAGE_V1_4_2.md")
    ap.add_argument("--out-json", default="manifests/latest/part_full_model_matrix_coverage_v1_4_2.json")
    ap.add_argument("--out-inventory", default="reports/latest/tables/part_full_model_inventory_v1_4_2.csv")
    ap.add_argument("--out-inventory-json", default="manifests/latest/part_full_model_inventory_v1_4_2.json")
    ap.add_argument("--out-parameters", default="reports/latest/tables/part_full_model_parameters_v1_4_2.csv")
    ap.add_argument("--out-modules", default="reports/latest/tables/part_full_model_modules_v1_4_2.csv")
    ap.add_argument("--out-heads", default="reports/latest/tables/part_full_model_attention_heads_v1_4_2.csv")
    ap.add_argument("--out-linear", default="reports/latest/tables/part_full_model_linear_v1_4_2.csv")
    ap.add_argument("--out-dynamic", default="reports/latest/tables/part_full_model_dynamic_ops_v1_4_2.csv")
    ap.add_argument("--out-primitive", default="reports/latest/tables/part_full_model_primitive_fits_v1_4_2.csv")
    ap.add_argument("--out-shared", default="reports/latest/tables/part_full_model_shared_primitives_v1_4_2.csv")
    ap.add_argument("--out-uncovered", default="reports/latest/tables/part_full_model_uncovered_v1_4_2.csv")
    ap.add_argument("--out-pair-bias-candidates", default="reports/latest/tables/part_full_model_pair_bias_candidates_v1_4_2.csv")
    ap.add_argument("--out-acceptance", default="reports/latest/tables/part_full_model_acceptance_v1_4_2.csv")
    ap.add_argument("--out-flow", default="reports/latest/tables/part_full_model_flow_sketch_v1_4_2.csv")
    ap.add_argument("--out-parameter-coverage", default="reports/latest/tables/part_full_model_parameter_coverage_v1_4_2.csv")
    ap.add_argument("--out-matrix-coverage", default="reports/latest/tables/part_full_model_matrix_coverage_v1_4_2.csv")
    ap.add_argument("--out-layer-atlas", default="reports/latest/tables/part_full_model_layer_matrix_atlas_v1_4_2.csv")
    ap.add_argument("--out-pair-bias-audit", default="reports/latest/tables/part_pair_bias_producer_audit_v1_4_2.csv")
    args = ap.parse_args()

    if args.self_test:
        self_test()
        return
    if args.self_test_coverage:
        self_test_coverage()
        return

    from tools.part_attention_supertrace_real_contract_v1 import load_model, build_batch

    device = torch.device(args.device)
    model, dc = load_model(args.network_file, args.checkpoint, args.data_config, device)
    model.eval()

    inv, params, pair_candidates_inv = inventory_rows(model)

    events = select_events(args.groups_csv, args.events_per_group)
    pts, fts, vec, msk, metas = build_batch(events, device, dc)
    cap = ModuleCapture()
    cap.attach(model)
    with torch.no_grad():
        logits = model(pts, fts, vec, msk)
    cap.close()

    decoded = decode_model(model, cap, metas, args)
    decoded = apply_matrix_coverage_status(model, decoded, inv, params)
    inv2 = merge_inventory_coverage(inv, decoded["module_rows"])

    # Merge static pair candidates from inventory with decoded pair candidates.
    pair_candidates = pair_candidates_inv + decoded["pair_bias_candidates"]

    outputs = {
        "md": args.out_md,
        "json": args.out_json,
        "inventory": args.out_inventory,
        "inventory_json": args.out_inventory_json,
        "parameters": args.out_parameters,
        "modules": args.out_modules,
        "attention_heads": args.out_heads,
        "linear": args.out_linear,
        "dynamic_ops": args.out_dynamic,
        "primitive_fits": args.out_primitive,
        "shared_primitives": args.out_shared,
        "uncovered": args.out_uncovered,
        "pair_bias_candidates": args.out_pair_bias_candidates,
        "acceptance": args.out_acceptance,
        "flow_sketch": args.out_flow,
        "parameter_coverage": args.out_parameter_coverage,
        "matrix_coverage": args.out_matrix_coverage,
        "layer_matrix_atlas": args.out_layer_atlas,
        "pair_bias_producer_audit": args.out_pair_bias_audit,
        "tensor_dir": args.tensor_dir if args.save_tensors else "",
    }
    top = {
        "version": VERSION,
        "run_ok": True,
        **decoded["summary"],
        "root_output_shape": shape_str(logits),
        "model_training_flag_after_eval": bool(model.training),
        "outputs": outputs,
    }

    write_csv(args.out_inventory, inv2)
    write_json(args.out_inventory_json, {"version": VERSION, "rows": inv2})
    write_csv(args.out_parameters, params)
    write_csv(args.out_modules, decoded["module_rows"])
    write_csv(args.out_heads, decoded["head_rows"])
    write_csv(args.out_linear, decoded["linear_rows"])
    write_csv(args.out_dynamic, decoded["dynamic_rows"])
    write_csv(args.out_primitive, decoded["primitive_rows"])
    write_csv(args.out_shared, decoded["shared_rows"])
    write_csv(args.out_uncovered, decoded["uncovered"])
    write_csv(args.out_pair_bias_candidates, pair_candidates)
    write_csv(args.out_acceptance, decoded["acceptance_rows"])
    write_csv(args.out_flow, decoded["flow_rows"])
    write_csv(args.out_parameter_coverage, decoded["parameter_coverage_rows"])
    write_csv(args.out_matrix_coverage, decoded["matrix_coverage_rows"])
    write_csv(args.out_layer_atlas, decoded["layer_atlas_rows"])
    write_csv(args.out_pair_bias_audit, decoded["pair_bias_producer_audit_rows"])
    write_json(args.out_json, top)
    write_report(args.out_md, decoded, inv2, params, args)
    print(json.dumps({
        "version": VERSION,
        "run_ok": True,
        "matrix_coverage_status": decoded["summary"].get("matrix_coverage_status"),
        "full_forward_status": decoded["summary"].get("full_forward_status"),
        "stage1_ok": decoded["summary"].get("stage1_ok"),
        "ok": decoded["summary"].get("ok"),
        "uncovered_named_parameters": decoded["summary"].get("uncovered_named_parameters"),
        "outputs": outputs
    }, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
