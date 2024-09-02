import sys
n = int(input())

# 와인 정보 입력, 인덱스 계산 편하려고 0번째에 0
wines = [0]
for _ in range(n):
  wines.append(int(sys.stdin.readline()))

dp = [0] * (n+1)
dp[1] = wines[1]
if n > 1:
  dp[2] = wines[1] + wines[2]

# 현재 인덱스의 잔을 안마시면, dp[i-1] // 마시면, XOO,OXO 의 경우가 존재
for i in range(3,n+1):
  # 안마심 / XOO / OXO 셋 중에서 큰 값 택하기
  dp[i] = max(dp[i-1], dp[i-3]+wines[i-1]+wines[i], dp[i-2]+wines[i])

# dp리스트 마지막 값 가져오면 해결
print(dp[-1])