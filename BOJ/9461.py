t = int(input())

n = [0]
for _ in range(t):
    n.append(int(input()))


dp = [0,1,1,1,2,2] + [0]*95
for i in range(6,max(n)+1):
    dp[i] = dp[i-1] + dp[i-5]

for i in n[1:]:
    print(dp[i])