import sys

n, m = map(int, input().split())
maze = [[0]*m for _ in range(n)]

# maze 값 입력
for i in range(n):
    arr = sys.stdin.readline().strip()
    for j in range(m):
        maze[i][j] = int(arr[j])

# bfs, maze값을 그대로 이용한다. ==> 별도의 visited를 만들 필요 없음, 시간 초과
def bfs(a,b):
    queue = []
    queue.append([a-1,b-1])
    while queue:
        y, x = queue.pop(0)

        # 도착지에 도달
        if y == (n-1) and x == (m-1):
            return maze[y][x]

        # 각 지점에서 움직일 수 있는 방향 탐색        
        for dx, dy in [[1,0],[0,1],[-1,0],[0,-1]]:
            next_x, next_y = x+dx, y+dy
            # 다음 지점이 범위 안에있고, 값이 1이면 (이미 방문한 곳은 1 이상의 값, 못가는 곳은 0임)
            if 0 <= next_x < m and 0 <= next_y < n:
                if maze[next_y][next_x] == 1:
                    maze[next_y][next_x] = maze[y][x] + 1
                    queue.append([next_y, next_x])

# (1,1)에서 출발해서 (n,m)에 도달경로 탐색
print(bfs(1,1))