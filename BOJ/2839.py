n = int(input())

# DP
MAX = 100000000
dp = [0] * (n+1) if n>=5 else [0,0,0,0,0,0]
dp[0] = MAX
dp[1] = MAX
dp[2] = MAX
dp[3] = 1
dp[4] = MAX
dp[5] = 1

for i in range(6,n+1):
    if dp[i-3] == MAX and dp[i-5] == MAX:
        dp[i] = MAX
    else:
        dp[i] = min(dp[i-3], dp[i-5]) + 1

if dp[n] == MAX:
    print(-1)
else:
    print(dp[n])


# GREEDY
# cnt = 0
# while n >= 0:
#     if n % 5 == 0:          # 5로 나눠떨어지면 5kg만으로 구성됨
#         cnt += (n // 5)
#         print(cnt)
#         break
#     n -= 3                  # 3kg 1봉지 추가
#     cnt += 1
# else:
#     print(-1)