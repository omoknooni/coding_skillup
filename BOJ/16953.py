a,b = map(int,input().split())

deque = [(a,1)]
while deque:
    node, cnt = deque.pop(0)

    if node > b:
        continue
    if node*2 == b or node*10+1 == b:
        cnt += 1
        break
    deque.append((node*2,cnt+1))
    deque.append((node*10+1,cnt+1))

else:
    cnt = -1
print(cnt)