n = int(input())
line = list(map(int, input().split()))

match = [0] * n

# 키가 가장 작은 index부터 자리를 찾아줌
for i,v in enumerate(line):
    position_cnt = 0

    # 각 index가 들어갈 수 있는 자리를 탐색
    for j in range(n):
        if match[j] == 0 and v == position_cnt:
            match[j] = (i+1)
            break
        elif match[j] == 0:
            position_cnt += 1

print(*match)