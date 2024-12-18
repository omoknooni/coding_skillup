import sys
input = sys.stdin.readline

n, atk = map(int, input().split())

room = []
for _ in range(n):
    room.append(list(map(int, input().split())))

def simulate(cur_atk, max_hp):
    cur_hp = max_hp
    for r in room:
        if r[0] == 1:
            mob_atk = r[1]
            mob_hp = r[2]

            # # battle phase
            # while (mob_hp > 0 and cur_hp > 0):
            #     mob_hp = mob_hp - cur_atk
            #     cur_hp = cur_hp - mob_atk

            # while문으로 체력깎으면서 돌리지 말고, 공격횟수 연산 후 적용
            atk_to_mob = mob_hp // cur_atk
            cur_hp -= (atk_to_mob-1 if mob_hp%cur_atk == 0 else atk_to_mob) * mob_atk
            
            # death
            if cur_hp <= 0:
                return False
        else:
            cur_atk += r[1]
            cur_hp = min(max_hp, cur_hp + r[2])
    return True

left, right = 1, sys.maxsize

while left <= right:
    mid = (left + right) // 2

    # 죽으면 체력을 늘림
    if not simulate(atk, mid):
        left = mid + 1
    # 클리어하면 체력을 줄임
    else:
        right = mid -1
        answer = mid

print(answer)