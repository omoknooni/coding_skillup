a = []
for _ in range(9):
    a.append(int(input()))

true_hobbit = []

def is_true_hobbit(index, count):
    # 7명을 채운 경우
    if count == 7:
        # 7명 합이 100 -> 정답
        if sum(true_hobbit) == 100:
            true_hobbit.sort()
            print(*true_hobbit, sep='\n')
            exit(0)
        else:
            return
        
    # index번째 난쟁이를 비교
    for i in range(index, len(a)):
        true_hobbit.append(a[i])
        is_true_hobbit(index+1, count+1)
        true_hobbit.pop()

is_true_hobbit(0,0)