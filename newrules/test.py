from mk91 import opp, bros, inv6, inv3, inv2


def test__opp():
    res = opp(81)
    assert res == 10, f"expected 10, had {res}"
    assert opp(81) + 81 == 91, "sum of n and opp(n) should always equal 91"


def test__bros():
    res = bros(81)
    assert res == {1, 9}, "expected {1, 9}, had " + f"{res}"
    assert opp(81) == sum({1, 9}), "sum of bros(n) should always equal opp(n)"


def test__inv6():
    res = inv6(81)
    assert res == (8,9,0,1,0,9), f"expected (8,9,0,1,0,9), had {res}"
    assert sum(inv6(81)) == 27, "inverse sum of digits should always equal 27"


def test__inv3():
    res = inv3(81)
    assert res == (89,1,9), f"expected (89,1,9), had {res}"
    assert sum(inv3(81)) == 99, \
        "inverse 3 sum of digits should always equal 99"

    bro1, bro2 = bros(81)

    for c in inv3(bro1):
        assert c in inv3(81), "inverse 3 coords of any n brother should be \
            the same as n (not in the same order though)"
    for c in inv3(bro2):
        assert c in inv3(81), "inverse 3 coords of any n brother should be \
            the same as n (not in the same order though)"

    first_coord = inv3(81)[0]
    secnd_coord = inv3(81)[1]
    assert 0 + inv3(bro1).index(first_coord) + inv3(bro2).index(first_coord) \
        == 1 + inv3(bro1).index(secnd_coord) + inv3(bro2).index(secnd_coord) \
        == 3, "inverse 3 coords should have same order between bros"


def test__inv2():
    res = inv2(81)
    assert res == (890,109), f"expected (890,109), had {res}"
    assert sum(inv2(81)) == 999, \
        "inverse 2 sum of digits should always equal 999"
    assert inv2(81)[0] == inv2(opp(81))[1] \
        and inv2(81)[1] == inv2(opp(81))[0], \
        "inverse 2 of n should have swapped coords of inverse 2 of opp(n)"


if __name__ == '__main__':
    test__opp()
    test__bros()
    test__inv6()
    test__inv3()
    test__inv2()
