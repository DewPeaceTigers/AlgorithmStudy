from collections import deque


def solution(board):
    answer = 0
    n = len(board)
    m = len(board[0])

    dx = [0, 0, 1, -1]
    dy = [-1, 1, 0, 0]
    rx, ry = 0, 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                rx, ry = i, j

    def bfs():
        q = deque()
        q.append([rx, ry])
        visit = [[0] * m for _ in range(n)]
        visit[rx][ry] = 1

        while q:
            x, y = q.popleft()
            if board[x][y] == 'G':
                return visit[x][y] - 1
            for i in range(4):
                nx, ny = x, y
                while True:
                    nx, ny = nx + dx[i], ny + dy[i]

                    if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 'D':
                        nx -= dx[i]
                        ny -= dy[i]
                        break
                    if (nx < 0 or nx >= n) or (ny < 0 or ny >= m):
                        nx -= dx[i]
                        ny -= dy[i]
                        break
                if visit[nx][ny] == 0:
                    visit[nx][ny] = visit[x][y] + 1
                    q.append([nx, ny])
        return -1

    answer = bfs()

    return answer