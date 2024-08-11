from collections import Counter

n,m = map(int, input().split())
s = Counter()
cnt = 0
for i, v in enumerate(range(n+m)):
    word = input()
    if i < n:
        s[word] += 1
    else:
        if word in s:
            cnt += 1
print(cnt)