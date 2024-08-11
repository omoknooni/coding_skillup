import sys
from itertools import permutations

k = int(input())
equ = list(sys.stdin.readline().split( ))

answers = []
numbers = [x for x in range(10)]

for p in permutations(numbers, k+1):
    flag = True
    for i,v in enumerate(equ):
        if v == "<":
            if p[i] > p[i+1]:
                flag = False
                break
        else:
            if p[i] < p[i+1]:
                flag = False
                break
    if flag:
        answers.append(''.join(map(str, p)))


### DFS
visited = [False] * 10

def fmt_check(a, equ, b):
    if equ == "<":
        if a > b:
            return False
    else:
        if a < b:
            return False
    return True

# 숫자를 하나씩 붙여보며 dfs 탐색
def dfs(cnt, num):
    if cnt == k+1:
        answers.append(num)
        return 
    
    for n in numbers:
        if not visited[n]:
            if cnt == 0 or fmt_check(int(num[-1]), equ[cnt-1], n):
                visited[n] = True
                dfs(cnt+1, num+str(n))
                
                # dfs 순회 후 return 되었을 때, 다음 숫자의 탐색을 위해 초기화
                visited[n] = False


dfs(0,"")

# 최대/최소 출력, 탐색을 오름차순으로 했으므로 제일 앞 값과 끝 값만 출력
# print(answers[-1])
# print(answers[0])