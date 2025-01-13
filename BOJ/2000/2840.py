from collections import deque

n,k = map(int,input().split())
result = []
for _ in range(k):
    s,c = map(str, input().split())
    result.append([int(s), c])

wheel = deque(['?']*n)

for i in range(k):
    s,c = result[i]

    # 휠은 시계방향 회전, 즉 rotate는 정수방향
    wheel.rotate(s)

    # 이미 결정된 칸에 다른 값이 들어오면 충돌
    if wheel[0] == '?' or wheel[0] == c:
        wheel[0] = c
    else:
        print('!')
        exit()

    # 바퀴에 같은 글자가 여러개 존재하지 않음
    if wheel.count(c) != 1:
        print('!')
        exit()

print(*list(wheel), sep='')

