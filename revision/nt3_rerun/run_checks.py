"""Offline rerun of the revision analyses for NT3 (An runs it personally).

Copies original/ into a fresh folder under ket_qua/, runs the 10 revision scripts there,
and compares the 15 output tables with the originals in original/. Nothing in original/
or audit_inputs/ is changed, no API is called and no embeddings are recomputed.
Run from this folder:  python run_checks.py --executed-by "Nguyen Hieu An"
"""
from pathlib import Path
import argparse, datetime, hashlib, importlib.metadata as md, json, platform, shutil, subprocess, sys

import pandas as pd

COMPARED = [
    'revision/results/descriptives_skeleton_cosine.csv', 'revision/results/exemplar_scores.csv',
    'revision/results/b3_threshold_sweep.csv', 'revision/results/b3_mutation_by_threshold.csv',
    'revision/results/h1_domain_table.csv', 'revision/results/h1_pairwise.csv',
    'revision/results/b1_overlap_per_file.csv', 'revision/results/b1_spearman.csv',
    'revision/results/syntax_parse_n261.csv', 'revision/h2/h2_syntax_C0.csv',
    'revision/h2/h2_syntax_C1.csv', 'revision/h2/h2_syntax_C2.csv',
    'revision/h2/h2_results_table.csv', 'revision/h2/h2_results_by_project.csv',
    'revision/h2/h2_results_pairwise.csv']


def sha256(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--executed-by', required=True)
    a = ap.parse_args()
    root = Path(__file__).resolve().parent
    source, inputs = root / 'original', root / 'audit_inputs'

    # 1. Inputs must match the manifest before anything runs.
    bad = []
    for line in (root / 'MANIFEST_SHA256.txt').read_text(encoding='utf-8').splitlines():
        digest, rel = line.split('  ', 1)
        if not (root / rel).is_file() or sha256(root / rel) != digest:
            bad.append(rel)
    if bad:
        print('Manifest mismatch, stopping:', *bad, sep='\n  ')
        return 1
    print('Manifest: all files match.')

    # 2. Run the 10 scripts in a fresh copy.
    run = root / 'ket_qua' / datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    for folder in ['revision', 'data', 'results']:
        shutil.copytree(source / folder, run / folder)
    logdir = run / 'execution_logs'
    logdir.mkdir()
    jobs = [['revision/check_syntax.py', '--input', 'results/full_gpt54mini_output.csv',
             '--out', 'revision/results/syntax_parse_n261.csv'],
            ['revision/e1_old_check_demo.py'],
            ['revision/recompute_descriptives.py'],
            ['revision/b3_threshold_sensitivity.py', '--audit', str(inputs / 'b2_annotation_An_CONFIRMED.csv'),
             '--mutation', str(inputs / 'mutation_results.csv')],
            ['revision/h1_domain_analysis.py'],
            ['revision/b1_leakage_proxy.py']]
    for c in ['C0', 'C1', 'C2']:
        src = 'results/full_gpt54mini_output.csv' if c == 'C0' else f'revision/h2/h2_{c}_output.csv'
        jobs.append(['revision/check_syntax.py', '--input', src, '--out', f'revision/h2/h2_syntax_{c}.csv'])
    jobs.append(['revision/h2/h2_analysis.py'])
    records = []
    for n, args in enumerate(jobs, 1):
        r = subprocess.run([sys.executable, '-X', 'utf8', *args], cwd=run, capture_output=True,
                           text=True, encoding='utf8')
        (logdir / f'{n:02d}_{Path(args[0]).stem}.txt').write_text(r.stdout + '\nSTDERR:\n' + r.stderr,
                                                                   encoding='utf8')
        records.append({'step': n, 'command': args, 'exit_code': r.returncode})
        print(f'Step {n:2d}/10  {args[0]:42s} exit {r.returncode}', flush=True)
        if r.returncode:
            break

    # 3. Compare the 15 output tables with the originals.
    comparisons = []
    if len(records) == 10 and all(x['exit_code'] == 0 for x in records):
        for rel in COMPARED:
            try:
                pd.testing.assert_frame_equal(pd.read_csv(source / rel), pd.read_csv(run / rel),
                                              check_dtype=False, rtol=1e-10, atol=1e-12)
                comparisons.append({'file': rel, 'match': True})
            except AssertionError as exc:
                comparisons.append({'file': rel, 'match': False, 'detail': str(exc)[:3000]})
    ok = len(comparisons) == 15 and all(x['match'] for x in comparisons)

    report = {'executed_by': a.executed_by,
              'recorded_at_local': datetime.datetime.now().astimezone().isoformat(),
              'machine': platform.platform(), 'python': platform.python_version(),
              'versions': {m: md.version(m) for m in ['pandas', 'numpy', 'scipy', 'behave']},
              'steps': records, 'comparisons': comparisons, 'all_15_tables_match': ok,
              'note': 'Written by run_checks.py. The person named above ran it; reading the logs '
                      'and the result is their own step.'}
    (run / 'KET_QUA.json').write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf8')
    print(f'\nTables matching the originals: {sum(x["match"] for x in comparisons)}/15')
    print('RESULT:', 'ALL MATCH' if ok else 'NOT ALL MATCH, see KET_QUA.json and execution_logs')
    print('Saved in:', run)
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
