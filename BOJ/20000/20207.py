n = int(input())

# 날짜를 1차원 리스트에서 일정 갯수를 채움
field = [0]*367
for _ in range(n):
    s,e = map(int, input().split())
    for i in range(s,e+1):
        field[i] += 1

# 스케쥴 없는 날짜 기준으로 구역 나누어 계산
answer = []
row, col = 0,0
for i in range(1,len(field)):
    if field[i] == 0:
        answer.append(row*col)
        row, col = 0,0
    else:
        row = max(row, field[i])
        col += 1
print(sum(answer))