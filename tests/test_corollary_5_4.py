import sympy as sp

from pnp_check.corollary_5_4 import (
    COUNTEREXAMPLE,
    corollary_5_4_residual,
    is_positive_strictly_decreasing,
    power_means,
    squared_residual_at_one_half,
    stabilization_factor,
)


def test_counterexample_meets_the_papers_stated_conditions():
    # lambda_i > 0 and decreasing in i (paper line 1134); a geometric tail 2^-k can be
    # appended to reach the limit 0 with sum lambda_i^(1/(1-r)) finite for r = 1/2.
    assert is_positive_strictly_decreasing(COUNTEREXAMPLE)


def test_the_intermediate_values_quoted_in_the_note():
    a1, b1 = power_means(COUNTEREXAMPLE, 1)
    ah, bh = power_means(COUNTEREXAMPLE, sp.Rational(1, 2))
    assert (a1, b1) == (sp.Rational(87, 2), sp.Rational(15, 2))
    assert stabilization_factor(COUNTEREXAMPLE) == sp.Rational(5, 29)
    assert (ah, bh) == (sp.Rational(13, 2), sp.Rational(5, 2))


def test_corollary_5_4_fails_exactly():
    # A_{1/2}^2 * w - B_{1/2}^2 = 169/4 * 5/29 - 25/4 = 30/29, so A_{1/2} * sqrt(w) != B_{1/2}.
    assert squared_residual_at_one_half(COUNTEREXAMPLE) == sp.Rational(30, 29)
    assert corollary_5_4_residual(COUNTEREXAMPLE, sp.Rational(1, 2)) != 0


def test_identity_does_hold_when_both_groups_are_proportional():
    # Sanity check of the machinery: if lambda_{5..8} = c * lambda_{1..4} then w = c and
    # A_r * c^r = B_r for every r, so the residual vanishes.
    lam = (16, 9, 4, 1, 64, 36, 16, 4)  # second group = 4 * first group, reordered within group
    assert corollary_5_4_residual(lam, sp.Rational(1, 2)) == 0
