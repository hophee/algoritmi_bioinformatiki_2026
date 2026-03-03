#Implement PatternToNumber

dna = input()

def SymbolToNumber(x):
    if x == 'A': return 0
    if x == 'C': return 1
    if x == 'G': return 2
    if x == 'T': return 3
def PatternToNumber(string):
    if string == '': return 0
    last_symbol = string[-1]
    prefix = string[:-1]
    return 4*PatternToNumber(prefix) + SymbolToNumber(last_symbol)

print(PatternToNumber(dna))