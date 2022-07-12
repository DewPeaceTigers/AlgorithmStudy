from collections import deque

N = int(input())

area_input = [list(map(int, input().split())) for _ in range(N)]


def check(a, b, N, k):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    if area[a][b] <= k:
        return False

    q = deque()
    q.append((a, b))
    area[a][b] = 0
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx < 0 or N <= nx or ny<0 or N<= ny:
                continue

            # 안전 영역인 경우
            if area[nx][ny] > k:
                area[nx][ny] = 0
                q.append((nx, ny))

    return True


m = -1  # 높이 최댓값 저장
for i in range(N):
    for j in range(N):
        m = max(m, area_input[i][j])

answer = 0
for k in range(m+1):
    count = 0
    area = [[area_input[i][j] for j in range(N)] for i in range(N)]

    for i in range(N):
        for j in range(N):
            if check(i, j, N, k):
                count += 1
    answer = max(count, answer)

print(answer)