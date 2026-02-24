# Generate the Frequency Array of a String

dna = 'ACGCGGCTCTGAAA'
k = 2

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

def get_freq_array(dna, k):
    freq = [0] * (4**k)
    for i in range(len(dna) - k + 1):
        freq[PatternToNumber(dna[i:i+k])] += 1
    return freq

filename = input()
with open(filename) as file:
    lines = [line.rstrip() for line in file]
dna = lines[0]
k = int(lines[1])


with open("/home/iz-user/Downloads/res_ba1k.txt", "w") as f:
    f.write(' '.join(map(str, get_freq_array(dna, k))))
    f.write("\n")
