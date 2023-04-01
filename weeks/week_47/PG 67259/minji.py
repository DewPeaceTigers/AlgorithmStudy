'''
cost를 visit 리스트가 아닌 큐에 담아야하는 이유
먼저 진행되는 방향에 따라 값이 달리질 수도 있다.
-> 방향 + 비용으로 찾아가야함
'''

from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def solution(board):
    n = len(board)

    def bfs(x, y, cost, dir):
        visit = [[int(1e9)] * n for _ in range(n)]
        visit[0][0] = 0

        queue = deque()
        queue.append((x, y, cost, dir))  # (시작X, 시작Y, 시작Cost, 시작방향)

        while queue:
            x, y, cost, dir = queue.popleft()

            if x == n - 1 and y == n - 1:
                continue

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<=nx<n and 0<=ny<n and board[nx][ny]==0:
                    if dir==i:
                        nc = cost + 100
                    else:
                        nc = cost + 600

                    if nc < visit[nx][ny]:
                        visit[nx][ny] = nc
                        queue.append((nx, ny, nc, i))

        return visit[-1][-1]

    return min(bfs(0, 0, 0, 0), bfs(0, 0, 0, 2)) #첫 시작 하, 우 비교

