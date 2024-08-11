import sys

target = []
answer = []
n = int(input())
for i in range(n):
    target.append(int(sys.stdin.readline()))

stk = []
num = 1         # stack은 오름차순으로 값을 넣으므로 어디까지 넣었는지 저장용

# 뽑아내고자 하는 수열을 하나씩 앞에서부터 완성해가기
for i in target:
    # 우선 해당 값까지 스택에 넣음, 이미 num이 그값을 넘어가면 while문 미실행
    while num <= i:
        answer.append('+')
        stk.append(num)
        num += 1
    
    # stack의 top이 얻고자하는 수열의 값과 동일하면 그 값을 top에서 뺌
    if stk[-1] == i:
        answer.append('-')
        stk.pop()
    # stack의 top이 수열값과 일치하지 않으면, 완성불가
    else:
        answer = ["NO"]
        break

print(*answer)