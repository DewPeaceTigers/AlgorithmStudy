'''
풀이 봄
벽에 닿기전까지 이동하는 방법을 몰라서 봄

'''
'''
from collections import deque

n, m=map(int, input().split())
boards=[]
visit=[[[[0] * m for _ in range(n)]for _ in range(m)]for _ in range(n)]
dx=[0, 0, -1, 1]
dy=[1, -1, 0, 0]
def move(x, y, dir) :
    cnt=0
    while boards[x+dx[dir]][y+dy[dir]]!='#' and boards[x][y]!='0' :
        x+=dx[dir]
        y+=dy[dir]
        cnt+=1
    return x, y, cnt

def bfs() :
    while q:
        rx, ry, bx, by, count=q.popleft()
        if count>10 :
            break
        for i in range(4):
            nrx, nry, r=move(rx, ry, i)
            nbx, nby, b=move(bx, by, i)
            if boards[nbx][nby]!='0' :
                if boards[nrx][nry]=='0' :
                    print(count)
                    exit(0)
                if nrx==nbx and nry==nby :
                    if r>b :
                        nrx-=dx[i]
                        nry-=dy[i]
                    else:
                        nbx-=dx[i]
                        nbx-=dy[i]
                if visit[nrx][nry][nbx][nby]==0 :
                    visit[nrx][nry][nbx][nby]=1
                    q.append([nrx, nry, nbx, nby, count+1])

    print(-1)
    return


for i in range(n) :
    a=list(input())
    boards.append(a)
    for j in range(m) :
        if a[j]=='R' :
            r_x, r_y=i, j
        if a[j]=='B' :
            b_x, b_y=i, j

q = deque()
q.append([r_x, r_y, b_x, b_y, 1])
visit[r_x][r_y][b_x][b_y]=1
bfs()
'''
from collections import deque
n, m = map(int, input().split())
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
visit = [[[[False] * m for i in range(n)] for i in range(m)] for i in range(n)]
s = []
def move(i, j, dx, dy):
    c = 0
    while s[i + dx][j + dy] != "#" and s[i][j] != "O":
        i += dx
        j += dy
        c += 1
    return i, j, c
def bfs():
    while q:
        ri, rj, bi, bj, d = q.popleft()
        if d > 10:
            break
        for i in range(4):
            nri, nrj, rc = move(ri, rj, dx[i], dy[i])
            nbi, nbj, bc = move(bi, bj, dx[i], dy[i])
            if s[nbi][nbj] != "O":
                if s[nri][nrj] == "O":
                    print(d)
                    return
                if nri == nbi and nrj == nbj:
                    if rc > bc:
                        nri -= dx[i]
                        nrj -= dy[i]
                    else:
                        nbi -= dx[i]
                        nbj -= dy[i]
                if not visit[nri][nrj][nbi][nbj]:
                    visit[nri][nrj][nbi][nbj] = True
                    q.append([nri, nrj, nbi, nbj, d + 1])
    print(-1)
for i in range(n):
    a = list(input())
    s.append(a)
    for j in range(m):
        if a[j] == "R":
            ri, rj = i, j
        if a[j] == "B":
            bi, bj = i, j
q = deque()
q.append([ri, rj, bi, bj, 1])
visit[ri][rj][bi][bj] = True
bfs()