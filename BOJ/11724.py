import sys
input = sys.stdin.readline

n,m = map(int, input().split())
lines = {}
cnt = 0
visited = [0] * (n+1)

def bfs(init_node):
    deque = [init_node]
    visited[init_node] = 1
    while deque:
        node = deque.pop(0)
        for g in lines[node]:
            if not visited[g]:
                visited[g] = 1
                deque.append(g)
                

for i in range(m):
    a,b = map(int, input().split())

    # lines[a] = lines.get(a,[]) + [b]
    # lines[b] = lines.get(b,[]) + [a]

    if a not in lines:
        lines[a] = [b]
    else:
        lines[a].append(b)

    if b not in lines:
        lines[b] = [a]
    else:
        lines[b].append(a)

for i in range(1, n+1):
    if not visited[i]:
        if lines.get(i):
            bfs(i)
            cnt += 1
        else:
            visited[i] = 1
            cnt += 1
print(cnt)