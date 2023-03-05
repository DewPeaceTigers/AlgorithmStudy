'''
메모리 초과
'''
import sys
from collections import deque

input=sys.stdin.readline
dx, dy=[-1, 1, 0, 0], [0, 0, -1, 1]
r, c=map(int, input().split())

maps=[]
q=deque() #고슴도치 위치
water=deque()

maps=[list(map(str, input().rstrip())) for _ in range(r)]

def bfs() :
    cnt = 0
    while q:
        #물
        for i in range(len(water)) :
            x, y=water.popleft()
            for i in range(4) :
                nx=x+dx[i]
                ny=y+dy[i]
                if 0<=nx<r and 0<=ny<c :
                    if maps[nx][ny]=='.':
                        water.append([nx, ny])
                        maps[nx][ny]='*'
        cnt+=1
        #고슴도치
        for i in range(len(q)) :
            x, y=q.popleft()
            for i in range(4) :
                nx=x+dx[i]
                ny=y+dy[i]
                if 0<=nx<r and 0<=ny<c :
                    if (maps[nx][ny]=='.'): #고슴도치
                        q.append([nx, ny])
                    elif maps[nx][ny]=='D':
                        return cnt
    return "KAKTUS"

for i in range(r):
    for j in range(c) :
        if maps[i][j]=='S' : #고슴도치
            q.append([i, j])
        elif maps[i][j]=='*' : #물
            water.append([i, j])

print(bfs())