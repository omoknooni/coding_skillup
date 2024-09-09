import sys
n,m = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))
numbers.sort()
answer = []

### 백트래킹
def back():
  if len(answer) == m:
    print(*answer)
    return
  for i in range(n):
    # 백트래킹
    if numbers[i] not in answer:
      answer.append(numbers[i])
      back()
      answer.pop()

back()

### Permutation
# from itertools import permutations
# for i in permutations(numbers, m):
#   print(*i)