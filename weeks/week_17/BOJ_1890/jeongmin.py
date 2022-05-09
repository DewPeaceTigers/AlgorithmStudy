"""
반드시 오른쪽이나 아래쪽으로만 이동 가능

시작 : (0, 0)
도착 : (N-1, N-1)

규칙에 맞게 이동할 수 있는 경로의 개수
"""
import sys
input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for i in range(N)]

dp =[[0]*N for i in range(N)]
dp[0][0] = 1

for i in range(N):
  for j in range(N):
    if i== N-1 and j==N-1:
      print(dp[i][j])
      break
      
    # 아래로 이동
    if i+board[i][j]<N:
      dp[i+board[i][j]][j] += dp[i][j]

    # 오른쪽 이동
    if j+board[i][j]<N:
      dp[i][j+board[i][j]] +=dp[i][j]



""" 
### 시간 초과..
"""
# import sys
# input = sys.stdin.readline

# N = int(input())
# board = [list(map(int, input().split())) for i in range(N)]

# path = [[0]*N for i in range(N)]
# path[0][0] = 1

# # 오른쪽, 아래쪽
# dx = [0, 1]
# dy = [1, 0]

# def dfs(x, y):
#   if x==N-1 and y==N-1:
#     return

#   for i in range(2):
#     nx = x+ dx[i]*board[x][y]
#     ny = y+ dy[i]*board[x][y]

#     if nx<0 or N<=nx or ny<0 or N<=ny:
#       continue

#     # 이동
#     if path[nx][ny]==0:
#       path[nx][ny] = path[x][y]

#     else:
#       path[nx][ny]+=1

#     dfs(nx, ny)

# dfs(0, 0)
# print(path[N-1][N-1])