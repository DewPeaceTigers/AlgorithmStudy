'''
녹는 높이?는 제일 높은 곳-1 기준으로 count
'''
import sys
from collections import deque

input=sys.stdin.readline

n=int(input())
rain=[]
max_rain=0
for i in range(n) :
    rain.append(list(map(int, input().split())))
    if max_rain < max(rain[i]) :
        max_rain=max(rain[i])
   
dx=[0, 0, 1, -1]
dy=[1, -1, 0, 0]
 
def bfs(a, b, height, visited) :
    q=deque()
    q.append([a, b])
    visited[a][b]=1
    while q:
        x, y=q.popleft()
        
        for i in range(4) :
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n and visited[nx][ny]==0 and rain[nx][ny]>height:
                visited[nx][ny]=1
                q.append([nx, ny])
     
answer=0  
for i in range(max_rain) :
    visited=[[0]*n for _ in range(n)]
    count=0
    
    for j in range(n) :
        for k in range(n) :
            if rain[j][k] > i and visited[j][k]==0 : #한덩어리 count
                bfs(j, k, i, visited) 
                count+=1
    if answer<count :
        answer=count
        
print(answer)
    
