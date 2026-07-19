"""
Compute Metrics (Role MS)
=========================
Script nay doc file output.csv (do LR tao ra) va ground truth,
tinh raw_cosine + skeleton_cosine + executable, roi luu vao summary.csv

Model: gpt-5.4-mini-2026-03-17 (temperature=0, few-shot)
"""
import pandas as pd
import re
import subprocess
import sys
import io
import os

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import argparse

parser = argparse.ArgumentParser(description="Compute Metrics for Gherkin Generation")
parser.add_argument("--output", help="Path to generated output CSV", default=r"results\full_gpt54mini_output.csv")
parser.add_argument("--gt", help="Path to ground truth CSV", default=r"data\full_ground_truth.csv")
parser.add_argument("--summary", help="Path to save summary CSV", default=r"results\summary.csv")
args = parser.parse_args()

# === 1. Load data ===
BASE_DIR = r"C:\Users\hoang\Downloads\RBL\RBL-to-configure"
output_path = os.path.join(BASE_DIR, args.output)
gt_path = os.path.join(BASE_DIR, args.gt)
summary_path = os.path.join(BASE_DIR, args.summary)

# Create results folder if not exist
os.makedirs(os.path.dirname(summary_path), exist_ok=True)

df_gen = pd.read_csv(output_path)
df_gt  = pd.read_csv(gt_path)

# Merge theo id
df = df_gen.merge(df_gt[['id', 'gherkin_content']], on='id', how='inner')
print(f"Matched rows: {len(df)}")

# === 2. Load Sentence Transformer model ===
print("Loading sentence-transformers/all-MiniLM-L6-v2 ...")
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')
print("Model loaded!")

# === 3. Skeleton function ===
def to_skeleton(gherkin_text):
    """
    Giu lai cau truc Given/When/Then, loai bo data cu the (trong dau ngoac kep).
    Vi du: Given a customer named "John" -> Given a customer named <PARAM>
    """
    if not isinstance(gherkin_text, str):
        return ""
    # Chuyen literal \n thanh newline that (fix CSV encoding)
    text = gherkin_text.replace('\\n', '\n')
    # Bo cac ky tu tag nhu @checkout, @api, @ui
    text = re.sub(r'@\w+', '', text)
    # Thay the cac gia tri trong dau ngoac kep bang <PARAM>
    text = re.sub(r'"[^"]*"', '<PARAM>', text)
    # Thay the cac so bang <NUM>
    text = re.sub(r'\b\d+(\.\d+)?\b', '<NUM>', text)
    # Giu lai cac dong co keyword BDD
    lines = text.split('\n')
    keywords = ['Feature', 'Scenario', 'Given', 'When', 'Then', 'And', 'But', 'Background']
    skeleton_lines = []
    for line in lines:
        stripped = line.strip()
        if any(stripped.startswith(kw) for kw in keywords):
            skeleton_lines.append(stripped)
    return '\n'.join(skeleton_lines)

# === 4. Check Executable ===
def check_executable(gherkin_text, temp_file="temp.feature"):
    if not isinstance(gherkin_text, str) or not gherkin_text.strip():
        return "FAIL"
    with open(temp_file, "w", encoding="utf-8") as f:
        f.write(gherkin_text)
    result = subprocess.run([sys.executable, "-m", "behave", "--dry-run", temp_file], capture_output=True, text=True)
    if "ParserError" in result.stderr or "ParserError" in result.stdout:
        return "FAIL"
    return "PASS"

# === 5. Compute all metrics ===
print("Computing cosine similarities and executable check...")

raw_cosines = []
skeleton_cosines = []
executables = []

for idx, row in df.iterrows():
    gen_text = str(row['generated_gherkin'])
    gt_text  = str(row['gherkin_content'])

    # Unescape ground truth
    gt_text_clean = gt_text.replace('\\n', '\n')

    # Raw cosine
    embeddings = model.encode([gen_text, gt_text_clean])
    raw_cos = cosine_similarity([embeddings[0]], [embeddings[1]])[0][0]
    raw_cosines.append(float(raw_cos))

    # Skeleton cosine
    gen_skel = to_skeleton(gen_text)
    gt_skel  = to_skeleton(gt_text)
    skel_embeddings = model.encode([gen_skel, gt_skel])
    skel_cos = cosine_similarity([skel_embeddings[0]], [skel_embeddings[1]])[0][0]
    skeleton_cosines.append(float(skel_cos))

    # Executable
    exe = check_executable(gen_text)
    executables.append(exe)

df['raw_cosine'] = raw_cosines
df['skeleton_cosine'] = skeleton_cosines
df['executable'] = executables

# === 6. Summary statistics ===
print("\n" + "="*50)
print("       DESCRIPTIVE STATISTICS")
print("="*50)
print(f"\n--- Raw Cosine ---")
print(f"  Mean:   {df['raw_cosine'].mean():.4f}")
print(f"  Median: {df['raw_cosine'].median():.4f}")
print(f"  Std:    {df['raw_cosine'].std():.4f}")
print(f"  Min:    {df['raw_cosine'].min():.4f}")
print(f"  Max:    {df['raw_cosine'].max():.4f}")

print(f"\n--- Skeleton Cosine ---")
print(f"  Mean:   {df['skeleton_cosine'].mean():.4f}")
print(f"  Median: {df['skeleton_cosine'].median():.4f}")
print(f"  Std:    {df['skeleton_cosine'].std():.4f}")
print(f"  Min:    {df['skeleton_cosine'].min():.4f}")
print(f"  Max:    {df['skeleton_cosine'].max():.4f}")

print(f"\n--- Executable Rate ---")
pass_count = (df['executable'] == 'PASS').sum()
print(f"  PASS: {pass_count}/{len(df)} ({pass_count/len(df)*100:.1f}%)")

# === 7. Save summary.csv (CHI CHUA METRIC - KHONG CHUA generated_gherkin) ===
df[['id', 'raw_cosine', 'skeleton_cosine', 'executable']].to_csv(summary_path, index=False, encoding='utf-8')
print(f"\nSaved summary (Role MS): {summary_path}")

# Clean up temp file
if os.path.exists("temp.feature"):
    os.remove("temp.feature")

print("DONE!")
