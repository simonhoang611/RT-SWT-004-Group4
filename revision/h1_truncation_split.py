"""
h1_truncation_split.py  (revision, Action Tracker H1 and H10)

The stories of 84 of the 100 Fineract files were written from only the first
15,000 characters of the reference (scripts/local_reverse_engineer_us.py,
str(gherkin_content)[:15000]), but every generated file is scored against the
full reference. Exemplars 2, 102, 202 are excluded (N = 258; Fineract 99 =
84 truncated + 15 not truncated).

Part 1 (original scores, results/full_per_row_metrics.csv): Fineract truncated
versus non-truncated: median, IQR, mean, count >= 0.85, two-sided Mann-Whitney.

Part 2 (sensitivity): skeleton cosine recomputed against the skeleton of the
first 15,000 characters of each reference, i.e. the text the story writer saw.
Files under 15,000 characters are unchanged by construction. Uses to_skeleton()
and the ONNX encoder of revision/h2/h2_cosine_onnx.py; C0 against the full
reference is recomputed first and compared with results/full_per_row_metrics.csv.

Usage (from the repository root):
  python revision/h1_truncation_split.py --onnx-dir <folder with model.onnx and tokenizer.json>
"""
import argparse
import os
import sys

import numpy as np
import pandas as pd
from scipy.stats import mannwhitneyu, wilcoxon
from tokenizers import Tokenizer

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "h2"))
from h2_cosine_onnx import Encoder, to_skeleton  # noqa: E402

T = 0.85
CUT = 15000
EXEMPLAR_IDS = [2, 102, 202]


def describe(name, x):
    q1, med, q3 = np.quantile(x, [0.25, 0.5, 0.75])
    k = int((x >= T).sum())
    return {"group": name, "N": len(x), "median": med, "Q1": q1, "Q3": q3, "mean": x.mean(),
            "n_ge_0.85": k, "share_ge_0.85": k / len(x)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--onnx-dir", required=True)
    ap.add_argument("--outdir", default="revision/results")
    a = ap.parse_args()
    os.makedirs(a.outdir, exist_ok=True)

    gt = pd.read_csv("data/full_ground_truth.csv")[["id", "project_name", "gherkin_content"]]
    gen = pd.read_csv("results/full_gpt54mini_output.csv")[["id", "generated_gherkin"]]
    orig = pd.read_csv("results/full_per_row_metrics.csv")[["id", "skeleton_cosine"]]
    df = gt.merge(gen, on="id", validate="one_to_one").merge(orig, on="id", validate="one_to_one")
    df = df[~df.id.isin(EXEMPLAR_IDS)].reset_index(drop=True)
    df["ref_chars"] = df.gherkin_content.astype(str).str.len()
    df["truncated"] = df.ref_chars > CUT

    enc = Encoder(a.onnx_dir)
    counter = Tokenizer.from_file(os.path.join(a.onnx_dir, "tokenizer.json"))
    counter.no_padding()
    counter.no_truncation()
    cos_full, cos_prefix, tok_full, tok_prefix = [], [], [], []
    for r in df.itertuples():
        g = enc.encode(to_skeleton(str(r.generated_gherkin)))
        ref_full = to_skeleton(str(r.gherkin_content))
        ref_prefix = to_skeleton(str(r.gherkin_content)[:CUT])
        cos_full.append(float(g @ enc.encode(ref_full)))
        cos_prefix.append(float(g @ enc.encode(ref_prefix)))
        tok_full.append(len(counter.encode(ref_full).ids))
        tok_prefix.append(len(counter.encode(ref_prefix).ids))
    df["cos_full_recomputed"] = cos_full
    df["cos_prefix_15000"] = cos_prefix
    df["ref_skeleton_tokens"] = tok_full
    df["ref_prefix_skeleton_tokens"] = tok_prefix
    repro = (df.cos_full_recomputed - df.skeleton_cosine).abs().max()

    df.drop(columns=["gherkin_content", "generated_gherkin"]).to_csv(
        os.path.join(a.outdir, "h1_truncation_per_file.csv"), index=False)

    fin = df[df.project_name == "Apache Fineract"]
    tr, nt = fin[fin.truncated], fin[~fin.truncated]
    rows = [describe("Fineract non-truncated (original)", nt.skeleton_cosine.to_numpy()),
            describe("Fineract truncated (original)", tr.skeleton_cosine.to_numpy()),
            describe("Fineract truncated (prefix reference)", tr.cos_prefix_15000.to_numpy()),
            describe("Fineract all (original)", fin.skeleton_cosine.to_numpy()),
            describe("Fineract all (prefix reference)", fin.cos_prefix_15000.to_numpy()),
            describe("All N=258 (original)", df.skeleton_cosine.to_numpy()),
            describe("All N=258 (prefix reference)", df.cos_prefix_15000.to_numpy())]
    table = pd.DataFrame(rows)
    table.to_csv(os.path.join(a.outdir, "h1_truncation_split.csv"), index=False)

    d = tr.cos_prefix_15000 - tr.skeleton_cosine
    changed = int((d.abs() > 1e-6).sum())
    unchanged_nt = (nt.cos_prefix_15000 - nt.skeleton_cosine).abs().max()
    p_mw_orig = mannwhitneyu(tr.skeleton_cosine, nt.skeleton_cosine, alternative="two-sided").pvalue
    p_mw_prefix = mannwhitneyu(tr.cos_prefix_15000, nt.cos_prefix_15000, alternative="two-sided").pvalue
    p_all = wilcoxon(df.cos_prefix_15000 - T, alternative="greater").pvalue
    p_all_orig = wilcoxon(df.skeleton_cosine - T, alternative="greater").pvalue

    rep = [table.round(4).to_string(index=False), "",
           f"reproduction of results/full_per_row_metrics.csv (N={len(df)}): max_abs_diff={repro:.2e}",
           f"non-truncated files, prefix vs original: max_abs_diff={unchanged_nt:.2e}",
           f"Fineract truncated vs non-truncated, Mann-Whitney two-sided: original p={p_mw_orig:.4f}, prefix p={p_mw_prefix:.4f}",
           f"Fineract truncated (n={len(tr)}): cosine changed by >1e-6 in {changed} files; "
           f"prefix - original: min={d.min():.4f} max={d.max():.4f}; changed ids: {tr.id[d.abs() > 1e-6].tolist()}",
           f"Fineract truncated references: skeleton tokens median full={tr.ref_skeleton_tokens.median():.0f}, "
           f"prefix={tr.ref_prefix_skeleton_tokens.median():.0f}; prefix skeleton > 256 tokens in "
           f"{int((tr.ref_prefix_skeleton_tokens > 256).sum())} of {len(tr)}",
           f"All N=258, one-sided Wilcoxon x - 0.85 > 0: original p={p_all_orig:.4f}, prefix p={p_all:.4f}"]
    open(os.path.join(a.outdir, "h1_truncation_report.txt"), "w", encoding="utf-8").write("\n".join(rep) + "\n")
    print("\n".join(rep))


if __name__ == "__main__":
    main()
