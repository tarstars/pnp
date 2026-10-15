"""Corollary 5.4 of the paper: the power-mean identity behind equation (2) of U.

The paper defines the "stabilization function" w by (page 15, paper.txt line
1147-1149)

    A_1 * w = B_1,   A_r = (1/4) sum_{i=1}^4 lambda_i^r,   B_r = (1/(N-4)) sum_{i=5}^N lambda_i^r,

and Corollary 5.4 (line 1164, "The proof is omitted") asserts for the same w

    A_r * w^r = B_r,   0 < r < 1,

which is then used as equation (2) of the system U. The counterexample below is
due to the note paper/topchyi_review.pdf ("A focused review of Topchyi's
proposed P = NP proof", prepared with ChatGPT, 15 October 2026), Section 3; it
is verified here in exact arithmetic.
"""

from __future__ import annotations

import sympy as sp

COUNTEREXAMPLE = (64, 49, 36, 25, 16, 9, 4, 1)


def power_means(lam: tuple[int, ...], r) -> tuple[sp.Expr, sp.Expr]:
    """(A_r, B_r): mean of lambda_i^r over the first four and over the remaining nodes."""
    r = sp.nsimplify(r)
    a = sum(sp.Integer(v) ** r for v in lam[:4]) / 4
    b = sum(sp.Integer(v) ** r for v in lam[4:]) / (len(lam) - 4)
    return sp.nsimplify(a), sp.nsimplify(b)


def stabilization_factor(lam: tuple[int, ...]) -> sp.Expr:
    """w defined by A_1 * w = B_1."""
    a1, b1 = power_means(lam, 1)
    return b1 / a1


def corollary_5_4_residual(lam: tuple[int, ...], r) -> sp.Expr:
    """A_r * w^r - B_r with w from stabilization_factor; Corollary 5.4 claims this is 0."""
    a_r, b_r = power_means(lam, r)
    w = stabilization_factor(lam)
    return sp.nsimplify(a_r * w ** sp.nsimplify(r) - b_r)


def squared_residual_at_one_half(lam: tuple[int, ...]) -> sp.Rational:
    """A_{1/2}^2 * w - B_{1/2}^2, a rational number when every lambda_i is a perfect square."""
    a, b = power_means(lam, sp.Rational(1, 2))
    return sp.nsimplify(a**2 * stabilization_factor(lam) - b**2)


def is_positive_strictly_decreasing(lam: tuple[int, ...]) -> bool:
    return all(v > 0 for v in lam) and all(x > y for x, y in zip(lam, lam[1:]))
