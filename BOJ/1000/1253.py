import sys
n = int(input())
a = list(map(int, sys.stdin.readline().split()))

a = sorted(a)
good = []
for i in range(n):
    check = a[:i] + a[i+1:]

    # two pointer method
    left, right = 0, len(check)-1
    while left < right:
        if check[left] + check[right] == a[i]:
            good.append(a[i])
            print(f"{check[left]} + {check[right]} == {a[i]}")
            break
        elif check[left] + check[right] < a[i]:
            left += 1
        else:
            right -= 1

print(good)
print(len(good))

### TODO : binary search로도 풀기
# def binary_search(array, value, left, right):
#     if left > right:
#         return -1
#     middle = (left + right) // 2
#     if value == array[middle]:
#         return middle
#     elif value > array[middle]:
#         return binary_search(array, value, middle+1, right)
#     else:
#         return binary_search(array, value, left, middle-1)

# a = sorted(a)
# good = []
# for i,v in enumerate(a):
#     small_val = a[:i]
#     for j,w in enumerate(small_val):
#         small_val2 = small_val[:j]+small_val[j+1:]
#         s = binary_search(small_val2, v-w, 0, len(small_val2)-1)
#         if s == -1:
#             continue
#         else:
#             good.append(f"{small_val2[s]}+{w}={v}")

# print(good)