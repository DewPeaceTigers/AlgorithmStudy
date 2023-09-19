import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
dr = [-1,0,1,0]
dc = [0,-1,0,1]
def isOut(r,c):
    return not(0<r<h-1 and 0<c<w-1);
for _ in range(T):
    answer = -1
    w, h  = map(int,input().split())
    boards = [list(input().rstrip()) for _ in range(h)]
    fires = [[int(1e9)]*w for _ in range(h)]
    f = deque()
    sx,sy = 0,0
    for i in range(h):
        for j in range(w):
            if boards[i][j]=='@':
                sx,sy = i,j
            if boards[i][j]=='*':
                f.append([i,j])
                fires[i][j] = 0
    while f:
        x,y = f.popleft()
        for d in range(4):
            nx = x+dr[d]
            ny = y+dc[d]
            if not(-1<nx<h and -1<ny<w) or fires[nx][ny] != int(1e9) or boards[nx][ny]=="#": continue
            f.append([nx,ny])
            fires[nx][ny] = fires[x][y]+1
    q = deque([[sx,sy,0]]) # 상근 위치, 시간
    while q:
        r, c, t = q.popleft()
        if isOut(r,c):
            answer = t+1
            break
        for d in range(4):
            nr = r+dr[d]
            nc = c+dc[d]
            if fires[nr][nc] <= t+1 : continue
            if boards[nr][nc]=='.':
                q.append([nr,nc,t+1])
                boards[nr][nc]="@"

    print(answer if answer!=-1 else "IMPOSSIBLE")
