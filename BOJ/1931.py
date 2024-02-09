import sys

n = int(input())

meetings = []
for i in range(n):
    start_time, end_time = map(int,sys.stdin.readline().split())
    meetings.append([start_time, end_time])

# 그리디 알고리즘 : 종료시각이 빠른 순으로 정렬부터
meetings.sort(key=lambda x: (x[1],x[0]))

# 회의 시작시간과 종료시각을 비교하며 탐색
answer, end = 0, 0
for s,e in meetings:
    if end <= s:
        answer += 1
        end = e

print(answer)

# answer = []
# for m in meetings:
#     if not answer:
#         answer.append(m)
#         continue
#     if answer[-1][1] <= m[0]:
#         answer.append(m)

# print(len(answer))