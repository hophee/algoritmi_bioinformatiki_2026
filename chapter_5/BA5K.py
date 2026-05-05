# Find a Middle Edge in an Alignment Graph in Linear Space
# https://rosalind.info/problems/ba5k/

def load_scoring_matrix(path):
    matrix = {}
    with open(path) as f:
        lines = [l for l in f.read().strip().split("\n") if l.strip()]
    col_headers = lines[0].split()
    for line in lines[1:]:
        parts  = line.split()
        row_aa = parts[0]
        scores = list(map(int, parts[1:]))
        for j, col_aa in enumerate(col_headers):
            matrix[(row_aa, col_aa)] = scores[j]
    return matrix


BLOSUM62 = load_scoring_matrix("other/blosum62.txt")
sigma    = 5


def forward_column(s1, s2):
    m = len(s1)
    col = [-i * sigma for i in range(m + 1)]

    for j in range(1, len(s2) + 1):
        new_col = [0] * (m + 1)
        new_col[0] = -j * sigma
        for i in range(1, m + 1):
            match  = col[i-1] + BLOSUM62[(s1[i-1], s2[j-1])]
            delete = col[i] - sigma
            insert = new_col[i-1] - sigma
            new_col[i] = max(match, delete, insert)
        col = new_col

    return col


def backward_column(s1, s2):
    return forward_column(s1[::-1], s2[::-1])[::-1]


def middle_edge(s1, s2):
    m, n = len(s1), len(s2)
    mid = n // 2

    fwd = forward_column(s1, s2[:mid])
    bck_same = backward_column(s1, s2[mid:])
    bck_next = backward_column(s1, s2[mid+1:])

    best_score = float('-inf')
    best_edge = None

    for i in range(m + 1):
        score = fwd[i] - sigma + bck_next[i]
        if score > best_score:
            best_score = score
            best_edge = ((i, mid), (i, mid+1))

    for i in range(m):
        score = fwd[i] - sigma + bck_same[i+1]
        if score > best_score:
            best_score = score
            best_edge = ((i, mid), (i+1, mid))

        score = fwd[i] + BLOSUM62[(s1[i], s2[mid])] + bck_next[i+1]
        if score > best_score:
            best_score = score
            best_edge = ((i, mid), (i+1, mid+1))

    return best_edge


filename = input()
with open(filename) as f:
    lines = [l.strip() for l in f if l.strip() and l.strip().isalpha()]
s1, s2 = lines[0], lines[1]

m, n   = len(s1), len(s2)
(r1, c1), (r2, c2) = middle_edge(s1, s2)

with open("results_store/res_ba5k.txt", "w") as f:
    f.write(f"({r1}, {c1}) ({r2}, {c2})")
