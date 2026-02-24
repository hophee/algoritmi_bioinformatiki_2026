# Find All Approximate Occurrences of a Pattern in a String

def hamming_dist(s1, s2):
    ham_dist = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]: ham_dist += 1
    return ham_dist

pattern = 'ATTCTGGA'
dna_string = 'CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAATGCCTAGCGGCTTGTGGTTTCTCCTACGCTCC'
d = 3

filename = input()
with open(filename) as file:
    lines = [line.rstrip() for line in file]
pattern = lines[0]
dna_string = lines[1]
d = int(lines[2])

k = len(pattern)
L = len(dna_string)

res = []
for i in range(L - k + 1):
    if hamming_dist(pattern, dna_string[i:i + k]) <= d: res.append(i)

with open("/home/iz-user/Downloads/res_ba1h.txt", "w") as f:
    f.write(" ".join(map(str, res)))
    f.write("\n")