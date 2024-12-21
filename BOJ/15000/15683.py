import sys
import copy
input = sys.stdin.readline

n,m = map(int, input().split())
room = []
cam = []
for i in range(n):
    line = list(map(int, input().split()))
    for j in range(m):
        if line[j] in [1,2,3,4,5]:
            cam.append([i,j,line[j]])
    room.append(line)

# 카메라 모드
# 0:상, 1:우, 2:하, 3:좌
# 회전하는 경우 포함
cam_type = {
    1: [[0],[1],[2],[3]],
    2: [[0,2],[1,3]],
    3: [[0,1],[1,2],[2,3],[0,3]],
    4: [[0,1,2],[1,2,3],[0,2,3],[0,1,3]],
    5: [[0,1,2,3]]
}
dt = [[-1,0],[0,1],[1,0],[0,-1]]


# 카메라를 지정된 방향에서 본 경우, 사각지대를 계산
def watch(y, x, type, room):
    for d in type:
        ny, nx = y, x
        while True:
            ny += dt[d][0]
            nx += dt[d][1]
            if 0 <= ny < n and 0 <= nx < m:
                # CCTV는 CCTV를 통과해서 볼 수 있으므로 벽만 고려
                if room[ny][nx] != 6:
                    room[ny][nx] = -1
                # 벽에 닿으면 막힘
                else:
                    break
            # 방 범위 넘어가면 break
            else:
                break

# 각 카메라를 회전시키며 사각지대 탐색
def dfs(cam_idx, room):
    global answer

    # 종료 조건
    # 모든 카메라에 대해 탐색했으면, 사각지대 갯수 계산
    if cam_idx == len(cam):
        cnt = 0
        for i in range(n):
            cnt += room[i].count(0)
        answer = min(answer, cnt)
        return

    # room 초기화에 사용할 원본 복제
    tmp = copy.deepcopy(room)
    # # 얕은 복사임, 최상위 객체만 복사하기에 이중리스트인 room의 완전복사를 위해 깊은 복사 필요
    # tmp = room[:]
    y,x,type = cam[cam_idx]

    for i in cam_type[type]:
        watch(y,x,i,tmp)
        dfs(cam_idx+1, tmp)
        # 백트래킹을 위한 room 초기화
        tmp = copy.deepcopy(room)

# 사각지대의 최소 크기
answer = n*m
dfs(0,room)
print(answer)
