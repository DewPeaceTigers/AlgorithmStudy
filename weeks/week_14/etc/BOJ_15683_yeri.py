import sys
from copy import deepcopy

input=sys.stdin.readline

n,m=map(int,input().split())
box=[list(map(str,input().split())) for _ in range(n)]
min_cnt=int(1e9)
dirs={'1':[[[+1,0]],[[0,+1]],[[-1,0]],[[0,-1]]],'2':[[[-1,0],[+1,0]],[[0,-1],[0,+1]]],'3':[[[0,-1],[+1,0]],[[+1,0],[0,+1]],[[0,+1],[-1,0]],[[-1,0],[0,-1]]],'4':[[[-1,0],[0,-1],[+1,0]],[[0,-1],[+1,0],[0,+1]],[[+1,0],[-1,0],[0,+1]],[[0,-1],[0,+1],[-1,0]]],'5':[[[-1,0],[0,-1],[+1,0],[0,+1]]]}
def dfs(stack,box):
    global min_cnt
    if not stack:
        # 모든 감시 카메라에 대해 적용했음
        cnt=0
        for b in box:
            cnt+=b.count('0')
        min_cnt=min(min_cnt,cnt)
    else:
        x,y=stack.pop()
        for dir in dirs[box[x][y]]:
            temp=deepcopy(box)
            for dx,dy in dir:
                nx,ny=x,y
                while True:
                    nx+=dx; ny+=dy;
                    if not(-1<nx<n and -1<ny<m) or temp[nx][ny]=='6':
                        # 벽을 만남
                        break
                    elif temp[nx][ny] in list(dirs.keys()):
                        continue
                    else:
                        temp[nx][ny]="#"
            dfs(deepcopy(stack),temp)
stack=[]
for i,bs in enumerate(box):
    for j,b in enumerate(bs):
        if b in list(dirs.keys()):
            stack.append([i,j])
dfs(stack,deepcopy(box))
print(min_cnt)