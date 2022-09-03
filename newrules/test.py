from mk91 import opp, bros, inv6, inv3, inv2


def fail(had, expected):
    return f"had {had}, expected: {expected}"


def int_to_str(n):
    res = str(n)
    res = (2-len(res)) * '0' + res
    return res


def test__bros():
    seq = [n if sum([int(d) for d in str(n)]) < 10 and n % 10 != 0
           else 91-n for n in range(1, 46)]
    for i in seq:
        assert opp(i) == sum(bros(i)), \
            f"sum of bros({i}) should always equal opp({i})"


def test__inv6():
    seq = range(1, 91)
    for n in seq:
        a = str(n/91)[2:8]
        b = ''.join([*map(lambda x: str(x), inv6(n))])
        assert a == b, f"{a} should match {b}"
        assert sum(inv6(n)) == 27, \
            "inverse sum of digits should always equal 27"


def test__inv3():
    seq = [n if sum([int(d) for d in str(n)]) < 10 and n % 10 != 0 
           else 91-n for n in range(1, 46)]
    for n in seq:
        a1 = str(n/91)[2:4]
        a2 = str(n/91)[4:6]
        a3 = str(n/91)[6:8]
        b1 = ''.join([*map(int_to_str, inv3(n))])[0:2]
        b2 = ''.join([*map(int_to_str, inv3(n))])[2:4]
        b3 = ''.join([*map(int_to_str, inv3(n))])[4:6]
        assert sum(inv3(n)) == 99, \
            f"input: {n}\ninverse 3 sum of digits should always equal 99"

    for n in range(1, 91):
        a1 = str(n/91)[2:4]
        a2 = str(n/91)[4:6]
        a3 = str(n/91)[6:8]
        b1 = ''.join([*map(int_to_str, inv3(n))])[0:2]
        b2 = ''.join([*map(int_to_str, inv3(n))])[2:4]
        b3 = ''.join([*map(int_to_str, inv3(n))])[4:6]
        assert a1 == b1, fail(a1, b1)
        assert a2 == b2, fail(a2, b2)
        assert a3 == b3, fail(a3, b3)
        bro1, bro2 = bros(n)
        for c in inv3(bro1):
            assert c in inv3(n), "inverse 3 coords of any n brother should be \
                the same as n (not in the same order though)"
        for c in inv3(bro2):
            assert c in inv3(n), "inverse 3 coords of any n brother should be \
                the same as n (not in the same order though)"

        fst_coord = inv3(n)[0]
        snd_coord = inv3(n)[1]
        assert 0 + inv3(bro1).index(fst_coord) + inv3(bro2).index(fst_coord) \
            == 1 + inv3(bro1).index(snd_coord) + inv3(bro2).index(snd_coord) \
            == 3, "inverse 3 coords should have same order between bros"


def test__inv2():
    for n in range(1, 91):
        a1 = str(n/91)[2:5]
        a2 = str(n/91)[5:8]
        b1 = ''.join([*map(int_to_str, inv3(n))])[0:3]
        b2 = ''.join([*map(int_to_str, inv3(n))])[3:6]
        assert a1 == b1, fail(a1, b1)
        assert a2 == b2, fail(a2, b2)
        assert inv2(81)[0] == inv2(opp(81))[1] \
            and inv2(81)[1] == inv2(opp(81))[0], \
            "inverse 2 of n should have swapped coords of inverse 2 of opp(n)"
        assert sum(inv2(n)) == 999, \
            "inverse 2 sum of digits should always equal 999"


if __name__ == '__main__':
    test__bros()
    test__inv6()
    test__inv3()
    test__inv2()
