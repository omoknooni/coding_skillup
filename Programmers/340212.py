def solution(diffs, times, limit):
    # 이진탐색을 위한 초기 좌/우 설정, 값제한이 1이상 100000이하이므로 right만 max값 -> 탐색 범위가 줄음
    left, right = 1, max(diffs)

    # 이진탐색, 부등호 조건 주의
    while left < right:
        level = (left+right) // 2
        
        total_time = 0
        for i in range(len(diffs)):
            # 이전 시간을 기억해야함
            if not i:
                time_priv = 0
            else:
                time_priv = times[i-1]
            time_cur = times[i]
            if diffs[i] <= level:
                total_time += time_cur
            else:
                total_time += (time_priv + time_cur) * (diffs[i]-level) + time_cur

        # limit을 넘어가는 경우, level을 늘림 -> left를 변경
        if total_time > limit:
            left = level+1
        # limit 안넘으면, level을 줄이고 탐색
        else:
            right = level
            
    # 반환값은 left -> 최솟값을 구하는 것이므로
    return left