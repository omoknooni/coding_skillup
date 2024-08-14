import sys
n = int(input())
tasks = []
for _ in range(n):
  tasks.append(list(map(int, sys.stdin.readline().split(" "))))

dp = [0] * (n+1)
for i in range(n-1,-1,-1):
  if i+tasks[i][0] <= n:
    dp[i] = max(dp[i+1], tasks[i][1] + dp[i+tasks[i][0]])
  else:
    dp[i] = dp[i+1]


print(dp[0])