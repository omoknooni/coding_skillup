import sys
input = sys.stdin.readline

n,m,l = map(int, input().split())

if n == 0:
    if l % (m+1) == 0:
        print(l // (m+1))
    else:
        print(l // (m+1) +1)
else:
    service = list(map(int, input().split()))
    service.sort()
    service = service + [l]

    # n개의 휴개소 구간 거리
    interval = []
    tmp = 0
    for i in service:
        interval.append(i-tmp)
        tmp = i

    # 최대 구간 거리를 기준으로 이진 탐색
    # 최대거리를 기준으로 몇개를 배치할 수 있는가를 확인
    left = 1
    right = l-1
    while left <= right:
        mid = (left + right) // 2
        cnt = 0
        for i in interval:
            if i > mid:
                # 1을 빼는 이유? > 구간 양 끝에 원래 배치된 곳에는 배치가 안되므로
                cnt += (i-1) // mid
        
        # 배치한 갯수가 모자란 경우, 최대 구간 거리를 줄여야함
        if cnt <= m:
            right = mid -1
            answer = mid
        # 배치한 갯수가 큰 경우, 최대 구간거리를 늘려야함
        else:
            left = mid + 1
    print(answer)