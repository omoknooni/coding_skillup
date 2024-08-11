import sys
n = int(input())

points = []
for i in range(n):
    x,y = map(int, sys.stdin.readline().split())
    points.append([x,y])

points.sort()

for i in points:
    print(*i)