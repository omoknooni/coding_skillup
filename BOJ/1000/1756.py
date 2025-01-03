from sys import stdin
input = stdin.readline

d,n = map(int, input().split())
oven = list(map(int, input().split()))
dough = list(map(int, input().split()))

# 들어갈 수 있는 크기에 맞게 재정의
for i in range(1,d):
  if oven[i] > oven[i-1]:
    oven[i] = oven[i-1]

# 오븐의 깊은곳 부터 채워짐
cnt = 0
for i in range(d-1,-1,-1):
  if dough[cnt] <= oven[i]:
    cnt += 1

  if cnt == n:
    print(i+1)
    break

# 오븐에 다 넣지 못하면 0
if cnt < n:
  print(0)