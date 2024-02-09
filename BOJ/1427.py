n = int(input())

nums = list(str(n))
nums.sort(reverse=True)

print(int(''.join(nums)))