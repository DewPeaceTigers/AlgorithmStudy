import sys

input=sys.stdin.readline
n=int(input())
forests=[]
dx=[1, -1, 0, 0]
dy=[0, 0, 1, -1]
dp=[[0]*n for i in range(n)]
ans=0
def dfs(x, y):
    if dp[x][y]: return dp[x][y]
    dp[x][y]=1
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]

        if 0<=nx<n and 0<=ny<n :
            if forests[x][y]<forests[nx][ny]:
                dp[x][y]=max(dp[x][y], dfs(nx, ny)+1)

    return dp[x][y]

for _ in range(n) :
    forests.append(list(map(int, input().split())))

for i in range(n) :
    for j in range(n) :
        ans=max(ans, dfs(i, j))

print(ans)

