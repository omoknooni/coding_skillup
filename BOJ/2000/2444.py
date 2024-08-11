a = int(input())
l1 = [2*i+1 for i in range(a)]
l2 = [(a-1-i,v) for i,v in enumerate(l1)]
l2 = l2 + l2[-2::-1]
for i in l2:
    print(' '*i[0], '*'*i[1], sep='')