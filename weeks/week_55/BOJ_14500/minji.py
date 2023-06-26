import sys

input=sys.stdin.readline

n, m=map(int, input().split())
boards=[list(map(int, input().split())) for _ in range(n)]

visit=[[False]*m for _ in range(n)]
ans=0
max_num=0
dx, dy=[1, -1, 0, 0], [0, 0, 1, -1]
for i in range(n) :
    max_num=max(max_num, max(boards[i]))

def dfs(x, y, depth, total):
    global ans
    if ans>total+max_num*(4-depth) :
        return
    if depth==4:
        ans=max(ans, total)
        return
    else:
        for i in range(4) :
            nx, ny=x+dx[i], y+dy[i]
            if 0<=nx<n and 0<=ny<m and not visit[nx][ny] :
                if depth==2 :
                    visit[nx][ny]=True
                    dfs(x, y, depth+1, total+boards[nx][ny])
                    visit[nx][ny]=False
                visit[nx][ny]=True
                dfs(nx, ny, depth+1, total+boards[nx][ny])
                visit[nx][ny]=False
for i in range(n) :
    for j in range(m) :
        if not visit[i][j] :
            visit[i][j]=True
            dfs(i, j, 1, boards[i][j])
            visit[i][j]=False

print(ans)