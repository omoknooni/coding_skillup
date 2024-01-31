n = int(input())
MAX = 100000000
dp = [0] * (n+1) if n>=5 else [0,0,0,0,0,0]
dp[0] = MAX
dp[1] = MAX
dp[2] = MAX
dp[3] = 1
dp[4] = MAX
dp[5] = 1

for i in range(6,n+1):
    if dp[i-3] == MAX and dp[i-5] == MAX:
        dp[i] = MAX
    else:
        dp[i] = min(dp[i-3], dp[i-5]) + 1

if dp[n] == MAX:
    print(-1)
else:
    print(dp[n])