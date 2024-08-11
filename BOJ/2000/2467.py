import sys

n = int(sys.stdin.readline())
values = list(map(int, sys.stdin.readline().split(" ")))

point = 2000000001
left = 0
right = n-1
answer = [left,right]

while left < right:
    tmp = values[left] + values[right]
    if abs(tmp) < abs(point):
        point = tmp
        answer = [left, right]
        if tmp == 0:
            break

    if tmp > 0:
        right -= 1
    else:
        left += 1
print(f"{values[answer[0]]} {values[answer[1]]}")
    