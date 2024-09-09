import sys
from itertools import combinations
n,m = map(int,sys.stdin.readline().split())

cities = []
houses = []
chickens = []
for i in range(n):
  line = list(map(int, sys.stdin.readline().split()))
  cities.append(line)
  for j,v in enumerate(line):
    if v == 1:
      houses.append([i,j])
    elif v == 2:
      chickens.append([i,j])

comb = combinations(chickens, m)      # m개의 치킨집에 대한 조합
answer = 1e9
for c in comb:
  tmp = 0                             # tmp = 각 치킨집 조합에서 도시치킨거리
  for h in houses:
    d = 1e9                           # d = 한 집에서의 치킨거리
    for i in c:
      d = min(d,abs(h[0]-i[0])+abs(h[1]-i[1]))    # 집에서 각 지점별로 거리가 최소가되는 지점의 거리를 갱신해감
    tmp += d
  answer = min(answer, tmp)     # 각 치킨집 조합에 대해 도시치킨거리를 최솟값으로 갱신해감

print(answer)

### 백트래킹
visited = [False] * len(chickens)
min_val = int(1e9)

def dfs(idx, cnt):
  global min_val
  # m개 선정한 경우, 선정한 닭집에 대해 치킨거리 계산
  if cnt == m:
    ans = 0
    for h in houses:
      d = int(1e9)
      for c in range(len(visited)):
        if visited[c]:
          chick_d = abs(h[0]-chickens[c][0]) - abs(h[1]-chickens[c][1])
          d = min(d,chick_d)
      ans += d
    min_val = min(min_val, ans)
    return

  for i in range(idx, len(chickens)):
    if not visited[i]:
      # 백트래킹, 닭집을 선정하는 경우를 각각 계산
      visited[i] = True
      dfs(idx+1, cnt+1)
      visited[i] = False


dfs(0,0)