import sys
input = sys.stdin.readline
r,c,n = map(int, input().split())

field = []
for _ in range(r):
    line = input().strip()
    field.append(list(line))

# 짝수 초에는 모든칸이 다 채워짐
field2 = [['O']*c for _ in range(r)]

def exploded(field):
    field3 = [['O']*c for _ in range(r)]
    dt = [[-1,0],[0,1],[1,0],[0,-1]] 
    for i in range(r):
        for j in range(c):
            if field[i][j] == 'O':
                field3[i][j] = '.'
                for d in dt:
                    ni = i + d[0]
                    nj = j + d[1]
                    if (0 <= ni < r) and (0 <= nj < c):
                        field3[ni][nj] = '.'
    return field3

# 3가지 패턴이 아님, 
if n == 1:
    for i in field:
        print(*i, sep='')
elif n%2 == 0:
    for i in field2:
        print(*i, sep='')
elif n > 1 and n%4 == 3:
    field3 = exploded(field)
    for i in field3:
        print(*i, sep='')
elif n > 1 and n%4 == 1:
    # 이 경우는 초기상태로 보일 수 있으나, field3에 놓인 폭탄이 터진 상태로 표현하는 것이 맞음
    field4 = exploded(field)
    field4 = exploded(field4)
    for i in field4:
        print(*i, sep='')