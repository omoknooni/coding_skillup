n = int(input())
t = int(input())
suggest = list(map(int,input().split()))

# 학생번호: [투표수, 게시시간]
photo = {}

for i in range(t):
    # 현재 후보에 추천자가 있는 경우
    if suggest[i] in photo:
        photo[suggest[i]][0] += 1
    else:
        if len(photo) < n:
            photo[suggest[i]] = [1,i]
        else:
            # 가장 적은 후보 탐색 -> 득표수, 게시기간순(짧으면 오래된 것)
            # items -> (key,val) -> x[1][0], x[1][1]
            least = sorted(photo.items(), key=lambda x: (x[1][0], x[1][1]))
            del(photo[least[0][0]])

            # 새로 넣기
            photo[suggest[i]] = [1,i]

# 결과, 번호의 오름차순
answer = list(sorted(photo.keys()))[:n]
print(*answer)
