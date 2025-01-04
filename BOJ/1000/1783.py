n,m = map(int, input().split())
answer = 0
# 세로사이즈가 1이면 이동 불가
if n == 1:
    answer = 1
# 2면 2,3번 방법만 가능, 4번 이상 이동할 수 X
elif n == 2:
    answer = min(4, (m+1) // 2)
# n이 3이상 부터는 4가지 방법 모두사용 가능. m이 7보다 작으면 최대 4칸까지만 가능
elif m < 7:
    answer = min(4,m)
# 나머지는 이동방법 제한 없으니까 오른쪽 1칸씩 먹으면서 이동하는게 최대
else:
    answer = m-2

print(answer)




# 사이즈가 최대 20억, 탐색하면 초과남
# import copy
# field = [[False]*m for _ in range(n)]
# field[n][0] = True
# # 이동 방법 4가지
# move = [[-2,1],[-1,2],[1,2],[2,1]]
# # 이동 횟수 >= 4 : 4가지 이동 다 해야함

# def dfs(cnt, field):
#     tmp = copy.deepcopy(field)
#     for m in move:
#         ny = y + m[0]
#         nx = x + m[1]
#         tmp[ny][nx] = True
#         dfs(cnt+1, tmp)

# answer = 0
# dfs(0,field)