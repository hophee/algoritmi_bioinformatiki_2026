# Compute the Edit Distance Between Two Strings
# https://rosalind.info/problems/ba5g/

filename = input()
with open(filename) as f:
    lines = f.read().split()

s1 = lines[0].strip()
s2 = lines[1].strip()

m, n = len(s1), len(s2)

dp = [[0] * (n + 1) for _ in range(m + 1)]

# Граничные условия: удалить все i символов или вставить все j
for i in range(m + 1):
    dp[i][0] = i
for j in range(n + 1):
    dp[0][j] = j

for i in range(1, m + 1):
    for j in range(1, n + 1):
        mismatch = 0 if s1[i-1] == s2[j-1] else 1
        dp[i][j] = min(
            dp[i-1][j-1] + mismatch, #совпадение/мисматч
            dp[i-1][j]   + 1, # удаление из s1
            dp[i][j-1]   + 1 # вставка в s1
        )

with open("results_store/res_ba5g.txt", "w") as f:
    f.write(str(dp[m][n]))