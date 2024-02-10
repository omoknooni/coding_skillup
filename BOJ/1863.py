import sys
n = int(input())

points = []
for i in range(n):
    x,y = map(int, sys.stdin.readline().split())
    points.append([x,y])

stack = [0]     # 이전 빌딩 높이 기록용 stack
answer = 0
for p in points:
    if stack[-1] < p[1]:        # 이전 빌딩이 현재 빌딩보다 낮은 경우
        answer += 1
        stack.append(p[1])
    else:                       # 이전 빌딩이 현재 빌딩보다 높은 경우
        while stack[-1] > p[1]:
            t = stack.pop()         # 이전 빌딩의 높이가 높아질때까지 stack pop
        if stack[-1] < p[1]:
            answer += 1
            stack.append(p[1])
print(answer)