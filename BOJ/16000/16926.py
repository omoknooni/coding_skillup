from collections import deque
import sys
input = sys.stdin.readline

n,m,r = map(int, input().split())
field = []
for _ in range(n):
  field.append(list(map(int, input().split())))
answer = [[0]*m for _ in range(n)]


# 반시계회전의 갯수 -> 껍질 갯수
loops = min(m,n) // 2

for i in range(loops):
  # 껍질내역을 1차원 나열
  loop = deque()

  # 껍질 상/우/하/좌
  # 코너 부분 확인
  loop.extend(field[i][i:m-i])
  loop.extend([row[m-i-1] for row in field[i+1:n-i-1]])
  loop.extend(field[n-i-1][i:m-i][::-1])
  loop.extend([row[i] for row in field[i+1:n-i-1][::-1]])

  # 회전 (반시계)
  loop.rotate(-r)

  # 회전 내역 저장 (상/우/하/좌)
  # 각 코너 부분 확인
  for j in range(i,m-i):
    answer[i][j] = loop.popleft()
  for j in range(i+1,n-i-1):
    answer[j][m-i-1] = loop.popleft()
  for j in range(m-i-1,i-1,-1):
    answer[n-i-1][j] = loop.popleft()
  for j in range(n-i-2,i,-1):
    answer[j][i] = loop.popleft()

# 최종 결과
for i in answer:
  print(*i)