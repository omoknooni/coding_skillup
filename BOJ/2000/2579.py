n = int(input())

points = [0]
for _ in range(n):
    points.append(int(input()))

if n<2:
    print(points[1])
else:
    # dp 초기화 
    dp = [0] * 301
    dp[1] = points[1]
    dp[2] = dp[1] + points[2]

    for i in range(3, n+1):
        dp[i] = max(dp[i-3]+points[i-1]+points[i], dp[i-2]+points[i])

    print(dp[n])