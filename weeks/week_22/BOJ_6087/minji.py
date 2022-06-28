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