import sys
input = sys.stdin.readline

sound = ['q','u','a','c','k']
record = list(input().strip())
visited = [False] * len(record)
cnt = 0

# 녹음 길이가 5의 배수가 아님 -> 올바르지 못함
if len(record) % 5 != 0:
    print(-1)
    exit()
else:
    for i in range(len(record)):
        find = False
        if record[i] == 'q' and not visited[i]:
            # 한마리가 계속 부르는가
            start = True
            sound_idx = 1
            visited[i] = True
            for j in range(i+1,len(record)):
                if record[j] == sound[sound_idx] and not visited[j]:
                    visited[j] = True
                    sound_idx += 1
                    if sound_idx == 5:
                        sound_idx = 0
                        start = False
                        find = True

            # 녹음 끝까지 가도 끝맺지 못한 quack -> 올바르지 못함
            if start:
                print(-1)
                exit()
            # 한마리를 찾음
            if find:
                cnt += 1
# 방문 안한 곳 탐색 -> 있으면 올바르지 못함
for i in range(len(visited)):
    if not visited[i]:
        print(-1)
        exit()

print(cnt)