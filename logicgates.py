def AND(a,b):
    return a & b
def OR(a,b):
    return a | b
def NOT(a):
    return not(a)
def NAND(a,b):
    return not(a &b)
def NOR(a,b):
    return not a|b
def XOR(a,b):
    return a^b
def XNOR(a,b):
    return not a^b
def truth_tables():
    print(" A | B | AND | OR | NAND | NOR | XOR | XNOR")
    for a in [0, 1]:
        for b in [0, 1]:
            and_result = a & b
            or_result = a | b
            nand_result = int(not(a&b))
            nor_result = int(not(a|b))
            xor_result = a^b
            xnor_result = int(not(a^b))
            print(f" {a} | {b} |  {and_result}  |  {or_result}  |  {nand_result}  |  {nor_result}  |  {xor_result}  |  {xnor_result} ")
def NOT():
    print("A | NOT")
    for a in[0,1]:
        NOT_res= int(not(a))
        print(f"{a} | {NOT_res}")
truth_tables()
NOT()
