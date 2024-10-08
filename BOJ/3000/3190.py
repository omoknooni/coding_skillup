import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
k = int(input())

# 4방향 / (y,x) / 우,하,좌,상
dt = [[0,1],[1,0],[0,-1],[-1,0]]
field = [[0]*n for _ in range(n)]

# 사과 입력 / -1로 표기
for _ in range(k):
  y,x = map(int, input().split())
  field[y-1][x-1] = -1

l = int(input())
info = deque([])
for _ in range(l):
  info.append(list(map(str, input().split())))


snake = deque([[0,0]])
y,x = 0,0
field[y][x] = 1
d = 0
answer = 0
change = info.popleft()
while True:
  answer += 1
  ny = y + dt[d][0]
  nx = x + dt[d][1]

  # 다음칸이 벽이나 몸통이면 끝
  if ny<0 or ny>=n or nx<0 or nx>=n:
    break
  elif field[ny][nx] > 0:
    break
  else:
    # 다음칸에 사과 있으면
    if field[ny][nx] == -1:
      # 꼬리 그대로
      pass
    else:
      # 이동에 따른 꼬리 비우기
      tail = snake.popleft()
      field[tail[0]][tail[1]] = 0

    # 머리의 이동
    field[ny][nx] = answer
    snake.append([ny,nx])
    y,x = ny,nx

    # 해당 시간에 회전 정보가 있으면 회전
    if answer == int(change[0]):
      if change[1] == "D":
        d = (d+1) % 4
      else:
        d = (d+3) % 4
      if info:
        change = info.popleft()
print(answer)