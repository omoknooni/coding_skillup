import sys
input = sys.stdin.readline

n = int(input())
pack = [0]
pack.extend(list(map(int, input().split())))

# dp[i] : i개를 구매할 수 있는 가장 최대 금액
dp = [0]*(n+1)
for i in range(1,n+1):
  for j in range(1,i+1):
    dp[i] = max(dp[i], dp[i-j]+pack[j])
  
print(dp[-1])

# 각 수에 대한 점화식, 이중에서 max만 취하면 됨
# 1=1
# 2=2, 1+1
# 3=3, 2+1, 1+2
# 4=4, 3+1, 2+2, 1+3