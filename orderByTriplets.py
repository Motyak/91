#!/usr/bin/env python3

from math import floor
from more_itertools import flatten

# # list comprehension (oneline) #
# seq = [(i,i*9%91,i*9*9%91) for i in [i if i<9 else i+3**floor(i/7) for i in range(1,16)]]
# print(seq)

# using higher-order functions, input -> ranged map -> split -> map -> output #
seq = [*range(1, 16)]
print(seq, '\n') # {1..15}

seq = [*seq[:8], *map(lambda n: n+3**floor(n/7), [seq[i] for i in range(8, 15)])]
print(seq, '\n') # {1..8,12,13,14,15,16,23,24}

seq = [*map(lambda n: tuple(n*9**i%91 for i in range(3)), seq)]
print(seq, '\n') # {triplet0..triplet14}

seq = [*map(lambda n: int('9'*6)*n//91, flatten(seq))]
print(seq) # {s0..s44}
