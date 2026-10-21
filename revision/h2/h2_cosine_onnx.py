"""
h2_cosine_onnx.py  (revision, Action Tracker H2/M1)

Skeleton cosine for C0, C1 and C2 with the unchanged to_skeleton() of
scripts/compute_metrics.py and all-MiniLM-L6-v2, run through onnxruntime
instead of sentence-transformers (the cloud container that computed the H2
results could not reach huggingface.co).

Model files: the ONNX export of all-MiniLM-L6-v2 published by Chroma at
https://chroma-onnx-models.s3.amazonaws.com/all-MiniLM-L6-v2/onnx.tar.gz
(SHA-256 of the archive recorded in the report). Pipeline reproduced from
sentence-transformers: tokenizer.json with truncation at 256 tokens
(max_seq_length of the model, special tokens included), token mean pooling
with the attention mask, L2 normalisation, dot product.

Validity check built in: C0 is recomputed and compared with
results/full_per_row_metrics.csv (the original sentence-transformers run).
The report states the largest absolute difference.

Usage (from the repository root):
  python revision/h2/h2_cosine_onnx.py --onnx-dir <folder with model.onnx and tokenizer.json>
"""
import argparse
import hashlib
import os
import re

import numpy as np
import onnxruntime as ort
import pandas as pd
from tokenizers import Tokenizer


def to_skeleton(gherkin_text):
    # Copied verbatim from scripts/compute_metrics.py (comments translated).
    if not isinstance(gherkin_text, str):
        return ""
    text = gherkin_text.replace('\\n', '\n')
    text = re.sub(r'@\w+', '', text)
    text = re.sub(r'"[^"]*"', '<PARAM>', text)
    text = re.sub(r'\b\d+(\.\d+)?\b', '<NUM>', text)
    lines = text.split('\n')
    keywords = ['Feature', 'Scenario', 'Given', 'When', 'Then', 'And', 'But', 'Background']
    skeleton_lines = []
    for line in lines:
        stripped = line.strip()
        if any(stripped.startswith(kw) for kw in keywords):
            skeleton_lines.append(stripped)
    return '\n'.join(skeleton_lines)


class Encoder:
    def __init__(self, d):
        self.tok = Tokenizer.from_file(os.path.join(d, "tokenizer.json"))
        self.tok.no_padding()
        self.tok.enable_truncation(max_length=256)
        self.sess = ort.InferenceSession(os.path.join(d, "model.onnx"), providers=["CPUExecutionProvider"])
        self.inputs = {i.name for i in self.sess.get_inputs()}

    def encode(self, text):
        e = self.tok.encode(text)
        feed = {"input_ids": np.array([e.ids], dtype=np.int64),
                "attention_mask": np.array([e.attention_mask], dtype=np.int64)}
        if "token_type_ids" in self.inputs:
            feed["token_type_ids"] = np.array([e.type_ids], dtype=np.int64)
        tok_emb = self.sess.run(None, feed)[0][0]          # (tokens, 384)
        m = feed["attention_mask"][0][:, None].astype(np.float32)
        v = (tok_emb * m).sum(0) / max(m.sum(), 1e-9)       # mean pooling
        return v / max(np.linalg.norm(v), 1e-12)            # Normalize module


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--onnx-dir", required=True)
    ap.add_argument("--outdir", default="revision/h2")
    x = ap.parse_args()
    enc = Encoder(x.onnx_dir)
    gt = pd.read_csv("data/full_ground_truth.csv")[["id", "gherkin_content"]]
    cache = {}

    def emb(t):
        if t not in cache:
            cache[t] = enc.encode(t)
        return cache[t]

    files = {"C0": "results/full_gpt54mini_output.csv",
             "C1": "revision/h2/h2_C1_output.csv",
             "C2": "revision/h2/h2_C2_output.csv"}
    rows = []
    for c, f in files.items():
        df = pd.read_csv(f).merge(gt, on="id", how="inner", validate="one_to_one")
        for r in df.itertuples():
            g = to_skeleton(str(r.generated_gherkin))
            ref = to_skeleton(str(r.gherkin_content))
            rows.append({"condition": c, "id": r.id, "skeleton_cosine": float(emb(g) @ emb(ref)),
                         "gen_chars": len(str(r.generated_gherkin))})
    out = pd.DataFrame(rows)
    out.to_csv(os.path.join(x.outdir, "h2_cosine_per_file.csv"), index=False)

    orig = pd.read_csv("results/full_per_row_metrics.csv")[["id", "skeleton_cosine"]]
    chk = out[out.condition == "C0"].merge(orig, on="id", suffixes=("_onnx", "_orig"))
    d = (chk.skeleton_cosine_onnx - chk.skeleton_cosine_orig).abs()
    lines = [f"onnx model.onnx sha256: {hashlib.sha256(open(os.path.join(x.onnx_dir, 'model.onnx'), 'rb').read()).hexdigest()}",
             f"C0 reproduction vs results/full_per_row_metrics.csv: n={len(chk)} max_abs_diff={d.max():.2e} mean_abs_diff={d.mean():.2e}",
             f"rows: {out.groupby('condition').size().to_dict()}"]
    open(os.path.join(x.outdir, "h2_cosine_check.txt"), "w", encoding="utf-8").write("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
