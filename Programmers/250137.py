def solution(bandage, health, attacks):
    t, x, y = bandage
    cur_health = health
    cnt = 0
    for i in range(1, attacks[-1][0]+1):
        if i == attacks[0][0]:
            info = attacks.pop(0)
            cnt = 0
            cur_health -= info[1]
            if cur_health <= 0:
                return -1
        else:
            cnt += 1
            if cnt == t:
                cur_health += y
                cnt = 0
            cur_health += x
            if cur_health > health:
                cur_health = health
    return cur_health