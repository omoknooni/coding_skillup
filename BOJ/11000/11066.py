t = int(input())
for _ in range(t):
    k = int(input())
    novel = list(map(int, input().split()))


    dp = [[0]*k for _ in range(k)]
    for i in range(k-1):
        dp[i][i+1] = novel[i] + novel[i+1]

        # 누적합 구하기
        for j in range(i+2, k):
            dp[i][j] = dp[i][j-1] + novel[j]

    # 최솟값 갱신
    # ex) 1,2,3,4의 최소 병합 합 = 1+(2,3,4)의 최소 합, 4+(1,2,3)의 최소 합 중 최소값
    for l in range(2,k):
        for m in range(k-l):
            dp[m][m+l] += min([dp[m][x] + dp[x+1][m+l] for x in range(m,m+l)])

    print(dp[0][k-1])