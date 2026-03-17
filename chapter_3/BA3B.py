# Reconstruct a String from its Genome Path
# https://rosalind.info/problems/ba3b/

filename = input()
with open(filename) as f:
    kmers = f.read().split()

result = kmers[0] + "".join(kmer[-1] for kmer in kmers[1:])

with open("results_store/res_ba3b.txt", "w") as f:
    f.write(result)
