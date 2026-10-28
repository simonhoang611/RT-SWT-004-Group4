"""
m6_provenance_check.py  (revision, Action Tracker M6)

Documents where the 261 reference files come from. Read-only; no API calls;
Python standard library and git only.

Inputs
  * the group repository (this checkout): data/full_ground_truth.csv as first
    committed with 261 rows (commit 2b09c3a, 19 July 2026), the 100-row version
    of commit 22b348b (16 July 2026, the first collection batch), and the files
    committed in data/raw/;
  * clone_records/<project>/: HEAD, packed-refs, shallow, config and the reflog
    (logs_HEAD) of the three clones made on 19 July 2026 with
    scripts/download_repos.py, copied unchanged from tmp/repos/<project>/.git/;
  * --upstream: one blob-less clone per project with the history of the branch
    named in the CSV URLs, for example
        git clone --bare --filter=blob:none --single-branch --branch 2.3 \
            --shallow-since=2025-06-01 https://github.com/Sylius/Sylius.git sylius
        (fineract: https://github.com/apache/fineract.git, branch develop;
         diaspora: https://github.com/diaspora/diaspora.git, branch develop)
    Only trees are compared, so no file contents are downloaded.

For every reference file it records the batch, how the scored CSV text relates
to the file in data/raw/ (same, narrative_removed, truncated_prefix, other),
whether each of them equals the upstream file at the clone commit, and the first
and last first-parent commit (up to 20 July 2026) at which the upstream file
equals the CSV text. It also counts the .feature files at each clone commit.

Outputs (default folder revision/m6_sources/results/):
  provenance_per_file.csv, source_table.csv,
  feature_inventory_<project>_<commit>.txt, provenance_report.txt

Usage (from the repository root):
  python revision/m6_sources/m6_provenance_check.py --upstream <folder with sylius/ fineract/ diaspora/>
"""
import argparse
import collections
import csv
import datetime
import hashlib
import io
import os
import re
import subprocess

csv.field_size_limit(2**31 - 1)
HERE = os.path.dirname(os.path.abspath(__file__))
FIRST_BATCH, FULL_DATASET = "22b348b", "2b09c3a"
UNTIL = "2026-07-20"
NARRATIVE = re.compile(r"^\s*(In order to|In order|As an?|I want|So that|I need)\b", re.IGNORECASE)
PROJECTS = [  # project_name in the CSV, upstream folder, data/raw folder, repository URL
    ("Sylius", "sylius", "Sylius_Ecommerce", "https://github.com/Sylius/Sylius"),
    ("Apache Fineract", "fineract", "Apache_Fineract_Finance", "https://github.com/apache/fineract"),
    ("Diaspora", "diaspora", "Diaspora_Social_Network", "https://github.com/diaspora/diaspora"),
]
C0_EXEMPLARS = {2, 102, 202}
H2_EXEMPLARS = {2, 102, 202, 86, 119, 203}


def git(cwd, *args):
    return subprocess.run(["git", *args], cwd=cwd, capture_output=True, text=True, encoding="utf-8",
                          check=True).stdout


def blob_id(data):
    return hashlib.sha1(b"blob %d\0" % len(data) + data).hexdigest()


def text_blob_ids(text):
    # The CSV does not keep the final newline of a file, so both endings are accepted.
    t = text.replace("\r\n", "\n")
    return {blob_id(s.encode("utf-8")) for s in {t, t.rstrip("\n") + "\n", t.rstrip("\n")}}


def tree(up, commit, paths):
    out = {}
    for line in git(up, "ls-tree", "-r", commit, "--", *paths).splitlines():
        meta, path = line.split("\t")
        out[path] = meta.split()[2]
    return out


def clone_record(name):
    d = os.path.join(HERE, "clone_records", name)
    head = open(os.path.join(d, "shallow"), encoding="utf-8").read().split()[0]
    log = open(os.path.join(d, "logs_HEAD"), encoding="utf-8").read().split("\n")[0]
    old, new = log.split()[:2]
    stamp, tz = re.search(r"> (\d+) ([+-]\d{4})\t", log).groups()
    assert old == "0" * 40 and new == head and "clone: from" in log, name
    return head, int(stamp), tz


def relation(raw, stored):
    stripped = "\n".join(l for l in raw.split("\n") if not NARRATIVE.match(l))
    if raw.rstrip() == stored.rstrip():
        return "same"
    if stripped.rstrip() == stored.rstrip():
        return "narrative_removed"
    if raw.startswith(stored[:-200]):
        return "truncated_prefix"
    return "other"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--upstream", required=True)
    ap.add_argument("--outdir", default=os.path.join("revision", "m6_sources", "results"))
    a = ap.parse_args()
    os.makedirs(a.outdir, exist_ok=True)

    first = {r["github_file_url"] for r in csv.DictReader(io.StringIO(
        git(".", "show", f"{FIRST_BATCH}:data/full_ground_truth.csv").lstrip("﻿")))}
    rows = list(csv.DictReader(io.StringIO(git(".", "show", f"{FULL_DATASET}:data/full_ground_truth.csv").lstrip("﻿"))))
    raw_blob = {}
    for line in git(".", "ls-tree", "-r", FULL_DATASET, "data/raw").splitlines():
        meta, path = line.split("\t")
        raw_blob[path] = meta.split()[2]

    per_file, table, report = [], [], []
    for project, name, rawdir, url in PROJECTS:
        up = os.path.join(a.upstream, name)
        head, stamp, tz = clone_record(name)
        commits = [c.split() for c in git(up, "log", "--first-parent", "--format=%H %cI", "HEAD",
                                          f"--until={UNTIL}").splitlines()][::-1]
        assert head in {h for h, _ in commits}, (project, "clone commit not on the branch")
        head_date = dict(commits)[head]
        fs = [r for r in rows if r["project_name"] == project]
        used = set()
        for r in fs:
            p = f"data/raw/{rawdir}/{r['expert_filename']}"
            if p in used or p not in raw_blob:  # extract_features.py renames duplicates to <name>_<id>
                p = f"data/raw/{rawdir}/{r['expert_filename'][:-len('.feature')]}_{r['id']}.feature"
            used.add(p)
            r["raw_path"], r["hits"] = p, []
            r["path"] = r["github_file_url"].split("/blob/")[1].split("/", 1)[1]
            r["stored"] = r["gherkin_content"].replace("\\n", "\n").replace("\r\n", "\n")
            r["ids"] = text_blob_ids(r["stored"])
        paths = sorted({r["path"] for r in fs})
        for h, t in commits:
            tr = tree(up, h, paths)
            for r in fs:
                if tr.get(r["path"]) in r["ids"]:
                    r["hits"].append((h, t))
        at_head = tree(up, head, paths)
        for r in fs:
            raw = git(".", "show", f"{FULL_DATASET}:{r['raw_path']}").replace("\r\n", "\n")
            hits = r["hits"]
            per_file.append({
                "id": int(r["id"]), "project": project,
                "batch": "first (28 Jun 2026)" if r["github_file_url"] in first else "second (19 Jul 2026)",
                "path": r["path"], "raw_path": r["raw_path"], "csv_field_chars": len(r["gherkin_content"]), "stored_chars": len(r["stored"]), "raw_chars": len(raw),
                "stored_vs_raw": relation(raw, r["stored"]),
                "raw_equals_clone_commit": at_head.get(r["path"]) == raw_blob[r["raw_path"]],
                "stored_equals_clone_commit": at_head.get(r["path"]) in r["ids"],
                "stored_first_commit": hits[0][0][:12] if hits else "", "stored_first_date": hits[0][1][:10] if hits else "",
                "stored_last_commit": hits[-1][0][:12] if hits else "", "stored_last_date": hits[-1][1][:10] if hits else ""})

        inv = sorted(p for p in git(up, "ls-tree", "-r", "--name-only", head).splitlines() if p.endswith(".feature"))
        with open(os.path.join(a.outdir, f"feature_inventory_{name}_{head[:12]}.txt"), "w", encoding="utf-8", newline="\n") as f:
            f.write("\n".join(inv) + "\n")
        mine = [x for x in per_file if x["project"] == project]
        folders = collections.Counter(os.path.dirname(x["path"]) for x in mine)
        top = lambda p: "/".join(p.split("/")[:2]) if p.startswith("features/") else "/".join(p.split("/")[:5])
        names = collections.Counter(os.path.basename(p) for p in inv)
        rel = collections.Counter(x["stored_vs_raw"] for x in mine)
        b1 = [x for x in mine if x["batch"].startswith("first")]
        exact_b1 = [r for r in fs if r["github_file_url"] in first and r["hits"]]
        window = set.intersection(*[{h for h, _ in r["hits"]} for r in exact_b1]) if exact_b1 else set()
        win = [(h, t) for h, t in commits if h in window]
        ids = {x["id"] for x in mine}
        table.append({
            "project": project, "repository": url, "branch": rows[[r["project_name"] for r in rows].index(project)]["github_file_url"].split("/blob/")[1].split("/")[0],
            "clone_commit": head, "clone_commit_date": head_date,
            "clone_time_utc": datetime.datetime.fromtimestamp(stamp, datetime.timezone.utc).isoformat(),
            "feature_files_at_clone_commit": len(inv), "distinct_feature_file_names": len(names),
            "feature_folders_at_clone_commit": "; ".join(f"{k} {v}" for k, v in sorted(collections.Counter(top(p) for p in inv).items())),
            "selected": len(mine), "selected_by_folder": "; ".join(f"{k} {v}" for k, v in sorted(collections.Counter(top(x['path']) for x in mine).items())),
            "first_batch": len(b1), "second_batch": len(mine) - len(b1),
            "C0_exemplars_excluded": len(ids & C0_EXEMPLARS), "C0_analysed": len(ids - C0_EXEMPLARS),
            "H2_exemplars_excluded": len(ids & H2_EXEMPLARS), "H2_analysed": len(ids - H2_EXEMPLARS),
            "raw_equals_clone_commit": sum(x["raw_equals_clone_commit"] for x in mine),
            "stored_equals_clone_commit": sum(x["stored_equals_clone_commit"] for x in mine),
            "stored_same_as_raw": rel["same"], "stored_narrative_removed": rel["narrative_removed"],
            "stored_truncated": rel["truncated_prefix"], "stored_other": rel["other"],
            "first_batch_window_first": f"{win[0][0][:12]} {win[0][1][:10]}" if win else "",
            "first_batch_window_last": f"{win[-1][0][:12]} {win[-1][1][:10]}" if win else "",
            "first_batch_files_defining_window": len(exact_b1)})
        report.append(f"{project}: clone {head[:12]} ({head_date}), {len(inv)} .feature files "
                      f"({len(names)} distinct names), {len(mine)} selected")

    per_file.sort(key=lambda x: x["id"])
    for name, data in (("provenance_per_file.csv", per_file), ("source_table.csv", table)):
        with open(os.path.join(a.outdir, name), "w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=list(data[0]), lineterminator="\n")
            w.writeheader()
            w.writerows(data)
    trunc = [x["id"] for x in per_file if x["stored_vs_raw"] == "truncated_prefix"]
    report += ["", "stored text vs data/raw: " + str(dict(collections.Counter((x["project"], x["stored_vs_raw"]) for x in per_file))),
               f"truncated references ({len(trunc)}): {trunc}",
               "CSV field length of truncated references: " + str(sorted({x["csv_field_chars"] for x in per_file if x["id"] in trunc})),
               "references whose CSV field is exactly 30,038 characters: " + str([x["id"] for x in per_file if x["csv_field_chars"] == 30038])]
    for t in table:
        report.append(f"{t['project']}: first-batch window {t['first_batch_window_first']} .. {t['first_batch_window_last']} "
                      f"({t['first_batch_files_defining_window']} files)")
    open(os.path.join(a.outdir, "provenance_report.txt"), "w", encoding="utf-8", newline="\n").write("\n".join(report) + "\n")
    print("\n".join(report))


if __name__ == "__main__":
    main()
