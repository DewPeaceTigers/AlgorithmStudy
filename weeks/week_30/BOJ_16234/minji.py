'''
pypy3 제출
(시간초과가 나를 힘들게 해...)
'''
import sys
from collections import deque

input=sys.stdin.readline

n, l, r=map(int, input().split())
people=[]

dx=[0, 0, -1, 1]
dy=[1, -1, 0, 0]

for _ in range(n) :
    people.append(list(map(int, input().split())))

def bfs(a, b):
    q=deque()
    q.append([a, b])
    temp=[]
    temp.append([a, b])
    while q:
        x, y=q.popleft()

        for i in range(4) :
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n and visit[nx][ny]==0 :
                if l <= abs(people[x][y]-people[nx][ny]) <= r :
                    q.append([nx, ny])
                    visit[nx][ny]=1
                    temp.append([nx, ny])
                    
    return temp

result=0
while 1:
    visit=[[0]*n for _ in range(n)]
    isChange=False
    for i in range(n) :
        for j in range(n) :
            if visit[i][j]==0 :
                visit[i][j]=1
                near_country=bfs(i, j)

                if len(near_country)>1 :
                    isChange=True
                    population=sum([people[x][y] for x, y in near_country])//len(near_country)

                    for x, y in near_country :
                        people[x][y]=population
    if isChange == False :
        break
    result+=1
    
print(result)    
                        