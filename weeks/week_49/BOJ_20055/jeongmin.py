"""
1번 : 올리는 위치
N번 : 내리는 위치

[로봇을 옮기는 과정]

1. 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전
2. 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동
   만약 이동할 수 없다면 가만히 있음   
   * 로봇이 이동할 수 있는 경우
    - 이동하려는 칸에 로봇 없음
    - 이동하려는 칸의 내구도 >= 1
3. 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇 올림
4. 내구도가 0인 칸의 개수가 K개 이상이면 과정 종료, 그렇지 않으면 다시 1번으로

"""

from collections import deque
import sys 

input = sys.stdin.readline 

N, K = map(int, input().split())
A = list(map(int, input().split()))

belt = deque(A)
robot = deque([False]*N)

# 수행되는 단계 저장
step = 0

while True:
    # 수행되는 단계 (처음이 1) 
    step += 1

    # 1. 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전
    belt.rotate(1)
    robot.rotate(1)
    # N번 위치의 로봇은 내림
    robot[-1] = False

    # 2. 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동
    # 로봇이 존재하면
    if sum(robot)>0:
        # 뒤에서부터 로봇 이동
        for i in range(N-2, -1, -1):
            if robot[i] and not robot[i+1] and belt[i+1]>=1:
                robot[i+1]= True
                robot[i] = False
                belt[i+1] -= 1
        # N번 위치의 로봇은 내림
        robot[-1] = False
        
    # 3. 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇 올림
    if not robot[0] and belt[0] >= 1:
        robot[0] = True
        belt[0] -= 1

    # 4. 내구도가 0인 칸의 개수가 K개 이상이면 과정 종료, 그렇지 않으면 다시 1번으로
    if belt.count(0) >= K:
        break

print(step)