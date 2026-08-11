# Reproducibility guide

This repository contains the exact computational material used in the content-freeze manuscript.

## Fast verification

From the repository root:

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python src/check_repository_results.py
python src/verify_independent.py
python src/standard_orbit_reproduce.py
```

`check_repository_results.py` validates the compact histogram and frozen summary stored in GitHub. The full per-seed depth array is retained in the frozen reproducibility archive for Zenodo deposition. `verify_independent.py` recomputes the fixed GitHub smoke sample using trial division rather than the sieve implementation; when the full 2,014-seed archive sample is present, the same script automatically uses it instead. `standard_orbit_reproduce.py` regenerates the exact standard-orbit appearance-index data and the historical OLS summary.

## Full exhaustive scan

To rerun the complete scan over all seeds `2 <= m <= 10,000,000`:

```bash
python src/seed_scan_archive.py
```

This overwrites `data/seed_depths_uint8.npz`, `data/seed_depth_counts.csv`, and `data/seed_scan_summary.txt` with newly generated results. The script uses a largest-prime-factor sieve through 10,500,000, which is above the largest state encountered before certification in the archived run.

## Integrity

The separately frozen reproducibility ZIP distributed with the manuscript has SHA-256

`dbb008412ce2e1f55636ae6a35e933e9827ed4e7b63b76dddbc83c4e70532131`.

The Zenodo DOI is intentionally omitted until the English/LaTeX manuscript and release metadata are frozen.
