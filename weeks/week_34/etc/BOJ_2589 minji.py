import sys
from collections import deque
input=sys.stdin.readline

n, m=map(int, input().split())
maps=[list(map(str, input().strip())) for _ in range(n)]

dx=[0, 0, -1, 1]
dy=[-1, 1, 0, 0]

def bfs(a, b):
    q=deque()
    q.append([a, b])
    visit=[[0]*m for _ in range(n)]
    visit[a][b]=1
    time=0
    while q:
        x, y=q.popleft()
        for i in range(4):
            nx, ny=x+dx[i], y+dy[i]
            if 0<=nx<n and 0<=ny<m :
                if maps[nx][ny]=='L' and visit[nx][ny]==0:
                    q.append([nx, ny])
                    # 보물은 서로 간에 최단 거리로 이동하는데 있어 가장 긴 시간이 걸리는 육지 두 곳에 있음
                    visit[nx][ny] = visit[x][y] + 1
                    time=max(visit[nx][ny], time)

    return time-1


time=0

for i in range(n) :
    for j in range(m) :
        #가장 자리가 아닌 경우는 탐색 X
        '''
        if i>0 and i+1<n :
            if maps[i-1][j]=='L'and maps[i+1][j]=='L':
                continue
        if j>0 and j+1<m :
            if maps[i][j-1]=='L' and maps[i][j+1]=='L':
                continue
        '''
        if(maps[i][j]=='L'):
            time=max(bfs(i, j), time)

print(time)