import sys
input = sys.stdin.readline
n = int(input())
seats = [[0]*n for _ in range(n)]

# 학생 정보
students = {}
for i in range(n*n):
  student = list(map(int, input().split()))
  students[student[0]] = student[1:]

# 탐색은 4방향
dt = [[-1,0],[0,-1],[1,0],[0,1]]

for s in students:
  # 조건에 따른 우선순위 매기기
  target = []
  for y in range(n):
    for x in range(n):
      blank = 0
      like = 0
      if seats[y][x] == 0:
        for d in dt:
          ny = y + d[1]
          nx = x + d[0]
          if 0 <= nx < n and 0 <= ny < n:
            if seats[ny][nx] == 0:
              blank += 1
            elif seats[ny][nx] in students[s]:
              like += 1
        # 우선순위를 계산하기 위해 각 지표를 삽입
        target.append([like,blank,y,x])
 
  # 우선순위 값이 큰거부터 나오도록 (like > blank > 행(y) > 열(x))
  target.sort(key=lambda x:(-x[0],-x[1],x[2],x[3]))
  # 학생 배치
  seats[target[0][2]][target[0][3]] = s

# 선호도 계산
point = 0
for y in range(n):
  for x in range(n):
    cnt = 0
    for d in dt:
      ny = y + d[1]
      nx = x + d[0]
      if 0 <= nx < n and 0 <= ny < n:
        # 주변 4칸에 선호학생이 있는지 체크
        if seats[ny][nx] in students[seats[y][x]]:
          cnt += 1
    if cnt > 0:
      point += 10**(cnt-1)

print(point)