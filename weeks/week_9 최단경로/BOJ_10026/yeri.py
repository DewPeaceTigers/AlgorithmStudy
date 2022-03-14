"""
두번의 반복문을 돌아 
첫번째에선 B 개수를 따로 구하고, R,G를 합쳐서 구한다. R이나 G면 RG로 통일되게 해둠
두번째에선 B가 아닐 때만 dfs를 하여 RG를 동시에 구했다.

원래는 다 따로 구했는데 시간 초과가 나서 바꿨다.
"""
import sys
input=sys.stdin.readline
n=int(input())
box=[list(map(str,input().strip())) for _ in range(n)]

def dfs(stack,visit):
    parent_color=box[stack[0][0]][stack[0][1]]
    while stack:
        x, y = stack.pop()
        if parent_color!='B': box[x][y]='RG'
        for i in range(4):
            nx = x + dx[i];
            ny = y + dy[i]
            if (-1 < nx < n and -1 < ny < n) and (nx,ny) not in visit and box[nx][ny]==parent_color:
                if parent_color!='B': box[nx][ny]='RG'
                visit.append((nx,ny))
                stack.append((nx,ny))



# stack=[[0,0]]
dx=[+1,0,-1,0]
dy=[0,-1,0,+1]
RG=0; B=0; R=0;
visit=[]
for i in range(n):
    for j in range(n):
        if (i,j) not in visit:
            visit.append((i,j))
            if box[i][j]=='R' or box[i][j]=='G':RG+=1
            else: B+=1
            dfs([(i,j)],visit)
visit=[]
for i in range(n):
    for j in range(n):
        if (i,j) not in visit and box[i][j]!='B':
            visit.append((i,j))
            dfs([(i,j)],visit)
            R+=1

print(RG+B,R+B)