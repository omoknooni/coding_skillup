import sys
from collections import deque
input = sys.stdin.readline
n, w, l = map(int, input().split())

# 대기중인 트럭 / 다리 위 / 이동된 트럭
# 다리 위는 다리 길이만큼 주고 매 초마다 변경되도록 구성
bridge = deque([0]*w)
truck = deque(list(map(int, input().split())))
arrive = []

time = 0
# 모든 트럭이 반대쪽에 도착까지 반복
while len(arrive) != n:
  time += 1
  i = bridge.popleft()
  if i != 0:
    arrive.append(i)

  if truck:
    # 다리 위 무게는 L 이하
    if sum(bridge)+truck[0] <= l:
      bridge.append(truck.popleft())
    else:
      bridge.append(0)
print(time)