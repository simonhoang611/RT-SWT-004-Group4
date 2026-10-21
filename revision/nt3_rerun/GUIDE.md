# Guide for An to run RUN CHECKS personally (NT3), 18 Oct 2026

English translation (19 Oct 2026, prepared with an AI assistant, Claude) of the Vietnamese original `HUONG_DAN.md` (SHA-256 1bb13b9ad497037c…), which the authors keep unchanged.

## Purpose

NT3 requires **An to rerun personally** the analysis scripts of the revision, and then **to read the results personally**. Before, Codex had run them on An's behalf, so NT3 was not yet met. This time An must type the commands and read the results personally. Do not ask Codex, Claude or any other AI to run them instead, because then NT3 would still not be met.

This package runs **offline**: it does not call any API, does not recompute embeddings, and does not change data or labels. The script does only 3 things:
1. It checks the hash of every input file against `MANIFEST_SHA256.txt`. If any file has been changed, the script stops immediately.
2. It copies `original/` to a new folder inside `ket_qua/`, then runs the 10 scripts one after another in that copy. ("ket_qua" in folder names and "KET_QUA" in `KET_QUA.json` are Vietnamese for "results"; the script still uses these names.)
3. It compares the 15 result tables just produced with the 15 original tables in `original/`. These original tables are the numbers currently used in the paper.

On Claude's computer, the package took about 25 seconds in total and gave 15/15 matching tables.

## Package contents

| File / folder | What it is |
|---|---|
| `GUIDE.md` (was `HUONG_DAN.md`) | This file |
| `RUN_CHECKS.ps1` (was `RUN_CHECKS_AN.ps1`) | Runner file for Windows: creates a Python environment, installs the libraries, runs the checks |
| `run_checks.py` | The check script (readable, about 100 lines) |
| `requirements.txt` | Library versions: behave 1.3.3, pandas 3.0.5, scipy 1.18.1, numpy 2.5.3 |
| `MANIFEST_SHA256.txt` | SHA-256 hashes of the 53 files in `original/` and `audit_inputs/` |
| `original/` | The group's original data, outputs and scripts, copied from `RBL-to-commit` |
| `audit_inputs/` | `b2_annotation_An_CONFIRMED.csv` (the labels An confirmed on 15 Oct) and `mutation_results.csv` |

## What you need

- A Windows computer with Internet access. The network is only needed for the first library installation.
- **Python 3.12 or 3.13**, downloaded from https://www.python.org/downloads/. Note: pandas 3.0.5 cannot be installed on Python 3.10 or older.
  - During installation, tick **"Add python.exe to PATH"** and keep the **"py launcher"** option.
  - Check: open PowerShell and type `py -3 --version`. It must show `Python 3.12.x` or `Python 3.13.x`.

## Steps

**Step 1. Unzip.** Right-click `FISAT_RUN_CHECKS_An_2026-10-18.zip` and choose **Extract All…**. It is best to extract to a short path, for example `D:\FISAT\`. Do not edit, rename or delete any file in the extracted folder.

**Step 2. Open PowerShell in the package folder.** Open the folder `FISAT_RUN_CHECKS_An_2026-10-18`. Click the address bar of File Explorer, type `powershell` and press Enter. A PowerShell window opens, already in this folder.

**Step 3. Run.** Type the command below and press Enter:

```powershell
powershell -ExecutionPolicy Bypass -File .\RUN_CHECKS.ps1
```

The script does 3 things by itself:
- It creates the `.venv` folder.
- It installs the libraries. The first time this takes a few minutes; later runs skip this step.
- It asks for a full name. An types **An's own real full name** and presses Enter.

**Step 4. Look at the screen.** A correct result looks like this:

```
Manifest: all files match.
Step  1/10  revision/check_syntax.py                   exit 0
...
Step 10/10  revision/h2/h2_analysis.py                 exit 0

Tables matching the originals: 15/15
RESULT: ALL MATCH
Saved in: ...\ket_qua\<date_time>
```

**Step 5. Read the results personally.** Open the folder `ket_qua\<date_time>\`.
- `KET_QUA.json` contains: the name of the person who ran it, the time, the Python and library versions, the exit codes of the 10 steps, the result of comparing the 15 tables, and the summary line `"all_15_tables_match": true`.
- `execution_logs\01_…txt` to `10_…txt` are the full output of each script. An should read at least the following lines and compare them with the paper:

| Log | Compare with the paper |
|---|---|
| `01_check_syntax.txt` | Over all 261 files: 258 PASS; the 3 files with errors are 136, 148, 154. Leaving out the 3 example files (2, 102, 202, all PASS) gives 255/258 = 98.84% (§4.6) |
| `03_recompute_descriptives.txt` | Line `no_exemplars_N258 all`: median 0.8533, one-sided p 0.4739; line `all_N261 all`: p 0.3554 (Table 2) |
| `04_b3_threshold_sensitivity.txt` | At the threshold 0.84, p = 9.68×10⁻³ ≈ 0.0097 (§4.3, Table 6) |
| `05_h1_domain_analysis.txt` | H = 60.869, eta^2_H = 0.231; the pair Fineract vs Diaspora has p_holm = 0.7397 (§4.2) |
| `06_b1_leakage_proxy.txt` | `story_gt_overlap` by project: 1.5% (Fineract), 5.2% (Diaspora), 6.7% (Sylius); ρ = 0.277 (Sylius), 0.313 (Diaspora) (§4.5). Note added 19 Oct 2026: these are the values of the earlier version of `b1_leakage_proxy.py`, which An's package ran; the corrected script gives 1.6%, 5.8%, 8.3% and ρ = 0.294, 0.333 (see `paper_revised/CHANGES_rev.md`, Corrections) |
| `10_h2_analysis.txt` | Median C1 = 0.8189, C2 = 0.8754; parse_pass 252 / 252 / 254 (Table 4) |

**Step 6. Send back to Hoàng.**
1. Compress the folder `ket_qua\<date_time>\` into a zip and send it to Hoàng.
2. Add a few lines of confirmation, for example: "I, Nguyễn Hiếu An, ran RUN_CHECKS.ps1 myself at … on my own computer, and read KET_QUA.json and the logs myself. Result: 15/15 tables match." If anything does not match or is not clear, write it down explicitly.

If you want to run it again, just run Step 3 again. Each run creates a new `ket_qua\<date_time>` folder and does not overwrite the previous run.

## Common errors

| Symptom | What to do |
|---|---|
| `py : The term 'py' is not recognized` | Python from python.org has not been installed, or it was installed without the "py launcher". Reinstall Python 3.13 and tick both options in the section "What you need" |
| `running scripts is disabled on this system` | Run exactly the command in Step 3, with `-ExecutionPolicy Bypass` |
| `Installing the libraries failed` or `No matching distribution found` | The Python in use is too old, or the network is down. Check `py -3 --version`. If you have installed a newer Python, delete the `.venv` folder and run again |
| `Manifest mismatch, stopping:` followed by a file name | A file has been edited or the extraction went wrong. Delete the folder and extract it again from the zip; do not open the CSV files in Excel and click Save |
| A step has `exit 1`, or `RESULT: NOT ALL MATCH` | Do not fix the script or the data yourself. Send Hoàng the whole `ket_qua\<date_time>\` folder, which contains the error logs and the details of where the results differ |
