#!/usr/bin/env python3
"""Fast consistency checks for the archived full-scan dataset."""
from __future__ import annotations

import csv
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
arr = np.load(DATA / "seed_depths_uint8.npz")
depths = arr["depths"]
assert int(arr["seed_min"]) == 2
assert int(arr["seed_max"]) == 10_000_000
assert len(depths) == 9_999_999
assert int((depths == 0).sum()) == 7_283_427
assert int(depths.max()) == 57
max_seeds = np.flatnonzero(depths == 57) + 2
assert max_seeds.tolist() == [4_415_366]
assert abs(float(depths.mean()) - 1.3401832340183235) < 1e-15
assert float(np.median(depths)) == 0.0

hist = {}
with (DATA / "seed_depth_counts.csv").open(encoding="utf-8") as f:
    for row in csv.DictReader(f):
        hist[int(row["depth"])] = int(row["count"])
unique, counts = np.unique(depths, return_counts=True)
assert hist == dict(zip(unique.tolist(), counts.tolist()))
print("archived full-scan dataset checks: OK")
