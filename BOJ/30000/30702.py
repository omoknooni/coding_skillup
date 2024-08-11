import sys
n,m = map(int, input().split())
flag_a = [['x']] * n
flag_b = [['x']] * n

visited_a = [[0] * m] * n
visited_b = [[0] * m] * n

for i in range(n):
    flag_a[i] = list(sys.stdin.readline().strip())

for i in range(n):
    flag_b[i] = list(sys.stdin.readline().strip())

# flag_a와 flag_b를 각각 bfs 탐색
def bfs(y,x):
    queue = [[y,x]]
    visited_a[y][x] = 1
    while queue:
        ny,nx = queue.pop(0)
        for dy, dx in [[1,0],[0,1],[-1,0],[0,-1]]:
            next_y, next_x = ny+dy, nx+dx
            if 0 <= next_x < m and 0 <= next_y < n:
                if not visited_a[next_y][next_x] and flag_a[ny][nx] == flag_a[next_y][next_x]:
                    visited_a[next_y][next_x] = 1
                    queue.append([next_y, next_x])

    queue = [[y,x]]
    visited_b[y][x] = 1
    while queue:
        ny,nx = queue.pop(0)
        for dy, dx in [[1,0],[0,1],[-1,0],[0,-1]]:
            next_y, next_x = ny+dy, nx+dx
            if 0 <= next_x < m and 0 <= next_y < n:
                if not visited_b[next_y][next_x] and flag_b[ny][nx] == flag_b[next_y][next_x]:
                    visited_b[next_y][next_x] = 1
                    queue.append([next_y, next_x])

def compare():
    for i in range(n):
        for j in range(m):
            if visited_a[i][j]:
                if visited_a[i][j] != visited_b[i][j]:
                    return False
    return True


answer = True
for i in range(n):
    for j in range(m):
        # visited 영역 초기화
        visited_a = [[0] * m] * n
        visited_b = [[0] * m] * n
        
        bfs(i,j)
        if not compare():
            answer = False
            break
if answer:
    print("YES")
else:
    print("NO")