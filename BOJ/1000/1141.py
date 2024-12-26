n = int(input())
words = []
for _ in range(n):
    words.append(input())
# 단어를 길이순으로 오름차순 정렬
words.sort(key=lambda x: len(x))

# answer = words    # 이렇게하면 둘다 같은 주소를 참조하므로 remove할때 words 인덱스 꼬임
answer = words[:]

# 각 단어를 비교
for i in range(n):
    for j in range(i+1,n):
        if words[j].startswith(words[i]):
            # 포함하는 문자열이 발생하면 짧은쪽을 빼서 계산
            answer.remove(words[i])
            break

print(len(answer))