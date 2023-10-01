#!/usr/bin/env python3

from tommymath import Int, Decimal, Fraction

import sys
from io import StringIO
import os

def printEquality(lst):
    out = [StringIO(), StringIO(), StringIO()] # 3 lines

    def append_to_line(lineno, text):
        assert lineno in {1, 2, 3}
        out[lineno - 1].write(text)

    def get_line(lineno):
        assert lineno in {1, 2, 3}
        return out[lineno - 1].getvalue()
    
    def append_elem(elem):
        if elem.numeric:
            # TODO:
            line2 = elem.__str__()
            if len(get_line(2)) != 0:
                line2 = " = " + line2
            append_to_line(2, line2)
            return
        
        line1, line2, line3 = elem.__str__().split("\n")
        if len(get_line(2)) != 0:
            line1 = len(" = ") * " " + line1
            line2 = " = " + line2
            line3 = len(" = ") * " " + line3
        append_to_line(1, line1)
        append_to_line(2, line2)
        append_to_line(3, line3)

    for elem in lst:
        append_elem(elem)
    
    res = map(lambda x: x.getvalue(), out)
    res = filter(lambda x: len(x) != 0, res)
    res = "\n".join(res)
    print(res, end="")
    if len(res) != 0:
        print(end="\n\n") # trailing newline

def printSeparator():
    term_width = os.get_terminal_size().columns
    print("=" * term_width, end="\n\n")

printSeparator()

for i in sys.stdin:
    i = int(i)

    lst = [Fraction(f"{i}", "1 000", numeric=False), 
           Fraction(f"{i} * 1 000", "1 000 000", numeric=False), 
           Fraction(Int(i * 1_000), Int(1_000_000), numeric=True)]
    printEquality(lst)
        
    lst = [Fraction(f"{i}", "1 001", numeric=False), 
           Fraction(f"{i} * 999", "999 999", numeric=False), 
           Fraction(Int(i * 999), Int(999_999), numeric=True)]
    printEquality(lst)

    printSeparator()
