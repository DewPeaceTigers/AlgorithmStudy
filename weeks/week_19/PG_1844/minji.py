from collections import deque


def solution(maps):
    answer = 0
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    n = len(maps)
    m = len(maps[0])
    visit = [[-1] * m for _ in range(n)]
    q = deque()
    q.append((0, 0))
    visit[0][0] = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                if visit[nx][ny] == -1:
                    q.append((nx, ny))
                    visit[nx][ny] = visit[x][y] + 1

    answer = visit[-1][-1]
    return answer