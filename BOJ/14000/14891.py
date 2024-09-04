import sys
from collections import deque
gear = []
# N극 0, S극 1
for _ in range(4):
  gear.append(deque(list(map(int, input()))))

k = int(input())
actions = []
for _ in range(k):
  actions.append(list(map(int, sys.stdin.readline().split())))

# 왼쪽 톱니
def left(idx, r):
  # 톱니 인덱스 넘어가면 return으로 넘김
  if idx < 0:
    return
  # 타깃 톱니와 왼쪽 톱니를 비교
  if gear[idx][2] != gear[idx+1][6]:
    left(idx-1, -r)
    gear[idx].rotate(r)

# 오른쪽 톱니
def right(idx, r):
  if idx > 3:
    return
  # 타깃 톱니와 오른쪽 톱니를 비교
  if gear[idx][6] != gear[idx-1][2]:
    right(idx+1, -r)
    gear[idx].rotate(r)

# 양 끝단 톱니 인덱스(0~7) : 2,6
# 방향 1: 시계, 방향 -1: 반시계
for action in actions:
  idx = action[0]-1
  rotate = action[1]

  # 반대로 돌아가므로 - 붙임
  left(idx-1, -rotate)
  right(idx+1, -rotate)

  gear[idx].rotate(rotate)



# 점수 계산
# 각 톱니의 0번 인덱스만 확인 (12시 방향)
# 1번톱니 2^0점, 2번 2^1점, 3번 2^2점, 4번 2^3점
answer = 0
for i,v in enumerate(gear):
  if v[0] == 1:
    answer += 2**i
print(answer)