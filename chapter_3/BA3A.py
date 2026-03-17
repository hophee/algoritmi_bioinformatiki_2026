# Generate the k-mer Composition of a String
# https://rosalind.info/problems/ba3a/

# Example
# k = 5
# dna  = 'CAATCCAAC'

filename = input()
with open(filename, "r") as f:
    lines = f.read().split()

k = int(lines[0])
dna = lines[1]


def composition(k, dna):
    reads = list()
    for i in range(len(dna) - k + 1):
        reads.append(dna[i:(i+k)])
    return sorted(reads)

#print(composition(k, dna))

with open("results_store/res_ba3a.txt", "w") as f:
    f.write("\n".join(composition(k, dna)))