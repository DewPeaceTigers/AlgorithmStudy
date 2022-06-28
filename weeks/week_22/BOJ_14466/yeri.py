import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline

n,k,r = map(int,input().split())
routes = [[[] for _ in range(n)] for _ in range(n)]
for _ in range(r):
    x1,y1,x2,y2 = map(int,input().split())
    routes[x1-1][y1-1].append([x2-1,y2-1])
    routes[x2-1][y2-1].append([x1-1,y1-1])

cows=[]
cow_map=[[False]*n for _ in range(n)]
for _ in range(k):
    x,y = map(int,input().split())
    cows.append([x-1,y-1])
    cow_map[x-1][y-1]=True

dx=[0,0,-1,+1]
dy=[-1,+1,0,0]
def bfs(start):
    global cow_map
    count=0 # 길을 건너지 않고 만날 수 있는 수
    q = deque([start])
    visit = [[False]*n for _ in range(n)]
    visit[start[0]][start[1]]=True
    while q:
        x,y = q.popleft()
        for d in range(4):
            nx=x+dx[d]
            ny=y+dy[d]
            if not(-1<nx<n and -1<ny<n): continue # 경계선 밖
            if [nx,ny] in routes[x][y]: continue # 길로 이동이 필요한 곳
            if visit[nx][ny]: continue # 이미 방문한 곳
            visit[nx][ny]=True
            q.append([nx,ny])
            if cow_map[nx][ny]: # 소라면
                count += 1
    return count
answer= 0
for start in cows:
    if cow_map[start[0]][start[1]]:
        k-=1
        cow_map[start[0]][start[1]]=False
        count = bfs(start)
        answer+= k-count
print(answer)