import sys

n,m = map(int, input().split())
s = 0

number_list = list(map(int, sys.stdin.readline().split()))
sum_list, answer = [0], []
for i in number_list:
    s += i
    sum_list.append(s)

for idx in range(m):
    i, j = map(int, input().split())
    answer.append(sum_list[j] - sum_list[i-1])

for a in answer:
    print(a)