#Find the Most Frequent Words with Mismatches in a String

dna = 'ACGTTGCATGTCGCATGATGCATGAGAGCT'
k = 4
d = 1

def hamming_dist(s1, s2):
    ham_dist = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]: ham_dist += 1
    return ham_dist

def generate_all_kmers(k):
    if k == 0:
        return ['']
    return [kmer + base for kmer in generate_all_kmers(k-1) for base in 'ACGT']

def most_frequent_kmers_with_mismatches(dna_string, k, d):
    counts = {}
    n = len(dna_string)
    for candidate in generate_all_kmers(k):
        count = sum(1 for i in range(n - k + 1)
                    if hamming_dist(candidate, dna_string[i:i+k]) <= d)
        counts[candidate] = count
    max_count = max(counts.values())
    return [kmer for kmer, cnt in counts.items() if cnt == max_count]

filename = input()
with open(filename) as file:
    lines = [line.rstrip() for line in file]
dna = lines[0]
params = lines[1].split(' ')
k = int(params[0])
d = int(params[1])

print(' '.join(most_frequent_kmers_with_mismatches(dna, k, d)))