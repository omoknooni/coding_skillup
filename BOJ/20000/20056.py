import sys
input = sys.stdin.readline

n,m,k = map(int, input().split())

# 실제 배치될 격자 구간
field = [[[] for _ in range(n)] for _ in range(n)]
dt = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

# 각 fireball 저장
fireball = []
for _ in range(m):
    r,c,m,s,d = map(int, input().split())
    fireball.append([r-1,c-1,m,s,d])

for order in range(k):
    # 이동, fireball을 연산 후, 필드에 배치하는 방식
    # 각 행와 열의 끝과끝은 연결되어있음 -> 막히는 부분은 없다
    while fireball:
        r,c,m,s,d = fireball.pop()
        ny = (r + s*dt[d][0]) % n
        nx = (c + s*dt[d][1]) % n
        field[ny][nx].append([m,s,d])

    # 칸 계산
    for i in range(n):
        for j in range(n):
            # 한 칸에 2개 이상이면 연산
            if len(field[i][j]) >= 2:
                m_sum, s_sum, cnt = 0,0,len(field[i][j])
                odd, even = 0,0
                while field[i][j]:
                    m,s,d = field[i][j].pop()
                    m_sum += m
                    s_sum += s
                    if d%2 == 0:
                        even += 1
                    else:
                        odd += 1
                
                # 방향이 모두 홀/짝일때만 0,2,4,6
                if even == cnt or odd == cnt:
                    split_d = [0,2,4,6]
                else:
                    split_d = [1,3,5,7]
                
                # 질량 0 이상이면 남음
                if m_sum // 5:
                    for sd in split_d:
                        # 나눠질 당시 좌표는 4개 모두 동일
                        fireball.append([i,j,m_sum // 5, s_sum // cnt, sd])
            
            # 하나면 그냥 더해줌
            elif len(field[i][j]) == 1:
                m,s,d = field[i][j].pop()
                fireball.append([i,j,m,s,d])

# 구하는 것은 총 질량 합
print(sum(s[2] for s in fireball))