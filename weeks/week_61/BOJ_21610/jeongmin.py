import sys

input = sys.stdin.readline

N, M = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(N)]

# 방향 : ↙, ←, ↖, ↑, ↗, →, ↘, ↓
dx = [1, 0, -1, -1, -1, 0, 1, 1]
dy = [-1, -1, -1, 0, 1, 1, 1, 0]

# 구름 초기 위치 (인덱스이므로 -1)
cloud_pos = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]


def move_cloud():  # 구름 이동
    global d, s

    for x, y in cloud_pos:
        nx = x + dx[d % 8]*s
        ny = y + dy[d % 8]*s

        # 이동을 할 때는 경계를 넘어갈 수 있음
        nx = nx % N
        ny = ny % N

        # 바구니 물의 양 1 증가
        A[nx][ny] += 1
        # 비 내리고 구름 사라짐
        rain[nx][ny] = True
        rain_pos.append((nx, ny))


def water_copy_bug():  # 물복사버그 마법
    global N

    # 비 내린 위치의 대각선 방향으로 거리가 1인 칸 확인
    for x, y in rain_pos:
        for i in range(0, 8, 2):
            nx = x + dx[i]
            ny = y + dy[i]

            # 경계를 넘어가면 안됨
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue

            # 물이 있으면 (x, y) 위치 바구니 물의 양 +1
            if A[nx][ny] > 0:
                A[x][y] += 1


def create_cloud():  # 구름 생성
    global N

    cloud_pos.clear()
    for r in range(N):
        for c in range(N):
            if A[r][c] >= 2 and not rain[r][c]:
                cloud_pos.append((r, c))
                A[r][c] -= 2


for _ in range(M):
    d, s = map(int, input().split())

    # 비 내린 위치 저장
    rain_pos = []
    rain = [[False]*N for _ in range(N)]

    move_cloud()
    water_copy_bug()
    create_cloud()

# 바구니에 들어있는 물의 양의 합
answer = 0
for r in range(N):
    answer += sum(A[r])
print(answer)
