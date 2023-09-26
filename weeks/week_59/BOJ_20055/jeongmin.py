from collections import deque
import sys

N, K = map(int, input().split())

# 컨베이어 벨트 내구도
belt = deque(list(map(int, input().split())))

# 로봇 정보
robot = [False] * N

# 내구도가 0인 칸의 개수
zero_cnt = 0


def rotate_robot():  # 로봇 회전
    global N

    # 인덱스이므로 하나씩 줄여서 생각
    for i in range(N-1, 0, -1):
        # 로봇이 있다면 한칸 이동
        if robot[i-1]:
            robot[i] = True
            robot[i-1] = False

    # 내리는 위치에 도달하면 그 즉시 내림
    robot[N-1] = False


def move_robot():  # 로봇 이동
    global zero_cnt, N

    # 이동하려는 칸에 로봇이 없으며, 그 칸에 내구도가 1 이상 남아 있어야 함
    for i in range(N-1, 0, -1):
        # 그 전 위치에 로봇이 있다면
        if not robot[i-1]:
            continue

        if robot[i] or belt[i] < 1:
            continue

        # 로봇 움직임
        robot[i] = True
        robot[i-1] = False

        # 칸의 내구도 감소
        belt[i] -= 1

        # 칸의 내구도가 0이 되면 값 업데이트
        if belt[i] == 0:
            zero_cnt += 1

    # 내리는 위치에 도달하면 그 즉시 내림
    robot[N-1] = False


# 몇 단계를 진행하는지 저장
step = 1
while True:
    # 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전
    # 벨트 회전
    belt.rotate(1)
    # 로봇 회전
    rotate_robot()

    # 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동
    move_robot()

    # 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올림
    if belt[0] > 0:
        robot[0] = True
        belt[0] -= 1

        if belt[0] == 0:
            zero_cnt += 1

    # 내구도가 0인 칸의 개수가 K개 이상이라면 과정 종료
    if zero_cnt >= K:
        break

    step += 1

print(step)
