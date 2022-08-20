import sys
from collections import deque

input = sys.stdin.readline

N, M, K = map(int, input().split())

garbage = [list(map(int, input().split())) for _ in range(K)]
# 음식물 쓰레기 정보 저장 ( 1: 음식물 쓰레기, 0: 아무것도 없음, -1: 방문)
path = [[0]*(M+1) for _ in range(N+1)]
for gr, gc in garbage:
    path[gr][gc] = 1

# 상, 하, 좌, 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

maxSize = 0
# 방문
for gr, gc in garbage:
    # 방문했던 곳이라면 넘어감
    if path[gr][gc]==-1:
        continue

    # 음식물 쓰레기의 크기
    q = deque()
    q.append((gr, gc))
    path[gr][gc] = -1 # 방문처리

    size = 1
    while q:
        r, c = q.popleft()

        for i in range(4):
            nr = r+dr[i]
            nc = c+dc[i]

            # 경계체크
            if nr<1 or nr>N or nc<1 or nc>M:
                continue

            # 음식물 쓰레기가 있는 곳이라면
            if path[nr][nc] == 1:
                size += path[nr][nc]
                q.append((nr, nc))
                path[nr][nc] = -1

    maxSize = max(maxSize, size)

print(maxSize)