'''
visit[i][j]는 i, j에 도달하는 경우의 수
'''
import sys
sys.setrecursionlimit(10 ** 8)
m, n=map(int, input().split())
boards=[]
dx=[1, -1, 0, 0]
dy=[0, 0, 1, -1]
visit=[[-1]*n for _ in range(m)]
for _ in range(m) :
    boards.append(list(map(int, input().split())))

def dfs(x, y):
    if x==m-1 and y==n-1 : #도착지점이면 한가지 경우이니까 1
        return 1
    if visit[x][y]!=-1 : #이미 방문한적 o
        return visit[x][y]
    visit[x][y]=0
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<m and 0<=ny<n :
            if boards[nx][ny]<boards[x][y] :
                visit[x][y]+=dfs(nx, ny)
    return visit[x][y]


print(dfs(0, 0))