import sys

n = int(input())

houses = []
for _ in range(n):
    houses.append(list(map(int, sys.stdin.readline().split( ))))

M = 1e10
answer = M
for i in range(3):                          # 첫 집을 칠하는 3가지 경우의 수
    dp = [[M,M,M] for _ in range(n)]        # 초기 dp테이블을 최댓값으로 채움, 색 변경될때마다 새로 초기화
    dp[0][i] = houses[0][i]
    for j in range(1,n):
        dp[j][0] = houses[j][0] + min(dp[j-1][1], dp[j-1][2])
        dp[j][1] = houses[j][1] + min(dp[j-1][0], dp[j-1][2])
        dp[j][2] = houses[j][2] + min(dp[j-1][0], dp[j-1][1])

    dp[-1][i] = M                           # 첫 집과 마지막 집이 같은색이 되면 안되므로 MAX값 처리
    answer = min(answer, min(dp[-1]))       # 기존 최솟값과 비교하면서 더 작으면 최소값 갱신

print(answer)
