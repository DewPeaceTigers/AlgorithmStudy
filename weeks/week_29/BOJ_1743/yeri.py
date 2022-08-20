import sys
from collections import deque

input = sys.stdin.readline

N, M, K = map(int,input().split())
space = [[False]*M for _ in range(N)]

for _ in range(K):
    r,c = map(int,input().split())
    space[r-1][c-1] = True
dx = [-1,0,1,0]
dy = [0,-1,0,1]
max_size = 0
for i in range(N):
    for j in range(M):
        if space[i][j]:
            space[i][j]=False
            q= deque([[i,j]])
            size = 1
            while q:
                x,y = q.popleft()
                for d in range(4):
                    nx = x+dx[d]
                    ny = y+dy[d]
                    if -1<nx<N and -1<ny<M and space[nx][ny]:
                        size+=1
                        q.append([nx,ny])
                        space[nx][ny]=False
            max_size = max(max_size,size)
print(max_size)