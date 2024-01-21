import sys

n = int(input())
times = list(map(int, sys.stdin.readline().split()))

times.sort()
answer = 0
for idx, val in enumerate(times):
    answer += sum(times[:(idx+1)])

print(answer)