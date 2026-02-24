# Implement NumberToPattern

n = 7675
k = 8

def NumberToSymbol(x):
    if x == 0: return 'A'
    if x == 1: return 'C'
    if x == 2: return 'G'
    if x == 3: return 'T'
def NumberToPattern(n, k):
    if k == 1: return NumberToSymbol(n)
    prefIndex = n//4
    r = n % 4
    symbol = NumberToSymbol(r)
    prefPattern = NumberToPattern(prefIndex, k-1)
    return prefPattern+symbol

print(NumberToPattern(n, k))