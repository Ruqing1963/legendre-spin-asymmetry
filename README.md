# Algebraic Rigidity and Quadratic Residue Asymmetry in Legendre Intervals

**Titan Project — Paper IX**

[![DOI](https://img.shields.io/badge/Zenodo-Paper_IX-blue)](https://github.com/Ruqing1963/legendre-spin-asymmetry)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

## Overview

This repository contains the source code, data, and manuscript for a paper proving the **Spin Asymmetry Theorem** for Legendre intervals:

> **Theorem.** Let $n \geq 2$ such that $p = 2n - 1$ is prime. The interior of the Legendre interval $\mathcal{I}_n = [(n-1)^2, n^2]$ contains exactly $p - 1$ consecutive integers forming a *punctured complete residue system* modulo $p$, missing exactly one quadratic residue class. Consequently, quadratic non-residues always exceed quadratic residues by exactly 1.

This is an unconditional algebraic identity — no conjectures are assumed.

## Key Results

| Result | Status | Section |
|--------|--------|---------|
| Spin Asymmetry Theorem ($N^- - N^+ = 1$) | **Proved** | §2 |
| Computational verification ($n \leq 2000$, 549/549) | **Verified** | §2.4 |
| Wronskian compression stabilization ($q_W \to 1.20$) | Observed | §4 |

## Repository Structure

```
├── paper/
│   ├── Spin_Asymmetry.tex          # LaTeX source
│   └── Spin_Asymmetry.pdf          # Compiled PDF
├── scripts/
│   ├── verify_spin_asymmetry.py    # Theorem verification (n ≤ 2000)
│   ├── wronskian_scanner.py        # Discrete Wronskian compression
│   ├── topology_scanner.py         # Full topology + Wronskian scanner
│   └── dual_weapon.py              # Combined residue + Wronskian tool
├── data/
│   ├── spin_verification.csv       # Full verification data (549 rows)
│   └── wronskian_compression.csv   # Compression ratios (6 targets)
├── figures/
│   ├── Figure_1_100.png            # Tension map n=100
│   ├── Figure_1_10000.png          # Tension map n=10000
│   └── Figure_1_10000_avg.png      # Tension map n=10000 (with averages)
├── LICENSE
└── README.md
```

## Quick Start

### Verify the Spin Asymmetry Theorem

```bash
pip install sympy
python scripts/verify_spin_asymmetry.py
```

Expected output:
```
Verified: 549/549 instances (100.00%)
Spin Asymmetry Theorem holds for ALL n ≤ 2000 with 2n-1 prime.
```

### Compute Wronskian Compression

```bash
python scripts/wronskian_scanner.py
```

## The Proof in One Paragraph

The identity $(n-1)^2 = n^2 - (2n-1) \equiv n^2 \pmod{p}$ shows both endpoints share the same residue $r$ modulo $p$. Since $p$ consecutive integers cover all residue classes mod $p$, the $p-1$ interior integers cover all classes *except* $r$. Since $r \equiv n^2$ is a perfect square mod $p$, it is a quadratic residue with Legendre symbol $+1$. Removing one QR class from the balanced $(p-1)/2$ vs $(p-1)/2$ split yields $N^+ = (p-3)/2$ and $N^- = (p-1)/2$, giving $N^- - N^+ = 1$.

## Companion Papers (Titan Project)

| # | Title | Link |
|---|-------|------|
| I | Conductor Incompressibility for Frey Curves | [Zenodo:18682375](https://zenodo.org/records/18682375) |
| III | Weil Restriction Rigidity via Genus 2 Jacobians | [Zenodo:18683194](https://zenodo.org/records/18683194) |
| IV | Landau's Fourth Problem: Conductor Rigidity and Sato–Tate | [Zenodo:18683712](https://zenodo.org/records/18683712) |
| V | The 2-2 Coincidence: Primes in Arithmetic Progressions | [Zenodo:18684151](https://zenodo.org/records/18684151) |
| VI | Genesis of Prime Constellations: GSp(8) | [Zenodo:18684352](https://zenodo.org/records/18684352) |
| VII | Conductor Rigidity and the Static Conduit in GSp(4) | [Zenodo:18684892](https://zenodo.org/records/18684892) |
| VIII | Legendre's Conjecture in Function Fields | Zenodo (forthcoming) |
| **IX** | **Quadratic Residue Asymmetry (this paper)** | **This repository** |

## Citation

```bibtex
@article{chen2026spin,
  author  = {Ruqing Chen},
  title   = {Algebraic Rigidity and Quadratic Residue Asymmetry in Legendre Intervals},
  year    = {2026},
  note    = {Titan Project Paper IX},
  url     = {https://github.com/Ruqing1963/legendre-spin-asymmetry}
}
```

## License

This work is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
