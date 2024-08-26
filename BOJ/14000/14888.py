import sys

n = int(input())
a = list(map(int, sys.stdin.readline().split()))
operators = list(map(int, sys.stdin.readline().split()))

max_val, min_val = -int(1e9), int(1e9)
def dfs(idx, operators, sum):
  global max_val, min_val
  if idx == n:
    max_val = max(max_val, sum)
    min_val = min(min_val, sum)
    return
  
  # 각 연산자를 시도하며 백트래킹
  if operators[0]:
    # operators를 매개변수로 넣을때 해당 연산자의 갯수를 줄이면서 넣어주어야함 
    # operators[0] -= 1
    dfs(idx+1, [operators[0]-1]+operators[1:], sum+a[idx])
  if operators[1]:
    dfs(idx+1, [operators[0]]+[operators[1]-1]+operators[2:], sum-a[idx])
  if operators[2]:
    dfs(idx+1, operators[:2]+[operators[2]-1]+[operators[3]], sum*a[idx])
  if operators[3]:
    dfs(idx+1, operators[:3]+[operators[3]-1], int(sum/a[idx]))
dfs(1, operators, a[0])
print(max_val)
print(min_val)