import sys

input=sys.stdin.readline

n, m=map(int, input().split())

boards=[list(map(int, input().split())) for _ in range(n)]

dx, dy=[1, -1, 0, 0], [0, 0, 1, -1]

visit=[[0]*m for _ in range(n)]
ans=0
max_board=0
for i in range(n) :
    max_board=max(max_board, max(boards[i]))

def dfs(x, y, depth, total) :
    global ans
    if ans>=total+max_board*(4-depth):
        return
    if depth==4 :
        ans=max(ans, total)
        return
    else:
        for i in range(4) :
            nx, ny=x+dx[i], y+dy[i]
            if 0<=nx<n and 0<=ny<m and visit[nx][ny]==0:
                if depth==2:
                    visit[nx][ny]=1
                    dfs(x, y, depth+1, total+boards[nx][ny])
                    visit[nx][ny]=0
                visit[nx][ny]=1
                dfs(nx, ny, depth+1, total+boards[nx][ny])
                visit[nx][ny]=0
for i in range(n) :
    for j in range(m) :
        visit[i][j]=1
        dfs(i, j, 1, boards[i][j])
        visit[i][j]=0

print(ans)