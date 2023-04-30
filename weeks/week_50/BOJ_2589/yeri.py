import sys
from collections import deque
input = sys.stdin.readline

R,C = map(int,input().split())

dx = [-1,0,1,0]
dy = [0,-1,0,1]

boards = [list(input().strip()) for _ in range(R)]
res = 0

for i in range(R):
    for j in range(C):
        if boards[i][j]=="L":
            q = deque([[i,j]])
            visit = [[-1]*C for _ in range(R)]
            visit[i][j] = 0
            cnt = 0
            while q:
                x,y = q.popleft()

                for d in range(4):
                    nx = x+dx[d]
                    ny = y+dy[d]
                    if -1<nx<R and -1<ny<C and boards[nx][ny] == "L" and visit[nx][ny]==-1:
                        visit[nx][ny] = visit[x][y]+1
                        q.append([nx,ny])
                        cnt = max(cnt, visit[nx][ny])
            res = max(cnt,res)
print(res)