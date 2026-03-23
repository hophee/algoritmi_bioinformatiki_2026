# Construct the De Bruijn Graph of a String
# https://rosalind.info/problems/ba3d/

filename = input()
with open(filename) as f:
    k, text = f.read().split()
k = int(k)

graph = {}
for i in range(len(text) - k + 1):
    kmer   = text[i:i+k]
    prefix = kmer[:-1]
    suffix = kmer[1:]
    if prefix not in graph:
        graph[prefix] = []
    graph[prefix].append(suffix)

result = []
for node in sorted(graph):
    neighbors = sorted(set(graph[node]))
    result.append(f"{node} -> {','.join(neighbors)}")

with open("results_store/res_ba3d.txt", "w") as f:
    f.write("\n".join(result))
