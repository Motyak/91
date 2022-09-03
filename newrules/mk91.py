def opp(n):
    return 91 - n


def bros(n):
    return {n*9%91, n*9*9%91}


def inv6(n):
    res = tuple([int(c) for c in str(n*999999//91)])
    if len(res) == 5:
        res = tuple([0, *res])
    return res


def inv3(n):
    res6 = ''.join([str(i) for i in inv6(n)])
    return (int(res6[0:2]), int(res6[2:4]), int(res6[4:6]))


def inv2(n):
    res6 = ''.join([str(i) for i in inv6(n)])
    return (int(res6[0:3]), int(res6[3:6]))
