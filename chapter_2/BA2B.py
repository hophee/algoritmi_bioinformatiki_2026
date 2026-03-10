alphabet = ('A', 'C', 'G', 'T')


def hamming_dist(s1, s2):
    ham_dist = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]: ham_dist += 1
    return ham_dist


def NumberToSymbol(x):
    if x == 0: return 'A'
    if x == 1: return 'C'
    if x == 2: return 'G'
    if x == 3: return 'T'

def NumberToPattern(n, k):
    if k == 1: return NumberToSymbol(n)
    prefIndex = n // 4
    r = n % 4
    symbol = NumberToSymbol(r)
    prefPattern = NumberToPattern(prefIndex, k - 1)
    return prefPattern + symbol


def distance_between_pattern_and_strings(pattern, dna):
    k = len(pattern)
    distance = 0
    for text in dna:
        hamming_distance = float('inf')
        for i in range(len(text) - k + 1):
            if hamming_distance > hamming_dist(pattern, text[i:i+k]):
                hamming_distance = hamming_dist(pattern, text[i:i+k])
        distance += hamming_distance
    return distance


def median_string(dna, k):
    distance = float('inf')
    median = ''
    for i in range(4**k):
        pattern = NumberToPattern(i, k)
        d = distance_between_pattern_and_strings(pattern, dna)
        if distance > d:
            distance = d
            median = pattern
    return median


filename = input()
with open(filename, "r") as f:
    lines = f.read().split()

k = int(lines[0])
dna = lines[1:]

result = median_string(dna, k)

with open("res_ba2b.txt", "w") as f:
    f.write(result)
