import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
field = [[0]*n for _ in range(n)]

size = 2
cnt = 0
fish = []
for i in range(n):
  line = list(map(int, input().split()))
  for j in range(n):
    if line[j] == 9:
      y,x = i,j
      line[j] = 0
  field[i] = line

# 상어 지점부터 각 물고기까지 거리 계산
def bfs(y,x):
  q = deque([[y,x]])
  dt = [[1,0],[0,-1],[-1,0],[0,1]]
  visited = [[-1]*n for _ in range(n)]
  visited[y][x] = 0
  while q:
    y,x = q.popleft()
    for d in dt:
      ny = y + d[0]
      nx = x + d[1]
      if 0 <= ny < n and 0 <= nx < n:
        if visited[ny][nx] == -1 and size >= field[ny][nx]:
          visited[ny][nx] = visited[y][x] + 1
          q.append([ny,nx])
  
  # 먹을 물고기 탐색
  d = 1e9
  for i in range(n):
    for j in range(n):
      # 빈칸이 아니고 자기보다 작으며, 기존 거리보다 짧을 경우 갱신 
      if visited[i][j] != -1 and 1 <= field[i][j] < size:
        if visited[i][j] < d:
          y,x = i,j
          d = visited[i][j]

  # 먹을 물고기를 못찾음
  if d == 1e9:
    return False
  # 먹을 물고기의 위치
  else:
    return [y,x,d]

time = 0
while True:
  # 이동
  result = bfs(y,x)
  if not result:
    print(time)
    break
  else:
    # 탐색한 물고기위치에 가서 먹음
    y, x = result[0], result[1]
    time += result[2]
    field[y][x] = 0
    cnt += 1

  # 사이즈 체크, 일정량을 먹어서 사이즈 증가
  if size == cnt:
    size += 1
    cnt = 0
