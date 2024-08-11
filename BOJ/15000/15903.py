import sys
from collections import deque

n,m = map(int, input().split( ))
cards = list(map(int, sys.stdin.readline().split( )))

# 작은 수 2개 뽑아서 그 값을 두 수 합으로 바꾸고 덱에 추가
### deque
if m == 0:
    print(sum(cards))
else:
    for i in range(m):
        cards.sort()
        card_deque = deque(cards)

        a = card_deque.popleft()
        b = card_deque.popleft()
        for _ in range(2):
            card_deque.append(a+b)
        cards = list(card_deque)
        
    print(sum(card_deque))

### heapq
import heapq

# heapify로 최소 힙 정렬됨
heapq.heapify(cards)

for i in range(m):
    a = heapq.heappop(cards)
    b = heapq.heappop(cards)
    for _ in range(2):
        heapq.heappush(cards,a+b)

print(sum(cards))