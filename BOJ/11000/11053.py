import sys

n = int(input())
sequence = list(map(int, sys.stdin.readline().split()))

dp = [0 for _ in range(n)]
for i in range(n):
    for j in range(len(sequence[:i])):
        if sequence[i] > sequence[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1
print(max(dp))



## [10, 20, 2, 5, 3, 8, 8, 25, 6] 같이 정답이 중간부터 시작하는 수열의 경우는 아래와 같은 비교는 실패
# dp = []
# length = 1
# for idx, val in enumerate(sequence):
#     if idx >= 1:
#         if val > dp[idx-1]:
#             dp.append(val)
#             length += 1
#         else:
#             dp.append(dp[idx-1])
#     else:
#         dp.append(val)
# print(length)
