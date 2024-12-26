n = int(input())
k = int(input())
sensors = list(map(int,input().split()))

# 집중국 갯수가 많으면 그냥 0
if n <= k:
    print(0)
else:
    sensors.sort()
    # 센서간 거리
    interval = []
    for i in range(1,len(sensors)):
        interval.append(sensors[i]-sensors[i-1])
    
    # 간격이 가장 큰 값부터 처리
    # 큰 간격을 0으로 처리 -> 큰 간격을 기준으로 집중국 영역 분리
    # 즉, 간격도 오름차순 정렬 후, 가장 큰 값을 k-1개 뺀 나머지를 합 
    interval.sort()
    print(sum(interval[:n-k]))

# 집중국의 배치 위치는 고려 X
# 집중국의 갯수만큼 묶음을 만든다
