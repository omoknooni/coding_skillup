import sys
n,x = map(int, input().split())

days = list(map(int, sys.stdin.readline().split()))

max_count, window_sum = 0,0
max_days = 1

# window size는 고정되어있음, 리스트를 순회하며 기존 window_sum에서 앞,뒷값만 더하고 빼줘서 구함
for i in range(n-x+1):
    if i == 0:
        window_sum = sum(days[:x])
        max_count = window_sum
        continue
    window_sum = (window_sum - days[i-1] + days[i+x-1])
    
    # 기존 최댓값과 동일한 구간합인 경우 날짜에 +1
    if max_count == window_sum:
        max_days += 1

    # 현재 구간합이 존 최댓값보다 크면 갱신, 날짜값도 1로 다시 초기화 해줘야함
    elif window_sum > max_count:
        max_days = 1
        max_count = window_sum

if max_count != 0:
    print(max_count)
    print(max_days)
else:
    print("SAD")

# 0   [1 2 3] 4 5 6 7 8
# 1   1 [2 3 4] 5 6 7 8
# 2   1 2 [3 4 5] 6 7 8
# 3   1 2 3 [4 5 6] 7 8
# 4   1 2 3 4 [5 6 7] 8
# 5   1 2 3 4 5 [6 7 8]


14
42
35
51