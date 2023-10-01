


def printSeparator():
    #TODO: use current terminal width
    print("==============")

def printEquality(lst):
    # print(" = ".join(lst))
    # gonna be more complicated than that

# multiples of 11, up to 11*90 = 990
multiples_of_11 = (11 * i for i in range(91))

def out_of_1000(a):
    print()

for a in multiples_of_11:
    lst = [Fraction(f"{a}", "1 000", isInt=false), Fraction(f"{a} * 1 000", "1 000 000", isInt=false), Fraction(a * 1_000, 1_000_000, isInt=true)]
    printEquality(lst)

    printSeparator()
        
    lst = [Fraction(f"{a}", "1 001", isInt=false), Fraction(f"{a} * 999", "999 999", isInt=false), Fraction(a * 999, 999_999, isInt=true)]
    printEquality(lst)
