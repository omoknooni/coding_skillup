import sys

n,k = map(int, input().split())
nations = {}
for _ in range(n):
  nation = list(map(int, sys.stdin.readline().split(" ")))
  number = nation.pop(0)
  nations[number] = nation

# 국가가 획득한 메달 수로 정렬 (금,은,동)
sorted_nations = dict(sorted(nations.items(), key=lambda x: (-x[1][0], -x[1][1], -x[1][2])))

# 구하고자 하는 국가의 메달 갯수
tmp = sorted_nations[k]

# 정렬된 메달 갯수를 순회하며 tmp와 동일한 메달항목이 나오면 순위 표시
for i,v in enumerate(sorted_nations.values()):
  if v == tmp:
    print(i+1)
    break