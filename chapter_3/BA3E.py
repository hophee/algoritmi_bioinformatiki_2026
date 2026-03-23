# Construct the De Bruijn Graph of a Collection of k-mers
# https://rosalind.info/problems/ba3e/

filename = input()
with open(filename) as f:
    kmers = f.read().split()

graph = {}
for kmer in kmers:
    prefix = kmer[:-1]
    suffix = kmer[1:]
    if prefix not in graph:
        graph[prefix] = []
    graph[prefix].append(suffix)

result = []
for node in sorted(graph):
    result.append(f"{node} -> {','.join(sorted(graph[node]))}")

with open("results_store/res_ba3e.txt", "w") as f:
    f.write("\n".join(result))