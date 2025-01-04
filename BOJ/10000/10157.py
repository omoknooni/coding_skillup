c,r = map(int, input().split())
k = int(input())

# 방문 여부 체크
# field를 오른쪽 90도 회전 시키고 계산, 결과는 동일
field = [[False]*r for _ in range(c)]
if k > c*r:
    print(0)
else:
    cnt = 1

    # 방향 관련 리스트 dt와 인덱스 d
    dt = [[0,1],[1,0],[0,-1],[-1,0]]
    d = 0
    y,x = 0,0
    while True:
        if cnt == k:
            print(f"{y+1} {x+1}")
            break
        field[y][x] = True
        ny = y + dt[d][0]
        nx = x + dt[d][1]
        if (0 <= ny < c) and (0 <= nx < r):
            # 방문 안한 곳이면 방문하기
            if not field[ny][nx]:
                cnt += 1
                y,x = ny,nx
            # 방문 했으면 방향 바꾸기
            else:
                d = (d+1)%4
        # 범위를 넘어가는 곳이면 방향 바꾸기
        else:
            d = (d+1)%4

# 필드에서 각 칸을 탐색하는 방식으로
# 인덱스 맞추기 어려우면 회전하는 방법