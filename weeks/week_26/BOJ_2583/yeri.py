import sys
from collections import deque
input = sys.stdin.readline
m,n,k = map(int,input().split())
spaces= [[False]*n for _ in range(m)]
for t in range(k):
    sy,sx, ey, ex = map(int,input().split())
    for i in range(sx,ex):
        for j in range(sy,ey):
            spaces[i][j]=True
dx=[-1,0,1,0]
dy=[0,-1,0,1]
blanks=[]
for i in range(m):
    for j in range(n):
        if not spaces[i][j]:
            q = deque([(i,j)])
            spaces[i][j]=True
            total=1
            while q:
                x,y = q.popleft()
                for d in range(4):
                    nx = x+dx[d]
                    ny = y+dy[d]
                    if -1<nx<m and -1<ny<n and not spaces[nx][ny]:
                        total+=1
                        spaces[nx][ny]=True
                        q.append((nx,ny))
            blanks.append(total)
print(len(blanks))
print(*sorted(blanks))