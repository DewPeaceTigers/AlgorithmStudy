import sys
from collections import deque

input = sys.stdin.readline

# 보드의 크기 N 입력 (2 ≤ N ≤ 100)
N = int(input())

# 0: 빈칸, 1: 뱀 위치, 2: 사과 위치
board = [[0]*N for _ in range(N)]

# 사과의 개수 K (0 ≤ K ≤ 100)
K = int(input())

# 사과의 위치 입력
for _ in range(K):
    r, c = map(int, input().split())
    # 1행 1열부터 시작하므로 인덱스 -1 처리
    board[r-1][c-1] = 2

# 우하좌상 방향
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 뱀은 맨위 맨좌측에 위치
snake = deque()
snake.append((0, 0))

# 처음에 오른쪽을 향함
sd = 0

# 뱀의 방향 변환 횟수 L
L = int(input())
# 방향 변환 정보
change = dict()
for _ in range(L):
    X, C = input().split()
    change[int(X)] = C

# 게임이 몇 초 동안 진행되었는지
time = 0

# 초마다 뱀 이동
while True:
    time += 1

    x, y = snake[-1]

    # 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킴
    nx = x + dx[sd]
    ny = y + dy[sd]

    # 벽이나 자기자신의 몸과 부딪히면 게임이 끝남
    if nx < 0 or nx >= N or ny < 0 or ny >= N or board[nx][ny] == 1:
        break

    snake.append((nx, ny))

    # 이동한 칸에 사과가 없다면
    if board[nx][ny] != 2:
        # 몸길이를 줄여서 꼬리가 위치한 칸을 비워줌
        tx, ty = snake.popleft()
        board[tx][ty] = 0

    # 뱀 추가된 위치 표시
    board[nx][ny] = 1

    # print(time, "초 후, ", snake)

    if time in change:
        # 방향 변경
        if change[time] == 'L':  # 왼쪽 90도 방향
            sd = (sd+3) % 4
        else:  # 오른쪽 90도 방향
            sd = (sd+1) % 4

print(time)
