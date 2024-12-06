import sys
input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))
x = int(input())

numbers.sort()
answers = []

# 시작, 끝 포인트 잡고 범위 줄이며 탐색
s, e = 0, n-1
while s < e:
    tmp = numbers[s] + numbers[e]
    if tmp == x:
        answers.append([numbers[s],numbers[e]])
        s += 1
    elif tmp < x:
        s += 1
    else:
        e -= 1

# from itertools import combinations
# comb = combinations(numbers, 2)

# for c in comb:
#     if c[0] + c[1] == x:
#         answers.append(c)

print(len(answers))