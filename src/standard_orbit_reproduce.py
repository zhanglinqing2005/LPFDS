#!/usr/bin/env python3
"""Reproduce standard-orbit datasets and the historical OLS summary.

Outputs are written into the repository's data/ directory, regardless of the
current working directory. The formulas used here are exact consequences of
the prime-block structure described in the manuscript.
"""
from __future__ import annotations

import csv
import math
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
DATA_DIR.mkdir(exist_ok=True)
LIMIT = 1_000_003


def sieve(n: int) -> np.ndarray:
    a = np.ones(n + 1, dtype=bool)
    a[:2] = False
    for p in range(2, int(math.isqrt(n)) + 1):
        if a[p]:
            a[p * p : n + 1 : p] = False
    return np.flatnonzero(a)


P = sieve(LIMIT).astype(np.int64)
I = np.empty_like(P)
I[0] = 1
I[1:] = P[:-1] + P[1:] - 2

with (DATA_DIR / "appearance_indices_up_to_1000003.csv").open(
    "w", newline="", encoding="utf-8"
) as f:
    w = csv.writer(f)
    w.writerow(["prime", "appearance_index"])
    w.writerows(zip(P.tolist(), I.tolist()))

x = P.astype(float)
y = I.astype(float)
slope, intercept = np.polyfit(x, y, 1)
yhat = slope * x + intercept
r = float(np.corrcoef(x, y)[0, 1])
rmse = float(np.sqrt(np.mean((y - yhat) ** 2)))

b: list[int] = []
for n in range(1, 81):
    if n < 3:
        q = 2
    else:
        q = 2
        for k in range(1, len(P) - 1):
            if P[k - 1] + P[k] - 2 <= n < P[k] + P[k + 1] - 2:
                q = int(P[k])
                break
    b.append(q)

with (DATA_DIR / "prime_plateaus_first80.csv").open(
    "w", newline="", encoding="utf-8"
) as f:
    w = csv.writer(f)
    w.writerow(["n", "largest_prime_factor"])
    w.writerows((i + 1, v) for i, v in enumerate(b))

with (DATA_DIR / "standard_orbit_summary.txt").open("w", encoding="utf-8") as f:
    f.write(f"prime_samples={len(P)}\n")
    f.write(f"last_prime={P[-1]}\n")
    f.write(f"last_appearance_index={I[-1]}\n")
    f.write(f"ols_slope={slope:.12f}\n")
    f.write(f"ols_intercept={intercept:.12f}\n")
    f.write(f"pearson_r={r:.12f}\n")
    f.write(f"rmse={rmse:.12f}\n")

print("prime_samples", len(P), "last_prime", P[-1], "last_I", I[-1])
print(
    "slope", f"{slope:.12f}",
    "intercept", f"{intercept:.12f}",
    "r", f"{r:.12f}",
    "rmse", f"{rmse:.12f}",
)
