# Implement BetterBWMatching
# https://rosalind.info/problems/ba9m/

def first_occurrence(transform):
    first_col = sorted(transform)
    first = {}

    for i, symbol in enumerate(first_col):
        if symbol not in first:
            first[symbol] = i

    return first


def count_matrix(transform):
    alphabet = sorted(set(transform))
    count = {symbol: [0] * (len(transform) + 1) for symbol in alphabet}

    for i, symbol in enumerate(transform):
        for char in alphabet:
            count[char][i + 1] = count[char][i]
        count[symbol][i + 1] += 1

    return count


def better_bw_matching(transform, pattern, first, count):
    top = 0
    bottom = len(transform) - 1

    while top <= bottom:
        if pattern:
            symbol = pattern[-1]
            pattern = pattern[:-1]

            if symbol not in count:
                return 0

            top_count = count[symbol][top]
            bottom_count = count[symbol][bottom + 1]

            if bottom_count > top_count:
                top = first[symbol] + top_count
                bottom = first[symbol] + bottom_count - 1
            else:
                return 0
        else:
            return bottom - top + 1

    return 0


filename = input()
with open(filename) as f:
    lines = [line.strip() for line in f if line.strip()]

transform = lines[0]
patterns = []
for line in lines[1:]:
    patterns.extend(line.split())

first = first_occurrence(transform)
count = count_matrix(transform)
matches = [better_bw_matching(transform, pattern, first, count) for pattern in patterns]

with open("results_store/res_ba9m.txt", "w") as f:
    f.write(" ".join(map(str, matches)))
