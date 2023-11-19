#!/usr/bin/env python3

import sys

for i in sys.stdin:
    i = int(i)
    i *= 999
    print(i)
