alphabet = ('A', 'C', 'G', 'T')


def hamming_dist(s1, s2):
    ham_dist = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]: ham_dist += 1
    return ham_dist


def pr_kmer(kmer, profile):
    p = 1.0
    for j, nuc in enumerate(kmer):
        p *= profile[nuc][j]
    return p


def profile_most_probable_kmer(text, k, profile):
    best_prob = -1
    best_kmer = text[:k]
    for i in range(len(text) - k + 1):
        kmer = text[i:i+k]
        p = pr_kmer(kmer, profile)
        if p > best_prob:
            best_prob = p
            best_kmer = kmer
    return best_kmer


filename = input()
with open(filename, "r") as f:
    lines = [line.strip() for line in f if line.strip()]

text = lines[0]
k    = int(lines[1])

profile = {}
for i, nuc in enumerate(alphabet):
    profile[nuc] = [float(x) for x in lines[2 + i].split()]

result = profile_most_probable_kmer(text, k, profile)

with open("res_ba2c.txt", "w") as f:
    f.write(result)
