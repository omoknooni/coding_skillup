import sys
n = int(input())

table = []
for i in range(n):
    obj = list(map(int, sys.stdin.readline().split()))
    table.append(obj)

# dp : 해당 날짜부터 마지막날까지 받을수있는 최대 금액
dp = [0 for _ in range(n+1)]
for i in range(n-1, -1, -1):

    # 현재일부터 해당 날짜의 작업에 걸리는 시간이 퇴사일보다 더 걸리는 경우
    # 이 날은 일은 안한다는 선택지만 존재
    if i + table[i][0] > n:
        dp[i] = dp[i+1]
    # 일을 할 수 있고 안할 수 있는 선택지 존재
    # 일을 하는 경우 -> 해당 날짜의 보수금액 + 해당 날짜 작업의 일 수만큼 지난 날에서의 최대 금액
    else:
        dp[i] = max(dp[i+1], table[i][1]+dp[i+table[i][0]])

print(dp[0])