"""
compute_metric.py - Compute Cosine Similarity (RQ1) + Executable Rate (RQ2) from CSV
Includes 'Skeleton Cosine Similarity' to abstract away Data Fixtures.
=========================================================================
"""
import os
import sys
import csv
import json
import subprocess
import argparse
import tempfile
import numpy as np
import re

try:
    from sentence_transformers import SentenceTransformer
    from sklearn.metrics.pairwise import cosine_similarity
except ImportError:
    print("Please install required ML packages: pip install sentence-transformers scikit-learn")
    sys.exit(1)

try:
    from scipy import stats
except ImportError:
    print("Please install scipy: pip install scipy")
    sys.exit(1)


# -- Skeletonizer ------------------------------------------------------------
def skeletonize_gherkin(text):
    """
    Remove Data Tables, Strings, Numbers, Tags, and Comments from Gherkin.
    Isolates the behavioral structure.
    """
    if not text: return ""
    text = text.replace('\\n', '\n')
    lines = text.split('\n')
    skeleton_lines = []
    for line in lines:
        stripped = line.strip()
        # Remove comments and tags
        if stripped.startswith('#') or stripped.startswith('@'):
            continue
        # Remove data table lines
        if '|' in stripped and stripped.startswith('|'):
            continue
            
        # Remove quoted strings
        line_clean = re.sub(r'".*?"', '""', line)
        line_clean = re.sub(r"'.*?'", "''", line_clean)
        
        # Remove standalone numbers
        line_clean = re.sub(r'\b\d+(\.\d+)?\b', '<NUM>', line_clean)
        
        # Normalize spaces and lowercase
        line_clean = re.sub(r'\s+', ' ', line_clean).strip().lower()
        if line_clean:
            skeleton_lines.append(line_clean)
            
    return '\n'.join(skeleton_lines)


# -- Metric 2: Executable Syntax Rate (RQ2) ----------------------------------
def check_executable_syntax(gherkin_text):
    if not gherkin_text or gherkin_text.strip() == "":
        return False
        
    with tempfile.TemporaryDirectory() as tmpdir:
        feature_path = os.path.join(tmpdir, "temp.feature")
        with open(feature_path, "w", encoding="utf-8") as f:
            f.write(gherkin_text)
            
        steps_dir = os.path.join(tmpdir, "steps")
        os.makedirs(steps_dir)
        with open(os.path.join(steps_dir, "dummy.py"), "w") as f:
            f.write("")
            
        try:
            result = subprocess.run(
                [sys.executable, "-m", "behave", "--dry-run", "--no-capture", feature_path],
                capture_output=True, text=True, timeout=30
            )
            return "ParserError" not in result.stderr and "ParserError" not in result.stdout
        except Exception:
            return False


# -- Metric 1: Cosine Semantic Similarity (RQ1) ------------------------------
def compute_similarity(text1, text2, model):
    if not text1 or not text2:
        return 0.0
    embeddings = model.encode([text1, text2])
    sim = cosine_similarity([embeddings[0]], [embeddings[1]])[0][0]
    return float(sim)


# -- Statistical Tests (Proposal 5.6) -----------------------------------
def run_statistical_tests(similarities, exec_results, thresh_sim, thresh_exec, prefix="Raw"):
    print("\n" + "=" * 60)
    print(f" STATISTICAL TESTS - {prefix}")
    print("=" * 60)

    sims = np.array(similarities)
    diffs = sims - thresh_sim
    diffs_nonzero = diffs[diffs != 0]

    print(f"\n-- RQ1: {prefix} Cosine Similarity >= {thresh_sim} --")
    print(f"   N = {len(sims)}, Mean = {sims.mean():.4f}, Median = {np.median(sims):.4f}, Std = {sims.std():.4f}")

    if len(diffs_nonzero) >= 10:
        stat, p_two = stats.wilcoxon(diffs_nonzero, alternative='greater')
        print(f"   Wilcoxon signed-rank (one-tailed, greater): W = {stat:.2f}, p = {p_two:.6f}")
        if p_two < 0.05:
            print("   [PASS] Reject H0 -> Threshold met")
        else:
            print("   [FAIL] Fail to reject H0")

        # Effect size
        pos_ranks = len(diffs[diffs > 0])
        neg_ranks = len(diffs[diffs < 0])
        total = pos_ranks + neg_ranks
        if total > 0:
            cliffs_delta = (pos_ranks - neg_ranks) / total
            print(f"   Cliff's delta = {cliffs_delta:.4f}")
    else:
        print("   Not enough non-zero differences for Wilcoxon test.")

    # -- RQ2: Executable Rate --
    if prefix == "Raw":
        print(f"\n-- RQ2: Executable Rate >= {thresh_exec} --")
        k = sum(exec_results)
        n = len(exec_results)
        rate = k / n if n > 0 else 0
        print(f"   N = {n}, Pass = {k}, Rate = {rate:.2%}")
        
        if n >= 10:
            result = stats.binomtest(k, n, p=thresh_exec, alternative='greater')
            print(f"   Binomial exact test (one-tailed, greater): p = {result.pvalue:.6f}")
            if result.pvalue < 0.05:
                print("   [PASS] Reject H0 -> Threshold met")
            else:
                print("   [FAIL] Fail to reject H0")


def main():
    parser = argparse.ArgumentParser(description="Evaluate Generated Gherkin vs Ground Truth (Raw & Skeleton)")
    parser.add_argument("--generated-csv", required=True, help="Path to full_generated_gherkin.csv")
    parser.add_argument("--ground-truth-csv", required=True, help="Path to full_ground_truth.csv")
    parser.add_argument("--threshold-sim", type=float, default=0.85, help="Threshold for RQ1")
    parser.add_argument("--threshold-exec", type=float, default=0.80, help="Threshold for RQ2")
    args = parser.parse_args()

    print("=" * 60)
    print(" LOADING DATA FROM CSV...")
    
    if not os.path.exists(args.generated_csv):
        print(f"ERROR: File not found: {args.generated_csv}")
        sys.exit(1)
    if not os.path.exists(args.ground_truth_csv):
        print(f"ERROR: File not found: {args.ground_truth_csv}")
        sys.exit(1)

    gt_map = {}
    with open(args.ground_truth_csv, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            gt_map[str(row["id"])] = row.get("gherkin_content", "")

    eval_data = []
    with open(args.generated_csv, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            sid = str(row["id"])
            generated = row.get("gherkin_generated", "")
            expert = gt_map.get(sid, "")
            if expert and expert.strip() != "":
                eval_data.append({
                    "id": sid,
                    "generated": generated,
                    "expert": expert
                })

    n = len(eval_data)
    print(f" Loaded {n} samples.")
    print("=" * 60)

    # RQ2: Executable Rate
    print(f"\n[1/3] Checking Executable Syntax ({n} samples)...")
    exec_results = []
    for item in eval_data:
        passed = check_executable_syntax(item["generated"])
        exec_results.append(passed)

    k_pass = sum(exec_results)
    print(f"  Executable Rate: {k_pass}/{n} = {k_pass/n:.2%}")

    # RQ1: Cosine Similarity (Raw and Skeleton)
    print(f"\n[2/3] Computing Cosine Similarity ({n} samples)...")
    print("  Loading model 'all-MiniLM-L6-v2' (may take a minute the first time)...")
    model = SentenceTransformer('all-MiniLM-L6-v2')

    raw_similarities = []
    skeleton_similarities = []
    
    for item in eval_data:
        # Raw
        raw_sim = compute_similarity(item["generated"], item["expert"], model)
        raw_similarities.append(raw_sim)
        
        # Skeleton
        gen_skel = skeletonize_gherkin(item["generated"])
        exp_skel = skeletonize_gherkin(item["expert"])
        skel_sim = compute_similarity(gen_skel, exp_skel, model)
        skeleton_similarities.append(skel_sim)
        
        icon = "[PASS]" if skel_sim >= args.threshold_sim else "[WARN]"
        print(f"  {icon} ID {item['id']}: Raw={raw_sim:.4f} | Skeleton={skel_sim:.4f}")

    mean_raw = np.mean(raw_similarities) if raw_similarities else 0
    mean_skel = np.mean(skeleton_similarities) if skeleton_similarities else 0
    print(f"\n  Mean RAW Cosine Similarity: {mean_raw:.4f}")
    print(f"  Mean SKELETON Cosine Similarity: {mean_skel:.4f}")

    # Statistical Tests
    print(f"\n[3/3] Running Statistical Tests...")
    if n >= 10:
        run_statistical_tests(raw_similarities, exec_results, args.threshold_sim, args.threshold_exec, prefix="Raw")
        run_statistical_tests(skeleton_similarities, exec_results, args.threshold_sim, args.threshold_exec, prefix="Skeleton")
    else:
        print(f"  WARNING: Only {n} samples. Need >= 10 to run stats.")

    # Save results
    output = {
        "n_samples":        n,
        "executable_rate":  k_pass / n if n > 0 else 0,
        "mean_raw_sim":     float(mean_raw),
        "mean_skeleton_sim":float(mean_skel),
        "raw_similarities": raw_similarities,
        "skel_similarities": skeleton_similarities,
        "exec_results":     exec_results
    }
    
    out_dir = os.path.dirname(args.generated_csv)
    base_name = os.path.splitext(os.path.basename(args.generated_csv))[0]
    
    output_file = os.path.join(out_dir, f"{base_name}_metrics.json")
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    metric_csv_path = os.path.join(out_dir, f"{base_name}_metrics_per_sample.csv")
    with open(metric_csv_path, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "raw_cosine", "skeleton_cosine", "executable"])
        for i, item in enumerate(eval_data):
            writer.writerow([
                item["id"],
                f"{raw_similarities[i]:.4f}",
                f"{skeleton_similarities[i]:.4f}",
                "PASS" if exec_results[i] else "FAIL"
            ])
            
    print(f"\nResults JSON saved to: {output_file}")
    print(f"Per-sample CSV saved to: {metric_csv_path}")


if __name__ == "__main__":
    main()
