'''pypy 통과'''
import sys
import copy
from collections import deque
input=sys.stdin.readline

boards=[]
n, m=map(int, input().split())
dx=[0, 0, 1, -1]
dy=[1, -1, 0, 0]
for i in range(n) :
    boards.append(list(map(int, input().split())))

#print(boards)
def wall(count):
    if count==3 :
        bfs()
        return
    for i in range(n):
        for j in range(m) :
            if boards[i][j]==0 :
                boards[i][j]=1
                wall(count+1)
                boards[i][j]=0

def bfs() :
    q=deque()
    tmp=copy.deepcopy(boards)
    for i in range(n) :
        for j in range(m) :
            if tmp[i][j]==2 :
                q.append((i, j))

    while q:
        x, y=q.popleft()
        for i in range(4) :
            nx, ny=x+dx[i], y+dy[i]

            if 0<=nx<n and 0<=ny<m and tmp[nx][ny]==0 :
                tmp[nx][ny]=2
                q.append((nx, ny))

    global section
    count=0
    for i in range(n) :
        count+=tmp[i].count(0)
    section=max(section, count)



section=0
wall(0)
print(section)