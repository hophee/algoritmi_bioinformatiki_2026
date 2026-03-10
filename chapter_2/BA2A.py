# Implement MotifEnumeration
# rosalind.info/problems/ba2a/
alphabet = ('A', 'C', 'G', 'T')


def hamming_dist(s1, s2):
    ham_dist = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]: ham_dist += 1
    return ham_dist


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


def appears_in_string(pattern, text, d):
    k = len(pattern)
    for i in range(len(text) - k + 1):
        if hamming_dist(pattern, text[i:i+k]) <= d:
            return True
    return False


def motif_enumeration(dna, k, d):
    patterns = set()
    for seq in dna:
        for i in range(len(seq) - k + 1):
            pattern = seq[i:i+k]
            for neighbor in neighbors(pattern, d):
                if all(appears_in_string(neighbor, s, d) for s in dna):
                    patterns.add(neighbor)
    return patterns


filename = input()
with open(filename, "r") as f:
    lines = f.read().split()

k, d = int(lines[0]), int(lines[1])
dna = lines[2:]

result = motif_enumeration(dna, k, d)

with open("results_store/res_ba2a.txt", "w") as f:
    f.write(" ".join(sorted(result)))
