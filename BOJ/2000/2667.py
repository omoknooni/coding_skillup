import sys

n = int(input())
d_map = []
for i in range(n):
    d_map.append(list(map(int,sys.stdin.readline().strip())))

# bfs
def bfs(y,x):
    queue = [[y,x]]
    size = 1
    d_map[y][x] = 0
    while queue:
        y, x = queue.pop(0)
        for dy, dx in [[1,0],[0,1],[-1,0],[0,-1]]:
            next_y, next_x = y+dy, x+dx
            if 0 <= next_x < n and 0 <= next_y < n:
                if d_map[next_y][next_x] == 1:

                    # 지나갈 곳은 0 처리
                    d_map[next_y][next_x] = 0
                    size += 1
                    queue.append([next_y,next_x])
    return size

danji = []

# 모든 원소를 순회, bfs에서 이미 지나간 곳은 0이므로 남은 구역에서 1인 곳을 찾아서 bfs를 수행
for i in range(n):
    for j in range(n):
        if d_map[i][j] == 1:
            danji.append(bfs(i,j))
print(len(danji))
for i in sorted(danji):
    print(i)