# 3003
input_arr = list(map(int, input().split()))
print(*[i1-i2 for i1,i2 in zip([1,1,2,2,2,8],input_arr)])

# 2444
a = int(input())
l1 = [2*i+1 for i in range(a)]
l2 = [(a-1-i,v) for i,v in enumerate(l1)]
l2 = l2 + l2[-2::-1]
for i in l2:
    print(' '*i[0], '*'*i[1], sep='')
    
# 10988
def check(st):
    if len(st) == 1 or len(st) == 0:
        print(1)
        return 0
    if st[0] == st[-1]:
        return check(st[1:-1])
    else:
        print(0)
check(input())