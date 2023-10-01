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

class Decimal:
    def __init__(self, int_part=0, fixed_dec_part_frac=None, periodic_dec_part_frac=None):
        self.int_part = int_part
        self.fixed_dec_part_frac = fixed_dec_part_frac
        self.periodic_dec_part_frac = periodic_dec_part_frac

    #TODO: this is an overly simplistic impl, only working in our scenarios
    @staticmethod
    def fromFrac(a, b):
        # e.g. of valid values: (13/1000), (42/99), ...
        assert (b % 10 == 0 and b != 0) or (all([c == "9" for c in str(b)]))

        int_part = int(a / b)

        if b % 10 == 0 and b != 0: # a multiple of 10
            fixed_dec_part_frac = (a, b)
            periodic_dec_part_frac = None
        else: # bunch of 9...
            fixed_dec_part_frac = None
            periodic_dec_part_frac = (a, b)

        return Decimal(int_part, fixed_dec_part_frac, periodic_dec_part_frac)
        
    def __str__(self):
        res = ""
        # first print integral part
        res += f"{self.int_part}"
        if self.fixed_dec_part_frac or self.periodic_dec_part_frac:
            res += "." # decimal separator
        # then print fixed decimal part
        if self.fixed_dec_part_frac:
            a, b = self.fixed_dec_part_frac
            assert b % 10 == 0 and b != 0
            width = len(str(b - 1))
            res += str(a).rjust(width, "0")
        # finally print periodic decimal part
        if self.periodic_dec_part_frac:
            a, b = self.periodic_dec_part_frac
            assert all([c == "9" for c in str(b)])
            width = len(str(b))
            res += "(" + str(a).rjust(width, "0") + ")"
        
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
        a, b = self.a.val, self.b.val
        if self.numeric:
            # TODO: faire en sorte que 50/1000 retourne 0.050 et non 0.05
            # TODO: faire en sorte que 123/999 retourne 0.(123) et non 0.12312312
            return Decimal.fromFrac(a, b).__str__()
        
            # TODO: si c'est un nombre rationnel périodique, on met la partie périodique entre parenthèses
            # TODO: si c'est un nombre rationnel décimal, on affiche jusqu'à 10 digits, ellipsis '...' si ça dépasse
        else:
            return formatFrac(*simplify(a, b))

print(Fraction.fromStr("a * 1 000", "1 000 000"), end="\n\n")

print(Fraction(Int(50), Int(1000), numeric=False), end="\n\n")

print(Fraction(Int(50), Int(1000), numeric=True), end="\n\n")

print(Fraction(Int(50), Int(999), numeric=True))
