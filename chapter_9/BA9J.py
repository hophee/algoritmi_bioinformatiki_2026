# Reconstruct a String from its Burrows-Wheeler Transform
# https://rosalind.info/problems/ba9j/

def numbered_column(column):
    counts = {}
    result = []

    for symbol in column:
        counts[symbol] = counts.get(symbol, 0) + 1
        result.append((symbol, counts[symbol]))

    return result


filename = input()
with open(filename) as f:
    transform = f.read().strip()

last = numbered_column(transform)
first = numbered_column(sorted(transform))
last_index = {last[i]: i for i in range(len(last))}
first_to_last = {i: last_index[first[i]] for i in range(len(first))}

row = 0
text = []
for _ in range(len(transform)):
    row = first_to_last[row]
    text.append(first[row][0])

with open("results_store/res_ba9j.txt", "w") as f:
    f.write(''.join(text))
