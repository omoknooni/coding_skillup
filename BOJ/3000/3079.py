import sys
input = sys.stdin.readline

n,m = map(int, input().split())
desk = []
for _ in range(n):
    desk.append(int(input()))

# 최소 : 짧은 심사대에 1명, 최대 : 오래걸리는 심사대 * 인원수
left, right = min(desk), max(desk) * m
answer = sys.maxsize

while left <= right:
    mid = (left + right) // 2

    # mid초 안에 모두 검사가능한가
    # total : 인원 수, 각 desk 별로 mid 시간안에 몇명 가능한지 구하고 더함
    total = 0
    for i in desk:
        total += mid // i

    # m명을 모두 검사할 수 있었으면, 시간을 줄임
    if total >= m:
        right = mid - 1
        answer = min(answer, mid)
    else:
        left = mid + 1
print(answer)