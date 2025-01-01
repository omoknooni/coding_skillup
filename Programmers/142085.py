from heapq import heappush, heappop 

def solution(n, k, enemy):
    # 무적권 갯수가 적보다 많으면 그냥 무적권만 써서 끗
    if k >= len(enemy):
        return len(enemy)
    hq = []
    for i,v in enumerate(enemy):
        # enemy 순회하면서 힙에 넣기 (최소 힙)
        heappush(hq, v)
        
        # 힙 길이가 k가 넘어가는 경우(무적권 갯수를 초과하는 경우), pop해서 최소값부터 빼줌
        if len(hq) > k:
            n -= heappop(hq)
            
        # 인원 없으면 끗
        if n < 0:
            return i
    # 모든 라운드 커버되는 경우
    return len(enemy)