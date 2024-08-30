import sys
from collections import deque

n = int(input())
field = []
max_height = 0
for _ in range(n):
  row = list(map(int, sys.stdin.readline().split()))
  
  # 주어진 field에서 가장 높은 높이 -> 해당 높이까지만 탐색하면 됨 (굳이 2~100까지 필요X)
  max_height = max(max_height,max(row))
  field.append(row)

# 한 지점에서부터 안전구역을 탐색
def bfs(point, rain):
  stk = deque([point])
  visited[point[0]][point[1]] = 1
  while stk:
    node = stk.popleft()
    for dx,dy in [[0,1],[1,0],[0,-1],[-1,0]]:
      nx = node[1] + dx
      ny = node[0] + dy
      if 0 <= nx < n and 0 <= ny < n:
        if not visited[ny][nx] and field[ny][nx] > rain:
          visited[ny][nx] = 1
          stk.append([ny,nx])


result = []
# 물높이를 높이면서 안전구역 갯수 탐색
for h in range(max_height):
  cnt = 0
  visited = [[0]*n for _ in range(n)]

  # 물높이에 대한 안전구역 탐색
  for i in range(n):
    for j in range(n):
      if field[i][j] > h and not visited[i][j]:
        bfs([i,j],h)
        cnt += 1
  result.append(cnt)
print(max(result))