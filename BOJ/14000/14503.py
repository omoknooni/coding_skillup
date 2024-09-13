import sys
n,m = map(int, input().split())
r,c,d = map(int, input().split())
room = []

for _ in range(n):
  room.append(list(map(int, sys.stdin.readline().split())))

# 칸이 0이면 청소안된 빈칸, 1이면 벽
# 청소하는 칸의 갯수를 구하기
cnt = 0
while True:
  # 현재칸이 청소되지 않으면, 청소(2)
  if room[r][c] == 0:
    room[r][c] = 2
    cnt += 1
  
  # 주변 4칸 계산
  dt = [[-1,0],[0,1],[1,0],[0,-1]]
  next_pt = [[r+x[0],c+x[1]] for x in dt]
  for i in next_pt:
    # 청소 안된칸이 있으면 반시계 90, 전진
    if room[i[0]][i[1]] == 0:
      # 반시계90도 회전은 0,1,2,3 값에서 1만 빼주면 됨, 0에서 1빼는 경우 3으로
      d = d-1 if d>0 else 3
      if room[r+dt[d][0]][c+dt[d][1]] == 0:
        r = r+dt[d][0]
        c = c+dt[d][1]
      break
  else:
    # 후진 가능하면 후진
    if room[r-dt[d][0]][c-dt[d][1]] != 1:
      r = r-dt[d][0]
      c = c-dt[d][1]
    # 후진 안되면 작동 중지 -> while break
    else:
      break

print(cnt)