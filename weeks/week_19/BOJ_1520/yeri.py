import sys
input = sys.stdin.readline

def dfs(x,y):
    dx=[-1,0,+1,0]
    dy=[0,-1,0,+1]
    routes=0
    for d in range(4):
        nx = x+dx[d]
        ny = y+dy[d]
        if -1<nx<M and -1<ny<N and boards[x][y] < boards[nx][ny]:
            if dp[nx][ny]==-1: routes+=dfs(nx,ny)
            else: routes+=dp[nx][ny]
    dp[x][y]=routes
    return dp[x][y]

M,N = map(int,input().split())
boards=[list(map(int,input().split())) for _ in range(M)]
dp = [[-1]*N for _ in range(M)]
dp[0][0]=1

for i in range(M):
    for j in range(N):
        if dp[i][j]==-1:
            dfs(i,j)
print(dp[-1][-1])

