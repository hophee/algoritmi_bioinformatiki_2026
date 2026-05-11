# Pattern Matching with the Suffix Array
# https://rosalind.info/problems/ba9h/

def suffix_array(text):
    return sorted(range(len(text)), key=lambda i: text[i:])


def pattern_range(text, array, pattern):
    left, right = 0, len(array)

    while left < right:
        mid = (left + right) // 2
        if text[array[mid]:array[mid] + len(pattern)] < pattern:
            left = mid + 1
        else:
            right = mid
    first = left

    left, right = first, len(array)
    while left < right:
        mid = (left + right) // 2
        if text[array[mid]:array[mid] + len(pattern)] <= pattern:
            left = mid + 1
        else:
            right = mid

    return first, right


filename = input()
with open(filename) as f:
    lines = [line.strip() for line in f if line.strip()]

text = lines[0]
patterns = []
for line in lines[1:]:
    patterns.extend(line.split())

array = suffix_array(text)
positions = set()

for pattern in patterns:
    first, last = pattern_range(text, array, pattern)
    for i in range(first, last):
        positions.add(array[i])

with open("results_store/res_ba9h.txt", "w") as f:
    f.write(" ".join(map(str, sorted(positions))))
