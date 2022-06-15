### 내꺼 ###
import sys
from collections import deque
input = sys.stdin.readline
w,h = map(int,input().split())
graphs = []
points=[]
for i in range(h):
    graphs.append(list(input().strip()))
    for j in range(w):
        if graphs[i][j]=='C':
            points.append([i,j])

def bfs(x,y):
    global min_mirror
    q=deque([[x,y,0,0],[x,y,1,0],[x,y,2,0],[x,y,3,0]])
    while q:
        x, y, dir, mirror = q.popleft()
        if mirror >= min_mirror: continue
        if x == points[1][0] and y == points[1][1]:
            # 도착
            min_mirror = min(min_mirror, mirror)
            continue
        for d in range(4):
            if d == (dir + 2) % 4:
                # 180도로 이동하는 것이라 제외
                continue
            nx = x + dx[d];
            ny = y + dy[d];
            if not (-1 < nx < h and -1 < ny < w) or graphs[nx][ny] == '*':
                # 갈 수 없는 곳 : 경계선, 벽
                continue
            if d == dir:
                q.append([nx, ny, d, mirror])
            elif mirror+1 >= min_mirror: continue
            else:
                q.append([nx, ny, d, mirror + 1])

dx=[-1,0,+1,0]
dy=[0,+1,0,-1]
min_mirror=10000

x,y = points[0]
bfs(x,y)
print(min_mirror)

### 참고 ###
from sys import stdin
input = stdin.readline
from collections import deque

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def bfs():
    check = [[float('inf')] * W for _ in range(H)]
    check[sr][sc] = -1
    Q = deque([(sr, sc)])
    while Q:
        r, c = Q.popleft()
        if (r, c) == (gr, gc):
            return check[gr][gc]

        # 4방향으로 각각 직진
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            while True:
                if not (0 <= nr < H and 0 <= nc < W):   # 격자 벗어나거나
                    break
                if A[nr][nc] == "*":                    # 벽 만나면 break
                    break
                if check[nr][nc] < check[r][c] + 1:     # 이동할 위치에 있는 거울이 현재까지 사용한 거울+1보다 작으면 갱신 X
                    break
                Q.append((nr, nc))                      # 새 위치 이동
                check[nr][nc] = check[r][c] + 1
                nr += dr[i]
                nc += dc[i]

# main
W, H = map(int, input().split())
A, C = [], []
sr, sc, gr, gc = 0, 0, 0, 0
for i in range(H):
    A.append(list(input().strip()))
    for j in range(W):
        if A[i][j] == "C":
            C.append((i, j))
(sr, sc), (gr, gc) = C
print(bfs())