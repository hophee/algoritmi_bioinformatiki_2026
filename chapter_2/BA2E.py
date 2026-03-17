# Implement GreedyMotifSearch with Pseudocounts
# https://rosalind.info/problems/ba2e/

import time
alphabet = ('A', 'C', 'G', 'T')


def hamming_dist(s1, s2):
    ham_dist = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]: ham_dist += 1
    return ham_dist


def pr_kmer(kmer, profile):
    p = 1.0 # вероятность 0-мера
    for j, nuc in enumerate(kmer):
        p *= profile[nuc][j]
    return p


def profile_most_probable_kmer(text, k, profile):
    best_prob = -1 # невозможная стартовая отрицательная вероятность
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

def score_new(motifs):
    k = len(motifs[0])
    consensus = ""
    for j in range(k):
        column = [motif[j] for motif in motifs]
        consensus += max(alphabet, key=column.count)

    return sum(hamming_dist(consensus, motif) for motif in motifs)

# def score_new(motifs):
#     score_val = 0
#     for column in zip(*motifs):
#         best_nuc = max(alphabet, key=column.count)
#         score_val += sum(nuc != best_nuc for nuc in column)
#     return score_val

def greedy_motif_search_new(dna, k, t):
    best_motifs = [seq[:k] for seq in dna]

    for i in range(len(dna[0]) - k + 1):
        motifs = [dna[0][i:i+k]]

        for j in range(1, t):
            profile = profile_with_pseudocounts(motifs)
            motifs.append(profile_most_probable_kmer(dna[j], k, profile))

        if score_new(motifs) < score_new(best_motifs):
            best_motifs = motifs

    return best_motifs

speed1, speed2 = [], []

for _ in range(100):
    a = time.perf_counter()
    result1 = greedy_motif_search(dna, k, t)
    speed1.append(time.perf_counter() - a)

    a = time.perf_counter()
    result2 = greedy_motif_search_new(dna, k, t)
    speed2.append(time.perf_counter() - a)

avg1 = sum(speed1) / len(speed1) * 1000
avg2 = sum(speed2) / len(speed2) * 1000
print(f"Функция 1: {avg1:.4f} мс/вызов")
print(f"Функция 2: {avg2:.4f} мс/вызов")
print(f"Ускорение: {avg1/avg2:.2f}x")
