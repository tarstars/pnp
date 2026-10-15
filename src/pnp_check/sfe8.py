"""Serendipity finite element on 8 nodes (SFE-8): the bases named in the paper.

Checks Claim 5.2 for N = 8 (paper page 11, paper.txt line 789): the interpolant
f = sum(lambda_i * L_i) is independent of the choice of basis exactly when the
mean of the four corner values equals the mean of the four mid-side values.

Two bases are compared:
- the paper's K_1..K_8 (page 12, paper.txt lines 892-905), attributed to
  Khomchenko's school and said to have positive loads;
- the standard Zienkiewicz serendipity basis, which the paper names in
  Section 5.2 comment 2 as the one with "negative loads" (Zienkiewicz's paradox).
"""

from __future__ import annotations

import sympy as sp

x, y = sp.symbols("x y")

# Node numbering as in the paper: 1..4 corners counter-clockwise from (-1,-1),
# 5..8 mid-sides in the same order (K_5 at (0,-1), K_6 at (1,0), ...).
NODES = [(-1, -1), (1, -1), (1, 1), (-1, 1), (0, -1), (1, 0), (0, 1), (-1, 0)]
CORNERS = [0, 1, 2, 3]
SIDES = [4, 5, 6, 7]
BUBBLE = (1 - x**2) * (1 - y**2)


def paper_basis() -> list[sp.Expr]:
    """K_1..K_8 exactly as printed on page 12 of the paper."""
    return [
        sp.Rational(1, 4) * (1 - x) * (1 - y) * x * y,
        -sp.Rational(1, 4) * (1 + x) * (1 - y) * x * y,
        sp.Rational(1, 4) * (1 + x) * (1 + y) * x * y,
        -sp.Rational(1, 4) * (1 - x) * (1 + y) * x * y,
        sp.Rational(1, 4) * (1 - x**2) * (1 - y) ** 2,
        sp.Rational(1, 4) * (1 - y**2) * (1 + x) ** 2,
        sp.Rational(1, 4) * (1 - x**2) * (1 + y) ** 2,
        sp.Rational(1, 4) * (1 - y**2) * (1 - x) ** 2,
    ]


def zienkiewicz_basis() -> list[sp.Expr]:
    """Standard 8-node serendipity shape functions."""
    basis = []
    for xi, yi in NODES[:4]:
        basis.append(sp.Rational(1, 4) * (1 + xi * x) * (1 + yi * y) * (xi * x + yi * y - 1))
    basis.append(sp.Rational(1, 2) * (1 - x**2) * (1 - y))
    basis.append(sp.Rational(1, 2) * (1 - y**2) * (1 + x))
    basis.append(sp.Rational(1, 2) * (1 - x**2) * (1 + y))
    basis.append(sp.Rational(1, 2) * (1 - y**2) * (1 - x))
    return basis


def is_nodal(basis: list[sp.Expr]) -> bool:
    """L_i(node_k) = delta_ik (footnote 12 of the paper)."""
    return all(
        basis[i].subs({x: xk, y: yk}) == (1 if i == k else 0)
        for i in range(8)
        for k, (xk, yk) in enumerate(NODES)
    )


def is_partition_of_unity(basis: list[sp.Expr]) -> bool:
    return sp.simplify(sum(basis) - 1) == 0


def loads(basis: list[sp.Expr]) -> list[sp.Rational]:
    """Integral of each basis function over the square (the paper's 'weight' chi_i times the area G = 4)."""
    return [sp.integrate(b, (x, -1, 1), (y, -1, 1)) for b in basis]


def difference_coefficients(a: list[sp.Expr], b: list[sp.Expr]) -> list[sp.Expr] | None:
    """If every a_i - b_i is c_i * BUBBLE, return the c_i; otherwise None."""
    coeffs = []
    for ai, bi in zip(a, b):
        c = sp.simplify((ai - bi) / BUBBLE)
        if c.free_symbols:
            return None
        coeffs.append(c)
    return coeffs


def invariance_condition() -> sp.Expr:
    """The linear form in the nodal values whose vanishing makes the two interpolants coincide.

    Returns sum(c_i * lambda_i) with c_i from difference_coefficients; Claim 5.2
    for N = 8 says this is proportional to (corner mean) - (side mean).
    """
    lam = sp.symbols("lambda1:9")
    c = difference_coefficients(paper_basis(), zienkiewicz_basis())
    assert c is not None
    return sp.expand(sum(ci * li for ci, li in zip(c, lam)))
