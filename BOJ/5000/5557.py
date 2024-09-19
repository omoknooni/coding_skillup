import sys
input = sys.stdin.readline
n = int(input())
numbers = list(map(int, input().split()))

# 연산결과 0~20
# dp[i][j] : i까지 연산 결과가 j가 되는 가짓수
dp = [[0]*21 for x in range(n-1)]
dp[0][numbers[0]] = 1

for i in range(1, n-1):
  for j in range(21):
    # 이전 열의 결과 값에서 0이 아닌 것을 가져와서 연산
    if dp[i-1][j] != 0:
      # 연산 방향 주의
      if 0 <= (j + numbers[i]) <= 20:
        dp[i][j+numbers[i]] += dp[i-1][j]
      if 0 <= (j - numbers[i]) <= 20:
        dp[i][j-numbers[i]] += dp[i-1][j]

print(dp[-1][numbers[-1]])
#   0 1 2 3 4 ... 20
# 8
# 3
# 2