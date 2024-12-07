import sys
input = sys.stdin.readline

n = int(input())
students = list(map(int, input().split()))
students.sort()

cnt = 0
for s in range(n-2):
    left = s+1
    right = n-1
    idx = n
    while left < right:
        tmp = students[s] + students[left] + students[right]
        if tmp == 0:
            # left부터 right까지 모두 동일한 수 -> right-left 가짓수
            if students[left] == students[right]:
                cnt += right - left
            else:
                # students[right]와 같은 값을 갖는 인덱스를 탐색
                # if문이 필요한 이유? > 불필요한 계산 횟수 줄이기
                if idx > right:
                    idx = right
                    while idx > left and students[idx-1] == students[right]:
                        idx -= 1
                # students[right]값과 같은 값 갯수만큼 더하기
                cnt += right - idx + 1
            left += 1
        elif tmp < 0:
            left +=1 
        else:
            right -= 1
print(cnt)