#!/usr/bin/env python3

def sumOfDigits(n):
    return sum(int(c) for c in str(n))

# # list comprehension (oneline) #
# seq = [int('9'*6)*n//91 for n in range(1,91) if n%10!=0 and sumOfDigits(n)<10]
# print(seq)

# using higher-order functions, input -> filter -> map -> output #
seq = [*range(1,91)]
print(seq, '\n')

seq = [*filter(lambda n: n%10!=0 and sumOfDigits(n)<10, seq)]
print(seq, '\n')

seq = [*map(lambda n: int('9'*6)*n//91, seq)]
print(seq)
