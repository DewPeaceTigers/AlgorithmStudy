import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split())

graph = []
viruss = []
for i in range(N):
    graph.append(list(map(int,input().split())))
    for j in range(N):
        if graph[i][j] == 2:
            viruss.append([i,j])

def simulate(run):
    mTime = 0
    visit = [[False]*N for _ in range(N)]
    q = deque()
    temp = [ g[:] for g in graph]
    for r in run:
        x,y = viruss[r]
        q.append([x,y,0])
        temp[x][y] = -2
        visit[x][y] = True
    dx=[-1,0,1,0]
    dy=[0,-1,0,1]
    while q:
        x,y,time = q.popleft()
        for d in range(4):
            nx = x+dx[d]
            ny = y+dy[d]
            if not(-1<nx<N and -1<ny<N) or visit[nx][ny]: continue
            visit[nx][ny] = True
            if temp[nx][ny]==0:
                temp[nx][ny]=time+1
                q.append(([nx,ny,time+1]))
            elif temp[nx][ny]==2:
                temp[nx][ny] = -3
                q.append([nx,ny,time+1])
            else:
                temp[nx][ny] = -1
    for t in temp:
        if t.count(0)!=0: return -1
        mTime = max(mTime,max(t))
    return mTime


def dfs(cnt,start,run):
    global minTime
    if cnt == M:
        time = simulate(run)
        if time!=-1: minTime = min(minTime,time)
        return
    for i in range(start,len(viruss)):
        dfs(cnt+1,i+1,run+[i])
minTime = int(1e9)
dfs(0,0,[])
print(minTime) if minTime!=int(1e9) else print(-1)

"""
틀림
"""