#!/usr/bin/env python3
"""Fast checks for compact results stored directly in the GitHub repository.

The full per-seed depth array is kept in the frozen reproducibility archive
(and will be deposited on Zenodo); GitHub stores the histogram, summary, and
fixed independent verification sample.
"""
from __future__ import annotations

import ast
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"

hist: dict[int, int] = {}
with (DATA / "seed_depth_counts.csv").open(encoding="utf-8") as f:
    for row in csv.DictReader(f):
        hist[int(row["depth"])] = int(row["count"])
assert sum(hist.values()) == 9_999_999
assert hist[0] == 7_283_427
assert max(hist) == 57

summary: dict[str, str] = {}
with (DATA / "seed_scan_summary.txt").open(encoding="utf-8") as f:
    for line in f:
        k, v = line.rstrip("\n").split("=", 1)
        summary[k] = v
assert int(summary["seed_min"]) == 2
assert int(summary["seed_max"]) == 10_000_000
assert int(summary["seed_count"]) == 9_999_999
assert int(summary["depth_zero_count"]) == 7_283_427
assert abs(float(summary["mean_depth"]) - 1.3401832340183235) < 1e-15
assert int(summary["median_depth"]) == 0
assert int(summary["max_depth"]) == 57
assert ast.literal_eval(summary["max_depth_seeds"]) == [4_415_366]
assert ast.literal_eval(summary["max_depth_state"]) == (4_495_501, 2_999, 1_499)
assert int(summary["max_state_visited_before_certificate"]) == 10_058_651
print("compact repository result checks: OK")
