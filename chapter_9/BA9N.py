# Find All Occurrences of a Collection of Patterns in a String
# https://rosalind.info/problems/ba9n/

def suffix_array(text):
    return sorted(range(len(text)), key=lambda i: text[i:])


def burrows_wheeler_transform(text, array):
    return ''.join(text[i - 1] if i > 0 else text[-1] for i in array)


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


def bw_matching_range(pattern, first, count, n):
    top = 0
    bottom = n - 1

    while top <= bottom:
        if pattern:
            symbol = pattern[-1]
            pattern = pattern[:-1]

            if symbol not in count:
                return None

            top_count = count[symbol][top]
            bottom_count = count[symbol][bottom + 1]

            if bottom_count > top_count:
                top = first[symbol] + top_count
                bottom = first[symbol] + bottom_count - 1
            else:
                return None
        else:
            return top, bottom

    return None


filename = input()
with open(filename) as f:
    lines = [line.strip() for line in f if line.strip()]

text = lines[0]
patterns = []
for line in lines[1:]:
    patterns.extend(line.split())

if not text.endswith("$"):
    text += "$"

array = suffix_array(text)
transform = burrows_wheeler_transform(text, array)
first = first_occurrence(transform)
count = count_matrix(transform)

positions = set()
for pattern in patterns:
    match_range = bw_matching_range(pattern, first, count, len(transform))
    if match_range is None:
        continue
    top, bottom = match_range
    for i in range(top, bottom + 1):
        if array[i] < len(text) - 1:
            positions.add(array[i])

with open("results_store/res_ba9n.txt", "w") as f:
    f.write(" ".join(map(str, sorted(positions))))
