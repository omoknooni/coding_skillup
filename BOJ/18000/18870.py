import sys
n = int(input())

x = list(map(int, sys.stdin.readline().split()))

x_pr = sorted(set(x))

# # Using Binary search    
def binary_search(array, value, left, right):
    if left > right:
        return -1
    middle = (left + right) // 2
    if value == array[middle]:
        return middle
    elif value > array[middle]:
        return binary_search(array, value, middle+1, right)
    else:
        return binary_search(array, value, left, middle-1)

for i in x:
    print(binary_search(x_pr, i, 0, len(x_pr)-1), end=' ')

# Using dictionary -> 이게 더 빠르게 찍힘
map_dict = dict(zip(x_pr, list(range(len(x_pr)))))
for i in x:
    print(map_dict[i], end=' ')