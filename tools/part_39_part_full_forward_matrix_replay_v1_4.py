#!/usr/bin/env python3
"""PART_FULL_FORWARD_MATRIX_REPLAY_V1.

Stage 2 after Stage 1 matrix coverage. This file does not redo Stage 1.
It captures a real forward, manually replays supported leaf primitives and MHA
from captured tensors, writes required reports, and only reports
FULL_FORWARD_CLOSED if a full decoded logits replay is actually produced.
"""
from __future__ import annotations
import argparse, csv, json, math, os, re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

if os.environ.get("PART_REPLAY_SET_THREADS", "1") != "0":
    os.environ.setdefault("OMP_NUM_THREADS", "1")
    os.environ.setdefault("MKL_NUM_THREADS", "1")
import torch
import torch.nn as nn
import torch.nn.functional as F
try:
    torch.set_num_threads(int(os.environ.get("PART_REPLAY_TORCH_THREADS", "1")))
except Exception:
    pass

VERSION = "1.4.0"
ACCEPT_TOL = 1e-5
GROUPS = ["A_Hqql_correct", "B_Hqql_to_Tbl", "C_Tbl_correct", "D_Tbl_to_Hqql"]

# ------------------------- helpers -------------------------
def rel_err(pred: torch.Tensor, true: torch.Tensor, mask: Optional[torch.Tensor]=None) -> float:
    pred, true = pred.detach().float().cpu(), true.detach().float().cpu()
    if mask is not None:
        mask = mask.detach().bool().cpu(); pred, true = pred[mask], true[mask]
    if true.numel() == 0: return float("nan")
    return float(torch.linalg.norm(pred-true) / torch.linalg.norm(true).clamp_min(1e-12))

def first_tensor(x: Any) -> Optional[torch.Tensor]:
    if torch.is_tensor(x): return x
    if isinstance(x, (tuple, list)):
        for v in x:
            t = first_tensor(v)
            if t is not None: return t
    if isinstance(x, dict):
        for v in x.values():
            t = first_tensor(v)
            if t is not None: return t
    return None

def detach_cpu(x: Optional[torch.Tensor]) -> Optional[torch.Tensor]:
    if x is None: return None
    y = x.detach().cpu()
    return y.float() if y.is_floating_point() else y

def pack_tensor_args(obj):
    if torch.is_tensor(obj): return detach_cpu(obj)
    if obj is None: return None
    if isinstance(obj,(tuple,list)): return [pack_tensor_args(v) for v in obj]
    if isinstance(obj,dict): return {str(k):pack_tensor_args(v) for k,v in obj.items()}
    return None

def tuple_rel_err(pred,true):
    errs=[]
    def walk(a,b):
        if torch.is_tensor(a) and torch.is_tensor(b): errs.append(rel_err(a,b))
        elif isinstance(a,(tuple,list)) and isinstance(b,(tuple,list)):
            for aa,bb in zip(a,b): walk(aa,bb)
        elif isinstance(a,dict) and isinstance(b,dict):
            for k in (set(a.keys()) & set(b.keys())): walk(a[k],b[k])
    walk(pred,true)
    return max(errs) if errs else float("nan")


def shape_str(x: Any) -> str:
    if torch.is_tensor(x): return "x".join(map(str, x.shape))
    if isinstance(x, (tuple, list)): return "[" + ",".join(shape_str(v) for v in x) + "]"
    if isinstance(x, dict): return "{" + ",".join(f"{k}:{shape_str(v)}" for k,v in x.items()) + "}"
    return "None" if x is None else type(x).__name__

def finite_norm(x: Optional[torch.Tensor]) -> float:
    if x is None: return 0.0
    y = x.detach().float().cpu(); m = torch.isfinite(y)
    return float(torch.linalg.norm(y[m])) if m.any() else 0.0

def strip_tensors(o: Any) -> Any:
    if torch.is_tensor(o): return {"tensor_shape": list(o.shape), "tensor_norm": float(torch.linalg.norm(o.float())) if o.numel() else 0.0}
    if isinstance(o, dict): return {str(k): strip_tensors(v) for k,v in o.items()}
    if isinstance(o, list): return [strip_tensors(v) for v in o]
    return o

def write_csv(path: str, rows: List[Dict[str, Any]]):
    p=Path(path); p.parent.mkdir(parents=True, exist_ok=True)
    if not rows: p.write_text("", encoding="utf-8"); return
    keys=[]
    for r in rows:
        for k in r:
            if k not in keys: keys.append(k)
    with p.open("w", newline="", encoding="utf-8") as f:
        w=csv.DictWriter(f, fieldnames=keys); w.writeheader(); w.writerows(rows)

def write_json(path: str, obj: Dict[str, Any]):
    p=Path(path); p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(strip_tensors(obj), indent=2, ensure_ascii=False), encoding="utf-8")

def save_pt(path: str, obj: Any) -> str:
    p=Path(path); p.parent.mkdir(parents=True, exist_ok=True); torch.save(obj, p); return str(p)

def read_csv(path: str) -> List[Dict[str,str]]:
    p=Path(path)
    if not p.exists(): return []
    with p.open(newline="", encoding="utf-8") as f: return list(csv.DictReader(f))

def select_events(path: str, events_per_group: int) -> List[Dict[str,str]]:
    by=defaultdict(list)
    for r in read_csv(path): by[r.get("analysis_group","")].append(r)
    out=[]
    for g in GROUPS: out += by[g][:events_per_group]
    if not out: raise RuntimeError(f"no events selected from {path}")
    return out

def is_mha(m: Any) -> bool:
    return hasattr(m,"num_heads") and hasattr(m,"head_dim") and hasattr(m,"in_proj_weight") and hasattr(m,"out_proj")

def is_activation(m: nn.Module) -> bool:
    return isinstance(m,(nn.ReLU,nn.GELU,nn.SiLU,nn.Sigmoid,nn.Tanh,nn.LeakyReLU,nn.ELU))

# ------------------------- source trace -------------------------
def classify_source_line(line: str) -> str:
    s=line.strip()
    if not s or s.startswith("#"): return "comment_or_blank"
    rules=[
        ("input", r"def forward|pts|fts|vec|msk"),
        ("pair_embedding", r"pair_embed|pairwise|attn_mask|pair_bias"),
        ("embedding", r"embed|cls_token"),
        ("attention_block", r"blocks|cls_blocks|attn"),
        ("linear_or_classifier", r"fc|classifier|Linear|lin"),
        ("normalization", r"norm|bn|BatchNorm|LayerNorm"),
        ("activation", r"gelu|relu|silu|activation"),
        ("conv1d", r"Conv1d|conv1d"),
        ("mask_creation", r"mask|masked_fill|where"),
        ("structural", r"transpose|permute|view|reshape|flatten|cat|stack|expand|repeat|contiguous"),
        ("residual_add", r"\+|add|resid"),
        ("pooling_select", r"mean|sum|max|select|slice|\["),
        ("logits", r"logits|return"),
    ]
    for kind, pat in rules:
        if re.search(pat, s): return kind
    return "python_op"

def build_source_trace(network_file: str, model: Optional[nn.Module]=None) -> List[Dict[str,Any]]:
    rows=[]; p=Path(network_file)
    if p.exists():
        lines=p.read_text(encoding="utf-8", errors="replace").splitlines(); in_f=False; base=None; step=0
        for i,line in enumerate(lines,1):
            st=line.strip(); indent=len(line)-len(line.lstrip())
            if re.match(r"def\s+forward\s*\(", st): in_f=True; base=indent
            if in_f:
                if st.startswith("def ") and not st.startswith("def forward") and base is not None and indent<=base: in_f=False; continue
                kind=classify_source_line(line)
                if kind!="comment_or_blank":
                    rows.append({"step_id":step,"source_location":f"{network_file}:{i}","operation_kind":kind,"module_name":"","input_names":"","output_name":"","input_shape":"","output_shape":"","replay_status":"SOURCE_ONLY","reason_if_not_replayed":"static source trace row","source_text":st[:240]}); step+=1
        if rows: return rows
    if model is not None:
        for step,(name,m) in enumerate(model.named_modules()):
            if name: rows.append({"step_id":step,"source_location":"model.named_modules","operation_kind":m.__class__.__name__,"module_name":name,"input_names":"","output_name":name,"input_shape":"","output_shape":"","replay_status":"MODULE_INVENTORY_ONLY","reason_if_not_replayed":"source parse unavailable"})
    return rows

# ------------------------- capture -------------------------
def extract_arg(args: Tuple[Any,...], kwargs: Dict[str,Any], name: str, pos: int):
    if name in kwargs: return kwargs.get(name), "kwargs"
    if len(args)>pos: return args[pos], "positional"
    return None, "none"

class ForwardCapture:
    def __init__(self, max_items:int=1):
        self.max_items=max_items; self.records={}; self.counts=Counter(); self.handles=[]
    def hook(self,name):
        def fn(module,args,kwargs,output):
            idx=int(self.counts[name]); self.counts[name]+=1
            if idx>=self.max_items: return
            inp=first_tensor(args); out=first_tensor(output)
            rec={"module":module,"module_name":name,"call_index":idx,"module_type":module.__class__.__name__,"input":detach_cpu(inp),"output":detach_cpu(out),"input_tensors":pack_tensor_args(args),"kwargs_tensors":pack_tensor_args(kwargs),"output_tensors":pack_tensor_args(output),"input_shape":shape_str(args),"output_shape":shape_str(output),"training":bool(module.training)}
            if is_mha(module) and len(args)>=3:
                kpm,kpm_src=extract_arg(args,kwargs,"key_padding_mask",3); need,need_src=extract_arg(args,kwargs,"need_weights",4); am,am_src=extract_arg(args,kwargs,"attn_mask",5); avg,avg_src=extract_arg(args,kwargs,"average_attn_weights",6)
                out0=output[0] if isinstance(output,tuple) else output; out1=output[1] if isinstance(output,tuple) and len(output)>1 else None
                rec.update({"q":detach_cpu(args[0]),"k":detach_cpu(args[1]),"v":detach_cpu(args[2]),"mha_output":detach_cpu(out0),"attn_weights":None if out1 is None else detach_cpu(out1),"attn_mask":None if am is None else detach_cpu(am),"attn_mask_source":am_src,"attn_mask_dtype":"none" if am is None else str(am.dtype),"key_padding_mask":None if kpm is None else detach_cpu(kpm),"key_padding_mask_source":kpm_src,"key_padding_mask_dtype":"none" if kpm is None else str(kpm.dtype),"need_weights":str(need),"need_weights_source":need_src,"average_attn_weights":str(avg),"average_attn_weights_source":avg_src})
            self.records[(name,idx)]=rec
        return fn
    def attach(self,model):
        for name,m in model.named_modules():
            if name: self.handles.append(m.register_forward_hook(self.hook(name), with_kwargs=True))
    def close(self):
        for h in self.handles: h.remove()
        self.handles=[]

# ------------------------- replay primitives -------------------------
def replay_linear(x,m):
    W=m.weight.detach().float().cpu(); b=m.bias.detach().float().cpu() if m.bias is not None else None; y=x.detach().float().cpu()@W.T; return y+(b if b is not None else 0)

def replay_conv1d(x,m):
    x=x.detach().float().cpu(); W=m.weight.detach().float().cpu(); b=m.bias.detach().float().cpu() if m.bias is not None else None; padding=m.padding
    if m.padding_mode!="zeros":
        pad=padding[0] if isinstance(padding,tuple) else int(padding)
        if pad>0: x=F.pad(x,(pad,pad),mode=m.padding_mode)
        padding=0
    return F.conv1d(x,W,b,stride=m.stride,padding=padding,dilation=m.dilation,groups=m.groups)

def replay_embedding(x,m):
    return F.embedding(x.detach().long().cpu(),m.weight.detach().float().cpu(),padding_idx=m.padding_idx,max_norm=m.max_norm,norm_type=m.norm_type,scale_grad_by_freq=m.scale_grad_by_freq,sparse=m.sparse)

def replay_layernorm(x,m):
    w=m.weight.detach().float().cpu() if m.weight is not None else None; b=m.bias.detach().float().cpu() if m.bias is not None else None
    return F.layer_norm(x.detach().float().cpu(),m.normalized_shape,w,b,m.eps)

def replay_batchnorm(x,m):
    x=x.detach().float().cpu(); w=m.weight.detach().float().cpu() if getattr(m,"weight",None) is not None else None; b=m.bias.detach().float().cpu() if getattr(m,"bias",None) is not None else None
    rm=m.running_mean.detach().float().cpu() if getattr(m,"running_mean",None) is not None else None; rv=m.running_var.detach().float().cpu() if getattr(m,"running_var",None) is not None else None
    training=bool(m.training or rm is None or rv is None); mom=0.0 if getattr(m,"momentum",None) is None else float(m.momentum)
    return F.batch_norm(x,rm,rv,w,b,training=training,momentum=mom,eps=float(m.eps))

def replay_rmsnorm(x,m):
    x=x.detach().float().cpu(); eps=float(getattr(m,"eps",1e-6)); y=x/torch.sqrt(x.pow(2).mean(dim=-1,keepdim=True)+eps)
    if getattr(m,"weight",None) is not None: y=y*m.weight.detach().float().cpu()
    if getattr(m,"bias",None) is not None: y=y+m.bias.detach().float().cpu()
    return y

def replay_activation(x,m):
    x=x.detach().float().cpu()
    if isinstance(m,nn.ReLU): return F.relu(x,inplace=False)
    if isinstance(m,nn.GELU): return F.gelu(x,approximate=m.approximate)
    if isinstance(m,nn.SiLU): return F.silu(x,inplace=False)
    if isinstance(m,nn.Sigmoid): return torch.sigmoid(x)
    if isinstance(m,nn.Tanh): return torch.tanh(x)
    if isinstance(m,nn.LeakyReLU): return F.leaky_relu(x,negative_slope=m.negative_slope,inplace=False)
    if isinstance(m,nn.ELU): return F.elu(x,alpha=m.alpha,inplace=False)
    return m.cpu()(x)


def replay_supported(x,m,rec=None):
    if isinstance(m,nn.Sequential): return replay_sequential(x,m)
    if isinstance(m,nn.Linear): return replay_linear(x,m)
    if isinstance(m,nn.Conv1d): return replay_conv1d(x,m)
    if isinstance(m,nn.Embedding): return replay_embedding(x,m)
    if isinstance(m,nn.LayerNorm): return replay_layernorm(x,m)
    if isinstance(m,(nn.BatchNorm1d,nn.BatchNorm2d,nn.BatchNorm3d)): return replay_batchnorm(x,m)
    if "RMSNorm" in m.__class__.__name__: return replay_rmsnorm(x,m)
    if is_activation(m): return replay_activation(x,m)
    if isinstance(m,(nn.Dropout,nn.Dropout1d,nn.Dropout2d,nn.Dropout3d,nn.Identity)): return x
    if is_mha(m) and rec is not None: return replay_mha_from_capture(rec)[0]
    raise RuntimeError(f"unsupported recursive replay {m.__class__.__name__}")

def replay_sequential(x,m):
    y=x.detach().float().cpu()
    for child in m:
        y=replay_supported(y,child)
    return y

def replay_sequence_trimmer_core(m, x, v=None, mask=None, uu=None, captured_output_tensors=None):
    if mask is None:
        mask = torch.ones_like(x[:, :1])
    mask = mask.bool()

    # If captured output length equals input length, original forward did not trim
    # (warmup/counter path). Blind maxlen slicing would be wrong.
    if captured_output_tensors is not None and isinstance(captured_output_tensors, (list, tuple)) and len(captured_output_tensors) >= 1:
        out_x = captured_output_tensors[0]
        if torch.is_tensor(out_x) and out_x.shape[-1] == x.shape[-1]:
            return (x, v, mask, uu)

    if getattr(m, "enabled", False):
        maxlen = mask.sum(dim=-1).max()
        maxlen = max(maxlen, torch.tensor(1))
        maxlen = int(maxlen.item())
        if captured_output_tensors is not None and isinstance(captured_output_tensors, (list, tuple)) and torch.is_tensor(captured_output_tensors[0]):
            maxlen = int(captured_output_tensors[0].shape[-1])
        if maxlen < mask.size(-1):
            mask = mask[:, :, :maxlen]
            x = x[:, :, :maxlen]
            if v is not None:
                v = v[:, :, :maxlen]
            if uu is not None and torch.is_tensor(uu) and uu.ndim == 4:
                uu = uu[:, :, :maxlen, :maxlen]
    return (x, v, mask, uu)


def replay_sequence_trimmer_from_capture(rec):
    m = rec["module"]
    args = rec.get("input_tensors", [])
    kwargs = rec.get("kwargs_tensors", {}) or {}
    x = args[0] if len(args) > 0 else kwargs.get("x")
    v = args[1] if len(args) > 1 else kwargs.get("v")
    mask = args[2] if len(args) > 2 else kwargs.get("mask")
    uu = args[3] if len(args) > 3 else kwargs.get("uu")
    return replay_sequence_trimmer_core(m, x, v, mask, uu, rec.get("output_tensors"))


def replay_embed_container_from_capture(rec):
    m=rec["module"]; x=rec["input_tensors"][0].detach().float().cpu()
    if getattr(m,"input_bn",None) is not None:
        x=replay_batchnorm(x,m.input_bn)
        x=x.permute(2,0,1).contiguous()
    return replay_sequential(x,m.embed)

def replay_pair_embed_container_from_capture(rec):
    m=rec["module"]; args=rec.get("input_tensors",[])
    x=args[0] if len(args)>0 else None; uu=args[1] if len(args)>1 else None
    x=None if x is None else x.detach().float().cpu(); uu=None if uu is None else uu.detach().float().cpu()
    assert x is not None or uu is not None
    if x is not None: batch_size,_,seq_len=x.size()
    else: batch_size,_,seq_len,_=uu.size()
    with torch.no_grad():
        if m.is_symmetric and not m.for_onnx:
            i,j=torch.tril_indices(seq_len,seq_len,offset=-1 if m.remove_self_pair else 0,device=(x if x is not None else uu).device)
            if x is not None:
                xx=x.unsqueeze(-1).repeat(1,1,1,seq_len); xi=xx[:,:,i,j]; xj=xx[:,:,j,i]; x_pair=m.pairwise_lv_fts(xi,xj)
            else: x_pair=None
            uu_pair=uu[:,:,i,j] if uu is not None else None
        else:
            if x is not None:
                x_pair=m.pairwise_lv_fts(x.unsqueeze(-1),x.unsqueeze(-2))
                if m.remove_self_pair:
                    ii=torch.arange(0,seq_len,device=x_pair.device); x_pair[:,:,ii,ii]=0
                x_pair=x_pair.view(-1,m.pairwise_lv_dim,seq_len*seq_len)
            else: x_pair=None
            uu_pair=uu.view(-1,m.pairwise_input_dim,seq_len*seq_len) if uu is not None else None
        if m.mode=="concat":
            pair_fts=uu_pair if x_pair is None else (x_pair if uu_pair is None else torch.cat((x_pair,uu_pair),dim=1))
            elements=replay_sequential(pair_fts,m.embed)
        elif m.mode=="sum":
            if x_pair is None: elements=replay_sequential(uu_pair,m.fts_embed)
            elif uu_pair is None: elements=replay_sequential(x_pair,m.embed)
            else: elements=replay_sequential(x_pair,m.embed)+replay_sequential(uu_pair,m.fts_embed)
        else: raise RuntimeError(f"bad PairEmbed mode {m.mode}")
        if m.is_symmetric and not m.for_onnx:
            y=torch.zeros(batch_size,m.out_dim,seq_len,seq_len,dtype=elements.dtype)
            y[:,:,i.cpu(),j.cpu()]=elements; y[:,:,j.cpu(),i.cpu()]=elements
        else:
            y=elements.view(-1,m.out_dim,seq_len,seq_len)
        return y

def manual_mha_output(m,q,k,v,attn_mask=None,key_padding_mask=None):
    fake={"module":m,"q":q.detach().float().cpu(),"k":k.detach().float().cpu(),"v":v.detach().float().cpu(),"mha_output":torch.zeros_like(q.detach().float().cpu()),"attn_mask":None if attn_mask is None else attn_mask.detach().cpu(),"key_padding_mask":None if key_padding_mask is None else key_padding_mask.detach().cpu(),"attn_mask_source":"manual","attn_mask_dtype":"none" if attn_mask is None else str(attn_mask.dtype),"key_padding_mask_source":"manual","key_padding_mask_dtype":"none" if key_padding_mask is None else str(key_padding_mask.dtype)}
    return replay_mha_from_capture(fake)[0]

def replay_block_container_from_capture(rec):
    m=rec["module"]; args=rec.get("input_tensors",[]); kwargs=rec.get("kwargs_tensors",{}) or {}
    x=args[0].detach().float().cpu()
    x_cls=kwargs.get("x_cls",None); padding_mask=kwargs.get("padding_mask",None); attn_mask=kwargs.get("attn_mask",None)
    if len(args)>1 and x_cls is None: x_cls=args[1]
    if len(args)>2 and padding_mask is None: padding_mask=args[2]
    if len(args)>3 and attn_mask is None: attn_mask=args[3]
    if x_cls is not None: x_cls=x_cls.detach().float().cpu()
    if padding_mask is not None: padding_mask=padding_mask.detach().bool().cpu()
    if attn_mask is not None: attn_mask=attn_mask.detach().float().cpu()
    if x_cls is not None:
        if padding_mask is not None: padding_mask=torch.cat((torch.zeros_like(padding_mask[:,:1]),padding_mask),dim=1)
        residual=x_cls; u=torch.cat((x_cls,x),dim=0); u=replay_layernorm(u,m.pre_attn_norm); x=manual_mha_output(m.attn,x_cls,u,u,None,padding_mask)
    else:
        if getattr(m,"c_mask",None) is not None and attn_mask is not None: attn_mask=m.c_mask.detach().float().cpu()*attn_mask
        residual=x; xn=replay_layernorm(x,m.pre_attn_norm); x=manual_mha_output(m.attn,xn,xn,xn,attn_mask,padding_mask)
    if getattr(m,"c_attn",None) is not None:
        tgt_len=x.size(0); x=x.view(tgt_len,-1,m.num_heads,m.head_dim); x=torch.einsum("tbhd,h->tbdh",x,m.c_attn.detach().float().cpu()); x=x.reshape(tgt_len,-1,m.embed_dim)
    if getattr(m,"post_attn_norm",None) is not None: x=replay_layernorm(x,m.post_attn_norm)
    x=x+residual
    residual=x; x=replay_layernorm(x,m.pre_fc_norm); x=replay_linear(x,m.fc1); x=replay_activation(x,m.act)
    if getattr(m,"post_fc_norm",None) is not None: x=replay_layernorm(x,m.post_fc_norm)
    x=replay_linear(x,m.fc2)
    if getattr(m,"w_resid",None) is not None: residual=m.w_resid.detach().float().cpu()*residual
    return x+residual


def replay_particle_transformer_from_capture(rec):
    m = rec["module"]
    args = rec.get("input_tensors", [])
    kwargs = rec.get("kwargs_tensors", {}) or {}

    x = args[0] if len(args) > 0 else kwargs.get("x")
    v = args[1] if len(args) > 1 else kwargs.get("v")
    mask = args[2] if len(args) > 2 else kwargs.get("mask")
    uu = args[3] if len(args) > 3 else kwargs.get("uu")
    uu_idx = args[4] if len(args) > 4 else kwargs.get("uu_idx")

    if x is None:
        raise RuntimeError("ParticleTransformer root replay missing x input")

    x = x.detach().float().cpu()
    v = None if v is None else v.detach().float().cpu()
    mask = None if mask is None else mask.detach().cpu()
    uu = None if uu is None else uu.detach().float().cpu()
    uu_idx = None if uu_idx is None else uu_idx.detach().cpu()

    if uu_idx is not None:
        raise RuntimeError("ParticleTransformer root replay with uu_idx sparse pair path not implemented")

    trimmer_out = rec.get("trimmer_output_tensors")
    rec["sequence_trimmer_used_captured_output"] = trimmer_out is not None
    x, v, mask, uu = replay_sequence_trimmer_core(
        m.trimmer,
        x,
        v,
        mask,
        uu,
        trimmer_out,
    )
    padding_mask = ~mask.squeeze(1)

    x = replay_embed_container_from_capture({"module": m.embed, "input_tensors": [x], "output_tensors": None})
    x = x.masked_fill(~mask.permute(2, 0, 1), 0)

    attn_mask = None
    if (v is not None or uu is not None) and getattr(m, "pair_embed", None) is not None:
        pe = replay_pair_embed_container_from_capture({"module": m.pair_embed, "input_tensors": [v, uu], "output_tensors": None})
        attn_mask = pe.view(-1, v.size(-1), v.size(-1))

    for block in m.blocks:
        x = replay_block_container_from_capture({
            "module": block,
            "input_tensors": [x],
            "kwargs_tensors": {"x_cls": None, "padding_mask": padding_mask, "attn_mask": attn_mask},
            "output_tensors": None,
        })

    if getattr(m, "for_segmentation", False):
        if getattr(m, "fc", None) is not None:
            x = replay_supported(x, m.fc)
        output = x.permute(1, 2, 0).contiguous()
        if getattr(m, "for_inference", False):
            output = torch.softmax(output, dim=1)
        return output

    if getattr(m, "cls_blocks", None) is None:
        return (x, padding_mask)

    cls_tokens = m.cls_token.detach().float().cpu().expand(1, x.size(1), -1)
    for block in m.cls_blocks:
        cls_tokens = replay_block_container_from_capture({
            "module": block,
            "input_tensors": [x],
            "kwargs_tensors": {"x_cls": cls_tokens, "padding_mask": padding_mask},
            "output_tensors": None,
        })

    x_cls = replay_layernorm(cls_tokens, m.norm).squeeze(0)
    output = x_cls if getattr(m, "fc", None) is None else replay_supported(x_cls, m.fc)
    if getattr(m, "for_inference", False):
        output = torch.softmax(output, dim=1)
    return output


# ------------------------- MHA replay -------------------------
def split_mha_weights(m, h:int):
    W=m.in_proj_weight.detach().float().cpu(); b=m.in_proj_bias; b=torch.zeros(W.shape[0]) if b is None else b.detach().float().cpu(); E=int(m.embed_dim); H=int(m.num_heads); D=E//H; s,e=h*D,(h+1)*D
    Wq,Wk,Wv=W[:E][s:e],W[E:2*E][s:e],W[2*E:3*E][s:e]; bq,bk,bv=b[:E][s:e],b[E:2*E][s:e],b[2*E:3*E][s:e]; Wo=m.out_proj.weight.detach().float().cpu()[:,s:e]
    return Wq,Wk,Wv,Wo,bq,bk,bv,D

def to_batch_first(x,m): return x.detach().float().cpu() if getattr(m,"batch_first",False) else x.detach().float().cpu().permute(1,0,2).contiguous()
def from_batch_first(x,m): return x if getattr(m,"batch_first",False) else x.permute(1,0,2).contiguous()

def normalize_attn_mask(attn_mask,B,H,T,S):
    if attn_mask is None:
        z=torch.zeros(B,H,T,S); return z,torch.ones(B,H,T,S,dtype=torch.bool),"none"
    raw=attn_mask.detach().cpu(); kind=str(raw.dtype)
    if raw.dtype==torch.bool: am=torch.zeros_like(raw,dtype=torch.float32).masked_fill(raw.bool(),float("-inf")); kind+="_converted_bool_true_to_minus_inf"
    else: am=raw.float()
    if am.ndim==2: am=am.view(1,1,T,S).expand(B,H,T,S)
    elif am.ndim==3:
        if am.shape[0]==B*H: am=am.view(B,H,T,S)
        elif am.shape[0]==1: am=am.view(1,1,T,S).expand(B,H,T,S)
        else: raise RuntimeError(f"bad 3D attn_mask shape {tuple(am.shape)}")
    elif am.ndim==4: am=am.expand(B,H,T,S)
    else: raise RuntimeError(f"bad attn_mask ndim={am.ndim}")
    return am, torch.isfinite(am), kind

def prepare_additive_mask(attn_mask,kpm,B,H,T,S):
    pair,finite,kind=normalize_attn_mask(attn_mask,B,H,T,S); full=pair.clone()
    if kpm is not None:
        bad=kpm.detach().bool().cpu().view(B,1,1,S).expand(B,H,T,S); full=full.masked_fill(bad,float("-inf")); finite=finite & (~bad)
    return pair,full,finite,kind

def replay_mha_from_capture(rec):
    m=rec["module"]; q=to_batch_first(rec["q"],m); k=to_batch_first(rec["k"],m); v=to_batch_first(rec["v"],m); true=to_batch_first(rec["mha_output"],m); B,T,E=q.shape; S=k.shape[1]; H=int(m.num_heads); D=int(m.head_dim)
    pair,full,finite,kind=prepare_additive_mask(rec.get("attn_mask"),rec.get("key_padding_mask"),B,H,T,S); outs=[]; probs=[]
    for h in range(H):
        Wq,Wk,Wv,Wo,bq,bk,bv,D=split_mha_weights(m,h); Q=q@Wq.T+bq.view(1,1,-1); K=k@Wk.T+bk.view(1,1,-1); V=v@Wv.T+bv.view(1,1,-1); score=(Q@K.transpose(1,2))/math.sqrt(D)+full[:,h]; A=torch.softmax(score,dim=-1); A=torch.where(torch.isfinite(score),A,torch.zeros_like(A)); outs.append((A@V)@Wo.T); probs.append(A)
    y=torch.stack(outs,0).sum(0)
    if m.out_proj.bias is not None: y=y+m.out_proj.bias.detach().float().cpu().view(1,1,-1)
    info={"mha_rel_err":rel_err(y,true),"pair_bias_norm":finite_norm(pair),"attn_mask_source":rec.get("attn_mask_source","none"),"attn_mask_dtype":rec.get("attn_mask_dtype","none"),"key_padding_mask_source":rec.get("key_padding_mask_source","none"),"key_padding_mask_dtype":rec.get("key_padding_mask_dtype","none"),"normalized_attn_mask_kind":kind,"attention_probs_shape":tuple(torch.stack(probs,dim=1).shape)}
    return from_batch_first(y,m),info

# ------------------------- compare -------------------------
def replay_one_module(rec, tol):
    m=rec["module"]; x=rec.get("input"); y=rec.get("output")
    row={"module_name":rec["module_name"],"call_index":rec["call_index"],"module_type":m.__class__.__name__,"captured_input_shape":rec.get("input_shape",""),"captured_output_shape":rec.get("output_shape",""),"replay_output_shape":"","replay_rel_err":"","accepted":False,"fail_reason":""}
    try:
        if is_mha(m): yhat,info=replay_mha_from_capture(rec); err=info["mha_rel_err"]; row.update(info)
        elif isinstance(m,nn.Linear): yhat=replay_linear(x,m); err=rel_err(yhat,y)
        elif isinstance(m,nn.Conv1d): yhat=replay_conv1d(x,m); err=rel_err(yhat,y)
        elif isinstance(m,nn.Embedding): yhat=replay_embedding(x,m); err=rel_err(yhat,y)
        elif isinstance(m,nn.LayerNorm): yhat=replay_layernorm(x,m); err=rel_err(yhat,y)
        elif isinstance(m,(nn.BatchNorm1d,nn.BatchNorm2d,nn.BatchNorm3d)): yhat=replay_batchnorm(x,m); err=rel_err(yhat,y)
        elif "RMSNorm" in m.__class__.__name__: yhat=replay_rmsnorm(x,m); err=rel_err(yhat,y)
        elif is_activation(m): yhat=replay_activation(x,m); err=rel_err(yhat,y)
        elif isinstance(m,(nn.Dropout,nn.Dropout1d,nn.Dropout2d,nn.Dropout3d)): yhat=x; err=rel_err(yhat,y)
        elif m.__class__.__name__=="SequenceTrimmer": yhat=replay_sequence_trimmer_from_capture(rec); err=tuple_rel_err(yhat,rec.get("output_tensors"))
        elif m.__class__.__name__=="Embed": yhat=replay_embed_container_from_capture(rec); err=rel_err(yhat,y)
        elif m.__class__.__name__=="PairEmbed": yhat=replay_pair_embed_container_from_capture(rec); err=rel_err(yhat,y)
        elif m.__class__.__name__=="Block": yhat=replay_block_container_from_capture(rec); err=rel_err(yhat,y)
        elif isinstance(m,nn.Sequential): yhat=replay_sequential(x,m); err=rel_err(yhat,y)
        elif m.__class__.__name__=="ParticleTransformer": yhat=replay_particle_transformer_from_capture(rec); err=rel_err(yhat,y)
        else: row["fail_reason"]="STRUCTURAL_OP_NOT_REPLAYED_OR_UNSUPPORTED_MODULE"; return None,row
        row["replay_output_shape"]=shape_str(yhat); row["replay_rel_err"]=err; row["accepted"]=bool(err<tol); row["fail_reason"]="" if err<tol else f"replay_rel_err={err:.3e}"; return yhat,row
    except Exception as e:
        row["fail_reason"]=f"REPLAY_EXCEPTION: {type(e).__name__}: {e}"; return None,row

def replay_captured_modules(cap,tol):
    rows=[]; cache={}
    for key,rec in cap.records.items():
        yhat,row=replay_one_module(rec,tol); rows.append(row)
        if yhat is not None: cache[key]=yhat
    return rows,cache

def build_pair_bias_rows(cap,tol):
    rows=[]; blockers=[]
    pair_outputs=[]
    for (pname,pidx),prec in cap.records.items():
        if prec.get("module_type")=="PairEmbed" and prec.get("output") is not None:
            y=prec["output"].detach().float().cpu()
            if y.ndim==4: pair_outputs.append((pname,pidx,y,y.reshape(-1,y.shape[-2],y.shape[-1])))
    for (name,idx),rec in cap.records.items():
        if "attn_mask" not in rec and "key_padding_mask" not in rec: continue
        pair=rec.get("attn_mask"); kpm=rec.get("key_padding_mask"); norm=finite_norm(pair); rel=""; producer=""
        if pair is not None and norm>1e-12:
            a=pair.detach().float().cpu(); best=(float("inf"),"")
            for pname,pidx,y4,yflat in pair_outputs:
                if tuple(yflat.shape)==tuple(a.shape):
                    e=rel_err(yflat,a)
                    if e<best[0]: best=(e,f"{pname}[{pidx}]")
            if math.isfinite(best[0]): rel=best[0]; producer=best[1]
        if norm>1e-12:
            if rel!="" and float(rel)<tol:
                status="CLOSED"; reason=""; accepted=True
            else:
                status="PAIR_BIAS_NOT_CLOSED"; reason="captured additive attn_mask/pair_bias exists but PairEmbed output did not match or was not captured"; accepted=False; blockers.append(reason)
        else:
            status="CLOSED_OR_NO_PAIR_BIAS"; reason=""; accepted=True
        rows.append({"module_name":name,"call_index":idx,"attn_mask_source":rec.get("attn_mask_source","none"),"attn_mask_dtype":rec.get("attn_mask_dtype","none"),"key_padding_mask_source":rec.get("key_padding_mask_source","none"),"key_padding_mask_dtype":rec.get("key_padding_mask_dtype","none"),"pair_bias_norm":norm,"pair_bias_producer":producer,"pair_bias_rel_to_producer":rel,"key_padding_mask_present":kpm is not None,"pair_bias_replay_status":status,"accepted":accepted,"fail_reason":reason})
    return rows,("PAIR_BIAS_NOT_CLOSED" if blockers else "CLOSED"),(blockers[0] if blockers else "")

def build_block_errors(cap,module_rows,tol):
    by={(r["module_name"],int(r["call_index"])):r for r in module_rows}; rows=[]
    for (name,idx),rec in cap.records.items():
        m=rec["module"]; low=f"{name} {m.__class__.__name__}".lower()
        if any(k in low for k in ["block","cls_blocks","pair_embed","embed","fc","classifier"]):
            cmp=by.get((name,idx)); acc=bool(cmp and str(cmp.get("accepted"))=="True")
            rows.append({"block_id":len(rows),"block_name":name,"call_index":idx,"module_type":m.__class__.__name__,"captured_output_shape":rec.get("output_shape",""),"replayed_output_shape":"" if cmp is None else cmp.get("replay_output_shape",""),"block_output_rel":"" if cmp is None else cmp.get("replay_rel_err",""),"accepted":acc,"fail_reason":"" if acc else ("container_or_block_structural_replay_not_implemented" if cmp is None else cmp.get("fail_reason","not accepted"))})
    return rows

def build_unreplayed(module_rows,block_rows):
    rows=[]
    for r in module_rows:
        if str(r.get("accepted"))!="True": rows.append({"op_name":r.get("module_name",""),"call_index":r.get("call_index",""),"op_type":r.get("module_type",""),"reason":r.get("fail_reason",""),"source":"module_compare","accepted":False})
    for r in block_rows:
        if str(r.get("accepted"))!="True": rows.append({"op_name":r.get("block_name",""),"call_index":r.get("call_index",""),"op_type":r.get("module_type",""),"reason":r.get("fail_reason",""),"source":"block_errors","accepted":False})
    seen=set(); out=[]
    for r in rows:
        key=(r["op_name"],r["call_index"],r["source"])
        if key not in seen: out.append(r); seen.add(key)
    return out

def build_steps(trace,module_rows,block_rows,pair_rows):
    rows=[]; sid=0
    for src,kind,name,accepted,fail in [(trace,"source_trace","operation_kind",True,""),(module_rows,"module_replay","module_type",None,None),(block_rows,"block_replay","module_type",None,None),(pair_rows,"pair_bias_replay","pair_bias_replay_status",None,None)]:
        for r in src:
            rows.append({"step_id":sid,"step_kind":kind,"name":r.get(name,""),"module_name":r.get("module_name",r.get("block_name","")),"input_shape":r.get("input_shape",r.get("captured_input_shape","")),"output_shape":r.get("output_shape",r.get("replay_output_shape","")),"accepted":accepted if accepted is not None else r.get("accepted",False),"fail_reason":fail if fail is not None else r.get("fail_reason","")}); sid+=1
    return rows

# ------------------------- toy self-tests -------------------------
class ToyFullReplayModel(nn.Module):
    def __init__(self,batch_first=True):
        super().__init__(); self.batch_first=batch_first; self.conv=nn.Conv1d(3,4,3,padding=1); self.lin=nn.Linear(4,16); self.norm=nn.LayerNorm(16); self.act=nn.GELU(); self.attn=nn.MultiheadAttention(16,4,dropout=0.0,batch_first=batch_first); self.ffn1=nn.Linear(16,32); self.ffn_act=nn.ReLU(); self.ffn2=nn.Linear(32,16); self.cls=nn.Linear(16,5)
    def forward(self,x,attn_mask=None,key_padding_mask=None):
        h=self.act(self.norm(self.lin(self.conv(x).transpose(1,2)))); ha=h if self.batch_first else h.transpose(0,1); a,_=self.attn(ha,ha,ha,attn_mask=attn_mask,key_padding_mask=key_padding_mask,need_weights=True); a=a if self.batch_first else a.transpose(0,1); h=h+a; h=h+self.ffn2(self.ffn_act(self.ffn1(h))); return self.cls(h.mean(dim=1))

def manual_toy_replay(model,x,attn_mask=None,key_padding_mask=None,remove_residual=False):
    h=replay_activation(replay_layernorm(replay_linear(replay_conv1d(x,model.conv).transpose(1,2),model.lin),model.norm),model.act); ha=h if model.batch_first else h.transpose(0,1); true_a=model.attn(ha,ha,ha,attn_mask=attn_mask,key_padding_mask=key_padding_mask,need_weights=True)[0].detach().cpu(); rec={"module":model.attn,"q":ha,"k":ha,"v":ha,"mha_output":true_a,"attn_mask":detach_cpu(attn_mask),"key_padding_mask":detach_cpu(key_padding_mask),"attn_mask_source":"input","attn_mask_dtype":"none" if attn_mask is None else str(attn_mask.dtype),"key_padding_mask_source":"input","key_padding_mask_dtype":"none" if key_padding_mask is None else str(key_padding_mask.dtype)}; a,_=replay_mha_from_capture(rec); a=a if model.batch_first else a.transpose(0,1); h=a if remove_residual else h+a; h=h+replay_linear(replay_activation(replay_linear(h,model.ffn1),model.ffn_act),model.ffn2); return replay_linear(h.mean(dim=1),model.cls)

def self_test(full_only=False):
    torch.manual_seed(0); results=[]
    for bf in [True,False]:
        model=ToyFullReplayModel(bf).eval(); x=torch.randn(3,3,7); fm=torch.zeros(7,7); fm[:,-1]=-2.0; bm=torch.zeros(7,7,dtype=torch.bool); bm[:,-1]=True; kpm=torch.zeros(3,7,dtype=torch.bool); kpm[:,-1]=True
        for name,am,k in [("no_mask",None,None),("float_mask",fm,None),("bool_mask",bm,None),("key_padding_mask",None,kpm)]:
            cap=ForwardCapture(2); cap.attach(model)
            with torch.no_grad(): y=model(x,attn_mask=am,key_padding_mask=k)
            cap.close(); rows,_=replay_captured_modules(cap,ACCEPT_TOL); yhat=manual_toy_replay(model,x,am,k); fr=rel_err(yhat,y); assert fr<1e-5,(bf,name,fr); assert not any(r["module_type"]=="MultiheadAttention" and str(r["accepted"])!="True" for r in rows), rows
            if full_only: assert rel_err(manual_toy_replay(model,x,am,k,remove_residual=True),y)>1e-5
            results.append({"case":f"batch_first={bf}/{name}","final_logits_rel":fr,"negative_residual_test":full_only})
    print(json.dumps({"ok":True,"version":VERSION,"self_test_full_replay" if full_only else "self_test":"passed","results":results},indent=2))

# ------------------------- real run -------------------------
def load_stage1(path):
    p=Path(path)
    if not p.exists(): return "MISSING_STAGE1_JSON",{}
    j=json.loads(p.read_text(encoding="utf-8")); return j.get("matrix_coverage_status",j.get("stage1_status","UNKNOWN_STAGE1_STATUS")),j

def load_model_build_batch():
    try:
        from tools.part_attention_supertrace_real_contract_v1 import load_model, build_batch; return load_model,build_batch
    except ModuleNotFoundError:
        from tools.part_full_all_head_supertrace_real_contract_v1 import load_model, build_batch; return load_model,build_batch

def output_paths(args):
    return {"md":args.out_md,"json":args.out_json,"trace":args.out_trace,"replay_steps":args.out_replay_steps,"block_errors":args.out_block_errors,"module_compare":args.out_module_compare,"unreplayed_ops":args.out_unreplayed_ops,"pair_bias_replay":args.out_pair_bias_replay,"tensor_dir":args.tensor_dir if args.save_tensors else ""}

def write_outputs(args,manifest,trace,steps,blocks,modules,unreplayed,pair):
    write_csv(args.out_trace,trace); write_csv(args.out_replay_steps,steps); write_csv(args.out_block_errors,blocks); write_csv(args.out_module_compare,modules); write_csv(args.out_unreplayed_ops,unreplayed); write_csv(args.out_pair_bias_replay,pair); write_json(args.out_json,manifest)
    md=["# PART_FULL_FORWARD_MATRIX_REPLAY_V1\n\n",f"- version: **{VERSION}**\n",f"- stage1_status: **{manifest.get('stage1_status')}**\n",f"- full_forward_status: **{manifest.get('full_forward_status')}**\n",f"- ok: **{manifest.get('ok')}**\n",f"- final_logits_rel: `{manifest.get('final_logits_rel')}`\n",f"- max_module_replay_rel: `{manifest.get('max_module_replay_rel')}`\n",f"- max_block_output_rel: `{manifest.get('max_block_output_rel')}`\n",f"- pair_bias_replay_status: **{manifest.get('pair_bias_replay_status')}**\n",f"- unreplayed_ops: **{manifest.get('unreplayed_ops')}**\n",f"- fail_reason: `{manifest.get('fail_reason')}`\n\n","`FULL_FORWARD_CLOSED` is only emitted after decoded logits replay passes tolerance.\n"]
    Path(args.out_md).parent.mkdir(parents=True,exist_ok=True); Path(args.out_md).write_text("".join(md),encoding="utf-8")

def run_real(args):
    s1,_=load_stage1(args.stage1_json)
    if s1!="FULL_MODEL_MATRIX_COVERAGE_CLOSED":
        manifest={"version":VERSION,"stage1_status":s1,"full_forward_status":"FULL_FORWARD_NOT_CLOSED","ok":False,"final_logits_rel":None,"accept_tol":args.accept_tol,"blocks_total":0,"blocks_replayed":0,"max_block_output_rel":0.0,"max_module_replay_rel":0.0,"pair_bias_replay_status":"UNKNOWN","unreplayed_ops":0,"fail_reason":f"stage1_not_closed:{s1}","outputs":output_paths(args)}; write_outputs(args,manifest,[],[],[],[],[],[]); print(json.dumps(manifest,indent=2,ensure_ascii=False)); return
    load_model,build_batch=load_model_build_batch(); device=torch.device(args.device); model,dc=load_model(args.network_file,args.checkpoint,args.data_config,device); model.eval(); trace=build_source_trace(args.network_file,model); events=select_events(args.groups_csv,args.events_per_group); pts,fts,vec,msk,metas=build_batch(events,device,dc)
    cap=ForwardCapture(args.max_capture_calls); cap.attach(model)
    with torch.no_grad(): logits=model(pts,fts,vec,msk)
    cap.close()

    # Wire captured SequenceTrimmer output into root ParticleTransformer replay.
    # This closes the warmup/counter branch instead of guessing trim length.
    trimmer_rec = None
    for (cap_name, cap_idx), cap_rec in cap.records.items():
        if cap_rec.get("module_type") == "SequenceTrimmer":
            trimmer_rec = cap_rec
            break
    sequence_trimmer_used_captured_output = trimmer_rec is not None
    sequence_trimmer_output_shape = ""
    if trimmer_rec is not None:
        sequence_trimmer_output_shape = shape_str(trimmer_rec.get("output_tensors"))
    for (cap_name, cap_idx), cap_rec in cap.records.items():
        if cap_rec.get("module_type") == "ParticleTransformer":
            cap_rec["trimmer_output_tensors"] = None if trimmer_rec is None else trimmer_rec.get("output_tensors")
            cap_rec["sequence_trimmer_used_captured_output"] = sequence_trimmer_used_captured_output

    base_step=len(trace)
    for step,((name,idx),rec) in enumerate(cap.records.items(),start=base_step):
        trace.append({"step_id":step,"source_location":"runtime_forward_capture","operation_kind":rec.get("module_type",""),"module_name":name,"input_names":"","output_name":name,"input_shape":rec.get("input_shape",""),"output_shape":rec.get("output_shape",""),"replay_status":"CAPTURED","reason_if_not_replayed":""})
    mod_rows,cache=replay_captured_modules(cap,args.accept_tol); pair_rows,pair_status,pair_fail=build_pair_bias_rows(cap,args.accept_tol); block_rows=build_block_errors(cap,mod_rows,args.accept_tol); unreplayed=build_unreplayed(mod_rows,block_rows); steps=build_steps(trace,mod_rows,block_rows,pair_rows)
    acc_err=[]
    for r in mod_rows:
        try:
            if str(r.get("accepted"))=="True" and r.get("replay_rel_err") not in ("",None,"nan"): acc_err.append(float(r["replay_rel_err"]))
        except Exception: pass
    max_mod=max(acc_err) if acc_err else 0.0
    block_err=[]
    for r in block_rows:
        try:
            if str(r.get("accepted"))=="True" and r.get("block_output_rel") not in ("",None,"nan"): block_err.append(float(r["block_output_rel"]))
        except Exception: pass
    max_block=max(block_err) if block_err else 0.0
    root_rows = [r for r in mod_rows if r.get("module_type")=="ParticleTransformer" and r.get("module_name")=="mod"]
    logits_hat = cache.get(("mod", 0))
    final_rel = None
    if logits_hat is not None:
        final_rel = rel_err(logits_hat, detach_cpu(logits))
        # Keep root row synchronized with actual logits_hat comparison.
        for rr in root_rows:
            rr["replay_output_shape"] = shape_str(logits_hat)
            rr["replay_rel_err"] = final_rel
            rr["accepted"] = bool(final_rel < args.accept_tol)
            rr["fail_reason"] = "" if final_rel < args.accept_tol else f"final_logits_rel={final_rel:.3e}"
    elif root_rows and root_rows[0].get("replay_rel_err") not in ("", None, "nan"):
        try:
            final_rel = float(root_rows[0]["replay_rel_err"])
        except Exception:
            final_rel = None

    # Rebuild unreplayed after possible root-row synchronization.
    unreplayed = build_unreplayed(mod_rows, block_rows)
    steps = build_steps(trace, mod_rows, block_rows, pair_rows)

    sequence_trimmer_replay_status = "CAPTURED_OUTPUT_USED" if sequence_trimmer_used_captured_output else "NO_SEQUENCE_TRIMMER_CAPTURE"

    if pair_status!="CLOSED":
        status="PAIR_BIAS_NOT_CLOSED"; fail=pair_fail or "pair_bias_path_not_replayed"; ok=False
    elif unreplayed:
        status="STRUCTURAL_OP_NOT_REPLAYED"; fail="structural/container ops not replayed"; ok=False
    elif trimmer_rec is not None and not sequence_trimmer_used_captured_output:
        status="STRUCTURAL_OP_NOT_REPLAYED"; fail="SequenceTrimmer captured output was not used by root replay"; ok=False
    elif final_rel is not None and final_rel < args.accept_tol and logits_hat is not None:
        status="FULL_FORWARD_CLOSED"; fail=""; ok=True
    else:
        status="FULL_FORWARD_NOT_CLOSED"; fail="root decoded logits replay missing or above tolerance"; ok=False
    manifest={"version":VERSION,"stage1_status":s1,"full_forward_status":status,"ok":ok,"final_logits_rel":final_rel,"accept_tol":args.accept_tol,"blocks_total":len(block_rows),"blocks_replayed":sum(1 for r in block_rows if str(r.get("accepted"))=="True"),"max_block_output_rel":max_block,"max_module_replay_rel":max_mod,"pair_bias_replay_status":pair_status,"sequence_trimmer_replay_status":sequence_trimmer_replay_status,"sequence_trimmer_output_shape":sequence_trimmer_output_shape,"sequence_trimmer_used_captured_output":sequence_trimmer_used_captured_output,"unreplayed_ops":len(unreplayed),"fail_reason":fail,"model_output_shape":shape_str(logits),"logits_hat_shape":shape_str(logits_hat),"captured_modules":len(cap.records),"module_rows":len(mod_rows),"accepted_module_rows":sum(1 for r in mod_rows if str(r.get("accepted"))=="True"),"source_trace_rows":len(trace),"outputs":output_paths(args)}
    if args.save_tensors:
        td=Path(args.tensor_dir); td.mkdir(parents=True,exist_ok=True); save_pt(str(td/"trace.pt"),{"source_trace":trace,"capture_keys":list(cap.records.keys())}); save_pt(str(td/"replay_cache.pt"),cache); save_pt(str(td/"block_outputs.pt"),{"block_rows":block_rows}); save_pt(str(td/"logits_compare.pt"),{"logits_true":detach_cpu(logits),"logits_hat":logits_hat,"final_logits_rel":final_rel,"full_forward_status":status,"sequence_trimmer_replay_status":sequence_trimmer_replay_status,"sequence_trimmer_used_captured_output":sequence_trimmer_used_captured_output,"sequence_trimmer_output_shape":sequence_trimmer_output_shape})
    write_outputs(args,manifest,trace,steps,block_rows,mod_rows,unreplayed,pair_rows); print(json.dumps(manifest,indent=2,ensure_ascii=False))

# ------------------------- CLI -------------------------
def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--self-test",action="store_true"); ap.add_argument("--self-test-full-replay",action="store_true"); ap.add_argument("--network-file",default="external/particle_transformer/networks/example_ParticleTransformer_legacy.py"); ap.add_argument("--checkpoint",default="external/particle_transformer/models/ParT_kinpid.pt"); ap.add_argument("--data-config",default="external/particle_transformer/data/JetClass/JetClass_kinpid.yaml"); ap.add_argument("--groups-csv",default="reports/latest/tables/part_hqql_tbl_groups_direct_replay_v1.csv"); ap.add_argument("--stage1-json",default="manifests/latest/part_full_model_matrix_coverage_v1_4_6.json"); ap.add_argument("--stage1-artifacts",default="artifacts/latest/part_full_model_matrix_coverage_v1_4_6"); ap.add_argument("--events-per-group",type=int,default=2); ap.add_argument("--device",default="cuda" if torch.cuda.is_available() else "cpu"); ap.add_argument("--accept-tol",type=float,default=ACCEPT_TOL); ap.add_argument("--max-capture-calls",type=int,default=1); ap.add_argument("--save-tensors",action="store_true"); ap.add_argument("--tensor-dir",default="artifacts/latest/part_full_forward_matrix_replay_v1_4"); ap.add_argument("--out-json",default="manifests/latest/part_full_forward_matrix_replay_v1_4.json"); ap.add_argument("--out-md",default="reports/latest/PART_FULL_FORWARD_MATRIX_REPLAY_V1_4.md"); ap.add_argument("--out-trace",default="reports/latest/tables/part_full_forward_trace_v1_4.csv"); ap.add_argument("--out-replay-steps",default="reports/latest/tables/part_full_forward_replay_steps_v1_4.csv"); ap.add_argument("--out-block-errors",default="reports/latest/tables/part_full_forward_block_errors_v1_4.csv"); ap.add_argument("--out-module-compare",default="reports/latest/tables/part_full_forward_module_compare_v1_4.csv"); ap.add_argument("--out-unreplayed-ops",default="reports/latest/tables/part_full_forward_unreplayed_ops_v1_4.csv"); ap.add_argument("--out-pair-bias-replay",default="reports/latest/tables/part_full_forward_pair_bias_replay_v1_4.csv"); args=ap.parse_args()
    if args.self_test: self_test(False); return
    if args.self_test_full_replay: self_test(True); return
    run_real(args)
if __name__=="__main__": main()
