import sys

n = int(input())
matrix = []
for _ in range(n):
    matrix.append(list(map(int,sys.stdin.readline().split(' '))))


# points = []
# for i in range(n):
#     for j in range(n):
#         if matrix[i][j] == 1:
#             points.append((i,j))

# print(points)
# for i in points:
#     for j in points:
#         for k in points:
#             if j[1] == k[0]:
#                 matrix[j[0]][k[1]] = 1
#                 if i[1] == j[0]:
#                     matrix[i[0]][k[1]] = 1

for transit in range(n):
    for src in range(n):
        for dst in range(n):
            if matrix[src][transit] and matrix[transit][dst]:
                matrix[src][dst] = 1


for i in matrix:
    print(*i)