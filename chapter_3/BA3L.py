# Construct a String Spelled by a Gapped Genome Path
# https://rosalind.info/problems/ba3l/

filename = input()
with open(filename) as f:
    lines = f.read().strip().split("\n")

k, d  = map(int, lines[0].split())
pairs = [line.split("|") for line in lines[1:]]

top    = pairs[0][0] + "".join(p[0][-1] for p in pairs[1:])
bottom = pairs[0][1] + "".join(p[1][-1] for p in pairs[1:])

for i in range(k + d, len(top)):
    if top[i] != bottom[i - k - d]:
        raise ValueError("there is no string spelled by the gapped patterns")

genome = top + bottom[len(top) - (k + d):]

with open("results_store/res_ba3l.txt", "w") as f:
    f.write(genome)
