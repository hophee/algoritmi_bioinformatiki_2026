# Find a Highest-Scoring Multiple Sequence Alignment
# https://rosalind.info/problems/ba5m/

filename = input()
with open(filename) as f:
    lines = [l.strip() for l in f if l.strip()]
s1, s2, s3 = lines[0], lines[1], lines[2]

l1, l2, l3 = len(s1), len(s2), len(s3)

dp   = [[[0] * (l3 + 1) for _ in range(l2 + 1)] for _ in range(l1 + 1)]
back = [[[None] * (l3 + 1) for _ in range(l2 + 1)] for _ in range(l1 + 1)]

for i in range(l1 + 1):
    for j in range(l2 + 1):
        for k in range(l3 + 1):
            if i == 0 and j == 0 and k == 0:
                continue

            candidates = []

            if i > 0 and j > 0 and k > 0:
                match = 1 if s1[i-1] == s2[j-1] == s3[k-1] else 0
                candidates.append((dp[i-1][j-1][k-1] + match, (i-1,j-1,k-1)))
            if i > 0 and j > 0:
                candidates.append((dp[i-1][j-1][k], (i-1,j-1,k)))
            if i > 0 and k > 0:
                candidates.append((dp[i-1][j][k-1], (i-1,j,k-1)))
            if j > 0 and k > 0:
                candidates.append((dp[i][j-1][k-1], (i,j-1,k-1)))
            if i > 0:
                candidates.append((dp[i-1][j][k], (i-1,j,k)))
            if j > 0:
                candidates.append((dp[i][j-1][k], (i,j-1,k)))
            if k > 0:
                candidates.append((dp[i][j][k-1], (i,j,k-1)))

            best_score, best_prev = max(candidates, key=lambda x: x[0])
            dp[i][j][k]   = best_score
            back[i][j][k] = best_prev

a1, a2, a3 = [], [], []
i, j, k = l1, l2, l3

while i > 0 or j > 0 or k > 0:
    pi, pj, pk = back[i][j][k]
    di, dj, dk = i - pi, j - pj, k - pk

    a1.append(s1[i-1] if di else '-')
    a2.append(s2[j-1] if dj else '-')
    a3.append(s3[k-1] if dk else '-')

    i, j, k = pi, pj, pk

a1 = ''.join(reversed(a1))
a2 = ''.join(reversed(a2))
a3 = ''.join(reversed(a3))

score = dp[l1][l2][l3]

with open("results_store/res_ba5m.txt", "w") as f:
    f.write(f"{score}\n{a1}\n{a2}\n{a3}")
