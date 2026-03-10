# Implement GreedyMotifSearch with Pseudocounts
# https://rosalind.info/problems/ba2e/

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


def profile_with_pseudocounts(motifs):
    k = len(motifs[0])
    t = len(motifs)
    count = {nuc: [1] * k for nuc in alphabet}
    for motif in motifs:
        for j, nuc in enumerate(motif):
            count[nuc][j] += 1
    total = t + 4
    return {nuc: [count[nuc][j] / total for j in range(k)] for nuc in alphabet}


def score(motifs):
    k = len(motifs[0])
    t = len(motifs)
    score_val = 0
    for j in range(k):
        column = [motif[j] for motif in motifs]
        max_count = max(column.count(nuc) for nuc in alphabet)
        score_val += t - max_count
    return score_val


def greedy_motif_search(dna, k, t):
    best_motifs = [seq[:k] for seq in dna]

    for i in range(len(dna[0]) - k + 1):
        motifs = [dna[0][i:i+k]]

        for j in range(1, t):
            profile = profile_with_pseudocounts(motifs)
            motifs.append(profile_most_probable_kmer(dna[j], k, profile))

        if score(motifs) < score(best_motifs):
            best_motifs = motifs

    return best_motifs


filename = input()
with open(filename, "r") as f:
    lines = f.read().split()

k, t = int(lines[0]), int(lines[1])
dna  = lines[2:]

result = greedy_motif_search(dna, k, t)

with open("results_store/res_ba2e.txt", "w") as f:
    f.write("\n".join(result))
