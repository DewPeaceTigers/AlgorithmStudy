import sys
from collections import deque

input=sys.stdin.readline

m, n, k=map(int, input().split())

dx=[0, 0, 1, -1]
dy=[1, -1, 0, 0]
                
boards=[[0]*n for _ in range(m)]
for _ in range(k) :
    x1, y1, x2, y2=map(int, input().split())
    for i in range(y1, y2) :
        for j in range(x1, x2) :
            boards[i][j]=1
            
def bfs(x, y) :
    q=deque()
    q.append([x, y])
    count=1
    while q :
        nx, ny=q.popleft()
        
        for i in range(4) :
            nx, ny=nx+dx[i], ny+dy[i]
            if 0<=nx<n and 0<=ny<m and boards[ny][nx]==0 :
                boards[ny][nx]=1
                q.append([nx, ny])
                count+=1
    return count
 
ans=[]            
for i in range(m) :
    for j in range(n) :
        if boards[i][j]==0 :
            boards[i][j]=1
            ans.append(bfs(i, j))
            
print(len(ans))
print(ans.sort())