import sys
from itertools import combinations
from collections import deque

input=sys.stdin.readline
n, m=map(int, input().split())
states = [list(map(int, input().split())) for _ in range(n)]

dx=[1, -1, 0, 0]
dy=[0, 0, 1, -1]

virus=[]
def bfs(virus_pos, wall_cnt) :
    q=deque()
    visit=[[-1]*n for _ in range(n)]

    time=0
    for x, y in virus_pos :
        q.append([x, y])
        visit[x][y]=0

    while q :
        x, y=q.popleft()
        for i in range(4):
            nx, ny=x+dx[i], y+dy[i]
            if 0<=nx<n and 0<=ny<n and visit[nx][ny]==-1 :
                if states[nx][ny]==0:
                    q.append([nx, ny])
                    visit[nx][ny]=visit[x][y]+1
                    time=max(time, visit[nx][ny])
                elif states[nx][ny]==2:
                    q.append([nx, ny])
                    visit[nx][ny]=visit[x][y]+1

    zero_cnt=0
    for i in range(n) :
        zero_cnt+=visit[i].count(-1)
    if zero_cnt != wall_cnt :
        return sys.maxsize
    return time

wall_cnt=0
for i in range(n):
    for j in range(n):
        if states[i][j]==2 :
            virus.append([i, j])
        if states[i][j]==1:
            wall_cnt+=1

time=sys.maxsize
for virus_pos in combinations(virus, m) :
    time=min(time, bfs(virus_pos, wall_cnt))

if time==sys.maxsize :
    print(-1)
else:
    print(time)