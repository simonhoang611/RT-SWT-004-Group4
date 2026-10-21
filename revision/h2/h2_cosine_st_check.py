"""
h2_cosine_st_check.py  (revision, H2: confirm the ONNX cosine with sentence-transformers)

Recomputes skeleton cosine for C0, C1 and C2 with sentence-transformers and
all-MiniLM-L6-v2, exactly as scripts/compute_metrics.py does
(model.encode on the two skeletons, then sklearn cosine_similarity), and
compares the result with revision/h2/h2_cosine_per_file.csv (ONNX run).

The model revision is pinned to the current commit of the Hugging Face repo
and written to the report, so the run can be repeated with the same weights.

Run on a machine that can reach huggingface.co, from the repository root:
  python -m pip install sentence-transformers scikit-learn pandas
  python revision/h2/h2_cosine_st_check.py
Outputs: revision/h2/h2_cosine_st.csv, revision/h2/h2_cosine_st_check.txt
"""
import platform
import re

import pandas as pd
import sentence_transformers
from huggingface_hub import model_info
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

REPO = "sentence-transformers/all-MiniLM-L6-v2"


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


def main():
    rev = model_info(REPO).sha
    model = SentenceTransformer(REPO, revision=rev, device="cpu")
    gt = pd.read_csv("data/full_ground_truth.csv")[["id", "gherkin_content"]]
    files = {"C0": "results/full_gpt54mini_output.csv",
             "C1": "revision/h2/h2_C1_output.csv",
             "C2": "revision/h2/h2_C2_output.csv"}
    rows = []
    for c, f in files.items():
        df = pd.read_csv(f).merge(gt, on="id", how="inner", validate="one_to_one")
        for n, r in enumerate(df.itertuples(), 1):
            e = model.encode([to_skeleton(str(r.generated_gherkin)), to_skeleton(str(r.gherkin_content))])
            rows.append({"condition": c, "id": r.id,
                         "skeleton_cosine_st": float(cosine_similarity([e[0]], [e[1]])[0][0])})
            if n % 50 == 0:
                print(f"{c}: {n}/{len(df)}", flush=True)
    st = pd.DataFrame(rows)
    st.to_csv("revision/h2/h2_cosine_st.csv", index=False)

    onnx = pd.read_csv("revision/h2/h2_cosine_per_file.csv")
    m = st.merge(onnx, on=["condition", "id"])
    d = (m.skeleton_cosine_st - m.skeleton_cosine).abs()
    orig = pd.read_csv("results/full_per_row_metrics.csv")[["id", "skeleton_cosine"]]
    c0 = st[st.condition == "C0"].merge(orig, on="id")
    d0 = (c0.skeleton_cosine_st - c0.skeleton_cosine).abs()
    lines = [f"model {REPO} revision {rev}",
             f"sentence-transformers {sentence_transformers.__version__}, python {platform.python_version()}, {platform.platform()}",
             f"sentence-transformers vs ONNX (h2_cosine_per_file.csv): n={len(m)} max_abs_diff={d.max():.2e}",
             "  per condition: " + ", ".join(f"{c} {g.max():.2e}" for c, g in d.groupby(m.condition)),
             f"C0 sentence-transformers vs results/full_per_row_metrics.csv: n={len(c0)} max_abs_diff={d0.max():.2e}"]
    open("revision/h2/h2_cosine_st_check.txt", "w", encoding="utf-8").write("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
