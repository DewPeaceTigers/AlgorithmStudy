import sys
from collections import deque

input = sys.stdin.readline

M, N, K = map(int, input().split())

# 1: 직사각형 내부, 0 : 직사각형 내부가 아닌 경우, -1 : 방문 처리
paper = [[0]*N for _ in range(M)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 분리된 영역의 넓이 저장
answer = []


def area(a, b):
    count = 1
    q = deque()
    q.append((a, b))
    paper[a][b] = -1

    while q:
        r, c = q.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if nr < 0 or M <= nr or nc < 0 or N <= nc:
                continue

            if paper[nr][nc] == 0:
                count += 1
                q.append((nr, nc))

                # 방문 처리
                paper[nr][nc] = -1

    answer.append(count)


for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())

    for r in range(y1, y2):
        for c in range(x1, x2):
            if paper[r][c] == 0:
                paper[r][c] = 1


for i in range(M):
    for j in range(N):
        # 직사각형 내부인 경우 or 방문한 곳인 경우는 제외
        if paper[i][j] == 0:
            area(i, j)

answer.sort()
print(len(answer))
print(*answer)