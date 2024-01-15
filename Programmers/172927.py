def solution(picks, minerals):
    answer = 0
    max_pickable = sum(picks) * 5
    if len(minerals) > max_pickable:
        minerals = minerals[:max_pickable]
    
    new_minerals = [minerals[i:i+5] for i in range(0,len(minerals),5)]
    values = []
    for m in new_minerals:
        value = [0,0,0]
        for i in m:
            if i == "diamond":
                value[0] += 1
                value[1] += 5
                value[2] += 25
            elif i == "iron":
                value[0] += 1
                value[1] += 1
                value[2] += 5
            else:
                value[0] += 1
                value[1] += 1
                value[2] += 1
        values.append(value)
    # values.sort(key= lambda x: (-x[0],-x[1],-x[2]))
    values = sorted(values, key = lambda x: (-x[0],-x[1],-x[2]))
    for value in values:
        if picks[0] > 0:        # dia pick
            picks[0] -= 1
            answer += value[0]
            continue
        elif picks[1] > 0:      # iron pick
            picks[1] -= 1
            answer += value[1]
            continue
        else:                   # stone pick
            picks[2] -= 0
            answer += value[2]
            continue
    return answer