import sys

t = int(input())

# DP
dp = [[0]*31 for _ in range(31)]
for i in range(31):
    dp[1][i] = i
for i in range(2,31):
    for j in range(i,31):
        if i == j:
            dp[i][j] = 1
        elif i < j:
            dp[i][j] = dp[i-1][j-1] + dp[i][j-1]

case = []
for _ in range(t):
    n,m = map(int, sys.stdin.readline().split())
    case.append(dp[n][m])
for c in case:
    print(c)