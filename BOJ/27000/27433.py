def solution(num):
    return 1 if num <= 1 else num * solution(num-1)
    
print(solution(int(input())))