import sys
from collections import deque

m,n = map(int, sys.stdin.readline().split(" "))
boxes = []
for i in range(n):
    boxes.append(list(map(int, sys.stdin.readline().split(" "))))

queue = deque()     # 단순 list보다 빠르게 값 넣고 빼기 위해 deque
for i in range(n):
    for j in range(m):
        if boxes[i][j] == 1:
            queue.append([i,j])

while queue:
    y,x = queue.popleft()
    for dy, dx in [[1,0],[0,1],[-1,0],[0,-1]]:
        new_x = x + dx
        new_y = y + dy
        if 0 <= new_x < m and 0 <= new_y < n and boxes[new_y][new_x] == 0:
            boxes[new_y][new_x] = boxes[y][x] + 1           # 이전 값에서 1씩 늘려 날짜를 기록
            queue.append([new_y,new_x])


# bfs 탐색 후, 안익은게 있는 칸 체크 후 답 도출
answer = 0
for i in boxes:
    for j in i:
        if j == 0:
            print(-1)
            exit()
    answer = max(answer,max(i))     # 각 row에서 가장 큰 값을 찾아 answer와 비교, 각 원소를 단순비교하면 time out

print(answer-1)