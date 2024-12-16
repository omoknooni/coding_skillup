import sys
from collections import deque
input = sys.stdin.readline

test_case = int(input())


# 벌레 이동 범위 탐색
def bfs(y,x):
    queue = deque([[y,x]])
    field[y][x] = 0
    while queue:
        y,x = queue.popleft()
        for dy,dx in [[-1,0],[0,1],[1,0],[0,-1]]:
            ny = y + dy
            nx = x + dx
            if 0 <= ny < n and 0 <= nx < m:
                if field[ny][nx] == 1:
                    field[ny][nx] = 0
                    queue.append([ny,nx])


for t in range(test_case):
    m,n,k = map(int, input().split())
    field = [[0]*m for _ in range(n)]

    for i in range(k):
        x,y = map(int, input().split())
        field[y][x] = 1
    
    # 탐색
    # 각 칸을 모두 탐색하되, 배추칸에서만 bfs 탐색
    cnt = 0
    for i in range(n):
        for j in range(m):
            if field[i][j] == 1:
                bfs(i,j)
                cnt += 1
    print(cnt)