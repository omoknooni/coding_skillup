import sys

n, k = map(int, input().split())
days = list(map(int, sys.stdin.readline().split(' ')))

deg = []
deg.append(sum(days[:k]))
for i in range(n-k):
    deg.append(deg[i]-days[i]+days[i+k])
print(max(deg))