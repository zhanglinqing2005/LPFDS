#!/usr/bin/env python3
"""Regenerate the fixed independent-verification sample from archived depths."""
from __future__ import annotations

import csv
import random
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
DATA = np.load(DATA_DIR / "seed_depths_uint8.npz")
depths = DATA["depths"]

random.seed(20260812)
seeds = {2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 4_415_366, 10_000_000}
while len(seeds) < 2014:
    seeds.add(random.randint(2, 10_000_000))

with (DATA_DIR / "verification_sample.csv").open(
    "w", newline="", encoding="utf-8"
) as f:
    w = csv.writer(f)
    w.writerow(["seed", "expected_depth"])
    for m in sorted(seeds):
        w.writerow([m, int(depths[m - 2])])

print("sample_size", len(seeds))
