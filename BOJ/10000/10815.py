import sys
num = int(input())
s_card = list(map(int,sys.stdin.readline().split()))
s_card = dict(zip(s_card,[0 for i in range(len(s_card))]))

num2 = int(input())
c_card = list(map(int, sys.stdin.readline().split()))

result = []
if num == len(s_card) and num2 == len(c_card):
    for i in c_card:
        if i in s_card:
            result.append(1)
        else:
            result.append(0)
print(*result)


# Dict 만들때 유용한 Counter...
import sys
from collections import Counter

num = int(input())
s_card = list(map(int,sys.stdin.readline().split()))
s_card = Counter(s_card)

num2 = int(input())
c_card = list(map(int, sys.stdin.readline().split()))

result = []
if num == len(s_card) and num2 == len(c_card):
    for i in c_card:
        if i in s_card:
            result.append(1)
        else:
            result.append(0)
print(*result)


# BinarySearch
import sys
num = int(input())
s_card = list(map(int,sys.stdin.readline().split()))
s_card.sort()

num2 = int(input())
c_card = list(map(int, sys.stdin.readline().split()))

def Solution(s_card):
    left, right = 0, num - 1
    while left <= right:
        mid = int((left + right) / 2)
        if s_card[mid] == i:
            return 1
        elif s_card[mid] < i:
            left = mid + 1
        else:
            right = mid -1
    return 0

if num == len(s_card) and num2 == len(c_card):
    for i in c_card:
        print(Solution(s_card), end=' ')