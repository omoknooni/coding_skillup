from collections import deque

def solutions(land):
    answer = 0
    n,m = len(land), len(land[0])
    visited = [[False]*m for _ in range(n)]

    # 각 열 별로 얻는 기름양
    gain = [0]*m

    def bfs(y,x):
        dt = [[-1,0],[0,1],[1,0],[0,-1]]
        cnt = 1

        # 기름이 있는 열을 저장하기 위한 set -> 중복을 없앨수 있음
        oil = set()
        oil.add(x)
        
        q = deque()
        q.append([y,x])
        visited[y][x] = True
        while q:
            y,x = q.popleft()
            for d in dt:
                ny, nx = y+d[0], x+d[1]
                if (0 <= ny < n) and (0 <= nx < m):
                    if not visited[ny][nx] and land[ny][nx] == 1:
                        visited[ny][nx] = True
                        q.append([ny,nx])
                        oil.add(nx)
                        cnt += 1        # 한 덩이의 석유량 계산

        # 기름이 있는 열에 한 덩이 석유량 추가
        for o in oil:
            gain[o] += cnt

    # 모든 칸 순회하면서 기름있는 한 덩이를 bfs 계산
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and not visited[i][j]:
                bfs(i,j)

    # 얻는 것은 한 열 시추에 최대 기름량
    answer = max(gain)