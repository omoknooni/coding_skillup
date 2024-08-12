import sys
n, m = map(int, input().split(" "))
trees = list(map(int, sys.stdin.readline().split(" ")))

height = m
left, right = 0, max(trees)

while left <= right:
  mid = (left + right) // 2
  tmp = 0
  for t in trees:
    if t > mid:
      tmp += (t-mid)
  if tmp < m:
    right = (mid-1)
  else:
    height = mid
    left = (mid+1)

print(height)

## Counter, 빠른 탐색
from collections import Counter
n,m = map(int, input().split(" "))
trees = Counter(map(int, sys.stdin.readline().split(" ")))

height = m
left, right = 0, max(trees.keys())

while left <= right:
  mid = (left + right) // 2
  tmp = 0
  for t in trees:
    if t > mid:
      tmp += ((t-mid) * trees[t])
  if tmp < m:
    right = (mid-1)
  else:
    height = mid
    left = (mid+1)
print(height)