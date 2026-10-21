"""
e1_old_check_demo.py  (revision, plan item E1)

Shows why check_executable() in scripts/compute_metrics.py reported PASS for
every file. The function is copied unchanged. It runs `behave --dry-run` on a
single .feature file in a folder that has no steps/ directory; behave stops
with a configuration error before parsing, its output never contains the word
"ParserError", and the function therefore returns "PASS".

The demo feeds it (1) plain text that is not Gherkin and (2) the generated file
of id 136, which behave's parser rejects (see check_syntax.py).

Usage (from the repository root):
    python revision/e1_old_check_demo.py
"""
import os
import subprocess
import sys
import tempfile

import pandas as pd


# --- copied unchanged from scripts/compute_metrics.py ---
def check_executable(gherkin_text, temp_file="temp.feature"):
    if not isinstance(gherkin_text, str) or not gherkin_text.strip():
        return "FAIL"
    with open(temp_file, "w", encoding="utf-8") as f:
        f.write(gherkin_text)
    result = subprocess.run([sys.executable, "-m", "behave", "--dry-run", temp_file], capture_output=True, text=True)
    if "ParserError" in result.stderr or "ParserError" in result.stdout:
        return "FAIL"
    return "PASS"
# --------------------------------------------------------


def main():
    out = pd.read_csv(os.path.join(os.getcwd(), "results/full_gpt54mini_output.csv"))
    id136 = out.loc[out["id"] == 136, "generated_gherkin"].iloc[0]
    cases = {"plain text, not Gherkin": "This is not a feature file at all.", "generated id 136": id136}
    cwd = os.getcwd()
    with tempfile.TemporaryDirectory() as d:
        os.chdir(d)  # empty folder: no steps/, as in the original run
        for name, text in cases.items():
            verdict = check_executable(text)
            r = subprocess.run([sys.executable, "-m", "behave", "--dry-run", "temp.feature"],
                               capture_output=True, text=True)
            first = (r.stdout + r.stderr).strip().splitlines()[:2]
            print(f"{name}: check_executable -> {verdict}; behave says: {first}")
        os.chdir(cwd)


if __name__ == "__main__":
    main()
