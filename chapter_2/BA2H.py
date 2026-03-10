alphabet = ('A', 'C', 'G', 'T')


def hamming_dist(s1, s2):
    ham_dist = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]: ham_dist += 1
    return ham_dist


def distance_between_pattern_and_strings(pattern, dna):
    k = len(pattern)
    distance = 0
    for text in dna:
        hamming_distance = float('inf')
        for i in range(len(text) - k + 1):
            if hamming_distance > hamming_dist(pattern, text[i:i+k]):
                hamming_distance = hamming_dist(pattern, text[i:i+k])
        distance += hamming_distance
    return distance


filename = input()
with open(filename, "r") as f:
    lines = f.read().split('\n')

pattern = lines[0].strip()
dna     = lines[1].strip().split()

result = distance_between_pattern_and_strings(pattern, dna)

with open("results_store/res_ba2h.txt", "w") as f:
    f.write(str(result))
