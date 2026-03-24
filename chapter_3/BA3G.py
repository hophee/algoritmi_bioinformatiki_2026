# Find an Eulerian Path in a Graph
# https://rosalind.info/problems/ba3g/

filename = input()
with open(filename) as f:
    lines = f.read().strip().split("\n")

graph = {}
for line in lines:
    left, right = line.split(" -> ")
    graph[int(left)] = list(map(int, right.split(",")))

out_deg = {v: len(graph[v]) for v in graph}
in_deg  = {}
for v in graph:
    for u in graph[v]:
        in_deg[u] = in_deg.get(u, 0) + 1

all_nodes = set(graph) | set(in_deg)
for v in all_nodes:
    out_deg.setdefault(v, 0)
    in_deg.setdefault(v, 0)

start = next(v for v in all_nodes if out_deg[v] - in_deg[v] == 1)
end   = next(v for v in all_nodes if in_deg[v]  - out_deg[v] == 1)

graph.setdefault(end, []).append(start)

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

with open("results_store/res_ba3g.txt", "w") as f:
    f.write("->".join(map(str, path)))
