import sys

n = int(input())
a = list(map(int, input().split()))

b,c = map(int, sys.stdin.readline().split(' '))
total_num = 0

for i in a:
    # 총관리자 커버 인원
    i = i - b
    total_num += 1

    # 부관리자 커버 인원
    if i > 0:
        total_num += (i // c)
        if i % c > 0:
            total_num +=1

print(total_num)