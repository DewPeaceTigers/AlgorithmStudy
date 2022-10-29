import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

dx = [0,-1,0,1]
dy = [1,0,-1,0]
space = [[False]*101 for _ in range(101)]

for _ in range(N):
    y,x,d,g = map(int,input().split())

    space[x][y] = True
    nx = x+dx[d]
    ny = y+dy[d]
    space[nx][ny] = True
    curves = [[[nx,ny],d]]
    dir = d

    for _ in range(g):
        len_curves = len(curves)
        for i in range(len_curves-1,-1,-1):
            ex, ey = curves[-1][0]
            ed = (curves[i][1]+1)%4
            nx = ex+dx[ed]
            ny = ey+dy[ed]
            if not(-1<nx<101 and -1<ny<101): break
            space[nx][ny] = True
            curves.append([[nx,ny],ed])
cnt = 0
for i in range(101):
    print(space[i])
    for j in range(101):
        if space[i][j] and space[i][j+1] and space[i+1][j] and space[i+1][j+1]: cnt+=1
print(cnt)