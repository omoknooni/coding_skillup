import sys

n = int(input())
nations = list(map(int, sys.stdin.readline().split(" ")))
total_cost = int(input())
left, right = 0, max(nations)
answer = 0

while left <= right:
    mid = (left + right) // 2
    tmp = 0
    for i in nations:
        if i >= mid:
            tmp += mid
        else:
            tmp += i

    # mid를 임계값으로 잡고 계산한 지출액이 전체예산보다 작은(아직 여유가 있는)경우, left범위를 우측으로 줄임
    if tmp <= total_cost:
        answer = mid
        left = mid + 1
    # 계산한 지출액이 전체예산보다 크면 이 임계값은 채택될 수 없음, right범위를 좌측으로 줄임
    else:
        right = mid - 1

print(answer)