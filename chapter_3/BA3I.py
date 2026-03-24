# Find a k-Universal Circular String
# https://rosalind.info/problems/ba3i/

filename = input()
with open(filename) as f:
    k = f.read().split()
k = int(k)  


kmers = [bin(i)[2:].zfill(k) for i in range(2**k)]

graph = {}
for kmer in kmers:
    graph.setdefault(kmer[:-1], []).append(kmer[1:])

stack = [next(iter(graph))]
cycle = []
while stack:
    v = stack[-1]
    if graph.get(v):
        stack.append(graph[v].pop())
    else:
        cycle.append(stack.pop())
cycle = cycle[::-1]

text = cycle[0] + "".join(node[-1] for node in cycle[1:])
text = text[:-(k - 1)]

with open("results_store/res_ba3i.txt", "w") as f:
    f.write(text)
