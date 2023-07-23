#/usr/bin/env python3
import math
import functools

def debug(func):
    """Print the function signature"""
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"DEBUG: calling {func.__name__}({signature})")
        return func(*args, **kwargs)
    return wrapper_debug

class Fraction:
    def __init__(self, a: int, b: int):
        assert isinstance(a, int)
        assert isinstance(b, int)
        
        gcd = math.gcd(a, b)
        
        self.a = a // gcd
        self.b = b // gcd
        
    def __repr__(self):
        return f"{self.a}/{self.b}"
        
class ContinuedFraction:
    def __init__(self):
        self.terms = []
    
    def add(self, term: int):
        assert isinstance(term, int)
        
        self.terms.append(str(term))
        
    def __repr__(self):
        out = "["
            
        if (len(self.terms) >= 1):
            out += f"{self.terms[0]}; "
        
        if (len(self.terms) >= 2):
            out += ", ".join(self.terms[1:])
        
        out += "]"
        
        return out

@debug
def continued_fraction(input: Fraction, out: ContinuedFraction):
    assert isinstance(input, Fraction)
    assert isinstance(out, ContinuedFraction)
    
    integer_part = math.floor(input.a / input.b)
    out.add(integer_part)
    if (input.b == 1):
        return out
    fractional_part = Fraction(input.a - input.b * integer_part, input.b)
    reciprocal=Fraction(fractional_part.b, fractional_part.a)

    return continued_fraction(input=reciprocal, out=out)

    
n = Fraction(27, 91)
res = continued_fraction(input=n, out=ContinuedFraction())
    
print(res)
