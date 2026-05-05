# Align Two Strings Using Affine Gap Penalties
# https://rosalind.info/problems/ba5j/

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
sigma    = 11
eps      = 1
NEG_INF  = float('-inf')

filename = input()
with open(filename) as f:
    lines = [l.strip() for l in f if l.strip() and l.strip().isalpha()]
s1, s2 = lines[0], lines[1]

m, n = len(s1), len(s2)

# M - middle, X - lover, Y - upper
M = [[NEG_INF] * (n + 1) for _ in range(m + 1)]
X = [[NEG_INF] * (n + 1) for _ in range(m + 1)]
Y = [[NEG_INF] * (n + 1) for _ in range(m + 1)]

backM = [[None] * (n + 1) for _ in range(m + 1)]
backX = [[None] * (n + 1) for _ in range(m + 1)]
backY = [[None] * (n + 1) for _ in range(m + 1)]

M[0][0] = 0

for i in range(1, m + 1):
    X[i][0]     = -sigma - (i - 1) * eps
    backX[i][0] = 'X' if i > 1 else 'open'

for j in range(1, n + 1):
    Y[0][j]     = -sigma - (j - 1) * eps
    backY[0][j] = 'Y' if j > 1 else 'open'

for i in range(1, m + 1):
    for j in range(1, n + 1):
        open_x = M[i-1][j] - sigma
        ext_x  = X[i-1][j] - eps
        if open_x >= ext_x:
            X[i][j] = open_x
            backX[i][j] = 'M'
        else:
            X[i][j] = ext_x
            backX[i][j] = 'X'

        open_y = M[i][j-1] - sigma
        ext_y  = Y[i][j-1] - eps
        if open_y >= ext_y:
            Y[i][j] = open_y
            backY[i][j] = 'M'
        else:
            Y[i][j] = ext_y
            backY[i][j] = 'Y'

        score = BLOSUM62[(s1[i-1], s2[j-1])]
        best  = max(M[i-1][j-1], X[i-1][j-1], Y[i-1][j-1])
        M[i][j] = score + best
        if best == M[i-1][j-1]:
            backM[i][j] = 'M'
        elif best == X[i-1][j-1]:
            backM[i][j] = 'X'
        else:
            backM[i][j] = 'Y'

final = max(M[m][n], X[m][n], Y[m][n])
if final == M[m][n]:
    cur = 'M'
elif final == X[m][n]:
    cur = 'X'
else:
    cur = 'Y'

a1, a2 = [], []
i, j = m, n

while i > 0 or j > 0:
    if cur == 'M':
        a1.append(s1[i-1])
        a2.append(s2[j-1])
        cur = backM[i][j]
        i -= 1
        j -= 1
    elif cur == 'X':
        a1.append(s1[i-1])
        a2.append('-')
        cur = backX[i][j]
        i -= 1
    else:
        a1.append('-')
        a2.append(s2[j-1])
        cur = backY[i][j]
        j -= 1

a1 = ''.join(reversed(a1))
a2 = ''.join(reversed(a2))

with open("results_store/res_ba5j.txt", "w") as f:
    f.write(f"{final}\n{a1}\n{a2}")
