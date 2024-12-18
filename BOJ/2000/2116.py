import sys
input = sys.stdin.readline

n = int(input())
dices = []
for _ in range(n):
    dices.append(list(map(int, input().split())))

# 주사위 반대면
# a-f / b-d / c-e
# a b c d e f
# 0 1 2 3 4 5
aside = [5,3,4,1,2,0]
max_sum = 0

# 0번째 주사위의 가장 위 숫자를 1~6까지 조절하며 비교
for i in range(1,7):
    tmp = 0
    for d in range(n):
        if d == 0:
            top = i
        bottom_idx = dices[d].index(top)
        top_idx = aside[bottom_idx]
        top = dices[d][top_idx]
        bottom = dices[d][bottom_idx]

        # 위아래 제외 나머지 4면 중 가장 큰값
        side = [x for x in range(1,7)]
        side.remove(top)
        side.remove(bottom)
        tmp += max(side)

    max_sum = max(max_sum, tmp)

print(max_sum)