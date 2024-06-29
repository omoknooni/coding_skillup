from collections import deque

n,k = map(int, input().split())

queue = deque([n])
visited = [-1] * 100001      # 이동할 수 있는 좌표공간은 0<=x<=100000
visited[n] = 0

while queue:
    pos = queue.popleft()
    if pos == k:
        print(visited[pos])
    for next_pos in (pos*2, pos-1, pos+1):          # 갈 수 있는 가짓 수는 3개
        if 0 <= next_pos <= 100000 and visited[next_pos] == -1:
            if next_pos == (pos*2):
                visited[next_pos] = visited[pos]
                queue.appendleft(next_pos)      # 순간이동은 cost가 0이라 우선탐색
            else:
                visited[next_pos] = visited[pos] + 1
                queue.append(next_pos)