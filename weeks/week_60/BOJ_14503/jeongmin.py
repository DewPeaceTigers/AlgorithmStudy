import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

# 로봇 청소기가 있는 칸의 좌표, 처음에 로봇 청소기가 바라보는 방향
r, c, d = map(int, input().split())

# 방의 상태
room = [list(map(int, input().split())) for _ in range(N)]

# 방향
# 0: 북쪽, 1: 동쪽, 2: 남쪽, 3: 서쪽
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

q = deque()
q.append((r, c, d))


def boundary_check(x, y):  # 경계 체크
    global N, M
    if x < 0 or x >= N or y < 0 or y >= M:
        return False
    return True


# 청소하는 영역의 개수
clean_cnt = 0
while q:
    x, y, d = q.popleft()

    # 현재 칸이 청소되지 않은 경우, 현재 칸 청소
    # 청소한 칸은 2로 표시
    if room[x][y] == 0:
        room[x][y] = 2
        clean_cnt += 1

    blank = False
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 경계 확인
        if not boundary_check(nx, ny):
            continue

        # 청소되지 않은 빈칸인 경우
        if room[nx][ny] == 0:
            blank = True
            break

    # 주변 4칸 중 청소되지 않은 빈칸이 없는 경우
    if not blank:
        # 바라보는 방향 유지
        # 뒤쪽 칸
        nx = x + dx[(d+2) % 4]
        ny = y + dy[(d+2) % 4]

        # 뒤쪽 칸이 벽이라면 작동 멈춤
        if room[nx][ny] == 1:
            break

        # 후진 가능하면 후진하고 1번으로 돌아감
        q.append((nx, ny, d))

    # 주변 4칸 중 청소되지 않은 빈칸이 있는 경우
    else:
        # 반시계 방향으로 90도 회전
        d = (d+3) % 4

        # 바라보는 방향을 기준으로 앞쪽 칸
        nx = x + dx[d]
        ny = y + dy[d]

        # 청소되지 않은 빈칸인 경우 한 칸 전진
        if boundary_check(nx, ny) and room[nx][ny] == 0:
            q.append((nx, ny, d))
        else:
            q.append((x, y, d))

print(clean_cnt)
