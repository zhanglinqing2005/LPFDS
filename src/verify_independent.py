#!/usr/bin/env python3
"""Independent trial-division verification of the archived seed sample."""
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FULL_SAMPLE = ROOT / "data" / "verification_sample.csv"
SMOKE_SAMPLE = ROOT / "data" / "verification_smoke_sample.csv"
SAMPLE = FULL_SAMPLE if FULL_SAMPLE.exists() else SMOKE_SAMPLE


def largest_prime_factor(n: int) -> int:
    x = n
    last = 1
    while x % 2 == 0:
        last = 2
        x //= 2
    p = 3
    while p * p <= x:
        while x % p == 0:
            last = p
            x //= p
        p += 2
    if x > 1:
        last = x
    return last


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    p = 3
    while p * p <= n:
        if n % p == 0:
            return False
        p += 2
    return True


def next_prime(q: int) -> int:
    x = q + 1
    if x <= 2:
        return 2
    if x % 2 == 0:
        x += 1
    while not is_prime(x):
        x += 2
    return x


def certification_depth(m: int, limit: int = 255):
    x = m
    for t in range(limit + 1):
        q = largest_prime_factor(x)
        r = x // q
        if r < next_prime(q):
            return t, x, q, r
        x += q
    raise RuntimeError((m, x))


bad = []
checked = 0
with SAMPLE.open(encoding="utf-8") as f:
    for row in csv.DictReader(f):
        m = int(row["seed"])
        expected = int(row["expected_depth"])
        got, *state = certification_depth(m)
        checked += 1
        if got != expected:
            bad.append((m, expected, got, state))

print(f"checked={checked}")
print(f"mismatches={len(bad)}")
if bad:
    print(bad[:20])
    raise SystemExit(1)

t, x, q, r = certification_depth(4_415_366)
print(
    "max_case=seed=4415366",
    f"depth={t}", f"state={x}", f"q={q}", f"r={r}",
    f"next_prime={next_prime(q)}",
)
