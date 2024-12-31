from collections import deque

def bfs(start, end, maps):
    n, m = len(maps), len(maps[0])
    q = deque()
    dt = [[-1,0],[0,1],[1,0],[0,-1]]
    visited = [[False]*m for _ in range(n)]
    
    # 출발점 좌표 찾기
    flag = False
    for i in range(n):
        for j in range(m):
            # 출발점은 단 하나
            if maps[i][j] == start:
                visited[i][j] = True
                q.append([i,j,0])
                flag = True
                break
        if flag:
            break
                
    while q:
        y,x,t = q.popleft()

        # 도착 확인
        if maps[y][x] == end:
            return t
        
        for d in dt:
            ny = y + d[0]
            nx = x + d[1]
            
            # 벽만 못지나감
            if 0 <= ny < n and 0 <= nx < m and maps[ny][nx] != "X":
                if not visited[ny][nx]:
                    visited[ny][nx] = True
                    q.append([ny,nx,t+1])
    return -1
                
def solution(maps):
    # start -> lever
    time1 = bfs("S", "L", maps)
    
    # lever -> exit
    time2 = bfs("L", "E", maps)
    
    if time1 != -1 and time2 != -1:
        answer = time1 + time2
    else:
        answer = -1
    return answer