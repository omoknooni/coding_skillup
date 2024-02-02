import sys

t = int(input())
box = []

def find_num(a,b):
    # a의 일의 자릿수
    num = int(list(map(int, str(a)))[-1])

    # 일의 자릿수가 0이면 제곱해도 항상 0, 따라서 return 10
    if num == 0:
        return 10
    else:
        arr = []

        # 일의 자릿수가 4개씩 주기를 이룸 ex) a=3 arr=[3,9,27,81,243...]
        for i in range(1,5):
            arr.append(int(str(pow(a,i))[-1]))
        return arr[(b%4)-1]


for i in range(t):
    a,b = map(int, sys.stdin.readline().split())
    print(find_num(a,b))