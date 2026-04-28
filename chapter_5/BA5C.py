# Find a Longest Common Subsequence of Two Strings 
# https://rosalind.info/problems/ba5c/

filename = input()
with open(filename) as f:
    lines = f.read().strip().split("\n")

s1 = lines[0].strip()
s2 = lines[1].strip()

m, n = len(s1), len(s2)

# dp[i][j] = длина LCS для s1[:i] и s2[:j]
dp   = [[0] * (n + 1) for _ in range(m + 1)]
back = [[None] * (n + 1) for _ in range(m + 1)]

for i in range(1, m + 1):
    for j in range(1, n + 1):
        if s1[i-1] == s2[j-1]:
            dp[i][j]   = dp[i-1][j-1] + 1
            back[i][j] = 'diag'
        elif dp[i-1][j] >= dp[i][j-1]:
            dp[i][j]   = dp[i-1][j]
            back[i][j] = 'up'
        else:
            dp[i][j]   = dp[i][j-1]
            back[i][j] = 'left'

# Обратный ход для восстановления LCS
lcs = []
i, j = m, n
while i > 0 and j > 0:
    if back[i][j] == 'diag':
        lcs.append(s1[i-1])
        i -= 1; j -= 1
    elif back[i][j] == 'up':
        i -= 1
    else:
        j -= 1

lcs = ''.join(reversed(lcs))

with open("results_store/res_ba5c.txt", "w") as f:
    f.write(lcs)