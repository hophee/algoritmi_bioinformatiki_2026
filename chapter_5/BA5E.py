# Find a Highest-Scoring Alignment of Two Strings
# https://rosalind.info/problems/ba5e/

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

filename = input()
with open(filename) as f:
    s1, s2 = f.read().split()

m, n = len(s1), len(s2)

dp   = [[0] * (n + 1) for _ in range(m + 1)]
back = [[None] * (n + 1) for _ in range(m + 1)]

for i in range(1, m + 1):
    dp[i][0]   = -i * sigma
    back[i][0] = 'up'
for j in range(1, n + 1):
    dp[0][j]   = -j * sigma
    back[0][j] = 'left'

for i in range(1, m + 1):
    for j in range(1, n + 1):
        match  = dp[i-1][j-1] + BLOSUM62[(s1[i-1], s2[j-1])]
        delete = dp[i-1][j]   - sigma
        insert = dp[i][j-1]   - sigma

        best = max(match, delete, insert)
        dp[i][j] = best

        if   best == match:  back[i][j] = 'diag'
        elif best == delete: back[i][j] = 'up'
        else:                back[i][j] = 'left'

a1, a2 = [], []
i, j = m, n

while i > 0 or j > 0:
    if back[i][j] == 'diag':
        a1.append(s1[i-1]); a2.append(s2[j-1])
        i -= 1; j -= 1
    elif back[i][j] == 'up':
        a1.append(s1[i-1]); a2.append('-')
        i -= 1
    else:
        a1.append('-'); a2.append(s2[j-1])
        j -= 1

a1 = ''.join(reversed(a1))
a2 = ''.join(reversed(a2))

with open("results_store/res_ba5e.txt", "w") as f:
    f.write(f"{dp[m][n]}\n{a1}\n{a2}")