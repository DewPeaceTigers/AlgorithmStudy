import sys
from collections import deque

n=int(sys.stdin.readline())
k=int(sys.stdin.readline())
direction=[]
boards=[[0]*n for _ in range(n)]
dx=[0, 1, 0, -1] #우, 하, 좌, 상
dy=[1, 0, -1, 0]

for i in range(k) : #사과 위치
    x, y=map(int, sys.stdin.readline().split())
    boards[x-1][y-1]=1

l=int(sys.stdin.readline())
for i in range(l) :
    x, c=map(str, sys.stdin.readline().split())
    direction.append([int(x), c])
direction.append([10001, ''])
q=deque() #뱀이 있는 위치
q.append([0, 0])
x, y, size=0, 0, 1 #뱀 위치와 방향
time=0 #진행시간
dir=0 #0:우 1:하 2:좌 3:상
stop=False
start=1
def turn_snack(direction):
    global dir
    if direction=='L':
        dir=(dir-1)%4
    else:
        dir=(dir+1)%4

for i in range(l+1) :
    start=time+1
    for j in range(start, direction[i][0]+1):
        nx, ny=x+dx[dir], y+dy[dir]
        if nx<0 or nx>=n or ny<0 or ny>=n or [nx, ny] in q: #종료 되는 경우
            time+=1
            stop=True
            break
        if boards[nx][ny]==1 : #사과를 먹으면 꼬리는 그대로
            x, y=nx, ny
            q.append([x, y])
            boards[x][y]=0
        else: #사과 없으면 꼬리 한칸씩 줄어듬
            x, y=nx, ny
            q.popleft()
            q.append([x, y])
        time+=1
    if stop == True :
        break
    turn_snack(direction[i][1]) #뱀 회전

print(time)