import sys, heapq
n = int(input())
max_heap, min_heap = [], []
answer = []

for i in range(n):
    number = int(sys.stdin.readline())

    # 최대 힙과 최소 힙 2가지를 사용해서 중앙값을 탐색
    # 최대 힙 : 값이 내림차순 정렬, 최소 힙 : 값이 오름차순 정렬
    # 두 힙의 길이가 같도록 하나씩 번갈아가며 값을 입력
    if len(max_heap) == len(min_heap):
        heapq.heappush(max_heap, -number)
    else:
        heapq.heappush(min_heap, number)

    # 각 힙의 Root 노드의 값을 비교 -> 최대 힙의 루트는 최댓값, 최소힙의 루트는 최솟값이 됨
    # 즉, [최대 힙의 루트가 최소 힙의 루트보다 작도록]만 하면 모든 원소 비교할 것 없이 정렬이 됨
    # 값 교체 시 부호 주의, 최대 힙은 음수를 넣어서 정렬한 것
    if max_heap and min_heap and -max_heap[0] > min_heap[0]:
        tmp1 = -heapq.heappop(max_heap)
        tmp2 = heapq.heappop(min_heap)
        heapq.heappush(min_heap, tmp1)
        heapq.heappush(max_heap, -tmp2)
    
    # 홀수 개인 경우, 중앙의 값(max_heap이 1개 더많음)
    # 짝수 개인 경우 중앙의 두 값중 작은 것(두 힙의 루트 중 작은 것은 항상 max_heap[0])
    answer.append(-max_heap[0])
for i in answer:
    print(i)