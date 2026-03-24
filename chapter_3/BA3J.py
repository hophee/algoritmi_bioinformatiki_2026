# Reconstruct a String from its Paired Composition
# https://rosalind.info/problems/ba3j/

filename = input()
with open(filename) as f:
    lines = f.read().strip().split("\n")

k, d = map(int, lines[0].split())
pairs = [line.split("|") for line in lines[1:]]

graph = {}
for a, b in pairs:
    prefix = (a[:-1], b[:-1])
    suffix = (a[1:],  b[1:])
    graph.setdefault(prefix, []).append(suffix)

out_deg = {v: len(graph[v]) for v in graph}
in_deg  = {}
for v in graph:
    for u in graph[v]:
        in_deg[u] = in_deg.get(u, 0) + 1

all_nodes = set(graph) | set(in_deg)
for v in all_nodes:
    out_deg.setdefault(v, 0)
    in_deg.setdefault(v, 0)

# start (out - in = 1), end (in - out = 1)
start = next(v for v in all_nodes if out_deg[v] - in_deg[v] == 1)
end   = next(v for v in all_nodes if in_deg[v]  - out_deg[v] == 1)

# Временное ребро → Эйлеров цикл
graph.setdefault(end, []).append(start)

# Хирхольцер
stack = [start]
cycle = []
while stack:
    v = stack[-1]
    if graph.get(v):
        stack.append(graph[v].pop())
    else:
        cycle.append(stack.pop())
cycle = cycle[::-1]

for i in range(len(cycle) - 1):
    if cycle[i] == end and cycle[i+1] == start:
        path = cycle[i+1:] + cycle[1:i+1]
        break

top    = path[0][0] + "".join(node[0][-1] for node in path[1:])
bottom = path[0][1] + "".join(node[1][-1] for node in path[1:])


genome = top + bottom[len(top) - (k + d):]

with open("results_store/res_ba3j.txt", "w") as f:
    f.write(genome)
