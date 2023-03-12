from collections import deque


def solution(maps):
    answer = []
    days = []
    n = len(maps)
    m = len(maps[0])
    visit = [[0] * m for _ in range(n)]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def bfs(a, b):
        visit[a][b] = 1
        if maps[a][b] == 'X':
            return -1
        q = deque()
        q.append([a, b])
        cnt = int(maps[a][b])  # 식량 개수 count

        while q:
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m:
                    if maps[nx][ny] != 'X' and visit[nx][ny] == 0:  # 바다 X, 방문 X
                        visit[nx][ny] = 1
                        q.append([nx, ny])
                        cnt += int(maps[nx][ny])
        return cnt

    for i in range(n):
        for j in range(m):
            if visit[i][j] == 0:
                cnt = bfs(i, j)
                if cnt > 0:
                    answer.append(cnt)

    if len(answer) == 0:
        return [-1]

    return sorted(answer)