import sys

input = sys.stdin.readline

N, M, x, y, K = map(int, input().split())

# 지도 정보 입력
board = [list(map(int, input().split())) for _ in range(N)]

# 이동 명령 입력
move = list(map(int, input().split()))

# 방향 : 남(0), 동(1), 서(2), 북(3)
dx = [1, 0, 0, -1]
dy = [0, 1, -1, 0]

# 주사위 정보 저장 (초기값은 0)
# 전개도 상에서 (1, 2, 3, 4, 5, 6) 위치 순
# 상단 : dice[0], 바닥면 : dice[-1]
dice = [0]*6


def roll_dice(r_dir):  # 주사위 굴리기
    global dice

    if r_dir == 1:  # 동
        ndice = [dice[3], dice[1], dice[0], dice[5], dice[4], dice[2]]
    elif r_dir == 2:  # 서
        ndice = [dice[2], dice[1], dice[5], dice[0], dice[4], dice[3]]
    elif r_dir == 3:  # 북
        ndice = [dice[4], dice[0], dice[2], dice[3], dice[5], dice[1]]
    else:
        ndice = [dice[1], dice[5], dice[2], dice[3], dice[0], dice[4]]

    dice = ndice


# 이동 명령 수행
for d in move:
    # 이동할 위치
    nx = x + dx[d % 4]
    ny = y + dy[d % 4]

    # 지도의 바깥으로 이동시키려고 하는 경우 무시
    if nx < 0 or nx >= N or ny < 0 or ny >= M:
        continue

    # 주사위 이동
    x, y = nx, ny

    # 주사위 굴리기
    roll_dice(d)

    # 이동한 칸에 쓰여 있는 수가 0이면
    if board[x][y] == 0:
        # 주사위의 바닥면에 쓰여 있는 수가 칸에 복사됨
        board[x][y] = dice[-1]
    # 이동한 칸에 쓰여 있는 수가 0이 아니라면
    else:
        # 칸에 쓰여 있는 수가 주사위의 바닥면으로 복사
        dice[-1] = board[x][y]
        # 칸에 쓰여 있는 수 0이 됨
        board[x][y] = 0

    # 주사위 상단에 쓰여 있는 값 출력
    print(dice[0])
