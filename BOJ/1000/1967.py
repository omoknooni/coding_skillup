import sys
from itertools import combinations
sys.setrecursionlimit(10**9)

n = int(input())
graph = {x:[] for x in range(1,n+1)}

# 트리를 dictionary로 구현
for _ in range(n-1):
  p, c, d = map(int, sys.stdin.readline().split())
  graph[p].append([c,d])
  graph[c].append([p,d])

# visited에는 start로부터의 가중치합이 들어감
def dfs(start, weight):
  for next, cost in graph[start]:
    if visited[next] == -1:
      visited[next] = weight + cost
      dfs(next, visited[next])

# 한 점에서 가장 먼 지점은 항상 끝 노드, 즉 한 지점에서 가장 먼 점(point)을 찾고, 그 점에서 가장 먼점을 찾으면 그 거리가 지름
# 총 2번의 탐색
visited = {x: -1 for x in range(1,n+1)}
dfs(1,0)
point = max(visited, key=visited.get)

# n=1인 경우도 있음, 이 경우 트리 지름은 0
visited = {x: -1 for x in range(1,n+1)}
visited[point] = 0
dfs(point, 0)

print(max(visited.values()))