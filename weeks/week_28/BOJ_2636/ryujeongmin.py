import sys
from collections import deque

input = sys.stdin.readline

H, W = map(int, input().split())

board = [[] for _ in range(H+2)]
# 판의 가장자리 추가
board[0] = [0]*(W+2)
for i in range(1, H+1):
    board[i] = [0] + list(map(int, input().split())) + [0]
board[H+1] = [0]*(W+2)

# 치즈 개수
cheeseCnt = 0
for i in range(H):
    for j in range(W):
        if board[i][j]==1:
            cheeseCnt += 1

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def melt(edge):
    v = [[0] * (W + 2) for _ in range(H + 2)]

    q = deque(edge)
    v[0][0] = 1
    c = []  # 공기와 접촉한 칸 위치 저장
    while q:
        x, y = q.popleft()

        # 인접한 곳 방문
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 경계 체크, 방문 체크
            if nx < 0 or nx >= H + 2 or ny < 0 or ny >= W + 2 or v[nx][ny] == 1:
                continue

            # 방문 표시
            v[nx][ny] = 1

            # 치즈가 있는 곳이라면
            if board[nx][ny] == 1:
                # 경계로 바꿔주기
                board[nx][ny] = 2
                c.append([nx, ny])
                continue

            q.append([nx, ny])

    return c


# 공기와 접촉한 칸(c) 구하기
boundary = [[0, 0], [0, W+1], [H+1, 0], [H+1, W+1]]

time = 0    # 치즈가 모두 녹아 없어지는 데 걸리는 시간
answer = 0  # 모두 녹기 한 시간 전에 남아있는 치즈 조각 개수
while cheeseCnt>0:
    answer = cheeseCnt
    time +=1
    boundary = melt(boundary)   #'c' 영역 구하기
    cheeseCnt -= len(boundary)

print(time)
print(answer)