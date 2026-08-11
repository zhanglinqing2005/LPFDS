#!/usr/bin/env python3
"""Exhaustive general-seed scan for x_{t+1}=x_t+P^+(x_t).

Scans every seed 2 <= m <= 10,000,000. Outputs are written to data/.
The certification condition is r=x/P^+(x) < nextprime(P^+(x)); by the
attraction theorem in the manuscript, this certifies eventual coalescence
with the standard seed-2 orbit.
"""
from __future__ import annotations

import bisect
import csv
from collections import Counter
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data"
OUT.mkdir(exist_ok=True)
N = 10_000_000
MAX_STATE = 10_500_000

lpf = np.zeros(MAX_STATE + 1, dtype=np.int32)
primes: list[int] = []
for p in range(2, MAX_STATE + 1):
    if lpf[p] == 0:
        primes.append(p)
        lpf[p::p] = p


def next_prime(q: int) -> int:
    return primes[bisect.bisect_right(primes, q)]


def certification_depth(m: int, limit: int = 255):
    x = m
    for t in range(limit + 1):
        q = int(lpf[x])
        r = x // q
        if r < next_prime(q):
            return t, x, q, r
        x += q
        if x > MAX_STATE:
            raise RuntimeError(f"working bound too small: x={x}, seed={m}")
    raise RuntimeError(f"depth exceeded {limit}: seed={m}")


depths = np.empty(N - 1, dtype=np.uint8)
counts: Counter[int] = Counter()
max_depth = -1
max_seeds: list[int] = []
max_depth_state = None
max_visited = 0
sum_depth = 0

for m in range(2, N + 1):
    t, x, q, r = certification_depth(m)
    depths[m - 2] = t
    counts[t] += 1
    sum_depth += t
    max_visited = max(max_visited, x)
    if t > max_depth:
        max_depth = t
        max_seeds = [m]
        max_depth_state = (x, q, r)
    elif t == max_depth:
        max_seeds.append(m)

np.savez_compressed(
    OUT / "seed_depths_uint8.npz",
    depths=depths,
    seed_min=np.int64(2),
    seed_max=np.int64(N),
)

with (OUT / "seed_depth_counts.csv").open("w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["depth", "count"])
    for d in sorted(counts):
        w.writerow([d, counts[d]])

cum = 0
median = None
total = N - 1
for d in sorted(counts):
    cum += counts[d]
    if cum >= (total + 1) // 2:
        median = d
        break

summary = {
    "seed_min": 2,
    "seed_max": N,
    "seed_count": total,
    "depth_zero_count": counts[0],
    "depth_zero_fraction": counts[0] / total,
    "mean_depth": sum_depth / total,
    "median_depth": median,
    "max_depth": max_depth,
    "max_depth_seeds": max_seeds,
    "max_depth_state": max_depth_state,
    "max_state_visited_before_certificate": max_visited,
}
with (OUT / "seed_scan_summary.txt").open("w", encoding="utf-8") as f:
    for k, v in summary.items():
        f.write(f"{k}={v}\n")
print(summary)
