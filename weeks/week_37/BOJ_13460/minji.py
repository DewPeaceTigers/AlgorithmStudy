import sys
from collections import deque
input=sys.stdin.readline

n, m=map(int, input().split())
maps=[]
visit=[[[[False] *m for _ in range(n)] for _ in range(m)] for _ in range(n)]

dx=[-1, 1, 0, 0]
dy=[0, 0, -1, 1]

def move(x, y, i):
    cnt=0
    while maps[x+dx[i]][y+dy[i]]!='#' and maps[x][y] !="O":
        x+=dx[i]
        y+=dy[i]
        cnt+=1
    return x, y, cnt

def bfs() :
    while q:
        rx, ry, bx, by, depth=q.popleft()
        if depth > 10 :
            break
        for i in range(4) :
            nrx, nry, rcnt=move(rx, ry, i)
            nbx, nby, bcnt=move(bx, by, i)
            if maps[nbx][nby]!="O":
                if maps[nrx][nry]=="O":
                    print(depth)
                    return
                if nrx==nbx and nry==nby :
                    if rcnt>bcnt :
                        nrx-=dx[i]
                        nry-=dy[i]
                    else:
                        nbx-=dx[i]
                        nby-=dy[i]
                if not visit[nrx][nry][nbx][nby]:
                    visit[nrx][nry][nbx][nby]=True
                    q.append([nrx, nry, nbx, nby, depth+1])
    print(-1)
for i in range(n):
    maps.append(list(input()))
    for j in range(m):
        if maps[i][j] == 'R':
            ri, rj = i, j
        elif maps[i][j] == 'B':
            bi, bj = i, j
q=deque()
q.append([ri, rj, bi, bj, 1])
visit[ri][rj][bi][bj]=True
bfs()

