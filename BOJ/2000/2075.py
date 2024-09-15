import heapq, sys
n = int(input())
table = []
for _ in range(n):
  for i in list(map(int, sys.stdin.readline().split())):
    # heap 리스트의 길이를 n을 유지하면서 진행 (모든값을 저장하고있으면 메모리 오버)
    if len(table) >= n:
      # heap 최소값이 현재값보다 작으면 하나 넣고빼고
      if table[0] < i:
        heapq.heappush(table, i)
        heapq.heappop(table)
    else:
      heapq.heappush(table, i)

print(table[0])

### 메모리 오버
# 정렬된 리스트를 위해서 하나씩 뽑아서 새로 넣어야함
# ordered_table = []
# while table:
#   ordered_table.append(heapq.heappop(table))
# print(ordered_table[-n])