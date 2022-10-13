"""
연구소의 상태가 주어졌을 때, 모든 빈 칸에 바이러스를 퍼뜨리는 최소 시간 구하기
"""
import sys
from itertools import combinations
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

board = [list(map(int, input().split())) for i in range(N)]
frame = [[0] * N for i in range(N)]

blank_cnt = 0
virus = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 2:
            virus.append((i, j))

        elif board[i][j] == 0:
            blank_cnt += 1


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

answer, time = 1e9, 0
if blank_cnt == 0:
    answer = 0


def spread():
    global answer, time

    visited = [[-1]*N for _ in range(N)]
    for x, y in case:
        visited[x][y] = 0

    q = deque(case)

    time, virus_cnt = 0, 0
    while q:
        x, y = q.popleft()

        # print(time, "[", x, y, "]")
        ######################################################

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            # 경계를 벗어나는 경우
            if nx < 0 or nx >= N or ny < 0 or ny >= N or visited[nx][ny] != -1:
                continue

            # 빈칸이거나, 비활성 바이러스가 있는 곳인 경우
            if board[nx][ny] == 0 or board[nx][ny] == 2:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))

                if board[nx][ny] == 0:
                    virus_cnt += 1
                    time = visited[nx][ny]

                # 답이 될 수 없는 경우는 리턴
                if time >= answer:
                    return False

    # for i in range(N):
    #     print(*visited[i])
    # print(blank_cnt, virus_cnt)
    # print()

    # 모든 빈칸에 바이러스가 퍼진 경우 True, 아닌 경우 False 리턴
    return blank_cnt == virus_cnt


if answer != 0:
    cases = combinations(virus, M)
    for case in cases:
        if spread():
            # print("걸린 시간", time)
            answer = min(answer, time)

print(answer if answer < 1e9 else -1)