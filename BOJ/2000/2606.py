n = int(input())
m = int(input())

pairs = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = list(map(int, input().split()))
    pairs[a].append(b)
    pairs[b].append(a)

deque = [1]
infected = [1]
visited = [0] * (n+1)

while deque:
    node = deque.pop(0)
    for g in pairs[node]:
        if not visited[g]:
            visited[g] = 1
            deque.append(g)
            infected.append(g)

print(len(set(infected))-1, infected)