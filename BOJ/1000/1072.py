x,y = map(int, input().split())

# y/x*100 하는 경우 부동소수점 이슈 발생, y*100 / x
win_rate = int(y * 100 / x)
left = 1
right = x
answer = x

# 승률이 이미 99면 100이 될수 없으므로 -1
if win_rate >= 99:
  print(-1)
else:
  while left < right:
    mid = (left + right) // 2

    # 부동소수점 문제 발생 주의
    if int((y+mid) * 100 / (x+mid)) == win_rate:
      left = mid+1
    else:
      answer = mid
      right = mid
  print(answer)