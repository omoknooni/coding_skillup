import sys

n = int(input())
houses = []
for _ in range(n):
    houses.append(list(map(int, sys.stdin.readline().split(" "))))

M = 1e8
answer = M
for i in range(3):                      # 각 집을 칠하는 3가지 색상
    dp = [[M,M,M] for _ in range(n)]
    dp[0][i] = houses[0][i]             # 첫번째 집을 칠함
    for j in range(1,n):
        dp[j][0] = houses[j][0] + min(dp[j-1][1], dp[j-1][2])   # 집을 R로 칠할때, 이전값과 중복되지않아야함
        dp[j][1] = houses[j][1] + min(dp[j-1][0], dp[j-1][2])
        dp[j][2] = houses[j][2] + min(dp[j-1][0], dp[j-1][1])
    answer = min(answer, min(dp[-1]))   # 결과(min(dp[-1]))가 기존 최솟값보다 작아지면 갱신

print(answer)