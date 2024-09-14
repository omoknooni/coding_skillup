t,w = map(int, input().split())
trees = [0]
for _ in range(t):
  trees.append(int(input()))

# 움직일수있는 횟수 w, 최대 자두 갯수를 구한다.
# 행 : time, 열 : 이동횟수
dp = [[0]*(w+1) for _ in range(t+1)]

for i in range(1,t+1):
  # 0번 이동 시, 1번 나무만 먹을수있음
  if trees[i] == 1:
    dp[i][0] = dp[i-1][0]+1
  else:
    dp[i][0] = dp[i-1][0]

  for j in range(1,w+1):
    # 이동을 짝수번->1번나무, 홀수번->2번나무
    if (trees[i] == 1 and j%2==0) or (trees[i] == 2 and j%2==1):
      dp[i][j] = max(dp[i-1][j-1], dp[i-1][j])+1
    else:
      dp[i][j] = max(dp[i-1][j-1], dp[i-1][j])

print(max(dp[t]))