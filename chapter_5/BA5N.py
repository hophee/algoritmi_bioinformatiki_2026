# Find a Topological Ordering of a DAG
# https://rosalind.info/problems/ba5n/

filename = input()
with open(filename) as f:
    lines = [l.strip() for l in f if l.strip()]

graph    = {}
in_deg   = {}
all_nodes = set()

for line in lines:
    left, right = line.split(" -> ")
    u = int(left.strip())
    neighbors = list(map(int, right.strip().split(",")))
    graph[u] = neighbors
    all_nodes.add(u)
    for v in neighbors:
        all_nodes.add(v)
        in_deg[v] = in_deg.get(v, 0) + 1

# Узлы без входящих рёбер — начальная очередь
for node in all_nodes:
    in_deg.setdefault(node, 0)
    graph.setdefault(node, [])

# Алгоритм Кана
queue = [v for v in sorted(all_nodes) if in_deg[v] == 0]
topo  = []
head  = 0

while head < len(queue):
    u = queue[head]
    head += 1
    topo.append(u)
    for v in sorted(graph[u]):
        in_deg[v] -= 1
        if in_deg[v] == 0:
            queue.append(v)

with open("results_store/res_ba5n.txt", "w") as f:
    f.write(", ".join(map(str, topo)))