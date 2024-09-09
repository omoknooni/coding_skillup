import sys
n,m = map(int, sys.stdin.readline().split())
answer = []

def back(idx):
  if len(answer) == m:
    print(*answer)
    return
  for i in range(idx, n+1):
    # 백트래킹
    answer.append(i)
    back(i)
    answer.pop()

back(1)