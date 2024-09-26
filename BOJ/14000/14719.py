import sys
input = sys.stdin.readline
h,w = map(int, input().split())
world = list(map(int, input().split()))

# 블록 사이에 물이 고임
start, end = None, None
answer = 0

# 앞뒤 제외 후, 현재 지점을 기준으로 좌측/우측에서 최댓값을 구함
for i in range(1,w-1):
  start = max(world[:i])
  end = max(world[i+1:])

  # 물이 고이는 기준은 start, end 중 작은 값
  point = min(start, end)
  if world[i] < point:
    answer += (point - world[i])

# # 실패
# # 물이 고일 구역을 나누어 계산
# tmp = 0
# for i in range(w):
#   if start is None:
#     if world[i] != 0:
#       start = i
#   else:
#     if world[i] >= world[start]:
#       end = i
#       print(start, end)
#       for j in range(start+1, end):
#         tmp += (min(world[start], world[end]) - world[j])
#       answer += tmp
#       start = None
      
print(answer)