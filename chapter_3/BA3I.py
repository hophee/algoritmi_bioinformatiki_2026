# Find a k-Universal Circular String
# https://rosalind.info/problems/ba3i/

filename = input()
with open(filename) as f:
    k = f.read()
k = int(k)

nodes = [bin(i)[2:].zfill(k - 1) for i in range(2 ** (k - 1))]
graph = {node: [node[1:] + "0", node[1:] + "1"] for node in nodes}

stack = [nodes[0]]
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
