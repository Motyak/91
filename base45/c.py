#!/usr/bin/env python3
 
from math import log as ln
from math import ceil
from math import floor
 
# n est un entier possédant entre 1 et 6 digits (compris)
def sommeDesDigits(n):
    return sum([int(c) for c in str(n)])
 
Mk = [
        i*int('9'*6)//91 for i in [
            i if i%10!=0 and sommeDesDigits(i)<10 else 91-i for i in 
                range(1,46)
        ]
]
Mk.insert(0, None) #dumb value to make the seq start at index 1
 
# m est un entier en base 10
# retourne une liste de symboles ("base 45")
def chiffrer(m):
    nbSymboles = ceil(ln(m) / ln(45 - 1))
    res = []
 
    for i in range(nbSymboles - 1, -1, -1):
        quotient = floor(m / 45**i)
        res.append(Mk[quotient + 1])
        m = m % 45**i
 
    return res
 
# x est une liste de symboles en "base 45"
# retourne un entier en base 10
def dechiffrer(x):
    x = [(n*91//int('9'*6)) for n in x]
    x = [n if n < 45 else 91-n for n in x]
    x = [n-1 for n in x]
    x.reverse()
    return sum([45**i*n for i,n in enumerate(x)])
 
# m est une chaine de caracteres
# retourne une liste de tuples d'entiers en "base 45"
def chiffrerStr(m):
    return [tuple(chiffrer(ord(c))) for c in m]
 
# x est une liste de tuples d'entier en "base 45"
# retourne une chaine de caractères
def dechiffrerToStr(x):
    return ''.join([chr(dechiffrer(list(t))) for t in x])
 
def _UT():
    print(chiffrer(116))
    print(dechiffrer([32967, 296703]))
 
    print(chiffrerStr("motyak"))
    secret = [(32967, 780219), (32967, 241758), (32967, 296703), (32967, 351648), (32967, 87912), (32967, 197802)]
    print(dechiffrerToStr(secret))
