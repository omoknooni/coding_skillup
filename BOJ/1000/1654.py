import sys

k,n = map(int,input().split())
cables = [int(input()) for _ in range(k)]

def length_search(cables, left, right, res):
    if left > right:
        return res
    mid = (left + right) // 2
    
    cnt = 0
    for i in cables:
        cnt += (i // mid)

    if cnt >= n:
        return length_search(cables, mid+1, right, mid)
    else:
        return length_search(cables, left, mid-1, res)

longest = max(cables)
print(length_search(cables, 1, longest, 0))
