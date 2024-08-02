import sys
n = int(input())
towers = list(map(int, sys.stdin.readline().split(" ")))

stk = []
answer = [0] * len(towers)

for idx, tower in enumerate(towers):
    # 각 타워의 수신 타워 계산
    # 완전탐색이라 time over, stk를 모두 볼 필요가 없음
    # stk = list(enumerate(towers[:idx]))
    # while stk:
    #     s = stk.pop()
    #     if s[1] >= tower:
    #         answer[idx] = s[0]+1
    #         break
    # else:
    #     answer[idx] = 0

    # 현재 tower와 stk의 top만 비교함, stk에는 계산에 필요없는 tower들은 넣지 않음
    while stk: 
        # stk top이 현재 tower보다 높으면 수신 가능
        if stk[-1][1] > tower:
            answer[idx] = stk[-1][0]+1
            break
        # 현재 tower가 높으면 해당 값(stk의 top)은 필요없으므로 빼기
        else:
            stk.pop()
    else:
        answer[idx] = 0
    # 계산을 마친 후 현재 tower를 stk에 추가
    stk.append([idx, tower])
print(*answer)