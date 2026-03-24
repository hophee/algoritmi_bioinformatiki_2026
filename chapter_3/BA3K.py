# Generate Contigs from a Collection of Reads
# https://rosalind.info/problems/ba3k/

filename = input()
with open(filename) as f:
    kmers = f.read().split()

# Граф де Брёйна
graph = {}
for kmer in kmers:
    graph.setdefault(kmer[:-1], []).append(kmer[1:])

# Степени
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

def path_to_string(path):
    return path[0] + "".join(node[-1] for node in path[1:])

contigs = []

# Maximal non-branching paths из ветвящихся узлов
visited_edges = set()
for v in all_nodes:
    if not is_one_in_one_out(v) and out_deg[v] > 0:
        for w in graph[v]:
            path = [v, w]
            visited_edges.add((v, w))
            while is_one_in_one_out(w):
                w = graph[w][0]
                path.append(w)
                visited_edges.add((path[-2], w))
            contigs.append(path_to_string(path))

# Изолированные циклы (все узлы 1-in-1-out)
for v in all_nodes:
    if is_one_in_one_out(v) and (v, graph[v][0]) not in visited_edges:
        w    = graph[v][0]
        path = [v, w]
        visited_edges.add((v, w))
        while w != v:
            w = graph[w][0]
            path.append(w)
            visited_edges.add((path[-2], w))
        contigs.append(path_to_string(path))

with open("results_store/res_ba3k.txt", "w") as f:
    f.write(" ".join(contigs))
