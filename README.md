# LPFDS — Largest-prime-factor recurrence

This repository accompanies the manuscript:

**Exact Structure, Prime-Gap Representations, and General-Seed Dynamics in a Largest-Prime-Factor Recurrence**  
Chinese content-freeze title: **《最大质因子递推的精确结构、素数间隔表示与一般初值动力学》**

Author: Zhang Linqing (张琳清), Henan University of Economics and Law.

## Mathematical status

We study

\[
x_{t+1}=x_t+P^+(x_t),
\]

where \(P^+(n)\) denotes the largest prime factor of \(n\).

The standard seed \(x_1=2\) is **not a newly discovered sequence**. It is OEIS A036441 and is equivalent, up to indexing, to A076271. Its induced largest-prime-factor plateaus and several directly related index sequences are also already represented by OEIS A076272, A076273, A075527, and A076274.

The current manuscript therefore does **not** present the standard-orbit monotonicity / non-skipping / coverage properties as computational conjectures. Those properties follow from the exact prime-block structure.

The current experimental focus is the **general-seed problem**: for arbitrary integer seed \(m\ge 2\), does the orbit eventually coalesce with the standard seed-2 orbit? The manuscript proves a sufficient attraction criterion and reports an exhaustive deterministic scan of every seed

\[
2\le m\le 10{,}000{,}000.
\]

All 9,999,999 tested seeds entered the proven attraction region; the maximum observed certification depth was 57, uniquely attained by seed 4,415,366. This finite computation supports an open conjecture and is **not** claimed as a proof for all integers.

## Repository layout

- `src/seed_scan_archive.py` — exhaustive general-seed scan using a largest-prime-factor sieve.
- `src/verify_independent.py` — independent trial-division verification on a fixed sample.
- `src/check_archived_results.py` — fast integrity checks for the archived full-scan dataset.
- `src/standard_orbit_reproduce.py` — exact standard-orbit appearance-index reproduction and historical OLS summary.
- `src/make_verification_sample.py` — creates the fixed verification sample.
- `data/seed_depths_uint8.npz` — compressed certification depth for every seed 2..10,000,000.
- `data/seed_depth_counts.csv` — depth histogram.
- `data/appearance_indices_up_to_1000003.csv` — exact appearance indices for 78,499 primes through 1,000,003.
- `data/verification_sample.csv` — fixed independent verification sample.
- `data/prime_plateaus_first80.csv` — data for the first plateau figure.
- `figures/` — publication figures corresponding to the final content-freeze manuscript.
- `docs/prior_art_audit_2026-08-12.md` — scope and conclusions of the final prior-art audit.
- `docs/reproducibility.md` — exact fast-check and full-rerun instructions.
- `environment.txt` — environment used for the archived final run.
- `CITATION.cff` — citation metadata for software/reproducibility archiving.

## Reproduce the computational results

Recommended environment:

```bash
python -m venv .venv
# Linux/macOS
source .venv/bin/activate
# Windows PowerShell
# .\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

For a fast verification of the archived results, run:

```bash
python src/check_archived_results.py
python src/verify_independent.py
python src/standard_orbit_reproduce.py
```

To rerun the complete 9,999,999-seed exhaustive scan (substantially more expensive), run:

```bash
python src/seed_scan_archive.py
```

Expected key general-seed results:

- tested seeds: 9,999,999
- depth-0 seeds: 7,283,427
- mean certification depth: 1.3401832340183235
- median depth: 0
- maximum depth: 57
- unique maximum-depth seed: 4,415,366
- certificate state at depth 57: `x=4,495,501`, `P^+(x)=2,999`, cofactor `1,499`, next prime `3,001`
- maximum state seen before certification: 10,058,651

## Relationship to the historical repository state

Earlier versions of this repository described three properties of the standard seed-2 orbit as conjectures and contained SPSS/PDF regression outputs. The current manuscript proves the standard block structure exactly, so those historical files should be retained only as exploratory history, not as the current evidence base.

Recommended treatment:

- move the old `LPFDS.py` to `legacy/LPFDS_v1_exploratory.py`;
- move the old SPSS/PDF regression outputs to `legacy/statistics_v1/`;
- use the scripts under `src/` and datasets under `data/` as the current reproducibility source.

## Release status

This branch/repository state is the manuscript content-freeze reproducibility candidate (`0.9.0`). The immutable `v1.0.0` GitHub/Zenodo release will be created only after the final English LaTeX manuscript, author metadata, and DOI cross-links are frozen.

## Zenodo archival workflow

The repository can be connected to Zenodo and archived by creating a GitHub release. `CITATION.cff` is included so Zenodo can ingest citation metadata. A paper/preprint DOI and a software/reproducibility DOI can be kept as separate, cross-linked research outputs.

For the journal manuscript, cite the final Zenodo preprint DOI if a preprint has been posted, and cite the archived code/software DOI in the Data and Code Availability section once it exists.

## License

Keep the repository's existing MIT license for code unless the author intentionally changes it. Licensing of the manuscript/preprint and data record should be selected explicitly when the Zenodo records are created.
