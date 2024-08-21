n = int(input())
B = 1000000000

# 이차원 dp table : 행-> n번째 자리의 숫자, 열-> 자릿수 n
dp = [[0]*10 for _ in range(n+1)]

# n=1인 경우에는 1~9, 각 숫자별로 하나씩 밖에 없음
for i in range(1,10):
  dp[1][i] = 1

for i in range(2,n+1):
  for j in range(10):
    # n번째 자리 숫자가 0으로 끝나면, 이전 자릿수에서 1로 끝난 경우에서만 올라올 수 있음 (XX1 -> XX10)
    if j == 0:
      dp[i][j] = dp[i-1][1]

    # 1~8이면 각 수의 앞/뒤 하나씩 있음
    elif 1 <= j <= 8:
      dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
    
    # 9로 끝나면, 이전 자릿수에서 8로 끝난 경우에서만 올라올 수 있음 (XX8 -> XX89)
    else:
      dp[i][j] = dp[i-1][8]

# 각 row값의 합 -> 각 자릿수에 대한 계단수
print(sum(dp[n]) % B)