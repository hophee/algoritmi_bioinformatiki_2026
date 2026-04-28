# Find the Minimum Number of Coins Needed to Make Change
# https://rosalind.info/problems/ba5a/

filename = input()
with open(filename) as f:
    lines = f.read().strip().split("\n")

money = int(lines[0])
coins = list(map(int, lines[1].split(",")))

dp = [float('inf')] * (money + 1)
dp[0] = 0

for m in range(1, money + 1):
    for c in coins:
        if c <= m and dp[m - c] + 1 < dp[m]:
            dp[m] = dp[m - c] + 1

with open("results_store/res_ba5a.txt", "w") as f:
    f.write(str(dp[money]))