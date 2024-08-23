import sys
from collections import deque
n = int(input())
tree = {x: [] for x in range(1,n+1)}

# tree 생성
for _ in range(n-1):
  p1, p2 = map(int, sys.stdin.readline().split())
  tree[p1].append(p2)
  tree[p2].append(p1)

# BFS로 트리를 루트부터 탐색
visited = [0] * (n+1)
stk = deque([1])
while stk:
  node = stk.popleft()
  for i in tree[node]:
    if not visited[i]:
      # visited 인덱스에 해당하는 값에 루트 노드 번호를 삽입 -> 해당 인덱스번호 노드의 부모노드 번호를 알 수 있음
      visited[i] = node
      stk.append(i)

for i in visited[2:]:
  print(i)