import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split())
boards = [list(map(int,input().split())) for _ in range(N)]
visit = [[False]*M for _ in range(N)]
dx = [-1,0,1,0]
dy = [0,-1,0,1]
answer = 0

def dfs(x, y, depth, add):
    global answer
    if depth == 4:
        answer = max(answer, add)
        return

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]

        if not (-1 < nx < N and -1 < ny < M) or visit[nx][ny]: continue
        if depth == 2:
            visit[nx][ny] = True
            dfs(x, y, depth + 1, add + boards[nx][ny])
            visit[nx][ny] = False
        visit[nx][ny] = True
        dfs(nx, ny, depth + 1, add + boards[nx][ny])
        visit[nx][ny] = False
for i in range(N):
    for j in range(M):
        visit[i][j] = True
        dfs(i,j,1,boards[i][j])
        visit[i][j]=False
print(answer)
