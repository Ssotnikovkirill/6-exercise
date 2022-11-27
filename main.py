def WIN1(x, s):
    return (x + 1 + s >= 48) or (x * 2 + s >= 48) or (x + s + 1 >= 48) or (x + s * 2 >= 48)

def LESS1(x, s):
    return (not(WIN1(x, s))) and WIN1(x + 1, s) and WIN1(x * 2, s) and WIN1(x, s+1) and WIN1(x, s*2)

def WIN2(x, s):
    return LESS1(x + 1, s) or LESS1(x * 2, s) or LESS1(x, s + 1) or LESS1(x, s * 2)

def LOSS12(x, s):
    return (WIN1(x + 1, s) or WIN2(x + 1, s)) and (WIN1(x * 2, s) or WIN2(x * 2, s)) and (WIN1(x, s+1) or WIN2(x, s+1)) and (WIN1(x, s*2) or WIN2(x, s*2)) and (WIN2(x + 1, s) or WIN2(x * 2, s) or WIN2(x, s+1) or WIN2(x, s*2))

x = 8
for s in range(1, 40):
    #if WIN1(x + 1, s) or WIN1(x * 2, s) or WIN1(x, s+1) or WIN1(x, s*2):
     #   print(s)
     if LOSS12(x, s):
         print(s)

print("ГИГАНСКОЕН ИЗМЕНЕНИЕ КОДА!")
