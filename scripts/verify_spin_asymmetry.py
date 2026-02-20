#!/usr/bin/env python3
"""
verify_spin_asymmetry.py
========================
Computational verification of the Spin Asymmetry Theorem
(Theorem 2.3 of the paper).

For each n >= 2 with p = 2n-1 prime, verifies that the interior
of the Legendre interval I_n = [(n-1)^2, n^2] satisfies:
  N^+ = (p-3)/2,  N^- = (p-1)/2,  N^0 = 1,  N^- - N^+ = 1.

Usage:
    python verify_spin_asymmetry.py [--limit N] [--csv OUTPUT]

Author: Ruqing Chen, GUT Geoservice Inc.
Titan Project — Paper IX, February 2026
"""

import argparse
import csv
import sys
import time

try:
    import sympy
except ImportError:
    print("Error: sympy is required. Install with: pip install sympy")
    sys.exit(1)


def verify_interval(n):
    """
    Verify the Spin Asymmetry Theorem for a single n.

    Returns a dict with verification data, or None if 2n-1 is not prime.
    """
    p = 2 * n - 1
    if not sympy.isprime(p):
        return None

    start = (n - 1) ** 2
    end = n ** 2
    interior = range(start + 1, end)  # p - 1 elements

    # Missing residue
    r = (n * n) % p

    # Count spins
    n_plus = 0   # QR (spin +1)
    n_minus = 0  # NR (spin -1)
    n_zero = 0   # multiples of p (spin 0)

    for x in interior:
        res = x % p
        if res == 0:
            n_zero += 1
        else:
            ls = sympy.jacobi_symbol(res, p)
            if ls == 1:
                n_plus += 1
            elif ls == -1:
                n_minus += 1

    # Theoretical predictions
    expected_plus = (p - 3) // 2
    expected_minus = (p - 1) // 2
    expected_zero = 1

    theorem_holds = (
        n_plus == expected_plus
        and n_minus == expected_minus
        and n_zero == expected_zero
    )

    return {
        "n": n,
        "p": p,
        "missing_residue": r,
        "N_plus": n_plus,
        "N_minus": n_minus,
        "N_zero": n_zero,
        "expected_plus": expected_plus,
        "expected_minus": expected_minus,
        "gap": n_minus - n_plus,
        "theorem_holds": theorem_holds,
    }


def main():
    parser = argparse.ArgumentParser(
        description="Verify the Spin Asymmetry Theorem for Legendre intervals."
    )
    parser.add_argument(
        "--limit", type=int, default=2000,
        help="Verify for all n <= LIMIT (default: 2000)"
    )
    parser.add_argument(
        "--csv", type=str, default=None,
        help="Output CSV file path (default: print summary only)"
    )
    args = parser.parse_args()

    print(f"Spin Asymmetry Theorem — Computational Verification")
    print(f"Scanning n = 2 to {args.limit}...")
    print()

    results = []
    total = 0
    holds = 0

    start_time = time.time()

    for n in range(2, args.limit + 1):
        result = verify_interval(n)
        if result is not None:
            total += 1
            if result["theorem_holds"]:
                holds += 1
            results.append(result)

    elapsed = time.time() - start_time

    # Print summary
    print(f"Scan complete in {elapsed:.2f} seconds.")
    print(f"Qualifying intervals (2n-1 prime): {total}")
    print(f"Theorem verified: {holds}/{total} ({100*holds/total:.2f}%)")
    print()

    if holds == total:
        print("✓ Spin Asymmetry Theorem holds for ALL qualifying n "
              f"≤ {args.limit}.")
    else:
        failures = [r for r in results if not r["theorem_holds"]]
        print(f"✗ FAILURES DETECTED at n = "
              f"{[r['n'] for r in failures[:10]]}")

    # Print first few and last few examples
    print()
    print(f"{'n':>8} {'p':>8} {'r':>6} {'N+':>6} {'N-':>6} "
          f"{'N0':>4} {'gap':>4} {'OK':>4}")
    print("-" * 52)
    display = results[:5] + [None] + results[-3:]
    for r in display:
        if r is None:
            print(f"{'...':>8}")
        else:
            ok = "✓" if r["theorem_holds"] else "✗"
            print(f"{r['n']:>8} {r['p']:>8} {r['missing_residue']:>6} "
                  f"{r['N_plus']:>6} {r['N_minus']:>6} "
                  f"{r['N_zero']:>4} {r['gap']:>4} {ok:>4}")

    # Write CSV if requested
    if args.csv:
        fieldnames = [
            "n", "p", "missing_residue",
            "N_plus", "N_minus", "N_zero",
            "expected_plus", "expected_minus",
            "gap", "theorem_holds"
        ]
        with open(args.csv, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(results)
        print(f"\nData written to {args.csv}")


if __name__ == "__main__":
    main()
