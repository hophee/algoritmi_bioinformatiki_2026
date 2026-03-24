# Find an Eulerian krug in a Graph
# https://rosalind.info/problems/ba3f/

filename = input()
with open(filename) as f:
    lines = f.read().strip().split("\n")

graph = {}
for line in lines:
    left, right = line.split(" -> ")
    graph[int(left)] = list(map(int, right.split(",")))

def eulerian_krug(graph):
    cuchka = [next(iter(graph))]
    krug = []

    while cuchka:
        v = cuchka[-1]
        if graph.get(v):
            cuchka.append(graph[v].pop())
        else:
            krug.append(cuchka.pop())

    return krug[::-1]

result = eulerian_krug(graph)

with open("results_store/res_ba3f.txt", "w") as f:
    f.write("->".join(map(str, result)))
