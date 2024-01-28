import sys

n = int(input())
a = list(map(int, sys.stdin.readline().split()))
m = int(input())
check = list(map(int, sys.stdin.readline().split()))

a.sort()
res = []

def binary_search(arr, left, right, target):
    while (left <= right):
        mid = (left+right) // 2

        if arr[mid] == target:
            return 1

        if arr[mid] > target:
            right = mid - 1 
        else:
            left = mid + 1
    return 0
    
for c in check:
    res.append(binary_search(a, 0, n-1, c))

for i in res:
    print(i)