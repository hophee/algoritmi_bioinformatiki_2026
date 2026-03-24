# Generate All Maximal Non-Branching Paths in a Graph
# https://rosalind.info/problems/ba3m/

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

def is_one_in_one_out(v):
    return in_deg[v] == 1 and out_deg[v] == 1

paths = []
visited_edges = set()

# Пути из ветвящихся узлов
for v in all_nodes:
    if not is_one_in_one_out(v) and out_deg[v] > 0:
        for w in graph[v]:
            path = [v, w]
            visited_edges.add((v, w))
            while is_one_in_one_out(w):
                w = graph[w][0]
                path.append(w)
                visited_edges.add((path[-2], w))
            paths.append(path)

# Изолированные циклы
for v in all_nodes:
    if is_one_in_one_out(v) and (v, graph[v][0]) not in visited_edges:
        w    = graph[v][0]
        path = [v, w]
        visited_edges.add((v, w))
        while w != v:
            w = graph[w][0]
            path.append(w)
            visited_edges.add((path[-2], w))
        paths.append(path)

with open("results_store/res_ba3m.txt", "w") as f:
    f.write("\n".join(" -> ".join(map(str, path)) for path in paths))
