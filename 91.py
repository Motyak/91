#!/usr/bin/env python3

from scipy.special import lambertw
from math import log

def sumOfDigits(n):
    return sum(int(c) for c in str(n))

# x tel que y = x**x, la fonction inverse de la tetration d'ordre 2
def invTower(y):
    return 1.0 if y==1 else log(y) / lambertw(log(y)).real

# on suppose que n est compris entre 0 et 10 non compris
def firstFourDigits(n):
    return int(str(n)[0] + str(n)[2:5] + ('00' if len(str(n)) < 4 else ''))


seqA = [firstFourDigits(invTower(n)) for n in [n if n%10!=0 and sumOfDigits(n)<10 else 91-n for n in range(1,46)]]
print(seqA, end='\n\n')


seqB = seqA

# convertir en float format x.xxx
seqB = [*map(lambda n: float(str(n)[0] + '.' + str(n)[1:4]), seqB)]
# print(seqB, end='\n\n')

# on calcule la tetration d'ordre 2 et on arrondit à l'entier le plus proche
seqB = [*map(lambda n: round(n ** n), seqB)]
# print(seqB, end='\n\n')

# on calcule la division par 91
seqB = [*map(lambda n: n / 91, seqB)]
# print(seqB, end='\n\n')

# on convertit en int format 0.xxxxxx
seqB = [*map(lambda n: int(str(n)[2:8]), seqB)]
print(seqB)
