import sys

input = sys.stdin.readline

N, M, x, y, K = map(int, input().split())

board = [list(map(int, input().split())) for i in range(N)]

# 남, 동, 서, 북
dx = [1, 0, 0, -1]
dy = [0, 1, -1, 0]

# 전개도
dice = [0, 0, 0, 0, 0, 0]

for k in list(map(int, input().split())):
    nx = x + dx[k%4]
    ny = y + dy[k%4]

    # 바깥으로 이동하는 경우 - 명령 무시하기
    if nx<0 or N<=nx or ny<0 or M<= ny:
        continue

    # 동
    if k == 1:
        dice = [dice[3], dice[1], dice[0], dice[5], dice[4], dice[2]]
    # 서
    elif k == 2:
        dice = [dice[2], dice[1], dice[5], dice[0], dice[4], dice[3]]
    # 남
    elif k == 3:
        dice = [dice[1], dice[5], dice[2], dice[3], dice[0], dice[4]]
    # 북
    else:
        dice = [dice[4], dice[0], dice[2], dice[3], dice[5], dice[1]]

    x, y = nx, ny
    # 이동한 칸에 쓰여 있는 수가 0이면
    if board[x][y] == 0:
        # 주사위 바닥면에 쓰여있는 숫자가 지도에 복사됨
        board[x][y] = dice[5]
    # 0이 아닌 경우
    else:
        dice[5] = board[x][y]
        board[x][y] = 0
    print(dice[0])