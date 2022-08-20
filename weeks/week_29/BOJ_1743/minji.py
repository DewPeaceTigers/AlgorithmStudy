from collections import deque
import sys

input=sys.stdin.readline

n, m, k=map(int, input().split())
trash=[[0]*m for _ in range(n)]

dx=[0, 0, -1, 1]
dy=[1, -1 ,0, 0]

def bfs(i, j) :
    q=deque()
    q.append([i, j])
    trash[i][j]=2
    count=1
    while q :
        x, y=q.popleft()
        for k in range(4) :
            nx=x+dx[k]
            ny=y+dy[k]
            if 0<=nx<n and 0<=ny<m and trash[nx][ny]==1 :
                q.append([nx, ny])
                trash[nx][ny]=2
                count+=1
    return count
for _ in range(k) :
    x, y=map(int, input().split())
    trash[x-1][y-1]=1

answer=0    
for i in range(n) :
    for j in range(m) :
        if trash[i][j]==1 :
            result=bfs(i, j)
            answer=max(answer, result)
            
print(answer)
