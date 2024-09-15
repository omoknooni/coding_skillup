import sys
input = sys.stdin.readline
t = int(input())

for _ in range(t):
  n = int(input())
  human = []
  for _ in range(n):
    human.append(list(map(int, input().split())))
  human.sort(key=lambda x: x[0])

  # 서류등수로 정렬하면 1등은 반드시 가져감
  answer = 1
  check = human[0][1]
  for i in range(1,n):
    
    # 서류점수순으로 정렬된 human에서 비교대상보다 [다음 사람이 높은 등수면] 그 사람을 채용
    if check > human[i][1]:
      answer += 1
      
      # 비교대상을 변경
      check = human[i][1]
  print(answer)

  # # 완전 탐색 (시간 초과)
  # answer = 0
  # for i in range(len(human)):
  #   cnt = 0
  #   for j in range(i+1, len(human)):
  #     if (human[i][0] < human[j][0]) or (human[i][1] < human[j][1]):
  #       cnt += 1
  #   if cnt == (len(human)-(i+1)):
  #     answer += 1
  # print(answer)
