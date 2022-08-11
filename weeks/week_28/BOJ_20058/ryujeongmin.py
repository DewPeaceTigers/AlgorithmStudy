"""
pypy3로 제출했을때만 통과! 
Python3로 제출하면 시간초과..
"""

import sys
from collections import deque

input = sys.stdin.readline

N, Q = map(int, input().split())

iSize = 2**N
# 얼음의 양
ice = [list(map(int, input().split())) for _ in range(iSize)]

# 마법사 상어가 시전한 단계
Ls = list(map(int, input().split()))

# 덩어리 확인을 위한 배열
v = [[0]*iSize for _ in range(iSize)]

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# 시계방향으로 90도 회전
def rotate(arr, lSize):
    newArr = [[0]*lSize for _ in range(lSize)]

    for i in range(lSize):
        for j in range(lSize):
            newArr[j][lSize-1-i] = arr[i][j]

    return newArr


def check(sx, sy, n_ice): # 마법사 상어 위치
    cnt = 0 # 얼음이 있는 칸 개수 저장
    for i in range(4):
        nx = sx+dx[i]
        ny = sy+dy[i]

        # 얼음판을 벗어나는 경우
        if nx<0 or nx>=iSize or ny<0 or ny>=iSize:
            continue

        if ice[nx][ny]>0:
            cnt += 1

    # 인접한 칸 중 얼음이 있는 칸이 3개 미만일 때 얼음의 양 -1
    if cnt<3:
        n_ice[sx][sy] -=1


def scale(sx, sy):
    q = deque()
    q.append((sx, sy))
    v[sx][sy] = 1
    ice_cnt = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            # 얼음판을 벗어나는 경우
            if nx < 0 or nx >= iSize or ny < 0 or ny >= iSize:
                continue

            if ice[nx][ny] > 0 and v[nx][ny]==0:
                ice_cnt += 1
                v[nx][ny] = 1   # 방문처리
                q.append((nx, ny))
    return ice_cnt


for L in Ls:
    lSize = 2**L

    if lSize>1:
        # 모든 부분 격자를 시계방향으로 90도 회전
        for r in range(iSize//lSize):
            for c in range(iSize//lSize):
                # 부분 격자 좌측 상단 좌표
                i, j = lSize*r, lSize*c

                # 부분 격자
                part = [ice[i+l][j:j+lSize] for l in range(lSize)]
                # 90도 회전
                part_rotate = rotate(part, lSize)

                # 얼음판 값 갱신
                for pr in range(lSize):
                    for pc in range(lSize):
                        ice[i+pr][j+pc] = part_rotate[pr][pc]

    # for r in range(iSize):
    #     print(*ice[r])

    n_ice = [[ice[r][c] for c in range(iSize)] for r in range(iSize)]

    # 인접한 칸 확인
    for r in range(iSize):
        for c in range(iSize):
            if n_ice[r][c] > 0:
                check(r, c, n_ice)

    ice = [[n_ice[r][c] for c in range(iSize)] for r in range(iSize)]
    # print("인접한 칸 확인")
    # for r in range(iSize):
    #     print(*ice[r])
    # print()

iceSum = 0  # 얼음 ice[r][c]의 합
dSize = 0   # 덩어리 크기
for r in range(iSize):
    for c in range(iSize):
        iceSum += ice[r][c]

        # 덩어리 체크!
        if ice[r][c] > 0 and v[r][c] == 0:
            dSize = max(dSize, scale(r, c))

print(iceSum)
print(dSize)