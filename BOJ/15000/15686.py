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