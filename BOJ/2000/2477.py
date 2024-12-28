k = int(input())

height, width, length = [], [], []
for _ in range(6):
  a,b = map(int, input().split())
  length.append(b)  
  if a == 1 or a == 2:
    width.append(b)
  else:
    height.append(b)

# 큰 사각형 - 작은 사각형
max_s = max(width) * max(height)

# 큰 사각형의 가로세로 변 앞뒤 인덱스에는 세로가로 변 값이 들어감
# 인덱스 범위 주의
small_s_width = abs(length[(length.index(max(height)) - 1)%6] - length[(length.index(max(height)) + 1)%6])
small_s_height = abs(length[(length.index(max(width)) - 1)%6] - length[(length.index(max(width)) + 1)%6])
print(k * (max_s - (small_s_width * small_s_height)))