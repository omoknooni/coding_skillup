n,k = map(int, input().split())

items = [(0,0)]
for i in range(n):
    w,v = map(int, input().split())
    items.append(tuple((w,v)))

# dp
dp = [[0]*(k+1) for _ in range(n+1)]

# i = item 목록, j = 무게
for i in range(n+1):
    for j in range(k+1):
        # item의 무게가 현재 남은 무게보다 큰 경우, 해당 item을 넣지 못한다.
        # 이전 item까지의 최대 value값을 그대로 가져옴
        if j < items[i][0]:
            dp[i][j] = dp[i-1][j]

        # 이 item을 넣을 수 있을 때, 이 item을 넣고 계산한 value값과 이 item을 넣지 않고 계산한 value값 중 큰 것을 사용
        # 이 item을 넣는 경우, 이 item 무게만큼 제하고 이전 item까지 계산한 dp값(dp[i-1][j-items[i][0]])에 이 item의 value를 더한 값을 이용한다.
        else:
            dp[i][j] = max(dp[i-1][j-items[i][0]]+items[i][1], dp[i-1][j])

print(dp[n][k])