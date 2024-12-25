from collections import deque
import sys
input = sys.stdin.readline

n,k = map(int, input().split())

step = 1
belt = deque(list(map(int, input().split())))
robot = deque([False]*n)    # 1~n까지만 로봇이 있을수있음

while True:
    # 벨트 회전
    belt.rotate(1)
    robot.rotate(1)
    # 내리는 자리 처리
    robot[n-1] = False

    # 로봇 이동 (0~n-1까지 벨트 중 뒷부분부터 -> 먼저올라온것이 뒤에 있으므로)
    for i in range(n-2,-1,-1):
        if robot[i] and not robot[i+1] and belt[i+1] >= 1:
            robot[i] = False
            robot[i+1] = True
            belt[i+1] -= 1

    # 내리는 자리 처리
    robot[n-1] = False

    # 올리는 자리에 올리기
    if belt[0] >= 1:
        robot[0] = True
        belt[0] -= 1

    # 종료 조건 검사
    if belt.count(0) >= k:
        break

    # 단계 증가
    step += 1

print(step)    