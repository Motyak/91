#!/usr/bin/env python3

def sumOfDigits(n):
    return sum(int(c) for c in str(n))

seq = [n+1 if n%91==0 else n//91*91+91-n%91 if sumOfDigits(n%91)>=10 or n%91%10==0 else n for n in range(1001)]

print(seq)
