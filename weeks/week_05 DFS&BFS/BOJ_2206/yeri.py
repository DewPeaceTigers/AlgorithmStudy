"""
1. bfs
최단 거리, 인접 만 보고 bfs를 했다.
"""

import sys
from collections import deque
input = sys.stdin.readline
n,m=map(int,input().split())
boxes=[list(input().strip()) for _ in range(n)]
routes=[[0]*m for _ in range(n)]
def bfs():
    queue=deque([(False,0,0)]) # 벽 뿌셨는지 여부, x, y
    boxes[0][0]=-1
    routes[0][0]=1
    dx=[-1,0,+1,0]
    dy=[0,+1,0,-1]
    while queue:
        broked,x,y=queue.popleft()
        if x==n-1 and y==m-1 : break
        if x==3 and y==4: print(broked,x,y,queue)
        for i in range(4):
            nx=x+dx[i]; ny=y+dy[i];
            if -1 < nx < n and -1 < ny < m: # 범위 내
                if boxes[nx][ny] == '0':  # 0일때만 무조건 이동
                    boxes[nx][ny]=-1
                    routes[nx][ny] = (x,y)#routes[x][y] + 1
                    queue.append((broked, nx, ny))
                elif not broked and boxes[nx][ny]=='1': # 한번도 부서진 적 없어서 부서도 됨. 1도 이동
                        boxes[nx][ny] = -1
                        routes[nx][ny]= (x,y)#routes[x][y]+1
                        queue.append((True,nx,ny))

    print(routes[n-1][m-1] if routes[n-1][m-1]!=0 else -1)
bfs()
# for box in boxes:
#     print(box)
# print('--')
# for route in routes:
#     print(route)
"""
queue가 비게 되면 종료가 된다. 다른 길이 있는데도 그 길이 최단 거리라고 여기고 종료가 된다.
bfs는 가장 먼저 도달하는게 최단 거리라는 원칙이 있기에 문제 해결과 안맞다고 생각했다.

2. dfs
모든 길을 가보고 가장 최단을 찾아야 겠다는 생각을 했다.
"""
import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())

boxes=[list(map(int,input().strip())) for _ in range(n)]
#for box in boxes: print(box)
routes=[[0]*m for _ in range(n)]
routes[0][0]=1

dx=[-1,0,1,0]
dy=[0,1,0,-1]
def dfs(queue):
    global min_route
    broke,x,y=queue.popleft()
    #print(broke,x,y)
    if x==n-1 and y==m-1:
        min_route=min(routes[x][y],min_route)
        #print(min_route)
        #for route in routes:print(route)
        return
    #print('done')
    for i in range(4):
        nx=x+dx[i]; ny=y+dy[i];
        #print(nx,ny)
        if -1 < nx < n and -1 < ny < m: # 범위 내
            if boxes[nx][ny] == 0: #'0':  # 0일때만 무조건 이동
                boxes[nx][ny]=-1
                routes[nx][ny] = routes[x][y] + 1
                queue.append((broke, nx, ny))
                dfs(queue)
                #print('0 out',nx,ny,queue)
                boxes[nx][ny]=0 #'0'
                routes[nx][ny]=0
                #queue.pop()
            elif not broke and boxes[nx][ny]==1: #'1': # 한번도 부서진 적 없어서 부서도 됨. 1도 이동
                boxes[nx][ny] = -1
                routes[nx][ny]= routes[x][y]+1
                queue.append((True,nx,ny))
                dfs(queue)
                #print('1 out',nx,ny,queue)
                boxes[nx][ny] = 1 #'1'
                routes[nx][ny] = 0
                #queue.pop()

min_route=int(1e9)
dfs(deque([[False,0,0]]))
print(min_route)