import sys
from bisect import bisect_left
input = sys.stdin.readline

m,n,l = map(int, input().split())
point = list(map(int,input().split()))
point.sort()

# animal -> point 방향
answer = 0
for _ in range(n):
  x,y = map(int, input().split())

  if y <= l:
    # 가장 x값이 작은 사로와 동물 거리 비교
    if x <= point[0]:
      if point[0]-x+y <= l:
        answer += 1
    # 가장 x값이 큰 사로와 동물 거리 비교
    elif x >= point[-1]:
      if x-point[-1]+y <= l:
        answer += 1
    # 이진탐색을 해야하는 경우
    else:
      idx = bisect_left(point, x)
      # idx-1값도 봐야하는 이유? => 왼쪽 인덱스가 더 가까울 수 있기에
      # bisect_right를 쓰면 오른쪽 인덱스를 확인
      if (abs(point[idx]-x)+ y <= l) or (abs(point[idx-1]-x)+ y <= l):
        answer += 1


  ### Solution 2
  # # abs(point[idx]-x)+y = l, 동물을 잡을 수 있는 지점의 최대/소
  # point_min = x+y-l # x-point[idx]+y=l
  # point_max = x-y+l # point[idx]-x+y=l

  # while left <= right:
  #   mid = (left+right) // 2
  #   if point_min <= point[mid] <= point_max:
  #     answer += 1
  #     break
  #   # 이 사로에서 동물을 못잡고(point[mid] < point_min), 최대지점보다 작은 경우 
  #   elif point[mid] < point_max:
  #     left = mid + 1
  #   else:
  #     right = mid -1

print(answer)