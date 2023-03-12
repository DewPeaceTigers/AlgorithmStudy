from collections import deque

import sys

input = sys.stdin.readline

R, C = map(int, input().split())

# 티떱숲의 지도
forest = [list(input().rstrip()) for _ in range(R)]

# 상, 하, 좌, 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 물 위치 저장
q_water = deque()
water = [[False]*C for _ in range(R)]

# 고슴도치 위치 저장
q_s = deque()
visited = [[False]*C for _ in range(R)]

for i in range(R):
    for j in range(C):
        if forest[i][j] == 'S':
            q_s.append((i, j))
            visited[i][j] = True
        if forest[i][j] == '*':
            q_water.append((i, j))
            water[i][j] = True

# 걸리는 시간
time = 0

# 안전하게 이동했는지 여부
safe = False

while q_s:
    time += 1

    # 비어있는 칸으로 물 확장
    tmp_water = deque()
    while q_water:
        wr, wc = q_water.popleft()

        for i in range(4):
            nr = wr + dr[i]
            nc = wc + dc[i]

            # 지도를 벗어나거나 이미 물인 경우는 넘어감
            if nr<0 or nr>=R or nc<0 or nc>=C or water[nr][nc]:
                continue

            # 돌이거나 비버의 소굴로는 이동 못함
            if forest[nr][nc] =='X' or forest[nr][nc]=='D':
                continue

            tmp_water.append((nr, nc))
            water[nr][nc] = True
    q_water = tmp_water

    # 고슴도치 이동
    tmp_s = deque()
    while q_s:
        sr, sc = q_s.popleft()

        for i in range(4):
            nr = sr + dr[i]
            nc = sc + dc[i]

            # 지도를 벗어난 경우 넘어감
            if nr < 0 or nr >= R or nc < 0 or nc >= C or visited[nr][nc]:
                continue

            if water[nr][nc] or forest[nr][nc]=='X':
                continue

            # 비버의 소굴을 찾은 경우
            if forest[nr][nc] == 'D':
                safe = True
                break

            tmp_s.append((nr, nc))
            visited[nr][nc] = True
    q_s = tmp_s

    if safe:
        break

    # 두더지가 더 이상 이동할 수 없다면
    # if not q_s:
    #     break

print(time if safe else "KAKTUS")