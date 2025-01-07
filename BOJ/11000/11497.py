import sys
input = sys.stdin.readline
t = int(input())

for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))

    l.sort()

    # 오름차순 정렬한 리스트를 작은값부터 앞,뒤 번갈아가면서 채운다
    result = [0]*n
    j,k = 0, n-1
    for i in range(n):
        if i%2 == 0:
            result[j] = l[i]
            j += 1
        else:
            result[k] = l[i]
            k -= 1

    # 구하는 것은 인접한 것끼리 차이의 최댓값
    answer = 0
    for i in range(-1, n-1):
        gap = abs(result[i] - result[i+1])
        answer = max(answer, gap)
    print(answer)