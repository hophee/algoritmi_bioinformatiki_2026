# Find Frequent Words with Mismatches and Reverse complements
import time
alphabet   = ('A', 'C', 'G', 'T')

def hamming_dist(s1, s2):
    ham_dist = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]: ham_dist += 1
    return ham_dist

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


def neighbors(pattern, d):
    if d == 0:
        return {pattern}
    if len(pattern) == 1:
        return set(alphabet)

    neighborhood = set()
    suffix = pattern[1:]
    suffix_neighbors = neighbors(suffix, d)

    for text in suffix_neighbors:
        if hamming_dist(suffix, text) < d:
            for x in alphabet:
                neighborhood.add(x + text)
        else:
            neighborhood.add(pattern[0] + text)
    return neighborhood

def reverse_complement(dna):
    comp = []
    for s in dna:
        if s == 'A': comp.append('T')
        if s == 'T': comp.append('A')
        if s == 'G': comp.append('C')
        if s == 'C': comp.append('G')
    return ''.join(comp[::-1])


#neww
def count_d(text, pattern, d):
    k = len(pattern)
    return sum(
        1 for i in range(len(text) - k + 1)
        if hamming_dist(text[i:i+k], pattern) <= d
    )


def new_frequent_words_mismatches_rc(text, k, d):
    freq = [0] * (4**k)
    for i in range(len(text) - k + 1):
        kmer = text[i:i+k]
        for p in neighbors(kmer, d):
            freq[PatternToNumber(p)] += 1
        for p in neighbors(reverse_complement(kmer), d):
            freq[PatternToNumber(p)] += 1

    max_freq = max(freq)
    return [NumberToPattern(i, k) for i in range(len(freq)) if freq[i] == max_freq]



def frequent_words_mismatches_rc(text, k, d):
    candidates = set()
    for i in range(len(text) - k + 1):
        kmer = text[i:i+k]
        candidates |= neighbors(kmer, d)
        candidates |= neighbors(reverse_complement(kmer), d)

    freq = {}
    for p in candidates:
        freq[p] = count_d(text, p, d) + count_d(text, reverse_complement(p), d)

    max_score = max(freq.values())
    return [p for p, s in freq.items() if s == max_score]



filename = input()
with open(filename) as f:
    lines = [line.rstrip() for line in f]
text    = lines[0]
k, d    = map(int, lines[1].split())
#text = 'ACGTTGCATGTCGCATGATGCATGAGAGCT'
#k, d = 4, 1

#result = frequent_words_mismatches_rc(text, k, d)
start1 = time.time()
print(frequent_words_mismatches_rc(text, k, d))
end1 = time.time()
elapsed_time = end1 - start1
print(f"Elapsed time: {elapsed_time} seconds")

start2 = time.time()
print(new_frequent_words_mismatches_rc(text, k, d))
end2 = time.time()
elapsed_time2 = end2 - start2
print(f"Elapsed time: {elapsed_time2} seconds")
#print(result)
#with open("res_ba1j.txt", "w") as f:
#    f.write(' '.join(result))
#   f.write('\n')
