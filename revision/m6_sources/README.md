# Dataset sources (Action Tracker M6)

This folder documents where the 261 reference files of `data/full_ground_truth.csv`
come from, and how the stored reference text relates to the upstream files.

## Sources

| Project | Repository | Branch | Commit (clone of 19 July 2026) | Commit date | .feature files at commit | Selected | C0 analysed | H2 analysed |
|---|---|---|---|---|---:|---:|---:|---:|
| Sylius | https://github.com/Sylius/Sylius | 2.3 | `9ab28ca4b5ad5797216fe14e72e4d6cfe29c3fdb` | 2026-07-17 | 839 | 100 | 99 | 98 |
| Apache Fineract | https://github.com/apache/fineract | develop | `5a93304677061501f5d0c243b8dbf84752e08b0b` | 2026-07-17 | 147 | 100 | 99 | 98 |
| Diaspora | https://github.com/diaspora/diaspora | develop | `b7bf1dc33566c036a3d788dd8876e97c30905842` | 2026-07-17 | 71 | 61 | 60 | 59 |

C0 excludes the exemplars 2, 102 and 202. H2 (conditions C0, C1 and C2 on common
files) also excludes 86, 119 and 203. All columns, including the selected files per
folder, are in `results/source_table.csv`.

**Clone records.** The commits are the heads of the clones made by
`scripts/download_repos.py`. `clone_records/<project>/` holds the files `HEAD`,
`packed-refs`, `shallow` and `config`, and the reflog `logs_HEAD`, copied unchanged
from `tmp/repos/<project>/.git/` of that machine. The reflog dates the three clones
to 2026-07-18 17:27 UTC (2026-07-19 00:27 +07:00). The clones are shallow (depth 1).

**Extraction paths.**
- Sylius: `features/` (admin 59, shop 39, domain 1, hybrid 1).
- Fineract: `fineract-e2e-tests-runner/src/test/resources/features/` (98 of its 125
  files) and `fineract-provider/src/test/resources/features/` (2 of 20).
- Diaspora: `features/desktop/` (44 of 50) and `features/mobile/` (17 of 21).

The complete file lists at each commit are in `results/feature_inventory_*.txt`.

**Licenses** at the three commits: MIT (Sylius), Apache-2.0 (Fineract),
AGPL-3.0-or-later with the exceptions stated in its COPYRIGHT file (Diaspora). The
license texts in `licenses/` equal the upstream blobs at these commits.

## Two collection batches

| Batch | Files | Collected | Upstream version of the stored text |
|---|---|---|---|
| First (ids 1–34, 101–133, 201–233) | 100: Sylius 34, Fineract 33, Diaspora 33 | 28 June 2026 (`data/raw/README.md`); first committed in `22b348b`, 16 July 2026 | No clone of this download was kept. The Fineract files that match upstream exactly fix the version to the develop branch between `69ace799c7c6` (2026-06-23) and `963bdaf8069f` (2026-06-29) |
| Second (all other ids) | 161: Sylius 66, Fineract 67, Diaspora 28 | Clones of 19 July 2026; first committed in `2b09c3a`, 19 July 2026 | Equal to the clone commits above, except Fineract 187 |

The first batch was a random sample of 100 files over the three projects
(`data/raw/README.md`). The dataset was then enlarged to 100 files per project by
drawing the second batch at random from the clones; the random seed was not recorded. For
Diaspora, the 71 files at the clone commit have 58 distinct file names: ten names
exist in both `desktop/` and `mobile/`. The 61 selected files cover all 58 names.

## Stored reference text versus the upstream file

The metric scores against `gherkin_content` in `data/full_ground_truth.csv`, not
against `data/raw/`. Per file (`results/provenance_per_file.csv`):

| | Same as the file in `data/raw/` | Feature description removed | Cut at 30,038 CSV characters | Other difference |
|---|---:|---:|---:|---:|
| Sylius | 66 | 34 (first batch) | 0 | 0 |
| Apache Fineract | 73 | 0 | 23 (first batch) | 4 (first batch) |
| Diaspora | 42 | 19 (first batch) | 0 | 0 |

The 23 cut files are 104, 106–112, 116–122, 124–127, 129–131 and 133. File 124 is
also an older upstream version. Of the other four, 101, 114 and 128 are older upstream
versions (matching develop between June and early July 2026), and 103 lacks one empty line. "Feature description removed" means that the free-text
lines under `Feature:` (In order to / As a / I want) are missing.

**Effect** (`m6_full_reference_rescore.py`, `results/full_reference_rescore_report.txt`).
Rescoring every C0 output against the full file in `data/raw/` changes the skeleton
cosine of two files: 114 (0.822 to 0.805) and 133 (0.704 to 0.825). Both stay below
0.85. On the 258 non-exemplar files the median stays 0.8533, the count stays 136
above and 122 below, and the sign test stays at p = 0.209. The Wilcoxon p-value
changes from 0.474 to 0.452. Removing the Feature description cannot change the score,
because the skeleton keeps only keyword lines.

**Parsing.** Of the 14 references that fail to parse, 13 are cut files (104, 108,
109, 110, 112, 117, 120, 121, 122, 125, 130, 131, 133). Their full files parse. File
200 fails in both versions.

## Reproduce

From the repository root:

    git clone --bare --filter=blob:none --single-branch --branch 2.3 --shallow-since=2025-06-01 https://github.com/Sylius/Sylius.git <up>/sylius
    git clone --bare --filter=blob:none --single-branch --branch develop --shallow-since=2025-06-01 https://github.com/apache/fineract.git <up>/fineract
    git clone --bare --filter=blob:none --single-branch --branch develop --shallow-since=2025-06-01 https://github.com/diaspora/diaspora.git <up>/diaspora
    python revision/m6_sources/m6_provenance_check.py --upstream <up>
    python revision/m6_sources/m6_full_reference_rescore.py --onnx-dir <folder with model.onnx and tokenizer.json>

`m6_provenance_check.py` uses Python and git only and compares trees, so no file
contents are downloaded. `m6_full_reference_rescore.py` needs numpy, pandas, scipy,
tokenizers, onnxruntime and behave, the same as `revision/h2/`. Expected outputs are in
`results/`. The stored dataset was not changed.
