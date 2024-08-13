import sys

n,s = map(int, input().split())
numbers = list(map(int, sys.stdin.readline().split(" ")))
tmp = 0
left, right = 0,0

# 최소 합의 '길이' -> 길이 값을 줄이며
answer = 1e9
while True:
  # 부분합이 s 이상이면, 부분합 배열의 길이 파악 후 좌측을 줄여 짧은 길이 탐색
  if tmp >= s:
    answer = min(answer, right-left)
    tmp -= numbers[left]
    left += 1

  # 부분합이 s에 도달하지 못하면 길이를 늘려 s에 도달하도록 탐색
  else:
    if right == n:
      break
    tmp += numbers[right] 
    right += 1

# 모든 수에 대해 탐색했음에도 모든 합이 s를 못넘으면 0
if answer == 1e9:
  print(0)
else:
  print(answer)