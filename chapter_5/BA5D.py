# Find the Longest Path in a DAG
# https://rosalind.info/problems/ba5d/

filename = input()
with open(filename) as f:
    lines = f.read().strip().split("\n")

source = int(lines[0])
sink   = int(lines[1])

graph     = {}
in_deg    = {}
all_nodes = set()

for line in lines[2:]:
    line = line.strip()
    if not line:
        continue
    left, right  = line.split("->")
    u            = int(left.strip())
    v_str, w_str = right.strip().split(":")
    v, w         = int(v_str.strip()), int(w_str.strip())

    graph.setdefault(u, []).append((v, w))
    all_nodes.update([u, v])
    in_deg[v] = in_deg.get(v, 0) + 1
    in_deg.setdefault(u, 0)

for node in all_nodes:
    in_deg.setdefault(node, 0)
    graph.setdefault(node, [])

# Топологическая сортировка (алгоритм Кана)
queue   = [v for v in all_nodes if in_deg[v] == 0]
deg_tmp = dict(in_deg)
topo    = []
head    = 0

while head < len(queue):
    u = queue[head]
    head += 1
    topo.append(u)
    for v, _ in graph[u]:
        deg_tmp[v] -= 1
        if deg_tmp[v] == 0:
            queue.append(v)

# ДП по топологическому порядку
NEG_INF = float('-inf')
dp      = {v: NEG_INF for v in all_nodes}
back    = {v: None    for v in all_nodes}
dp[source] = 0

for u in topo:
    if dp[u] == NEG_INF:
        continue
    for v, w in graph[u]:
        if dp[u] + w > dp[v]:
            dp[v]   = dp[u] + w
            back[v] = u

# Восстановление пути
path = []
node = sink
while node is not None:
    path.append(node)
    node = back[node]
path.reverse()

with open("results_store/res_ba5d.txt", "w") as f:
    f.write(f"{dp[sink]}\n")
    f.write("->".join(map(str, path)))
