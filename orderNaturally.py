#!/usr/bin/env python3

def sumOfDigits(n):
    return sum(int(c) for c in str(n))

# # list comprehension (oneline) #
# seq = [int('9'*6)*n//91 for n in [n if n%10!=0 and sumOfDigits(n)<10 else 91-n for n in range(1,46)]]
# print(seq)

# using higher-order functions, input -> map -> map -> output #
seq = [*range(1,46)]
print(seq, '\n')

seq = [*map(lambda n: n if n%10!=0 and sumOfDigits(n)<10 else 91-n, seq)]
print(seq, '\n')

seq = [*map(lambda n: int('9'*6)*n//91, seq)]
print(seq)
