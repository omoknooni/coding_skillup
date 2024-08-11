import sys
n,m = map(int, input().split(" "))

field = [[0] * m for i in range(n)]
for i in range(n): 
    field[i] = list(map(int, sys.stdin.readline().split(" ")))

def bfs(y,x):
    visited = [[False]*m for i in range(n)]
    queue = [[y,x]]
    visited[y][x] = True
    while queue:
        y,x = queue.pop(0)
        for dy, dx in [[-1,0],[0,-1],[1,0],[0,1]]:
            next_y, next_x = y+dy, x+dx
            if 0 <= next_y < n and 0 <= next_x < m and not visited[next_y][next_x]:
                if field[next_y][next_x] >= 1:      # 다음 위치가 치즈 칸이면
                    field[next_y][next_x] += 1      # 치즈 칸에 닿는 공기칸이 +1 
                else:
                    queue.append([next_y,next_x])
                    visited[next_y][next_x] = True


def melting():
    is_melted = False
    for i in range(n):
        for j in range(m):
            if field[i][j] >= 3:        # 해당 치즈 공간에 닿는 공기칸이 2개 이상인 경우
                field[i][j] = 0         # 녹음 처리
                is_melted = True
            elif field[i][j] >= 2:
                field[i][j] = 1         # 녹지 않은 치즈는 카운트를 다시 원래대로
    return is_melted

time = 0
while True:
    bfs(0,0)

    if melting():
        time += 1
    else:                               # 녹일게 없으면 끝
        print(time)
        break