import math

class Int:
    def __init__(self, val):
        self.val = val

    def __str__(self):
        res = ""
        cur_digit = 0
        # lst[::-1] <=> reverse the lst
        for c in str(self.val)[::-1]:
            if cur_digit % 3 == 0:
                res = f" {res}"
            res = f"{c}{res}"
            cur_digit += 1
        return res

    

# for nb in [Int(1), Int(123), Int(1234), Int(999999), Int(1000000)]:
#     print(nb)

class Fraction:
    def __init__(self, a, b, numeric):
        self.a = a
        self.b = b
        self.numeric = numeric

    @staticmethod
    def fromStr(a, b):
        assert isinstance(a, str)
        assert isinstance(b, str)
        return Fraction(a, b, numeric=False)

    def __str__(self):
        def formatFrac(a, b):
            len_longest_operand = max(len(str(a)), len(str(b)))
            def align(text):
                return text.center(len_longest_operand)
            aligned_a = align(str(a))
            aligned_b = align(str(b))
            return "\n".join([aligned_a, "-" * len_longest_operand, aligned_b])

        def simplify(a: int, b: int):
            gcd = math.gcd(a, b)
            return a // gcd, b // gcd

        if isinstance(self.a, str) and isinstance(self.b, str):
            return formatFrac(self.a, self.b)

        assert isinstance(self.a, Int) and isinstance(self.b, Int)
        a = self.a.val
        b = self.b.val
        if self.numeric:
            # TODO: faire en sorte que 50/1000 retourne 0.050 et non 0.05
            if b % 10 == 0:
                pass
            # return str(a / b)
            # TODO: si c'est un nombre rationnel périodique, on met la partie périodique entre parenthèses
            # TODO: si c'est un nombre rationnel décimal, on affiche jusqu'à 10 digits, ellipsis '...' si ça dépasse
            pass
        else:
            return formatFrac(*simplify(a, b))

# print(Fraction.fromStr("a * 1 000", "1 000 000"))

# print(Fraction(Int(50), Int(1000), numeric=False))

print(Fraction(Int(50), Int(1000), numeric=True))

# print(Fraction(Int(50), Int(999), numeric=True))
