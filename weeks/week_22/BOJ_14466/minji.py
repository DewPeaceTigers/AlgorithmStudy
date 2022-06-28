import sys
from collections import deque

N,K,R = map(int, sys.stdin.readline().split())

load = [[[] for _ in range(N+1)] for _ in range(N+1)]
cow_map = [[False for _ in range(N+1)] for _ in range(N+1)]
cow_list = []

for i in range(R):
    r,c,rr,cc = map(int, sys.stdin.readline().split())
    load[r][c].append([rr,cc])
    load[rr][cc].append([r,c])

for i in range(K):
    r, c = map(int, sys.stdin.readline().split())
    cow_list.append([r,c])
    cow_map[r][c] = True

dy = [-1,0,1,0]
dx = [0,1,0,-1]

result = 0
for r,c in cow_list:
    if cow_map[r][c]:
        visited = [[True for _ in range(N+1)] for _ in range(N+1)]
        que = deque()
        que.append([r,c])
        cow_map[r][c] = False
        cnt = 0
        K -= 1
        while que:
            y,x = que.popleft()
            for u in range(4):
                yy = y + dy[u]
                xx = x + dx[u]
                if 1<=yy<=N and 1<=xx<=N and visited[yy][xx]:
                    if [yy,xx] not in load[y][x]:
                        que.append([yy,xx])
                        visited[yy][xx] = False
                        if cow_map[yy][xx]:
                            cnt += 1
        result += K-cnt
print(result)