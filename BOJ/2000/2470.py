import sys
n = int(input())
targets = list(map(int,sys.stdin.readline().split()))

# 1차적으로 오름차순 정렬
targets.sort()

start, end = 0, n-1

# 초깃값 : 양 쪽 끝 원소합 +1 (아니면 MAX값 임의로 지정)
# val = abs(targets[start] + targets[end]) + 1
val = sys.maxsize
while start < end:
    total = targets[start] + targets[end]
    
    # 양 끝 원소 합이 기존에 계산했던 0에 가까운 수(val)보다 더 0에 가까우면 val 갱신
    if abs(total) < val:
        val = abs(total)
        answer = [targets[start], targets[end]]
        if total == 0:
            break

    # 양 끝 원소 합이 음수 -> start 지점 오른쪽으로
    if total < 0:
        start += 1
    # 양 끝 원소 합이 양수 -> end 지점 왼쪽으로
    else:
        end -= 1

print(*answer)