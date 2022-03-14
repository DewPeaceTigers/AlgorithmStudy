"""
재귀를 쓰면 파이썬 재귀 Limit에 걸리기 때문에
bfs를 사용한다.

연결되있는 부분의 개수를 구하면 된다.
"""
import sys
from collections import deque
input = sys.stdin.readline


t=int(input())

def bfs(x,y):
    dx=[+1,0,-1,0]
    dy=[0,+1,0,-1]
    arr[x][y]=0
    q=deque([(x,y)])

    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if (-1<nx<m and -1<ny<n) and arr[nx][ny]==1:
                q.append([nx,ny])
                arr[nx][ny]=0


for _ in range(t):
    m,n,k=map(int,input().split())
    arr=[[0]*n for _ in range(m)]
    for _ in range(k):
        x,y=map(int,input().split())
        arr[x][y]=1
    worm=0
    for i in range(m):
        for j in range(n):
            if arr[i][j]==1:
                worm+=1
                bfs(i,j)
    print(worm)
