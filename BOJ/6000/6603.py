import sys
from collections import deque
from itertools import combinations

case = []
subset = deque()
numbers = 1
while (numbers != 0):
  subset = deque(map(int, sys.stdin.readline().split(" ")))
  numbers = subset.popleft()
  if numbers != 0:
    case.append(list(subset))

# 집합 S에 대해 6개를 조합하는 경우를 모두 출력
for idx, c in enumerate(case):
  comb = combinations(c, 6)
  for i in comb:
    print(*i)
  if idx < len(case) - 1:
    print("")