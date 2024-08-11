def check(st):
    if len(st) == 1 or len(st) == 0:
        print(1)
        return 0
    if st[0] == st[-1]:
        return check(st[1:-1])
    else:
        print(0)
check(input())