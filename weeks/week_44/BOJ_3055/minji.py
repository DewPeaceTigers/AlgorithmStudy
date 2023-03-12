import sys
from collections import deque

input=sys.stdin.readline

r, c=map(int, input().split())
maps=[list(map(str, input().rstrip())) for _ in range(r)]

dx=[-1, 1, 0, 0]
dy=[0, 0, -1, 1]

q=deque()
water=deque()
visit=[[False]*c for _ in range(r)]

def bfs() :
    cnt=0
    while q :
        #물
        for _ in range(len(water)) :
            x, y=water.popleft()
            for i in range(4) :
                nx=x+dx[i]
                ny=y+dy[i]
                if 0<=nx<r and 0<=ny<c :
                    if maps[nx][ny]=='.' :
                        water.append([nx, ny])
                        maps[nx][ny]='*'
                        visit[nx][ny]=True
        cnt+=1

        for _ in range(len(q)) :
            x, y=q.popleft()
            for i in range(4) :
                nx=x+dx[i]
                ny=y+dy[i]
                if 0<=nx<r and 0<=ny<c and visit[nx][ny]==0:
                    if maps[nx][ny]=='.' :
                        visit[nx][ny]=True
                        q.append([nx, ny])
                    elif maps[nx][ny]=='D' :
                        return cnt
    return "KAKTUS"
for i in range(r) :
    for j in range(c) :
        if maps[i][j]=='S' :
            q.append([i, j])
            visit[i][j]=True
        elif maps[i][j]=='*' :
            water.append([i, j])
            visit[i][j]=True
        elif maps[i][j]=='X' :
            visit[i][j]=True

print(bfs())