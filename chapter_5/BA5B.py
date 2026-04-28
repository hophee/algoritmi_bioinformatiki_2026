# Find the Length of a Longest Path in a Manhattan-like Grid
# https://rosalind.info/problems/ba5b/

filename = input()
with open(filename) as f:
    content = f.read().strip()

parts = content.split("-")
header_and_down = parts[0].strip().split("\n")
right_lines     = parts[1].strip().split("\n")

n, m = map(int, header_and_down[0].split())


Down = []
for line in header_and_down[1:]:
    line = line.strip()
    if line:
        Down.append(list(map(int, line.split())))

Right = []
for line in right_lines:
    line = line.strip()
    if line:
        Right.append(list(map(int, line.split())))

dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    dp[i][0] = dp[i-1][0] + Down[i-1][0]

for j in range(1, m + 1):
    dp[0][j] = dp[0][j-1] + Right[0][j-1]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        from_top  = dp[i-1][j] + Down[i-1][j]
        from_left = dp[i][j-1] + Right[i][j-1]
        dp[i][j]  = max(from_top, from_left)

with open("results_store/res_ba5b.txt", "w") as f:
    f.write(str(dp[n][m]))