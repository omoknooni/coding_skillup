import sys
s = list(map(str, sys.stdin.readline().strip()))
t = list(map(str, sys.stdin.readline().strip()))

# t에서 s를 만드는 과정으로
while len(s) != len(t):
  # 끝이 A면 끝원소 삭제
  if t[-1] == "A":
    t.pop()

  # 끝이 B면 끝원소 삭제하고 뒤집기
  else:
    t.pop()
    t.reverse()

  if s == t:
    print(1)
    break
else:
  print(0)

# 메모리 초과
# stk = deque([s])
# while stk:
#   node = stk.popleft()

#   if len(node) <= len(t):
#     node_a = node + 'A'
#     node_b = node[::-1] + 'B'

#     if node_a == t or node_b == t:
#       print(1)
#       break
#     stk.append(node_a)
#     stk.append(node_b)
# else:
#   print(0)
