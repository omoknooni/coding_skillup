import sys
from collections import deque
input = sys.stdin.readline

n,m,k = map(int, input().split())
field = [[5]*n for _ in range(n)]

a = []
for _ in range(n):
    a.append(list(map(int, input().split())))

tree = [[deque() for _ in range(n)] for _ in range(n)]
for i in range(m):
    x,y,l = map(int, input().split())
    tree[x-1][y-1].append(l)
dead = [[list() for _ in range(n)] for _ in range(n)]

def spring_summer():
    # 봄
    for i in range(n):
        for j in range(n):
            for k in range(len(tree[i][j])):
                if field[i][j] >= tree[i][j][k]:
                    field[i][j] -= tree[i][j][k]
                    tree[i][j][k] += 1
                else:
                    for _ in range(k, len(tree[i][j])):
                        dead[i][j].append(tree[i][j].pop())
                    break

    for i in range(n):
        for j in range(n):
            while dead[i][j]:
                field[i][j] += dead[i][j].pop() // 2
    
def fall_winter():
    for i in range(n):
        for j in range(n):
            for k in range(len(tree[i][j])):
                if tree[i][j][k] % 5 == 0:
                    for l in [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]:
                        nx = i + l[0]
                        ny = j + l[1]
                        if 0 <= nx < n and 0 <= ny < n:
                            tree[nx][ny].appendleft(1)
            field[i][j] += a[i][j]

for i in range(k):
    spring_summer()
    fall_winter()

answer = 0
for i in range(n):
    for j in range(n):
        answer += len(tree[i][j])
print(answer)


# n,m,k = map(int, input().split())
# field = [[5]*n for _ in range(n)]

# a = []
# for _ in range(n):
#     a.append(list(map(int, input().split())))

# # 나무 정보 : x,y좌표, 나이, 생존여부
# tree = []
# for i in range(m):
#     l = list(map(int, input().split()))
#     l[0] -= 1
#     l[1] -= 1
#     l.append(True)
#     tree.append(l)
# tree.sort(key=lambda x: x[2])
# for i in range(k):
#     for l in tree:
#         # 자신의 나이만큼 양분을 먹음
#         if field[l[0]][l[1]] >= l[2]:
#             field[l[0]][l[1]] -= l[2]
            
#             # 양분 먹으면 나이 증가
#             l[2] += 1
#         # 양분을 못먹으면 죽음 -> 여름에 처리하므로 0처리
#         else:
#             l[3] = False

#     # 여름
#     for l in tree:
#         if not l[3]:
#             # 죽은 나무 나이 // 2가 해당 칸에 양분으로 추가
#             field[l[0]][l[1]] += l[2] // 2
#     tree = [l for l in tree if l[3]]

#     # 가을
#     new_tree = []
#     for l in tree:
#         if l[2] % 5 == 0:
#             for m in [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]:
#                 nx = l[0] + m[0]
#                 ny = l[1] + m[1]
#                 if 0 <= nx < n and 0 <= ny < n:
#                     new_tree.append([nx,ny,1,True])
#     tree.extend(new_tree)
#     tree.sort(key= lambda x: x[2])
            

#     # 겨울
#     for l in range(n):
#         for m in range(n):
#             field[l][m] += a[l][m]

# answer = 0
# for i in tree:
#     if i[3]:
#         answer += 1
# print(answer)