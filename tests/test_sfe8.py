import sympy as sp

from pnp_check.sfe8 import (
    BUBBLE,
    CORNERS,
    SIDES,
    difference_coefficients,
    invariance_condition,
    is_nodal,
    is_partition_of_unity,
    loads,
    paper_basis,
    zienkiewicz_basis,
)


def test_paper_basis_is_a_nodal_basis():
    # Footnote 12: L_i(x_k, y_k) = delta_ik and sum L_i = 1.
    assert is_nodal(paper_basis())
    assert is_partition_of_unity(paper_basis())


def test_zienkiewicz_basis_is_a_nodal_basis():
    assert is_nodal(zienkiewicz_basis())
    assert is_partition_of_unity(zienkiewicz_basis())


def test_paper_basis_has_positive_loads_and_zienkiewicz_negative_corner_loads():
    # Section 5.2 comment 2: Zienkiewicz's paradox (negative loads) versus Khomchenko's positive loads.
    paper = loads(paper_basis())
    std = loads(zienkiewicz_basis())
    assert all(v > 0 for v in paper)
    assert all(std[i] < 0 for i in CORNERS)
    assert sum(paper) == 4 and sum(std) == 4  # loads sum to the area of the square


def test_two_bases_differ_by_the_bubble_with_sign_by_node_type():
    c = difference_coefficients(paper_basis(), zienkiewicz_basis())
    assert c is not None
    assert all(c[i] == sp.Rational(1, 4) for i in CORNERS)
    assert all(c[i] == -sp.Rational(1, 4) for i in SIDES)


def test_claim_5_2_for_n_equals_8():
    # f_K - f_Z = (BUBBLE/4) * (sum of corner values - sum of side values), so the
    # interpolant is basis-independent iff corner mean == side mean. This is the
    # N = 4k line of Claim 5.2 with N = 8.
    lam = sp.symbols("lambda1:9")
    expected = sp.Rational(1, 4) * (sum(lam[i] for i in CORNERS) - sum(lam[i] for i in SIDES))
    assert sp.expand(invariance_condition() - expected) == 0
    assert BUBBLE.subs({"x": 0, "y": 0}) == 1
