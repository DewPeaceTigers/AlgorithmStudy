import sys
from collections import deque
read = sys.stdin.readline

def bfs():
    q = deque()
    q.append(artic[0])

    visited = [[False] * M for _ in range(N)]
    visited[artic[0][0]][artic[0][1]] = True

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    selected_iceberg = 0  # 탐색한 빙산
    reduce = []

    # 녹일 빙산 탐색
    while q:
        x, y = q.popleft()

        selected_iceberg += 1
        cnt = 0  # 인접한 바다 개수

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if arr[nx][ny] == 0:
                    cnt += 1
                elif arr[nx][ny] > 0 and not visited[nx][ny]:  # 육지인 경우
                    visited[nx][ny] = True
                    q.append((nx, ny))

        if cnt != 0:
            reduce.append((x, y, cnt))

    # 녹이기
    for x, y, h in reduce:
        arr[x][y] = arr[x][y] - h if arr[x][y] - h > 0 else 0
        if arr[x][y] == 0 and (x, y) in artic:
            artic.remove((x, y))

    return selected_iceberg

# 입력
N, M = map(int, read().split())
arr = [list(map(int, read().split())) for _ in range(N)]

# 풀이
answer = 0
artic = []  # 빙산

for x in range(1, N):
    for y in range(1, M):
        if arr[x][y] != 0:
            artic.append((x, y))

while True:
    # 덩어리가 2개 이상인 경우
    if len(artic) != bfs():
        break

    answer += 1

    if sum(map(sum, arr[1:-1])) == 0:  # 빙하가 다 녹을때까지 덩어리가 1개
        answer = 0
        break

# 출력
print(answer)