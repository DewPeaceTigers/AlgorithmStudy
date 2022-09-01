from collections import deque

N, L, R = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(N)]

# 상, 하, 좌, 우 확인
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

lock = [[True] * N for _ in range(N)]
move_cnt = 0
while True:
    # 인구 이동이 있었는지
    move = False

    visited = [[False] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            # 방문했던 곳이라면 넘어감
            if lock[i][j] or visited[i][j]: continue

            # 연합국 구하기
            countries = []    # 연합국 위치
            population = 0  # 연합의 인구수
            cnt = 0         # 연합을 이루고 있는 칸 수

            q = deque()
            q.append((i, j))
            visited[i][j] = True

            while q:
                x, y = q.popleft()
                population += A[x][y]
                countries.append((x, y))
                cnt += 1

                # 인접 국가 확인
                for d in range(4):
                    nx = x+dx[d]
                    ny = y+dy[d]

                    # 경계를 넘어가거나 방문했던 곳인 경우
                    if nx<0 or N<=nx or ny<0 or N<=ny or visited[nx][ny]:
                        continue

                    # 두 나라의 인구 차이가 L명 이상, R명 이하라면
                    if L <= abs(A[x][y]-A[nx][ny]) <= R:
                        # 인구 이동 발생
                        move = True

                        # 연합국 리스트 추가
                        q.append((nx, ny))
                        visited[nx][ny] = True
                        lock[nx][ny] = False

            if cnt == 1:
                continue

            lock[i][j] = True
            # 연합국이 있는 경우 인구 이동
            avg = population//cnt
            for c in countries:
                A[c[0]][c[1]] = avg

    # 더 이상 인구 이동이 없으면 종료
    if not move:
        break

    move_cnt += 1

print(move_cnt)