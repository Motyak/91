#!/usr/bin/env python3
list1 = [i for i in range(1, 49 +1)]
list2 = [*filter(lambda n: n % 11 != 0, list1)]
list3 = [*map(lambda n: 99 - n if n // 10 > n % 10 else n, list2)]
list4 = [
    (
        n,                                                  # xy
        ((9 - n // 10) + n % 10 - 10) * 10 + (9 - n // 10), # S(xy)
        99 - (n % 10 * 10 + (9 - n // 10) + n % 10 - 10),   # S(S(xy))
    ) for n in list3
]
list5 = [a*10**4 + b*10**2 + c*10**0 for t in list4 for a, b, c in [t]]

for x in list5:
    print(f"{x:06}")
