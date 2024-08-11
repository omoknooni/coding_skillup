input_arr = list(map(int, input().split()))
print(*[i1-i2 for i1,i2 in zip([1,1,2,2,2,8],input_arr)])