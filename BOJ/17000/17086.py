import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int, input().split())

field = []
shark = deque([])
for i in range(n):
  line = list(map(int, input().split()))
  for j in range(m):
    if line[j] == 1:
      shark.append([i,j])
  field.append(line)

# 이동은 8방향
dt = [[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1]]

# # 각 칸에 대해 가장 가까운 상어까지 거리를 탐색
# def bfs(y,x):
#   queue = deque([])
#   queue.append([y,x])
#   visited = [[0]*m for _ in range(n)]
#   visited[y][x] = 1
#   length = 0
#   is_shark = 0
#   while queue:
#     y,x = queue.popleft()
#     for d in dt:
#       ny = y + d[0]
#       nx = x + d[1]
#       if visited[ny][nx] == 0 and 0 <= ny < n and 0 <= nx < m:
#         if field[ny][nx] == 0:
#           visited[ny][nx] = visited[y][x] + 1
#           queue.append([ny,nx])
#         else:
#           is_shark = True
#           length = visited[y][x] + 1
#     if is_shark:
#       break
#   return length


# answer = 0
# for i in range(n):
#   for j in range(m):
#     if field[i][j] != 1:
#       tmp = bfs(i,j)
#       if answer < tmp:
#         answer = tmp
# print(answer)


### [각 상어 지점에서] 각 칸에 대한 거리를 탐색
def bfs():
  while shark:
    y,x = shark.popleft()
    for d in dt:
      ny = y + d[0]
      nx = x + d[1]
      if 0 <= ny < n and 0 <= nx < m:
        # 상어에 인접한 칸부터 하나씩 거리를 늘리며, 탐색하지 않은 칸에 한해서 수를 늘림
        if field[ny][nx] == 0:
          field[ny][nx] = field[y][x] + 1
          shark.append([ny,nx])

bfs()
answer = 0
for i in range(n):
  for j in range(m):
    answer = max(answer, field[i][j])

# 상어지점의 값이 1이므로
print(answer-1)