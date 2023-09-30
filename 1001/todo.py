class Int:
    def __init__(self, n):
        self.n = n

    def __str__(self):
        str(self.n)
    
class Fraction:
    def __init__(self, a, b, isInt):
        self.a = a
        self.b = b
        self.isInt = isInt

    @staticmethod
    def fromStr(a, b):
        assert isinstance(a, str)
        assert isinstance(b, str)
        return Fraction(a, b, isInt=False)

    @staticmethod
    def fromInt(a, b):
        assert isinstance(a, int)
        assert isinstance(b, int)
        return Fraction(a, b, isInt=True)

    def __str__(self):
        if self.isInt:
            return str(self.a / self.b)
        else:



"""
on passe une liste de Number(Fraction(a, b), dec=true)
et ça va print chaque Number, séparé d'un " = ", en tenant compte
de la height du terminal (si on trouve pas la valeur du terminal, on prendra
une valeur par défaut "raisonnable")
"""

"""

 143    143 * 1 000
----- = ----------- = 0.143000
1 000    1 000 000

 143    143 * 999   143 * 1000 - 143   142 857
----- = --------- = ---------------- = ------- = 0.(142857)
1 001    999 999        999 999        999 999

"""