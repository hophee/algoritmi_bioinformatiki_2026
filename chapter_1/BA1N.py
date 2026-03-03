# Generate the d-Neighborhood of a String

alphabet = ("A", "C", "G", "T")

def hamming_dist(s1: str, s2: str) -> int:
    if len(s1) != len(s2):
        raise ValueError("Hamming distance is defined for strings of equal length")
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))

def neighbors(pattern: str, d: int) -> set[str]:
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

dna = 'ACG'
d = 1

filename = input()
with open(filename) as file:
    lines = [line.rstrip() for line in file]
dna = lines[0]
d = int(lines[1])

with open("/home/iz-user/Downloads/res_ba1n.txt", "w", encoding="utf-8") as f:
    for kmer in neighbors(dna, d):
        f.write(kmer)
        f.write("\n")
    f.write("\n")
