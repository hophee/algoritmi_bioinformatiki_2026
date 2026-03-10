# Implement GibbsSampler
# https://rosalind.info/problems/ba2g/

import random

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


def profile_randomly_generated_kmer(text, k, profile):
    kmers = [text[i:i+k] for i in range(len(text) - k + 1)]
    probs = [pr_kmer(kmer, profile) for kmer in kmers]
    total = sum(probs)
    if total == 0:
        return random.choice(kmers)
    r = random.random() * total
    cumulative = 0.0
    for kmer, p in zip(kmers, probs):
        cumulative += p
        if r <= cumulative:
            return kmer
    return kmers[-1]


def gibbs_sampler(dna, k, t, N):
    motifs = []
    for seq in dna:
        start = random.randint(0, len(seq) - k)
        motifs.append(seq[start:start + k])

    best_motifs = motifs[:]

    for j in range(N):
        i = random.randint(0, t - 1)
        motifs_minus_i = motifs[:i] + motifs[i+1:]
        profile   = profile_with_pseudocounts(motifs_minus_i)
        motifs[i] = profile_randomly_generated_kmer(dna[i], k, profile)
        if score(motifs) < score(best_motifs):
            best_motifs = motifs[:]

    return best_motifs


filename = input()
with open(filename, "r") as f:
    lines = f.read().split()

k, t, N = int(lines[0]), int(lines[1]), int(lines[2])
dna     = lines[3:]

best_motifs = None
best_score  = float('inf')

for _ in range(20):
    motifs = gibbs_sampler(dna, k, t, N)
    s = score(motifs)
    if s < best_score:
        best_score  = s
        best_motifs = motifs

with open("results_store/res_ba2g.txt", "w") as f:
    f.write("\n".join(best_motifs))
