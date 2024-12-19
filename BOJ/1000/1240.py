from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b,d = map(int, input().split())

    # 노드간 연결이 주어지면 항상 두 노드 모두 간선정보 삽입
    tree[a].append([b,d])
    tree[b].append([a,d])

def bfs(src, dst):
    visited = [0]*(n+1)
    queue = deque()
    queue.append([src,0])
    visited[src] = 1
    while queue:
        node, d = queue.popleft()

        if node == dst:
            return d

        for i,j in tree[node]:
            if not visited[i]:
                visited[i] = 1
                queue.append([i,j+d])


for case in range(m):
    src, dst = map(int, input().split())
    # 하나를 root로 잡고 dst를 탐색
    print(bfs(src,dst))