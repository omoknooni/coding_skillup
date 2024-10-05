import sys
input = sys.stdin.readline
r,c,t = map(int, input().split())

room = []
purifier = []
point = []
for i in range(r):
  row = list(map(int, input().split()))
  room.append(row)
  if row[0] == -1:
    purifier.append([i,0])
  for j,val in enumerate(row):
    # 먼지 지점 체크
    if val>0:
      point.append([i,j,val])

# 4가지 방향 : 상 / 우 / 하 / 좌
dt = [[0,-1],[1,0],[0,1],[-1,0]]

def spread():
  while point:
    y,x,v = point.pop()
    cnt = 0
    for d in dt:
      ny = y+d[1]
      nx = x+d[0]

      # 막힌 방향으로는 확산하지 않음
      if nx<0 or ny<0 or nx>=c or ny>=r:
        continue
      # 청정기로는 확산하지 않음
      if [ny,nx] in purifier:
        continue
      room[ny][nx] += (v // 5)
      cnt += 1
    room[y][x] -= (v // 5) * cnt


def flow():
  # 청정기의 상단부 / 하단부로 나누어 계산
  for i,v in enumerate(purifier):
    tmp = 0
    idx = 1
    y,x = v[0],1

    # 상단 : 우 / 상 / 좌 / 하
    if i == 0:
      while True:
        ny = y+dt[idx][1]
        nx = x+dt[idx][0]
        # 벽에 닿는 경우, 방향을 전환
        if nx == c or ny == -1 or nx == -1 or ny == r:
          idx = (idx+3) % 4
          continue
        # 공기청정기로 복귀
        if y == v[0] and x == 0:
          break
        room[y][x], tmp = tmp, room[y][x]
        y,x = ny,nx

    # 하단 : 우 / 하 / 좌 / 상
    else:
      while True:
        ny = y+dt[idx][1]
        nx = x+dt[idx][0]
        # 벽에 닿는 경우, 방향을 전환
        if nx == c or ny == -1 or nx == -1 or ny == r:
          idx = (idx+1) % 4
          continue
        # 공기청정기로 복귀
        if y == v[0] and x == 0:
          break
        room[y][x], tmp = tmp, room[y][x]
        y,x = ny,nx
    
# 시간 흐름
for _ in range(t):
  # 확산
  spread()

  # 순환
  flow()

  # 먼지위치 재확인
  for i, row in enumerate(room):
    for j, val in enumerate(row):
      if val > 0:
        point.append([i,j,val])

# 먼지 총량 계산
print(sum(point[i][2] for i in range(len(point))))