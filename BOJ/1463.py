n = int(input())

M = int(1e7)
# bottom-up 방법, 역으로 연산, 1에서 n이 되는 순서로 탐색
# dp : i->연산할 숫자, dp[i]->그 숫자에 대한 최소 연산 횟수
dp = [0] * M
for i in range(2, n+1):
    dp[i] = dp[i-1]+1                       # 현재 숫자(i)는 직전 숫자에서 1을 더해서 올라올 수 있음
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)    # 현재 수가 2로 나눠떨어지면, 2로 나눈 수에서 올라오거나, 직전 수에서 1더해서 올라오는 방법 중 횟수가 적은 것 선택
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)    # 현재 수가 3으로 나눠떨어지면, 3으로 나눈 수에서 올라오거나, 직전 수에서 1더해서 올라오는 방법 중 횟수가 적은 것 선택

print(dp[n])    # n이 되는 가장 적은 연산횟수