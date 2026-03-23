# Find an Eulerian Cycle in a Graph
# https://rosalind.info/problems/ba3f/

filename = input()
with open(filename) as f:
    lines = f.read().strip().split("\n")

graph = {}
for line in lines:
    left, right = line.split(" -> ")
    graph[int(left)] = list(map(int, right.split(",")))

def eulerian_cycle(graph):
    stack = [next(iter(graph))]
    cycle = []

    while stack:
        v = stack[-1]
        if graph.get(v):
            stack.append(graph[v].pop())
        else:
            cycle.append(stack.pop())

    return cycle[::-1]

result = eulerian_cycle(graph)

with open("results_store/res_ba3f.txt", "w") as f:
    f.write("->".join(map(str, result)))
