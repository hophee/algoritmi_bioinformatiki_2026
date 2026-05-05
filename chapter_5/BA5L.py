# Align Two Strings Using Linear Space
# https://rosalind.info/problems/ba5l/

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
sigma = 5


def forward_col(s1, s2):
    m, n = len(s1), len(s2)
    col  = [-i * sigma for i in range(m + 1)]
    for j in range(1, n + 1):
        new_col = [0] * (m + 1)
        new_col[0] = -j * sigma
        for i in range(1, m + 1):
            match  = col[i-1] + BLOSUM62[(s1[i-1], s2[j-1])]
            delete = col[i] - sigma
            insert = new_col[i-1] - sigma
            new_col[i] = max(match, delete, insert)
        col = new_col
    return col


def backward_col(s1, s2):
    return forward_col(s1[::-1], s2[::-1])[::-1]


def middle_edge(s1, s2):
    m, n = len(s1), len(s2)
    mid  = n // 2

    fwd = forward_col(s1, s2[:mid])
    bck_same = backward_col(s1, s2[mid:])
    bck_next = backward_col(s1, s2[mid+1:])

    best_score = float('-inf')
    best_edge  = None

    for i in range(m + 1):
        score = fwd[i] - sigma + bck_next[i]
        if score > best_score:
            best_score = score
            best_edge  = ((i, mid), (i, mid+1))

    for i in range(m):
        score = fwd[i] - sigma + bck_same[i+1]
        if score > best_score:
            best_score = score
            best_edge  = ((i, mid), (i+1, mid))

        score = fwd[i] + BLOSUM62[(s1[i], s2[mid])] + bck_next[i+1]
        if score > best_score:
            best_score = score
            best_edge  = ((i, mid), (i+1, mid+1))

    return best_edge


def nw_align(s1, s2):
    m, n = len(s1), len(s2)
    if m == 0:
        return list('-' * n), list(s2)
    if n == 0:
        return list(s1), list('-' * m)

    dp   = [[0] * (n + 1) for _ in range(m + 1)]
    back = [[None] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        dp[i][0] = -i * sigma
        back[i][0] = 'u'
    for j in range(1, n + 1):
        dp[0][j] = -j * sigma
        back[0][j] = 'l'

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            match  = dp[i-1][j-1] + BLOSUM62[(s1[i-1], s2[j-1])]
            delete = dp[i-1][j] - sigma
            insert = dp[i][j-1] - sigma
            best   = max(match, delete, insert)
            dp[i][j] = best

            if best == match:
                back[i][j] = 'd'
            elif best == delete:
                back[i][j] = 'u'
            else:
                back[i][j] = 'l'

    a1, a2 = [], []
    i, j = m, n

    while i > 0 or j > 0:
        if back[i][j] == 'd':
            a1.append(s1[i-1])
            a2.append(s2[j-1])
            i -= 1
            j -= 1
        elif back[i][j] == 'u':
            a1.append(s1[i-1])
            a2.append('-')
            i -= 1
        else:
            a1.append('-')
            a2.append(s2[j-1])
            j -= 1

    a1.reverse()
    a2.reverse()
    return a1, a2


def linear_space_alignment(s1_full, s2_full):
    res1, res2 = [], []

    def solve(s1, s2):
        m, n = len(s1), len(s2)

        if m == 0:
            res1.extend(['-'] * n)
            res2.extend(list(s2))
            return

        if n == 0:
            res1.extend(list(s1))
            res2.extend(['-'] * m)
            return

        if m == 1 or n == 1:
            c1, c2 = nw_align(s1, s2)
            res1.extend(c1)
            res2.extend(c2)
            return

        (i1, j1), (i2, j2) = middle_edge(s1, s2)

        solve(s1[:i1], s2[:j1])

        if i2 > i1:
            res1.append(s1[i1])
        else:
            res1.append('-')

        if j2 > j1:
            res2.append(s2[j1])
        else:
            res2.append('-')

        solve(s1[i2:], s2[j2:])

    solve(s1_full, s2_full)
    return res1, res2


filename = input()
with open(filename) as f:
    lines = [l.strip() for l in f if l.strip() and l.strip().isalpha()]
s1, s2 = lines[0], lines[1]

a1_list, a2_list = linear_space_alignment(s1, s2)
a1 = ''.join(a1_list)
a2 = ''.join(a2_list)

score = 0
for x, y in zip(a1, a2):
    if x == '-' or y == '-':
        score -= sigma
    else:
        score += BLOSUM62[(x, y)]

with open("results_store/res_ba5l_rec.txt", "w") as f:
    f.write(f"{score}\n{a1}\n{a2}")