import sys
from collections import deque

input=sys.stdin.readline
n, m=map(int, input().split())

boards=[]
for _ in range(n) :
    boards.append(list(map(int, input().split())))

dx=[0, 0, -1, 1]
dy=[1, -1, 0, 0]
ans=[]  
def bfs() :
    q=deque()
    q.append([0, 0])
    visited[0][0]=1
    count=0
    while q :
        x, y=q.popleft()
        for i in range(4) :
            nx=x+dx[i]
            ny=y+dy[i]
            
            if 0<=nx<n and 0<=ny<m and visited[nx][ny]==0 :
                if boards[nx][ny]==0:
                    visited[nx][ny]=1
                    q.append([nx, ny])
                elif boards[nx][ny]==1:
                    boards[nx][ny]=0
                    visited[nx][ny]=1
                    count+=1
    ans.append(count)
    return count
time=0
while 1:
    time+=1
    visited=[[0]*m for _ in range(n)]
    count=bfs()
    if count==0 :
        break
    
print(time-1)
print(ans[-2])