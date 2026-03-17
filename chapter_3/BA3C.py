# Construct the Overlap Graph of a Collection of k-mers
# https://rosalind.info/problems/ba3c/

filename = input()
with open(filename) as f:
    kmers = f.read().split()

prefix_map = {}
for kmer in kmers:
    prefix = kmer[:-1]
    if prefix not in prefix_map:
        prefix_map[prefix] = []
    prefix_map[prefix].append(kmer)

result = []
for kmer in kmers:
    for neighbor in prefix_map.get(kmer[1:], []):
        if neighbor != kmer:
            result.append(f"{kmer} -> {neighbor}")

with open("results_store/res_ba3c.txt", "w") as f:
    f.write("\n".join(result))
