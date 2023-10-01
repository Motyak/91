#!/usr/bin/env python3

import sys

def sum_of_digits(n):
    return sum(int(c) for c in str(n))

for i in sys.stdin:
    i = int(i)
    if i % 10 == 0 or sum_of_digits(i) >= 10:
        i = 91 - i
    print(i)
