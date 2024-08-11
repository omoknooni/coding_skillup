n = int(input())
p1, p2 = map(int, input().split())
m = int(input())
relations = []
for _ in range(m):
    parent, child = map(int, input().split())
    relations.append([parent, child])

# 그래프 dictionary
graph = {i:[] for i in range(n+1)}
for rel in relations:
    graph[rel[0]].append(rel[1])
    graph[rel[1]].append(rel[0])

visited = [False] * (n+1)

# 출발 노드를 p1으로 하고 p2를 탐색 (DFS)
def dfs(node, cnt):
    visited[node] = cnt
    if node == p2:
        visited[node] = cnt
    for i in graph[node]:
        if not visited[i]:
            visited[i] = cnt+1
            dfs(i,cnt+1)

dfs(p1, 0)

# BFS
from collections import deque
def bfs(node):
    queue = deque([node])
    while queue:
        now = queue.popleft()

        if now == p2:
            break

        for next in graph[now]:
            if not visited[next]:
                visited[next] = visited[now] + 1
                queue.append(next)

bfs(p1)

print(visited[p2] if visited[p2] else -1)
