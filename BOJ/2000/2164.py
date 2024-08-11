from collections import deque
n = int(input())

queue = [i+1 for i in range(n)]
q = deque(queue)

while len(q) != 1:
    q.popleft()
    item = q.popleft()
    q.append(item)

print(q[0])