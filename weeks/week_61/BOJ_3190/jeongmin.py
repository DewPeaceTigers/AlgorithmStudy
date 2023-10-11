import sys
from collections import deque

N = int(input())
K = int(input())

# 사과 위치 표시
apple = [[False]*N for _ in range(N)]
for _ in range(K):
    r, c = map(int, input().split())
    apple[r-1][c-1] = True

# 방향 : 우, 하, 좌, 상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 게임 수행 시간
time = 0
# 뱀의 방향
d = 0
# 뱀의 몸 위치
snake_pos = deque([(0, 0)])
snake = [[False]*N for _ in range(N)]
snake[0][0] = True

# 게임 종료 여부
finish = False

# 뱀의 방향 전환 정보
dir_change = deque()
for _ in range(int(input())):
    X, C = input().split()
    dir_change.append((int(X), 3 if C == 'L' else 1))


def move():
    # 몸의 길이 늘림
    x, y = snake_pos[-1]
    # 머리를 다음칸에 위치
    hx = x + dx[d]
    hy = y + dy[d]

    # 벽이나 자기자신의 몸과 부딪히면 게임 끝
    if hx < 0 or hx >= N or hy < 0 or hy >= N or snake[hx][hy]:
        return False

    # 이동한 칸에 사과가 있다면
    if apple[hx][hy]:
        # 칸에 있는 사과 없어짐
        apple[hx][hy] = False

    # 이동한 칸에 사과가 없다면
    else:
        # 꼬리 위치한 칸 비워줌
        tx, ty = snake_pos.popleft()
        snake[tx][ty] = False

    snake_pos.append((hx, hy))
    snake[hx][hy] = True

    return True


X, C = dir_change[0]
while True:
    time += 1

    if not move():
        break

    # 게임 시작 시간으로부터 X초가 끝난 뒤에 방향 전환
    if time == X:
        d = (d+C) % 4
        dir_change.popleft()

        if dir_change:
            X, C = dir_change[0]

print(time)
