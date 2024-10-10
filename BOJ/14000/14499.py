import sys
input = sys.stdin.readline
n,m,y,x,k = map(int, input().split())

field = []
for i in range(n):
  l = list(map(int, input().split()))
  field.append(l)

action = list(map(int, input().split()))
answer = []

dice = [0,0,0,0,0,0]
# 굴려서 변화하는 주사위를 직접 계산
def roll(move):
  if move == 1:
    dice[0],dice[1],dice[2],dice[3],dice[4],dice[5] = dice[3],dice[1],dice[0],dice[5],dice[4],dice[2]
  elif move == 2:
    dice[0],dice[1],dice[2],dice[3],dice[4],dice[5] = dice[2],dice[1],dice[5],dice[0],dice[4],dice[3]
  elif move == 3:
    dice[0],dice[1],dice[2],dice[3],dice[4],dice[5] = dice[4],dice[0],dice[2],dice[3],dice[5],dice[1]
  elif move == 4:
    dice[0],dice[1],dice[2],dice[3],dice[4],dice[5] = dice[1],dice[5],dice[2],dice[3],dice[0],dice[4]


# 동:1 / 서:2 / 북:3 / 남:4
dt = [[0,1],[0,-1],[-1,0],[1,0]]
for i in range(len(action)):
  d = dt[(action[i]-1)]
  ny = y + d[0]
  nx = x + d[1]
  if 0 <= ny < n and 0 <= nx < m:
    # 이동은 굴려서
    roll(action[i])

    # 칸이 0 -> 주사위 바닥수가 칸으로
    if field[ny][nx] == 0:
      field[ny][nx] = dice[5]
    # 칸이 0이 아님 -> 바닥수가 칸수로, 칸수는 0으로
    else:
      dice[5] = field[ny][nx]
      field[ny][nx] = 0
    y,x = ny,nx
    print(dice[0])