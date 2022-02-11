import sys
from collections import deque
input = sys.stdin.readline
n,m=map(int,input().split())
boxes=[list(input().strip()) for _ in range(n)]
print(boxes)

def bfs():
    cnt=0
    queue=deque([(0,0)])
    boxes[0][0]=1
    visit=[(0,0)]
    dx=[0,+1,0,-1]
    dy=[-1,0,+1,0]
    while queue:
        x,y=queue.popleft()
        cnt+=1
        if x==n-1 and y==m-1 : break
        for i in range(4):
            nx=x+dx[i]; ny=y+dy[i];
            if -1<nx<n and -1<ny<m and boxes[nx][ny]=='1':
                boxes[nx][ny]= boxes[x][y]+1
                queue.append((nx,ny))
                visit.append((nx,ny))
    print(boxes[n-1][m-1])

bfs()
# for box in boxes:
#     print(box)