from pnp_check.weight_order import clauses, min_prefix_for_readable_suffix, sat_sequence, summary, switches


def test_clause_alphabet_size():
    # widths 1..3 over 4 variables: 4*2 + C(4,2)*4 + C(4,3)*8
    assert len(clauses(4)) == 8 + 24 + 32
    assert len(clauses(4, widths=(3,))) == 32


def test_brute_force_agrees_on_hand_cases():
    cl = clauses(3)
    lits = [c[0] for c in cl]
    # (x1 v x2 v x3) alone is satisfiable
    one = cl[lits.index((1, 2, 3))][1]
    assert one != 0
    # all 8 sign patterns over the same 3 variables together are unsatisfiable
    acc = 0xFF
    for lits_, mask in cl:
        if len(lits_) == 3:
            acc &= mask
    assert acc == 0
    # a unit clause and its negation are unsatisfiable
    assert cl[lits.index((1,))][1] & cl[lits.index((-1,))][1] == 0


def test_switch_helpers():
    assert switches([True, True, False, True]) == 2
    assert min_prefix_for_readable_suffix([True, False, True, False]) == 2
    assert min_prefix_for_readable_suffix([False, False, True, True]) == 0


def test_satisfiability_is_not_readable_from_a_prefix_of_the_weight_order():
    # n = 3 variables, m = 3 clauses of width 1..3: 26**3 = 17576 instances in word order.
    s = summary(3, 3)
    assert s["instances"] == 17576
    assert 0 < s["satisfiable"] < s["instances"]
    # Measured 2026-10-15: 862 flips between neighbours, and the suffix becomes
    # 'one position number' only from M = 17034 (96.9 % of all instances).
    assert s["switches"] > 500
    assert s["prefix_fraction"] > 0.9
