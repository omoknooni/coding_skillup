import sys
from collections import Counter

n = int(input())
owned_list = list(map(int, sys.stdin.readline().split()))
m = int(input())
check_list = list(map(int, sys.stdin.readline().split()))

owned = Counter(owned_list)
check = Counter(check_list)

for i in check:
    if owned[i] != 0:
        check[i] = owned[i]
    else:
        check[i] = 0

for i in check_list:
    print(check[i], end=' ')