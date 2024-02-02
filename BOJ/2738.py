import sys
n, m = map(int, input().split())

mat_a = [[0]*m for _ in range(n)]
mat_b = [[0]*m for _ in range(n)]
mat_sum = [[0]*m for _ in range(n)]

for i in range(n):
    mat_a[i] = list(map(int, sys.stdin.readline().split()))

for i in range(n):
    mat_b[i] = list(map(int, sys.stdin.readline().split()))

for i in range(n):
    for j in range(m):
        mat_sum[i][j] = mat_a[i][j] + mat_b[i][j]
    print(*mat_sum[i])