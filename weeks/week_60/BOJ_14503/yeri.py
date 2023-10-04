import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split())
x, y, rd = map(int,input().split())
if rd == 1: rd = 3
elif rd == 3: rd = 1
boards= [list(map(int,input().split())) for _ in range(N)]
dx = [-1,0,1,0]
dy = [0,-1,0,1]
cnt = 0
while True:
    if boards[x][y] == 0:
        boards[x][y] = 2
        cnt += 1

    for d in range(rd+1,rd+1+4):
        nx = x+dx[d%4]
        ny = y+dy[d%4]
        if not(-1<nx<N and -1<ny<M): continue
        if boards[nx][ny] == 0:
            x = nx
            y = ny
            rd = d%4
            break
    else:
        nx = x-dx[rd]
        ny = y-dy[rd]
        if not(-1<nx<N and -1<ny<M) or boards[nx][ny]==1: break
        x = nx
        y = ny
print(cnt)