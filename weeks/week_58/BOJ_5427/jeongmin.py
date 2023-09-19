import sys
from collections import deque

input = sys.stdin.readline

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(int(input())):
    # 빌딩 지도의 너비와 높이
    w, h = map(int, input().split())

    building = [list(input().rstrip()) for _ in range(h)]

    # 방문 배열
    visited = [[False]*w for _ in range(h)]

    # 상근이의 위치
    sx, sy = 0, 0

    # 불이 붙은 칸 표시
    fire = [[False]*w for _ in range(h)]
    f_pos = []

    for i in range(h):
        for j in range(w):
            if building[i][j] == '@':
                sx, sy = i, j
                visited[i][j] = True
            elif building[i][j] == '*':
                f_pos.append((i, j))
                fire[i][j] = True

    q = deque()
    q.append((sx, sy, 0))

    # 탈출했는지 여부
    escape = False

    # 얼마만에 빌딩을 탈출했는지
    answer = 0

    while q:
        nfire = []
        # 불이 붙으려는 칸 표시
        for fx, fy in f_pos:
            for i in range(4):
                nfx = fx + dx[i]
                nfy = fy + dy[i]

                # 경계를 벗어나거나 벽인 경우
                if nfx < 0 or nfx >= h or nfy < 0 or nfy >= w or building[nfx][nfy] == '#':
                    continue

                if fire[nfx][nfy]:
                    continue

                fire[nfx][nfy] = True
                nfire.append((nfx, nfy))
        f_pos = nfire
        # print("불위치!!", f_pos)

        cnt = len(q)
        while cnt > 0:
            x, y, time = q.popleft()
            # print("상근", x, y)

            if x == 0 or x == h - 1 or y == 0 or y == w - 1:
                escape = True
                answer = time + 1
                break

            # 상근이 이동
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                # 경계를 벗어난 경우 탈출 가능!
                if nx < 0 or nx >= h or ny < 0 or ny >= w:
                    continue

                # 방문한 곳인 경우, 벽이거나 불이 붙어있는 경우는 넘어감
                if visited[nx][ny] or building[nx][ny] == '#' or fire[nx][ny]:
                    continue

                visited[nx][ny] = True
                q.append((nx, ny, time+1))
            cnt -= 1

        if escape:
            break

    print(answer if escape else "IMPOSSIBLE")
