from collections import deque


def solution(maps):
    answer = []

    N, M = len(maps), len(maps[0])

    # 상, 하, 좌, 우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # 방문체크
    visited = [[False]*M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if maps[i][j] != 'X' and not visited[i][j]:
                # 최대 며칠 머물 수 있는지
                days = int(maps[i][j])

                q = deque()
                q.append((i, j))
                visited[i][j] = True

                while q:
                    x, y = q.popleft()

                    for d in range(4):
                        nx = x + dx[d]
                        ny = y + dy[d]

                        # 경계확인, 방문체크
                        if nx < 0 or nx >= N or ny < 0 or ny >= M or visited[nx][ny]:
                            continue

                        if maps[nx][ny] == 'X':
                            continue

                        days += int(maps[nx][ny])
                        visited[nx][ny] = True
                        q.append((nx, ny))

                answer.append(days)

    # 오름차순
    answer.sort()
    if not answer:
        answer = [-1]

    return answer
