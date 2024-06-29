from collections import deque

n,k = map(int, input().split())

queue = deque([n])
visited = [-1] * 100001      # 이동할 수 있는 좌표공간은 0<=x<=100000
visited[n] = 0
path = [-1] * 100001            # 이동 경로 체크를 위함
path[n] = n

# 현재 위치부터 타겟(처음 출발지 n)까지 경로를 역연산
def get_routes(target, cur, path):
    routes = []
    while cur != target:
        routes.append(cur)
        cur = path[cur]
    routes.append(target)
    return routes

while queue:
    pos = queue.popleft()
    if pos == k:
        routes = get_routes(n,k, path)
        print(len(routes)-1)
        print(*routes[::-1])
    for next_pos in (pos*2, pos-1, pos+1):          # 갈 수 있는 가짓 수는 3개
        if 0 <= next_pos <= 100000 and visited[next_pos] == -1:
            visited[next_pos] = visited[pos] + 1
            queue.append(next_pos)
            path[next_pos] = pos                    # path[다음 경로] = 현재 경로 로 경로 추적