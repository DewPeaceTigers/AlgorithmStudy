import sys
from collections import deque
input = sys.stdin.readline

boards = [list(input())[:-1] for _ in range(12)]
answer=0
dx = [-1,0,1,0]
dy = [0,-1,0,1]

semi=-1
while semi!=0:
    visit = [[False]*6 for _ in range(12)]
    semi = 0
    for i in range(12):
        for j in range(6):
            if not visit[i][j] and boards[i][j]!='.':
                q = deque([[i,j]])
                visit[i][j] = True
                now = boards[i][j]
                cands = [[i,j]]
                while q:
                    x,y = q.popleft()

                    for d in range(4):
                        nx = x+dx[d]
                        ny = y+dy[d]
                        if not(-1<nx<12 and -1<ny<6): continue
                        if not visit[nx][ny] and boards[nx][ny] == now:
                            visit[nx][ny] = True
                            cands.append([nx,ny])
                            q.append([nx,ny])
                if len(cands)>3:
                    for x,y in cands:
                        boards[x][y]='.'
                    semi+=1
                else:
                    for x,y in cands:
                        visit[x][y]=False
    if semi!=0:
        for j in range(6):
            temp = [ boards[i][j] for i in range(12)]
            new_temp =[]
            for t in temp:
                if t!='.':
                    new_temp.append(t)
            temp = ["."]*(len(temp)-len(new_temp))+new_temp
            for i in range(12):
                boards[i][j]= temp[i]
        answer+=1
print(answer)