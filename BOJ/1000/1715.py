import heapq
n = int(input())

# 최소 비용을 구하기 위해서는 작은 것끼리 합쳐서 비용을 작게 만들어야함
card = []
for _ in range(n):
    heapq.heappush(card, int(input()))

# 길이가 1이면 비교할 필요가 없음
if len(card) == 1:
    print(0)
    exit(0)

tmp = 0
while len(card) > 1:
    a = heapq.heappop(card)
    b = heapq.heappop(card)

    tmp += a+b

    # 두 요소의 합(카드 뭉치)을 다시 넣어주어야함
    heapq.heappush(card, a+b)

print(tmp)