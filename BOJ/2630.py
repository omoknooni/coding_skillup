import sys

n = int(input())
target = []
for i in range(n):
    target.append(list(map(int,sys.stdin.readline().split())))
paper = [0,0]

def cut(target):
    size = int(len(target) / 2)
    matrix = []
    for i in range(2):
        for j in range(2):
            matrix.append([row[j*size:(j+1)*size] for row in target[i*size:(i+1)*size]])

    full = set(sum(sum(matrix,[]),[]))
    if len(full) == 1:
        if 0 in full:
            paper[0] += 1
        else:
            paper[1] += 1
        return

    for m in matrix:
        s = set(sum(m,[]))
        if len(s) == 1:
            if 0 in s:
                paper[0] += 1
            elif 1 in s:
                paper[1] += 1
        else:
            cut(m)

cut(target)
print(*paper, sep='\n')