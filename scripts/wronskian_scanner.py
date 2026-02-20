#!/usr/bin/env python3
"""
wronskian_scanner.py
====================
Compute the Discrete Wronskian Compression ratio for maximal
prime-free subsequences in Legendre intervals I_n = [(n-1)^2, n^2].

For each target n, finds the longest run of consecutive composites
and computes:
    q_W = log(prod C_i) / log(rad(prod C_i))

Usage:
    python wronskian_scanner.py [--targets N1 N2 ...] [--csv OUTPUT]

Author: Ruqing Chen, GUT Geoservice Inc.
Titan Project — Paper IX, February 2026
"""

import argparse
import csv
import math
import sys
import time

try:
    import sympy
except ImportError:
    print("Error: sympy is required. Install with: pip install sympy")
    sys.exit(1)


def find_max_composite_gap(n):
    """
    Find the longest run of consecutive composites in [(n-1)^2, n^2].
    Returns the list of composites in the longest gap.
    """
    start = (n - 1) ** 2
    end = n ** 2

    max_gap = []
    current_gap = []

    for x in range(start, end + 1):
        if not sympy.isprime(x):
            current_gap.append(x)
        else:
            if len(current_gap) > len(max_gap):
                max_gap = current_gap
            current_gap = []

    if len(current_gap) > len(max_gap):
        max_gap = current_gap

    return max_gap


def compute_wronskian(composites):
    """
    Compute the Wronskian compression ratio q_W for a sequence
    of composites.

    q_W = log(prod C_i) / log(rad(prod C_i))

    Uses log-space arithmetic to avoid overflow.
    """
    if not composites:
        return None, None, None

    log_volume = sum(math.log(c) for c in composites)

    # Collect all distinct prime factors
    all_primes = set()
    for c in composites:
        factors = sympy.factorint(c)
        all_primes.update(factors.keys())

    log_radical = sum(math.log(p) for p in all_primes)

    q_w = log_volume / log_radical if log_radical > 0 else float('inf')

    return log_volume, log_radical, q_w


def main():
    parser = argparse.ArgumentParser(
        description="Discrete Wronskian compression scanner."
    )
    parser.add_argument(
        "--targets", type=int, nargs="+",
        default=[100, 500, 1000, 5000, 10000, 50000, 100000, 200000],
        help="Target n values (default: 100 500 ... 200000)"
    )
    parser.add_argument(
        "--csv", type=str, default=None,
        help="Output CSV file path"
    )
    args = parser.parse_args()

    print("Discrete Wronskian Volume — ABC Compression Scanner")
    print("=" * 70)
    print(f"{'n':>10} | {'Gap':>6} | {'log(Volume)':>14} | "
          f"{'log(Radical)':>14} | {'q_W':>8}")
    print("-" * 70)

    results = []
    for n in args.targets:
        t0 = time.time()
        gap = find_max_composite_gap(n)
        log_vol, log_rad, q_w = compute_wronskian(gap)
        elapsed = time.time() - t0

        row = {
            "n": n,
            "gap_length": len(gap),
            "gap_start": gap[0] if gap else None,
            "gap_end": gap[-1] if gap else None,
            "log_volume": round(log_vol, 2) if log_vol else None,
            "log_radical": round(log_rad, 2) if log_rad else None,
            "q_W": round(q_w, 4) if q_w else None,
            "time_sec": round(elapsed, 2),
        }
        results.append(row)

        print(f"{n:>10} | {len(gap):>6} | {log_vol:>14.2f} | "
              f"{log_rad:>14.2f} | {q_w:>8.4f}  ({elapsed:.1f}s)")

    print("=" * 70)

    if args.csv:
        fieldnames = list(results[0].keys())
        with open(args.csv, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(results)
        print(f"Data written to {args.csv}")


if __name__ == "__main__":
    main()
