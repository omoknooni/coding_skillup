import sys

n, c = map(int, input().split())
house = [0] * n
for i in range(n):
    house[i] = int(sys.stdin.readline().strip())

# 이진 탐색을 위한 정렬
house.sort()
answer = 0

# 두 공유기 사이 최대거리를 구해야함
def binary_search(house, left, right):
    if left > right:
        return None
    
    # 핵심 : 두 공유기 사이 거리를 이진탐색으로 
    mid = (left + right) // 2
    router = house[0]
    router_cnt = 1

    # 이진탐색으로 구하는 최대거리를 바탕으로 일단 공유기를 배치
    for i in range(1,len(house)):
        if house[i] >= (router + mid):              # 다음 지점이 공유기설치지점 + 최대거리 보다 크면
            router = house[i]                       # 다음 지점에 공유기 설치
            router_cnt += 1
    if router_cnt >= c:                             # 설치된 공유기 갯수가 지정된 갯수보다 크면, 
        global answer
        answer = mid
        return binary_search(house, mid+1, right)   # 최대거리 탐색 구간을 큰 값으로
    else:
        return binary_search(house, left, mid-1)    # 최대거리 탐색 구간을 작은 값으로
        

binary_search(house, 1, house[-1]-house[0])
print(answer)